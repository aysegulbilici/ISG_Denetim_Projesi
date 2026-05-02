import cv2
from ultralytics import YOLO
import datetime
import os
import time

# 1. Klasör Hazırlığı
if not os.path.exists("ihlaller"):
    os.makedirs("ihlaller")

model = YOLO('yolov8n.pt') 
cap = cv2.VideoCapture(0)

# Kayıt kontrolü için son kaydedilen zaman
son_kayit_zamani = 0

while cap.isOpened():
    success, frame = cap.read()
    if success:
        # Görüntüyü işle
        results = model(frame, conf=0.5)
        detected_ids = results[0].boxes.cls.tolist()
        
        person_count = detected_ids.count(0) 
        helmet_count = detected_ids.count(1) # Kask (Şimdilik temsili ID)
        
        # --- 📊 PROFESYONEL PANEL (Dashboard) ---
        # Bilgi kutusu arka planı (Siyah dikdörtgen)
        cv2.rectangle(frame, (10, 10), (280, 110), (0, 0, 0), -1)
        
        # Metinleri yerleştir
        cv2.putText(frame, f"SISTEM AKTIF", (20, 35), 1, 1.2, (255, 255, 0), 2)
        cv2.putText(frame, f"Isci Sayisi: {person_count}", (20, 65), 1, 1, (255, 255, 255), 1)
        cv2.putText(frame, f"Kaskli: {helmet_count}", (20, 95), 1, 1, (0, 255, 0), 1)

        # --- 🚨 İHLAL DENETİMİ ---
        if person_count > helmet_count:
            # 1. Görsel Uyarı: Ekranın Etrafına Kırmızı Çerçeve
            cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), (0, 0, 255), 15)
            cv2.putText(frame, "IHLAL: KASKSIZ PERSONEL!", (frame.shape[1]//2 - 150, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

            # 2. Otomatik Kayıt: 5 saniyede en fazla 1 fotoğraf (Klasörü doldurmamak için)
            su_an = time.time()
            if su_an - son_kayit_zamani > 5:
                zaman_etiketi = datetime.datetime.now().strftime("%H-%M-%S")
                dosya_adi = f"ihlaller/ihlal_{zaman_etiketi}.jpg"
                cv2.imwrite(dosya_adi, frame)
                son_kayit_zamani = su_an
                print(f"[BILGI] İhlal kaydedildi: {dosya_adi}")

        # Görüntüyü göster
        cv2.imshow("Aysegul Bilici - ISG Denetim Projesi", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
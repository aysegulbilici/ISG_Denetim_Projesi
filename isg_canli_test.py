import cv2
from ultralytics import YOLO

# 1. Uzman Modeli Tanımlıyoruz
# Not: Yarın kask uzmanı .pt dosyasını bulduğumuzda ismini buraya yazacağız
model = YOLO('yolov8n.pt') 

cap = cv2.VideoCapture(0)

print("Sistem Baslatildi... Cikis icin 'q' basiniz.")

while cap.isOpened():
    success, frame = cap.read()
    if success:
        # Yapay zeka tahmini
        results = model(frame, conf=0.5)
        
        # Tespit edilen nesnelerin listesi
        # Diyelim ki modelimizde: 0=Insan, 1=Kask, 2=Yelek
        detected_ids = results[0].boxes.cls.tolist()
        
        # --- ISG DENETIM MANTIGI ---
        if 0 in detected_ids: # Eğer bir insan (işçi) varsa
            if 1 in detected_ids:
                # Hem insan hem kask varsa: GÜVENLİ
                msg = "Giris Onaylandi: Kaskli Personel"
                color = (0, 255, 0) # Yeşil
            else:
                # İnsan var ama kask yoksa: TEHLİKE
                msg = "UYARI: KASKSIZ PERSONEL!"
                color = (0, 0, 255) # Kırmızı
            
            # Ekrana uyarıyı yazdırıyoruz
            cv2.putText(frame, msg, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

        # Sonucu göster
        annotated_frame = results[0].plot()
        cv2.imshow("ISG Yapay Zeka Denetim", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
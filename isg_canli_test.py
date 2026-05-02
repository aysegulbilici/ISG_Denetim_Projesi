import cv2
from ultralytics import YOLO

# 1. Modeli yüklüyoruz (Şimdilik genel model, ama mantık aynı)
model = YOLO('yolov8n.pt') 

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        # Yapay zekaya soruyoruz
        results = model(frame, conf=0.5)
        
        # Tespit edilen sınıfları kontrol edelim
        # results[0].boxes.cls bize bulunan nesnelerin ID'lerini verir
        detected_classes = results[0].boxes.cls.tolist()
        
        # MANTIK: Eğer ortamda 'person' (ID 0) varsa ama 'kask' yoksa uyarı ver
        # Not: Şu an genel modelde kask olmadığı için sadece mantığı kuruyoruz
        if 0 in detected_classes: # Eğer bir insan tespit edildiyse
             cv2.putText(frame, "ISCI TESPIT EDILDI", (50, 80), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Görüntüyü göster
        annotated_frame = results[0].plot()
        cv2.imshow("ISG Denetim Sistemi", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
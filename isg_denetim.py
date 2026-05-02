from ultralytics import YOLO

# Hazır eğitilmiş temel bir model yüklüyoruz (YOLOv8 Nano sürümü)
# Bu model kaskı henüz bilmez ama insanı, sandalyeyi, masayı tanır.
model = YOLO('yolov8n.pt') 

print("Model basariyla yuklendi!")
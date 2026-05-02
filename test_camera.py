import cv2 # OpenCV kütüphanesini projeye dahil ediyoruz

# 0 numaralı kamerayı (varsayılan webcam) kullanmak üzere başlatıyoruz
cap = cv2.VideoCapture(0)

print("Kamera aciliyor... Kapatmak icin 'q' tusuna basiniz.")

# 'while True' sonsuz bir döngü başlatır, canlı yayın akışı sağlar
while True:
    # cap.read() kameradan anlık bir kare (fotoğraf) okur
    # ret: Görüntü alındı mı? (True/False)
    # frame: Okunan fotoğraf karesi
    ret, frame = cap.read()

    # Eğer görüntü başarıyla gelmediyse döngüyü sonlandır
    if not ret:
        break

    # Görüntü üzerine yazı ekleme (Annotation)
    # (resim, metin, koordinat, font, boyut, renk(BGR), kalınlık)
    #cv2.putText(frame, "Aysegul Bilici - ISG Projesi", (30, 30), 
               # cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # İşlenmiş görüntüyü bir pencerede göster
    cv2.imshow("Canli Kamera Testi", frame)

    # Klavyeden 'q' tuşuna basılıp basılmadığını kontrol et
    # waitKey(1) her kare arasında 1 milisaniye bekler
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# İşimiz bittiğinde kamerayı serbest bırakıyoruz
cap.release()
# Açılan tüm OpenCV pencerelerini kapatıyoruz
cv2.destroyAllWindows()
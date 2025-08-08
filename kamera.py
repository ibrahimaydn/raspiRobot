import cv2
from motor_control import ileri, geri, sola, saga, dur, setup
import time

setup()
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # Görüntüyü griye çevir ve threshold uygula
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

    # Kontur bul
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Engel algılandı
        print("Engel Algılandı!")
        dur()
        time.sleep(0.5)
        geri()
        time.sleep(0.5)
        saga()
        time.sleep(0.5)
    else:
        ileri()

    cv2.imshow("Kamera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

dur()
cam.release()
cv2.destroyAllWindows()

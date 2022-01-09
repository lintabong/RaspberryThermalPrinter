import cv2
from time import sleep

a = 'A'
no = 0
noDB = []

for i in range(0, 100):
    no = no + 1
    stringDB = a + str(no)
    noDB.append(stringDB)

print(noDB)

cam = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    succes, img = cam.read()
    data, bbox, _ = detector.detectAndDecode(img)

    for i in range(0,len(noDB)):
        if data == noDB[i]:
            print(data)
            sleep(2)
    cv2.imshow("img", img)

    if cv2.waitKey(1) == ord("Q"):
        break

cam.release()
cv2.destroyAllWindows()

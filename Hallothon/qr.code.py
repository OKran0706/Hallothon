#recognizes qr code and is able to tell link of it too.
import cv2
import pyzbar.pyzbar as pyzbar
from datetime import datetime

camera = cv2.VideoCapture(0)

try:
    
    while True:
        ret, frame = camera.read()
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            barcodeData = barcode.data.decode('utf-8')
            barcodeType = barcode.type
            text = "{} ( {} )".format(barcodeData, barcodeType)
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)

            print("Information : \n Found Type : {} Barcode : {}".format(barcodeType, barcodeData))
        cv2.imshow("Image", frame)
        cv2.waitKey(10)
    
except KeyboardInterrupt:
    print('interrupted!')
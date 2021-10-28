#recognizes qr code and is able to tell link of it too.
import cv2
import pyzbar.pyzbar as pyzbar
from datetime import datetime
a=0
def video_record():
    global a
    camera = cv2.VideoCapture(1)

    try:
        
        while a==0:
            ret, frame = camera.read()
            barcodes = pyzbar.decode(frame)
            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                barcodeData = barcode.data.decode('utf-8')
                print(barcodeData, type(barcodeData))
                barcodeType = barcode.type
                text = "{} ( {} )".format(barcodeData, barcodeType)
                return barcodeType
                a=1
            cv2.imshow("Image", frame)
            cv2.waitKey(10)
            
        
    except KeyboardInterrupt:
        print('interrupted!')
#video_record()
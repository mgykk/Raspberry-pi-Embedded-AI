"""
    @author: MiGuanyu
"""

from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2

ap=argparse.ArgumentParser()
#提供一个csv文件，这样，在最后不仅可以将二维码内容显示在屏幕上，还有专门的文件进行保存
ap.add_argument("-o","--output",type=str,default="content.csv",
                help="path to output csv file containing barcode")
args=vars(ap.parse_args())

print('starting video stream....')
#使用web摄像头的写法
vs=VideoStream(src=0).start()
#树莓派自带摄像头的写法
#vs=VideoStream(usePiCamera=True).start()
time.sleep(2.0)

#把内容写入csv
csv=open(args["output"],"w")
found=set()
while True:
    frame=vs.read()
    frame=imutils.resize(frame,width=400)
    barcodes=pyzbar.decode(frame)
    for barcode in barcodes:
        (x,y,w,h)=barcode.rect
        
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        #对二维码内容进行解码，输入时间，内容和类型
        barcodeData=barcode.data.decode("utf-8")
        barcodeType=barcode.type
        
        text="{}({})".format(barcodeData,barcodeType)
        
        cv2.putText(frame,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,
                    (0,0,255),2)
        
        if barcodeData not in found:
            csv.write("{},{}\n".format(datetime.datetime.now(),barcodeData))
            csv.flush()
            found.add(barcodeData)
    cv2.imshow("found_code",frame)
    key=cv2.waitKey(1)&0xFF
    if key==ord("q"):
        break


csv.close()
cv2.destroyAllWindows()
vs.stop()
        
        
        
        
        
        
        

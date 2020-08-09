"""
* @author       Miguanyu
"""

from __future__ import division
import cv2
import time
import numpy as np

cap=cv2.VideoCapture(0)

#设置摄像头分辨率为（640，480）
#如果感觉图像卡顿严重，可以降低为（320，240）
cap.set(3,480)
cap.set(4,320)

#设置黄色的阙值
yellow_lower=np.array([156,43,46])
yellow_upper=np.array([180,255,255])

time.sleep(1)

while 1:
    #ret为是否找到图像， frame是帧本身
    ret,frame=cap.read()

    frame=cv2.GaussianBlur(frame,(5,5),0)                    #高斯模糊
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)                #转hsv
    mask=cv2.inRange(hsv,yellow_lower,yellow_upper)          #生成掩膜
    
    #形态学操作
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)
    mask=cv2.GaussianBlur(mask,(3,3),0)
    res=cv2.bitwise_and(frame,frame,mask=mask)               #与运算
    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,
                          cv2.CHAIN_APPROX_SIMPLE)[-2]       #检测颜色的轮廓
    if len(cnts)>0:
        cnt = max (cnts,key=cv2.contourArea)
        (x,y),radius=cv2.minEnclosingCircle(cnt)
        cv2.circle(frame,(int(x),int(y)),int(radius)*2,
                   (255,0,255),2)                            #找到后在每个轮廓上画圆
        print('x:',x,'y:',y)
    cv2.imshow('capture',frame)
    if cv2.waitKey(1)==119:
        break
cap.release()
cv2.destroyAllWindows()

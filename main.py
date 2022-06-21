# coding=gbk
"""
图片人脸识别
作者：川川
@时间  : 2021/9/5 17:22
"""
import cv2 as cv
import numpy as np
print( cv.__version__ )
#加载彩色灰度图像
img = cv.imread('D:\picture.png',0)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
# coding=gbk
"""
ͼƬ����ʶ��
���ߣ�����
@ʱ��  : 2021/9/5 17:22
"""
import cv2 as cv
import numpy as np
print( cv.__version__ )
#���ز�ɫ�Ҷ�ͼ��
img = cv.imread('D:\picture.png',0)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
import os 
import cv2
from os import listdir

file = open("info.txt","w") 
a = listdir('out1')


for j,i in enumerate(a):
    #print i
    img = cv2.imread("out1/"+i)
    img2 = cv2.imwrite("info/"+str(j)+".bmp",img)
    print j
    print str(j)+".bmp 1 0 0 "+str(img.shape[1])+" "+str(img.shape[0])
    file.write(str(j)+".bmp 1 0 0 "+str(img.shape[1])+" "+str(img.shape[0])+'\n')




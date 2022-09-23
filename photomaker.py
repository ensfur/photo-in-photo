import glob
import cv2
import numpy as np
import random

def mostUseingColor(img):
    color=np.zeros([1331],np.uint8)
    
    x=y=0
    while x<15:
        while y<15:
            a=int(img[x,y,0]/25)
            b=int(img[x,y,1]/25)*11
            c=int(img[x,y,2]/25)*121
            color[a+b+c]+=1
            y+=1
        y=0
        x+=1
    colorSort=np.copy(color)
    colorSort.sort()
    f=colorSort[-1]
    i=len(color)-1
    while i>=0:
        if f==color[i]:
            break
        i-=1

    b=int((i%11)*25)
    g=int(((i-i%11)%121)*25/11)
    r=int(((i-((i-i%11)%121))%1331)*25/121)

    
    return [b,g,r]
            
        
    

images = [cv2.imread(file) for file in glob.glob("gray/*.png")]

photo=cv2.imread("best.jpg")
photo=photo[0:4020,0:3000]

newPhoto=np.zeros([21440,16000,3],np.uint8)
x=y=0
while x<268:
    while y<200:
        color=mostUseingColor(photo[15*x:15*x+15,15*y:15*y+15])
        filtre=np.zeros((80,80,3),np.uint8)
        filtre[:,:]=color

        ran=random.randint(0,315)
        smallPhoto=cv2.addWeighted(images[ran],1.0,filtre,0.5,0)
        newPhoto[80*x:80*x+80,80*y:80*y+80]=smallPhoto

        y+=1

    x+=1
    y=0

cv2.imwrite("newPhoto.png",newPhoto)

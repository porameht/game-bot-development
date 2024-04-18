import cv2 as cv
import numpy as np

class Classbot:
    def __init__(self,main_img,temp_img):
        self.mainimg =  cv.imread(main_img,cv.IMREAD_ANYCOLOR)
        self.temping = cv.imread(temp_img,cv.IMREAD_ANYCOLOR)
        
    def search(self):
        result = cv.matchTemplate(self.mainimg,self.temping,cv.TM_CCOEFF_NORMED)    
        _,maxval,_,maxloc = cv.minMaxLoc(result)
        threshold = 0.9
        locations = np.where(result >= threshold)

        locations= list(zip(*locations[::-1]))
        #print(locations)
        
        height = self.temping.shape[0]
        width =  self.temping.shape[1]
        #print(maxval) ## ค่าความแม่นยำ
        #print(maxloc) ##  xy ที่เจอ จะเจอมุมซ้ายบนเสมอ
        rectangles =[]
        
        for loc in locations:
            rect = [int(loc[0]),int(loc[1]),width,height]
            rectangles.append(rect)
            rectangles.append(rect)
        
        point = []
        rectangles,_ =cv.groupRectangles(rectangles,groupThreshold=1,eps=0.2)
        #print(len(rectangles))
        if len(rectangles):
            for (x,y,w,h) in rectangles:
                topleft = (x,y)
                bottomright = (x+w,y+h)
                cv.rectangle(self.mainimg,topleft,bottomright,color=(255,0,255),thickness=2,lineType=cv.LINE_8)

                #get x y 
                centerx = x + int( w / 2)
                centery = y +int( h / 2)
                
                ##add x y to point for click
                point.append((centerx,centery))
                #print(centerx,centery)
                
                cv.drawMarker(self.mainimg,(centerx,centery),color=(0,255,0),thickness=2,markerSize=40,markerType=cv.MARKER_CROSS)

        
         ##show
        cv.imshow("result",self.mainimg)
        cv.waitKey()
        cv.destroyAllWindows()        
        return point
                
     
mybot= Classbot('img/newmain.jpg','img/newtemp.jpg')  
mypoint = mybot.search()     
for myclick in mypoint:
    print(myclick)
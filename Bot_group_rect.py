import cv2 as cv
import numpy as np

class Bot:

    def __init__(self, main_image, temp_image):
        self.main_img = cv.imread(main_image, cv.IMREAD_ANYCOLOR)
        self.temp_img = cv.imread(temp_image, cv.IMREAD_ANYCOLOR)

    def search(self):
        threshold = 0.9
        result = cv.matchTemplate(self.main_img, self.temp_img, cv.TM_CCOEFF_NORMED)

        _, max_val, _, max_log = cv.minMaxLoc(result)

        locations = np.where(result >= threshold)

        locations = list(zip(*locations[::-1]))

        width = self.temp_img.shape[0]
        height = self.temp_img.shape[1]

        rectangles = []

        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), width, height]
            rectangles.append(rect)
            rectangles.append(rect)

        rectangles, _ = cv.groupRectangles(rectangles,groupThreshold=1,eps=0.5)
        print(rectangles)

        if len(rectangles):
            for (x, y, w, h) in rectangles:
                top_left = x, y
                bottom_right = x + w, y + h

                cv.rectangle(self.main_img, top_left, bottom_right, color=(200,30,41), thickness=2, lineType=cv.LINE_4)
                    
                font = cv.FONT_ITALIC

                position = (top_left[0]+5, top_left[1]-10)
                font_size = 0.5
                color = (200,30,41)
                cv.putText(self.main_img, "T", position, font, font_size, color=color, thickness=2)

            cv.imshow('result', self.main_img)
            cv.waitKey()
            cv.destroyAllWindows()

my_bot = Bot('img/newmain.jpg', 'img/newtemp.jpg')
my_bot.search()
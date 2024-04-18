import cv2 as cv
import numpy as np

class Bot:

    def __init__(self, main_image, temp_image):
        self.main_img = cv.imread(main_image, cv.IMREAD_ANYCOLOR)
        self.temp_img = cv.imread(temp_image, cv.IMREAD_ANYCOLOR)

    def search(self):
        result = cv.matchTemplate(self.main_img, self.temp_img, cv.TM_CCOEFF_NORMED)

        _, max_val, _, max_log = cv.minMaxLoc(result)

        threshold = 0.9
        if max_val > threshold:
            top_left = max_log

            # top_left[0] = x, top_left[1] = y
            width = self.temp_img.shape[0]
            height = self.temp_img.shape[1]
            buttom_right = (top_left[0]+width, top_left[1]+height)

            cv.rectangle(self.main_img, top_left, buttom_right, color=(200,30,41), thickness=2, lineType=cv.LINE_4)
            
            font = cv.FONT_ITALIC

            position = (top_left[0]+5, top_left[1]-10)
            font_size = 0.5

            color = (200,30,41)
            cv.putText(self.main_img, "Ramos", position, font, font_size, color=color, thickness=2)


            cv.imshow('result', self.main_img)

            cv.waitKey()
            cv.destroyAllWindows()


my_bot = Bot('img/main.jpg', 'img/temp.jpg')

my_bot.search()
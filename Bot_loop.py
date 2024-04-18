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

        print(locations)
        if locations:
            width = self.temp_img.shape[0]
            height = self.temp_img.shape[1]

            for loc in locations:
                buttom_right = (loc[0] + width, loc[1] + height)
                cv.rectangle(self.main_img, loc, buttom_right, color=(200,30,41), thickness=2, lineType=cv.LINE_4)
                    
                font = cv.FONT_ITALIC

                position = (loc[0]+5, loc[1]-10)
                font_size = 0.5

                color = (200,30,41)
                cv.putText(self.main_img, "T", position, font, font_size, color=color, thickness=2)

            cv.imshow('result', self.main_img)
            cv.waitKey()
            cv.destroyAllWindows()

my_bot = Bot('img/newmain.jpg', 'img/newtemp.jpg')
my_bot.search()
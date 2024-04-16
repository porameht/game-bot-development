import cv2 as cv
import numpy as np


main_img = cv.imread("img\\main.jpg", cv.IMREAD_ANYCOLOR)
temp_img = cv.imread("img\\temp.jpg", cv.IMREAD_ANYCOLOR)


result = cv.matchTemplate(main_img, temp_img, cv.TM_CCOEFF_NORMED)

_, max_val, _, max_log = cv.minMaxLoc(result)


threshold = 0.9

if max_val > threshold:
    top_left = max_log

    # top_left[0] = x, top_left[1] = y
    width = temp_img.shape[0]
    height = temp_img.shape[1]
    buttom_right = (top_left[0]+width, top_left[1]+height)

    cv.rectangle(main_img, top_left, buttom_right, color=(200,30,41), thickness=2, lineType=cv.LINE_4)
    
    font = cv.FONT_ITALIC

    position = (top_left[0]+5, top_left[1]-10)

    font_size = 0.5

    color = (200,30,41)
    cv.putText(main_img, "Ramos", position, font, font_size, color=color, thickness=2)


    cv.imshow('result', main_img)

    cv.waitKey()
    cv.destroyAllWindows()
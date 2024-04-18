from Windows_capture import *
import cv2 as cv



capture = WindowCapture("Ragnarok Landverse")

window = capture.screenshot()

cv.imshow('test', window)

cv.waitKey()
cv.destroyAllWindows()

print(window)




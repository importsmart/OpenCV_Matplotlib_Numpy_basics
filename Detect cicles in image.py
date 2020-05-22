import cv2
import numpy as np

img = cv2.imread("Detect circles in image (test image).png", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_blurred = cv2.blur(gray, (3, 3))

detected_circles = cv2.HoughCircles(gray_blurred,
                                    cv2.HOUGH_GRADIENT, 1, 20, param1=50,
                                    param2=30, minRadius=1, maxRadius=40)

if detected_circles is not None:

    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        cv2.circle(img, (a, b), r, (0, 255, 0), 2)

        cv2.circle(img, (a, b), 1, (0, 0, 255), 3) #centre

        cv2.imshow("Detected Circles", img)
        cv2.imwrite("Detected Circles.png", img)

else:
    print("No circes detected")

cv2.waitKey(0)
cv2.destroyAllWindows()
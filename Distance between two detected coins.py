import cv2
import numpy as np

img = cv2.imread('2coins.jpg', cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray_blurred = cv2.blur(gray, (3, 3))

detected_circles = cv2.HoughCircles(gray_blurred,
                                    cv2.HOUGH_GRADIENT, 1, 20, param1=50,
                                    param2=30, minRadius=90, maxRadius=100)

x, y, rad = [], [], []

if detected_circles is not None:

    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        x.append(a)
        y.append(b)
        rad.append(r)

        cv2.circle(img, (a, b), r, (0, 255, 0), 2)

        cv2.circle(img, (a, b), 1, (0, 0, 255), 3) #centre

else:
    print("No circes detected")

x = np.array(x, dtype=np.float64)
y = np.array(y, dtype=np.float64)
rad = np.array(rad, dtype=np.float64)

avgrad = (rad[0] + rad[1])/2
dist = ((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2 )**0.5
rel_dist = dist/avgrad

print(dist)
print(rel_dist)

text1 = "The relative distance (distance/avd radius) is " + "{:.2f}".format(rel_dist)
cv2.putText(img, text1, (0, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
text2 = f"The radii of the circles are {rad[0]} and {rad[1]}"
cv2.putText(img, text2, (0, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

cv2.imshow("Detected Circles", img)
#cv2.imwrite("assignment_2_output.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
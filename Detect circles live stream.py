'''Need to stop program from crashing when circles not detected but works otherwise'''

import cv2
import numpy as np

def main():
    windowName = "Live Video Feed"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)

    if cap.isOpened():
        ret, img = cap.read()
    else:
        ret = False

    while ret:
        ret, img = cap.read()

        cv2.imshow(windowName, img)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        gray_blurred = cv2.blur(gray, (3, 3))

        detected_circles = cv2.HoughCircles(gray_blurred,
                                            cv2.HOUGH_GRADIENT, 1, 20, param1=50,
                                            param2=30, minRadius=50, maxRadius=90)

        x, y, rad = [], [], []

        if detected_circles is not None:

            detected_circles = np.uint16(np.around(detected_circles))

            for pt in detected_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]

                x.append(a)
                y.append(b)
                rad.append(r)

                cv2.circle(img, (a, b), r, (0, 255, 0), 2)

                cv2.circle(img, (a, b), 1, (0, 0, 255), 3)  # centre

        else:
            print("No circes detected")

        x = np.array(x, dtype=np.float64)
        y = np.array(y, dtype=np.float64)
        rad = np.array(rad, dtype=np.float64)

        if len(rad)>1:
            avgrad = (rad[0] + rad[1]) / 2
            dist = ((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2) ** 0.5
            rel_dist = dist / avgrad

            text1 = "The relative distance (distance/avd radius) is " + "{:.2f}".format(rel_dist)
            cv2.putText(img, text1, (0, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
            text2 = f"The radii of the circles are {rad[0]} and {rad[1]}"
            cv2.putText(img, text2, (0, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

            print(dist)
            print(rel_dist)

            cv2.imshow("Detected Circles", img)
        else:
            cap.release()

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()

    cap.release()


if __name__ == "__main__":
    main()
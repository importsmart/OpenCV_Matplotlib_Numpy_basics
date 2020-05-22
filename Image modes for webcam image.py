import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, img = cap.read()
    print(ret)
else:
    ret = False

img1 = cv2.bitwise_not(img)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img4 = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
img5 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

titles = ['BGR', 'Invert', 'RGB', 'HSV', 'HLS', 'Gray']
images = [img, img1, img2, img3, img4, img5]

for i in range(6):
    plt.subplot(3, 2, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

cap.release()
from PIL import Image
import numpy as np

A = np.zeros((1000,1000,3),dtype=np.uint8)

for r in range(500):
   c = int(255*(1-r/500))
   for x in range(500-r,500+r):
       y = int(500 + (r**2 - (x-500)**2)**0.5)
       A[y, x] = [c, c, c]
       A[1000-y,x] = [c,c,c]

img = Image.fromarray(A,'RGB')
img.show()
#img.save(r"C:\Users\dhruv\Python\Kratos\Assignment1.jpeg")


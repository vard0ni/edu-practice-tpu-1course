import numpy as np
import cv2

# Import image and resize it
img = cv2.imread("C:\\Users\\zahar\Desktop\\edu-practice\\image.png")
width = 400
height = 400
dim = (width, height)
rimg = cv2.resize(img, dim)

# Task 3.2
img = rimg.copy()
for i in range(0, 1001):
   cords = np.random.randint(0, high=400, size=(2,))
   radius = 2
   color = list(np.random.random(size=3) * 256)
   thickness = -1

   cv2.circle(img, cords, radius, color, thickness)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Task 3.4
def task4(channel):
   if channel == "R":
       red = rimg.copy()
       red[:, :, 0] = 0
       red[:, :, 1] = 0
       cv2.imshow('Red', red)
   elif channel == "G":
       green = rimg.copy()
       green[:, :, 0] = 0
       green[:, :, 2] = 0
       cv2.imshow('Green', green)
   else:
       blue = rimg.copy()
       blue[:, :, 1] = 0
       blue[:, :, 2] = 0
       cv2.imshow('Blue', blue)
   cv2.waitKey(0)
   cv2.destroyAllWindows()

channel = str(input("Enter 'R' or 'G' or 'B':"))
task4(channel)

# Task 3.6
def task6(rimg):
   # fill inside triangle
   img = rimg.copy()
   points = np.array([[160, 130], [350, 130], [250, 300]])
   cv2.fillPoly(rimg, pts=[points], color=(192, 192, 192))

   # fill outside triangle
   fill_color = [255, 255, 0]
   mask_value = 255
   contours = [np.array([[160, 130], [350, 130], [250, 300]])]
   stencil = np.zeros(rimg.shape[:-1])
   cv2.fillPoly(stencil, contours, mask_value)
   sel = stencil != mask_value  # select everything != mask_value
   rimg[sel] = fill_color  # and fill it with fill_color

   cv2.polylines(img, [points], True, (0, 255, 0), 2)
   cv2.imshow("img1", img)
   cv2.imshow("img2", rimg)
   cv2.waitKey(0)
   cv2.destroyAllWindows()


task6(rimg)

# Task 3.8
def task8(rimg):
   cv2.imshow("img1", rimg)
   for i in range(0, 401, 2):
       image = cv2.line(rimg, (0,i), (400, i), (128,128,128), 1)

   cv2.imshow("img2", image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
task8(rimg)

import cv2
import numpy as np
import math
def mse(img1,img2):
     mse = np.mean((img1 - img2) ** 2 )
     a=mse
     return a
 
def psnr1(img1, img2):
   mse = np.mean((img1 - img2) ** 2 )
   if mse < 1.0e-10:
      return 100
   return 10 * math.log10(255.0**2/mse)
# E:\VIT\3_TY\Sem1\CS\CS course project\image_search_1668682587604.jpg
gt = cv2.imread(r"image_1.png")
img= cv2.imread(r"image_11.png")

#peak singnal to noise ratio
print("The PSNR Value is" ,psnr1(gt,img))
print("The MSE Value is" ,mse(gt,img))



import matplotlib.pyplot as plt
import cv2
im = cv2.imread(r"image_1.png")
vals1 = im.mean(axis=2).flatten()
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2)
ax0.hist(vals1, 255)
ax0

im1 = cv2.imread(r"image_11.png")
vals2 = im1.mean(axis=2).flatten()
print(vals1 ,"\n", vals2)
ax1.hist(vals2, 255)

fig.tight_layout()
plt.show()


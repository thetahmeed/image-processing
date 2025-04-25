import numpy as np
import cv2 as cv

img = cv.imread('images/COVID19(390).jpg', cv.IMREAD_GRAYSCALE)

### Histograms Equalization
equ = cv.equalizeHist(img)
res = np.hstack((img,equ)) # stacking images side-by-side
cv.imwrite('output/equalization/histograms_equalization.png',res)
# cv.imwrite('histograms_equalization.jpg',equ) 
 
### CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
res2 = np.hstack((img,cl1)) # stacking images side-by-side
cv.imwrite('output/equalization/clahe_equalization.png',res2)
# cv.imwrite('clahe_equalization.jpg',cl1)
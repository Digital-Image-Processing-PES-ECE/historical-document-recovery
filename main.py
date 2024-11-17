import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = '<image_path>'
img = cv2.imread(image_path)

if len(img.shape) == 3:
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
else:
    gray_img = img

denoised_img = cv2.GaussianBlur(gray_img, (5, 5), 0.5)

clahe = cv2.createCLAHE(clipLimit=0.01, tileGridSize=(8, 8))
clahe_img = clahe.apply(denoised_img)

T = cv2.adaptiveThreshold(
    clahe_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 10
)

binary_img = 255 - T

final_enhanced_text = cv2.normalize(binary_img, None, 0, 255, cv2.NORM_MINMAX)

plt.figure(figsize=(15, 8))
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(gray_img, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(denoised_img, cmap='gray')
plt.title('Denoised (Gaussian Filter)')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(clahe_img, cmap='gray')
plt.title('CLAHE Enhanced')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(binary_img, cmap='gray')
plt.title('Adaptive Thresholding (Sauvola)')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(final_enhanced_text, cmap='gray')
plt.title('Final Enhanced Image')
plt.axis('off')

plt.tight_layout()
plt.show()

import numpy as np
import cv2

# Read the image
img = cv2.imread("D:\\B21AI002_CVIP\\img3.jpg")

# Get image dimensions
row, col, _ = img.shape

# Define shear parameters (shear in the x-direction)
shear_factor = 0.2
shear_matrix = np.float32([[1, shear_factor, 0], [0, 1, 0]])

# Apply shear transformation
sheared_img = cv2.warpAffine(img, shear_matrix, (col, row))

# Display the original and sheared images side by side
combined_image = np.hstack((img, sheared_img))
cv2.imshow("Original vs. Sheared", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

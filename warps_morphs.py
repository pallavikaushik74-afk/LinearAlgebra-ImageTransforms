import cv2
import numpy as np

IMAGE_PATH_WARP = "C:\\Users\\palla\\OneDrive\\Pictures\\Screenshots\\xyz.png"
IMAGE_PATH_SOURCE = "C:\\Users\\palla\\Downloads\\kid.jpeg"
IMAGE_PATH_DESTINATION = "C:\\Users\\palla\\Downloads\\images (1).jpg"

# ==================== PART 1: LINEAR ALGEBRA WARP ====================

image = cv2.imread(IMAGE_PATH_WARP)
if image is None:
    print("Error: Image not found")
    exit()

height, width = image.shape[:2]

# Affine Transformation (Uses 2x3 Matrix - LINEAR ALGEBRA)
# preserves parallel lines
def affine_warp(img):
    # 3 source points
    src_pts = np.float32([
        [width * 0.3, height * 0.3],
        [width * 0.7, height * 0.3],
        [width * 0.5, height * 0.7]
    ])
    
    # 3 destination points (distorted)
    dst_pts = np.float32([
        [width * 0.25, height * 0.25],
        [width * 0.75, height * 0.35],
        [width * 0.5, height * 0.75]
    ])
    
    # Get transformation matrix (LINEAR ALGEBRA!)
    matrix = cv2.getAffineTransform(src_pts, dst_pts)
    
    # Apply matrix transformation
    warped = cv2.warpAffine(img, matrix, (width, height))
    
    return warped

# Perspective Transformation (Uses 3x3 Matrix - LINEAR ALGEBRA)
def perspective_warp(img):
    # 4 corner points
    src_pts = np.float32([
        [0, 0],
        [width-1, 0],
        [0, height-1],
        [width-1, height-1]
    ])
    
    # 4 distorted points
    dst_pts = np.float32([
        [width * 0.15, height * 0.1],
        [width * 0.85, height * 0.1],
        [width * 0.05, height * 0.9],
        [width * 0.95, height * 0.9]
    ])
    
    # Get perspective matrix (LINEAR ALGEBRA!)
    matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)
    
    # Apply matrix transformation
    warped = cv2.warpPerspective(img, matrix, (width, height))
    
    return warped

# Apply transformations
warped_affine = affine_warp(image)
warped_perspective = perspective_warp(image)

# Display side by side
cv2.namedWindow("Linear Algebra Warps", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Linear Algebra Warps", 1000, 500)

combined = np.hstack((image, warped_affine, warped_perspective))
cv2.imshow("Linear Algebra Warps", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ---------------------- PART 2: Image Morphing ----------------------

image_source = cv2.imread(IMAGE_PATH_SOURCE)
image_destination = cv2.imread(IMAGE_PATH_DESTINATION)

if image_source is None or image_destination is None:
    print("Error: Images not found")
    exit()

TARGET_SIZE = (400, 500)
image_source = cv2.resize(image_source, TARGET_SIZE)
image_destination = cv2.resize(image_destination, TARGET_SIZE)

cv2.namedWindow("Image Morphing", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image Morphing", 500, 600)

for i in range(51):
    percentage = i / 100
    morphed = cv2.addWeighted(image_source, 1 - percentage, image_destination, percentage, 0)
    cv2.imshow("Image Morphing", morphed)
    cv2.waitKey(50)

cv2.waitKey(0)
cv2.destroyAllWindows()
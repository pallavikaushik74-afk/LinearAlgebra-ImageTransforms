# LinearAlgebra-ImageTransforms
A visual demo of how images can be warped and blended using OpenCV and simple math.

This project demonstrates how Affine Transformation, Perspective Transformation, and Image Morphing work using Linear Algebra and OpenCV.
It includes three main components:
1. Affine Warp – 2×3 matrix transformation
2. Perspective Warp – 3×3 matrix transformation
3. Image Morphing – Pixel-level blending between two images

Features

✅ Affine Transformation

    Uses three point pairs

    Preserves parallel lines
Implemented with:

cv2.getAffineTransform()

cv2.warpAffine()

✅ Perspective Transformation

    Uses four corner points
    
    Allows keystone distortion
    
Implemented with:

cv2.getPerspectiveTransform()

cv2.warpPerspective()

✅ Image Morphing

    Smooth blend between a source and destination image
    
    Uses weighted linear interpolation
    
morphed = cv2.addWeighted(src, 1 - t, dst, t, 0)

🧠 Concepts Used

Linear algebra (matrices & coordinate mapping)

Pixel interpolation

Spatial transforms

Weighted averaging

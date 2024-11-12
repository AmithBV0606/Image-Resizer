# 1) Importing the OpenCV Library:
import cv2
# The cv2 module from OpenCV is used for image processing tasks.

# 2) Configurable parameters
source = "Ghost.jpg"
destination = "newGhost.jpg"
scale_percent = 50

# Breakdown : 
# - "source" specifies the file path for the input image, in this case, "Ghost.jpg".
# - "destination" is the filename for the output image.
# - "scale_percent" is the scaling factor to determine the size of the new image, here set to 50 percent of the original dimensions.

# 3) Reading the Image:
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
cv2.imshow("title", src) 

# Breakdown :
# "cv2.imread()" reads the image from the specified source.
# The "cv2.IMREAD_UNCHANGED" flag is used to load the image with all channels and depth unchanged. 
# The "src" variable now contains the original image data.

# 4) Calculating the 50 percent of original dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# Breakdown : 
# "src.shape[1]" gives the width of the original image, and "src.shape[0]" gives the height.
# These dimensions are multiplied by "scale_percent / 100" to get the new width and height, resulting in an image that is "50%"" of the original size.

# 5) Resizing the Image:
output = cv2.resize(src, (new_width, new_height))

# Breakdown :
# "cv2.resize()" resizes the original image (src) to the calculated "new_width" and "new_height". The resized image is stored in output variable.

# 6) Saving the Resized Image:
cv2.imwrite(destination, output)

# Breakdown :
# "cv2.imwrite()" saves the resized image output to a file with the name specified by destination, in this case, "newGhost.jpg".

# 7) Wait Key:
cv2.waitKey(0)

# Breakdown : 
# "cv2.waitKey(0)" holds the program open for a key press event to close any OpenCV windows if any were displayed. This line has no visible effect here since there are no windows open (cv2.imshow() is commented out).
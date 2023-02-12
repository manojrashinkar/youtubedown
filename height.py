import cv2
import numpy as np

# Load the image
image = cv2.imread("body1.jpeg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect the edges in the image using Canny edge detection
edges = cv2.Canny(gray, 50, 150)

# Find the contours in the image
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Find the contour with the largest area (presuming it corresponds to the body)
body_contour = max(contours, key=cv2.contourArea)

# Find the bounding rectangle for the body contour
x, y, w, h = cv2.boundingRect(body_contour)

# Draw a rectangle around the body in the original image
cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Measure the height of the body by computing the height of the bounding rectangle
body_height = h

# Define the ratio of pixels to inches
pixels_per_inch = 100

# Convert the height in pixels to inches
body_height_inches = body_height / pixels_per_inch

# Convert the height in inches to feet
body_height_feet = body_height_inches / 12

# Display the height in feet
print("Body height (in feet):", body_height_inches)

# Display the image
cv2.imshow("Body", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

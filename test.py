import cv2
import numpy as np

def measure_body(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect edges using Canny edge detector
    edges = cv2.Canny(gray, 50, 150)

    # Find contours in the image
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour
    largest_contour = max(contours, key=cv2.contourArea)

    # Fit an ellipse around the largest contour
    ellipse = cv2.fitEllipse(largest_contour)

    # Draw the ellipse on the image
    cv2.ellipse(image, ellipse, (0, 255, 0), 2)

    # Calculate the width and height of the ellipse
    width, height = ellipse[1][0], ellipse[1][1]

    # Draw the width and height on the image
    cv2.putText(image, "Width: {:.2f}".format(width), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(image, "Height: {:.2f}".format(height), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Return the processed image
    return image

# Load the image
image = cv2.imread("body.jpg")

# Measure the body in the image
result = measure_body(image)

# Display the result
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# Load the image
image = cv2.imread("body.jpg")

# Resize the image to meet passport photo size requirements
required_size = (600, 600)
image = cv2.resize(image, required_size)

# Crop the image to a square centered on the face
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

if len(faces) > 0:
    x, y, w, h = faces[0]
    cropped = image[y:y+h, x:x+w]
    cropped = cv2.resize(cropped, required_size)
    image = cropped

# Save the 8 copies of the processed image
for i in range(8):
    cv2.imwrite("processed_image_{}.jpg".format(i), image)

# Display the first processed image
cv2.imshow("Passport Photo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

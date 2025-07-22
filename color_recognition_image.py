
import cv2
import math

# Simple color list with RGB values
colors = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Cyan": (0, 255, 255),
    "Magenta": (255, 0, 255),
    "Black": (0, 0, 0),
    "White": (255, 255, 255),
    "Gray": (128, 128, 128),
    "Orange": (255, 165, 0),
    "Purple": (128, 0, 128),
    "Pink": (255, 192, 203),
    "Brown": (139, 69, 19)
}

# Load the image
image = cv2.imread('test_image.jpg')

# Convert image from BGR to RGB for correct color matching
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Function to get the closest color name based on RGB
def get_color_name(r, g, b):
    min_distance = float('inf')
    color_name = "Unknown"
    for name, (cr, cg, cb) in colors.items():
        distance = math.sqrt((r-cr)**2+(g-cg)**2+(b-cb)**2)
        if distance < min_distance:
            min_distance = distance
            color_name = name
    return color_name

# Mouse click event
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        r, g, b = image_rgb[y, x]  # Correct: using RGB values
        color_name = get_color_name(r, g, b)
        text = f'{color_name} (R={r}, G={g}, B={b})'
        print(text)
        img_copy = image.copy()
        cv2.putText(img_copy, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (int(b), int(g), int(r)), 2)
        cv2.imshow('Color Recognition', img_copy)

# Show image and set mouse callback
cv2.imshow('Color Recognition', image)
cv2.setMouseCallback('Color Recognition', click_event)

print("Click on the image to detect the color and RGB values. Press any key to exit.")

cv2.waitKey(0)
cv2.destroyAllWindows()
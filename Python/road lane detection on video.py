import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

def region_of_interest(image, vertices):
    mask = np.zeros_like(image)
    match_mask_color = 255
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(image, mask)
    return masked_image

def draw_lines(img, lines):
    img = np.copy(img)
    line_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    img = cv.addWeighted(img, 0.8, line_image, 1, 0.0)
    return img

def process(image):
    height = image.shape[0]
    width = image.shape[1]
    region_of_interest_vertices = [
        (0, height),
        (width / 2, height / 2),
        (width, height)
    ]
    gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    canny_image = cv.Canny(gray_image, 100, 120)
    cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))

    lines = cv.HoughLinesP(
        cropped_image,
        rho=2,
        theta=np.pi / 60,
        threshold=50,
        lines=np.array([]),
        minLineLength=40,
        maxLineGap=100
    )
    img_with_lines = draw_lines(image, lines)
    return img_with_lines

cap = cv.VideoCapture("bike road.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    frame = process(frame)
    cv.imshow("output", cv.cvtColor(frame, cv.COLOR_RGB2BGR))
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

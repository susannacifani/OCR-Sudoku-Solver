import cv2

# Grayscale
img = cv2.imread("sudoku-test3.jpeg")
img2 = img.copy()

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# One way to get rid of the noise on the image and find edges, is by using Cannys edge detection algorithm 
edged = cv2.Canny(gray, 100, 500)
'''
cv2.imshow('Contours', edged)
cv2.waitKey(0)
'''

# Finding Contours
# Use a copy of the image e.g. edged.copy() since findContours alters the image, RETR_TREE retrieves all possible contours, 
# CHAIN_APPROX_NONE stores all the boundary points
contours, hierarchy = cv2.findContours(edged, 
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#cv2.imshow("Original Sudoku", edged)
#cv2.waitKey(0)

# Draw all contours
# the contours obtained from findContours(), -1 draws all contours, color of contours is green, thickness is 2
cv2.drawContours(img2, contours, -1, (0, 255, 0), 2)
  
cv2.imshow('Contours', img2)
cv2.waitKey(0)


# Find the largest contour
largest_contour = max(contours, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(largest_contour)
sudoku_area = img[y:y+h, x:x+w]

cv2.imshow('Sudoku Area', sudoku_area)
cv2.waitKey(0)

print(largest_contour)


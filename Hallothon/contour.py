import cv2
import numpy as np
  
# Let's load a simple image with 3 black squares
image = cv2.imread('C:/Users/chiragr/Music/PES_SEM_3/Hallothon/contour.png')
cv2.waitKey(0)
  
# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
# Find Canny edges
edged = cv2.Canny(gray, 40, 500)
  
contours, hierarchy = cv2.findContours(edged, 
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

  
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
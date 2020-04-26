import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

img[55,55] = [0,0,0]
px = img[55,55]

print(px)

img[100:150, 100:150] = [0,0,255]

watch_face = img[100:600, 300:900] #le indicamos las coordenadas
img[0:500, 0:600] = watch_face #estamos añadiendo a la imagen las coordenadas que hemos cogido antes

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

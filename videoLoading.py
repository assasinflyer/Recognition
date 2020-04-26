import cv2
import numpy as np

cap = cv2.VideoCapture(0) #el 0 es para indicar la webcam que quieres usar 1 o 2 o ... la 0 es por defecto
##cap = cv2.VideoCapture('output.avi') #si quieres usar un video en lugar de la camara, lo pones ahi
fourcc = cv2.VideoWriter_fourcc(*'XVID') #indicamos el code para grabar
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480)) #indicamos el nombre del video, el codec y la calidad
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #crea un filtro para ver la imagen en b/n
    out.write(frame) #le decimos que grabe frame en el video
    cv2.imshow('frame',frame)
    cv2.imshow('gray', gray) #muestra una pantalla donde se aplica el filtro b/n

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release() #crea el archivo de video
cv2.destroyAllWindows()
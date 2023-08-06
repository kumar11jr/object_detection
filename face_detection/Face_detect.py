import cv2

face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('dv.png')


gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


face_coordinates = face_data.detectMultiScale(gray_img)
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img, (x,y),(w+x,h+y),(0,255,0),2)

print(face_coordinates)
cv2.imshow('prabhat face detection',img)

cv2.waitKey()

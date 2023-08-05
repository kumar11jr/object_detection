import cv2

face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

webcam = cv2.VideoCapture(0)

while True:
    successful_frame_read,frame = webcam.read()
    
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_coordinates = face_data.detectMultiScale(gray_img)
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x,y),(w+x,h+y),(0,255,0),2)
    cv2.imshow('prabhat face detection',frame)
    cv2.waitKey(1)
    
    
webcam.release()
cv2.destroyAllWindows()
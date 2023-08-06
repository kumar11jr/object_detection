import cv2

face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detect = cv2.CascadeClassifier('haarcascade_smile.xml')

webcam = cv2.VideoCapture(0)

while True:
    
    (successful_frame_read,frame) = webcam.read()
    
    if not successful_frame_read:
        break
    
    gray_scale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_detect.detectMultiScale(gray_scale)
    smiles = smile_detect.detectMultiScale(gray_scale,scaleFactor=1.7,minNeighbors=20)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(w+x,h+y),(0,255,0),2)
    for (x,y,w,h) in smiles:
        cv2.rectangle(frame, (x,y),(w+x,h+y),(0,255,0),2)
    cv2.imshow('smile_detection',frame)
    cv2.waitKey(1)
    
    
webcam.release()
cv2.destroyAllWindow()
import cv2

# img = cv2.imread('car.jpg')

video = cv2.VideoCapture('car-and-pedestrian-video0.mp4')
car_cascade = cv2.CascadeClassifier('cars.xml')
pedestrian_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

while True:
    (read_successful,frame) = video.read()
    if read_successful:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    pedestrian = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)      
    
    for (x,y,w,h) in pedestrian:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow('video', frame)
    
    if cv2.waitKey(25) & 0xFF == 27:  # Press 'Esc' key to exit
        break
    

video.release()
cv2.destroyAllWindows()

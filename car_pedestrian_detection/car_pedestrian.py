import cv2

# img = cv2.imread('car.jpg')

video = cv2.VideoCapture('dataset_video1.avi')
car_cascade = cv2.CascadeClassifier('cars.xml')
pedestrian_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    (read_successful,frame) = video.read()
    if read_successful:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)      
    
    cv2.imshow('video', frame)
    
    cv2.waitKey(1)
    

cv2.destroyAllWindows()

import cv2
video=cv2.VideoCapture("#Samples/cctv.mp4")
face_clsfr=cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

while True:
    rat,frame=video.read()
    
    if rat==False:
        break
    frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_clsfr.detectMultiScale(gray,1.5,4,minSize=(9,9),maxSize=(1000,1000))
    for face in faces:
        #print(face)
        x=face[0]
        y=face[1]
        w=face[2]
        h=face[3]
        face_crop=frame[y:y+h,x:x+w]
        cv2.rectangle(frame, (x, y - 25), (x + w, y), (0, 0, 255), -1)
        
        
        cv2.putText(
            frame,
            "  Face",
            (x + 5, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2,
)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        
        
        if face_crop.size > 0:
            face_crop=cv2.resize(face_crop,(0,0),fx=3.0,fy=3.0)
            cv2.imshow('face',face_crop)

    cv2.imshow('video',frame)
    x=cv2.waitKey(10)
    if x==113:
        break
cv2.destroyAllWindows()

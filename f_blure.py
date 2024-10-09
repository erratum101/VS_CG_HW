import cv2
import os

def blurf(inputvid):
    outvid = os.path.splitext(inputvid)[0] + "_anananimus-_-.mp4"

    cap = cv2.VideoCapture(inputvid)
    model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # сначала вставил расшириную, думал будет лучше работать, а она даж  лицо джереми не распознала :(
    out = cv2.VideoWriter(outvid, cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (int(cap.get(3)), int(cap.get(4))))  

    while(True):
        getnxtfr, frame = cap.read()
        if not getnxtfr:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = model.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            blurred = cv2.blur(face, (100, 100))
            frame[y:y+h, x:x+w] = blurred

        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    inputvid = 'Jeremy.mp4' 
    blurf(inputvid)

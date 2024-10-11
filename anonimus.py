import cv2
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import threading

def blurf(inputvid, blurlv):
    outvid = os.path.splitext(inputvid)[0] + "_anananimus-_-.mp4"

    cap = cv2.VideoCapture(inputvid)
    model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    out = cv2.VideoWriter(outvid, cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (int(cap.get(3)), int(cap.get(4))))

    while(True):
        getnxtfr, frame = cap.read()
        if not getnxtfr:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = model.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            blurred = cv2.blur(face, (blurlv, blurlv))
            frame[y:y+h, x:x+w] = blurred

        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"seved")


def upf():
    global inputvid, preview
    inputvid = filedialog.askopenfilename(
        initialdir="/", 
        title="Select a Video", 
        filetypes=(("Video files", "*.mp4;*.avi;*.mkv"), ("all files", "*.*"))
    )
    if inputvid:
        popup.config(text=f"Selected Video: {os.path.basename(inputvid)}")
        preview = threading.Thread(target=display_preview, args=(inputvid,))
        preview.start()

def downvidf():
    global inputvid, adjust
    if inputvid:
        blurlv = int(adjust.get())
        blurf(inputvid, blurlv)
        print(f"Blurred video saved as: {os.path.splitext(inputvid)[0] + '_anananimus-_-.mp4'}")
    else:
        print("Upload a video first!")

def display_preview(inputvid):
    cap = cv2.VideoCapture(inputvid)
    if cap.isOpened():
        while(True):
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('Video Preview', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()

def update_blur_label(event):
    blurlv = int(adjust.get())
    bleble.config(text=f"Blur Level: {blurlv}")

root = tk.Tk()
root.title("Face Blurring proga")

upf = ttk.Button(root, text="Upload Video", command=upf)
upf.pack(pady=10)

popup = ttk.Label(root, text="No video selected")
popup.pack()

adjust = ttk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL)
adjust.pack(pady=10)
adjust.bind("<ButtonRelease-1>", update_blur_label)

bleble = ttk.Label(root, text="Blur Level: 1")  
bleble.pack()

downbtn = ttk.Button(root, text="Download ananimus vid", command=downvidf)
downbtn.pack(pady=10)

root.mainloop()

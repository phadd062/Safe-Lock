import time

import cv2
import pyautogui

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

cap = cv2.VideoCapture(1)

t = 10
while True:
    ret, frame = cap.read()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray, 1.05, 5)

    for face_array in faces:
        cv2.rectangle(
            frame,
            (face_array[0], face_array[1]),
            (face_array[0] + face_array[2], face_array[1] + face_array[3]),
            (237, 133, 72),
            5,
        )
        face_gray = img_gray[
            face_array[1] : face_array[1] + face_array[3],
            face_array[0] : face_array[0] + face_array[2],
        ]
        face_color = frame[
            face_array[1] : face_array[1] + face_array[3],
            face_array[0] : face_array[0] + face_array[2],
        ]
        eyes = eye_cascade.detectMultiScale(face_gray, 1.05, 5)
        for eye_array in eyes:
            t = 10
            cv2.rectangle(
                face_color,
                (eye_array[0], eye_array[1]),
                (eye_array[0] + eye_array[2], eye_array[1] + eye_array[3]),
                (84, 186, 60),
                5,
            )
    cv2.imshow("frame", frame)
    time.sleep(0.999)
    t -= 1
    print(f"{t} seconds left before the screen locks")
    if t <= 0:
        pyautogui.hotkey("win", "r")
        time.sleep(0.5)
        pyautogui.typewrite("rundll32.exe user32.dll, LockWorkStation")
        pyautogui.press("enter")
        break

    if ord("c") == cv2.waitKey(1):
        break


cap.release()
cv2.destroyAllWindows()

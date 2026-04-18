import cv2 as cv
import mediapipe as mp
import numpy as np

cam = cv.VideoCapture(0)
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
mp_drawing_styles = mp.solutions.drawing_styles

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
mp_face = mp_face_mesh.FaceMesh(min_detection_confidence = 0.5, min_tracking_confidence = 0.5, refine_landmarks=True)


def if_Person_there():
    pass

def eye_Detection(marks):
    if mark[0] == 473:            #Right eye
        print(mark[1].x)
        x_coor = int(mark[1].x * width)
        y_coor = int(mark[1].y * height)
        cv.circle(frame, (x_coor,y_coor), 5, (0, 0, 255), -1)
    
    if mark[0] == 468:            #Left eye
        pass
    

def no_of_People():
    pass

def unwanted_objects():
    pass

def alert_Management():
    pass


while True:
    ret, frame = cam.read()
    # frame = cv.rotate(frame, cv.CAP_PROP_OPENNI2_MIRROR)
    frame = frame[: , ::-1]                     #Mirroring the image
    height, width, _ = frame.shape
    frame.flags.writeable = False

    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    results = mp_face.process(rgb_frame)

    frame.flags.writeable = True
    frame = np.ascontiguousarray(frame)                          #Read about this!!!
    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0]

        for mark in enumerate(landmarks.landmark):

            eye_Detection(mark)


    cv.imshow("Webcam", frame)
    if cv.waitKey(1) == ord(" "):
        break
cam.release()
cv.destroyAllWindows()

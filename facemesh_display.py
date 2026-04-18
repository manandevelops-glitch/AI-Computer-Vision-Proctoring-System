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

def eye_Detection():
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

    frame.flags.writeable = False


    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    results = mp_face.process(rgb_frame)


    frame.flags.writeable = True
    frame = np.ascontiguousarray(frame)                          #Read about this!!!
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # print(face_marks)
            mp_drawing.draw_landmarks(
            image=frame,
            landmark_list=face_landmarks,
            connections=mp_face_mesh.FACEMESH_TESSELATION,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles
            .get_default_face_mesh_tesselation_style())
        
        mp_drawing.draw_landmarks(
            image=frame,
            landmark_list=face_landmarks,
            connections=mp_face_mesh.FACEMESH_CONTOURS,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles
            .get_default_face_mesh_contours_style())
        
        mp_drawing.draw_landmarks(
            image=frame,
            landmark_list=face_landmarks,
            connections=mp_face_mesh.FACEMESH_IRISES,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles
            .get_default_face_mesh_iris_connections_style())
        





    cv.imshow("Webcam", frame)
    if cv.waitKey(1) == ord(" "):
        break
cam.release()
cv.destroyAllWindows()

import cv2 as cv

cam = cv.VideoCapture(0)


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
    cv.imshow("Webcam", frame)

    if cv.waitKey(1) == ord(" "):
        break
cam.release()
cv.destroyAllWindows()

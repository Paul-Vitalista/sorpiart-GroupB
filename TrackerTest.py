import cv2
import time
import math
import mediapipe as mp
import subprocess

width=1920
height=1080
cap = cv2.VideoCapture(0,cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FPS, 30)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
index_y = 0

def init_videocapture():
    global width, height
    camera = cv2.VideoCapture(0, cv2.CAP_V4L2)
    camera.set(cv2.CAP_PRbpm,OP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    camera.set(cv2.CAP_PROP_FPS, 30)
    return camera
def rescale_frame(frame, percent=100):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

while True:               
                        _, frame = cap.read()
                        frame = rescale_frame(frame, percent=20)
                        frame = cv2.flip(frame, 1)
                        frame_height, frame_width, _ = frame.shape
                        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        output = hand_detector.process(rgb_frame)
                        hands = output.multi_hand_landmarks
                        if hands:
                            for hand in hands:
                                drawing_utils.draw_landmarks(frame, hand)
                                landmarks = hand.landmark
                                for id, landmark in enumerate(landmarks):
                                    x = int(landmark.x*width)
                                    y = int(landmark.y*height)
                                        
                                    if id == 8:
                                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
        #                                 return x

                                    if id == 4:
                                        cv2.circle(img=frame, center=(x,y), radius=10, color=(255, 105, 180))
                                    print("X is {} and Y is {}. Type of X is {} and Y is {}".format(x,y, type(x), type(y)))
                        cv2.imshow("Image", frame)
                        cv2.waitKey(1)
                        
                    
def goodtracker(a):
    global x,y,cx,cy
    if a == 1:
            while True:               
                _, frame = cap.read()
                frame = rescale_frame(frame, percent=20)
                frame = cv2.flip(frame, 1)
                frame_height, frame_width, _ = frame.shape
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                output = hand_detector.process(rgb_frame)
                hands = output.multi_hand_landmarks
                if hands:
                    for hand in hands:
                        drawing_utils.draw_landmarks(frame, hand)
                        landmarks = hand.landmark
                        for id, landmark in enumerate(landmarks):
                            x = int(landmark.x*width)
                            y = int(landmark.y*height)
                                
                            if id == 8:
                                cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                                return y 

                            if id == 4:
                                cv2.circle(img=frame, center=(x,y), radius=10, color=(255, 105, 180))
#                             print("X is {} and Y is {}. Type of X is {} and Y is {}".format(x,y, type(x), type(y)))
                        
                        return  
from tkinter import *
from tkinter import ttk
from pix2music import *
import os
import cv2
import mediapipe as mp
import time
import autopy
import pyautogui
##creating toggle function
main = Tk()

def btnpress(h):
    global toggle, button
    i = h[0]; j = h[1]
    print("i is {} and j is {}".format(i,j))
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
        print("ON  toggle is {}".format(toggle))
    else:
        toggle[i][j]=0
        button[i][j].config(bg="lightgrey")
        print("OFF toggle is {}".format(toggle))
        
        
#Color grid

def Lightdown(h):
    global a
    if a==0:
        colorRow[0][0].config(bg="yellow")
    else:
        colorRow[0][0].config(bg="lightgrey")
        
    if a==a and a != 14:
        colorRow[a][j].config(bg="lightgrey")
        a=a+1
        colorRow[a][j].config(bg="yellow")
    else:
        a=14
        colorRow[a][j].config(bg="yellow")
def Lightup(h):
    global a
    if a==a and a !=0:
        colorRow[a][j].config(bg="lightgrey")
        a=a-1
        colorRow[a][j].config(bg="yellow")
    else:
        a=0
        colorRow[a][j].config(bg="yellow")
#binding

def downpressed (event):
    global h,toggle,button,a
    if a==a and a != 14:
        a=a+1
    else:
        a=14
def uppressed (event):
    global h,toggle,button,a
    if a==a and a != 0:
        a=a-1  
    else:
        a=0
    
def apressed (event):
    global h,toggle,button,a
    h=[a,0]
    i = h[0]; j = h[1]
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=0
        button[i][j].config(bg="lightgrey")
def spressed (event):
    global h,toggle,button,a
    h=[a,1]
    i = h[0]; j = h[1]
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=0
        button[i][j].config(bg="lightgrey")
def dpressed (event):
    global h,toggle,button,a
    h=[a,2]
    i = h[0]; j = h[1]
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=0
        button[i][j].config(bg="lightgrey")
def fpressed (event):
    global h,toggle,button,a
    h=[a,3]
    i = h[0]; j = h[1]
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=0
        button[i][j].config(bg="lightgrey")
def gpressed (event):
    global h,toggle,button
    h=[a,4]
    i = h[0]; j = h[1]
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=0
        button[i][j].config(bg="lightgrey")
def hpressed (event):
    global h,toggle,button
    h=[a,5]
    i = h[0]; j = h[1]
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=0
        button[i][j].config(bg="lightgrey")
def jpressed (event):
    global h,toggle,button
    h=[a,6]
    i = h[0]; j = h[1]
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=0
        button[i][j].config(bg="lightgrey")
def kpressed (event):
    global h,toggle,button
    h=[a,7]
    i = h[0]; j = h[1]
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=0
        button[i][j].config(bg="lightgrey")
    
##Music playing function
def play():
    global toggle, button,h,a,colorRow
    pix2music(variable.get(), BPM.get(), Notevariable.get() , toggle)
    button[i][j].config(state= DISABLED)
    
##clearing all keys
def Clear ():
    global toggle, button,h,a,colorRow,canvas
    canvas.delete("all")
    for i in range(row):
        for j in range(col):
            toggle[i][j] = 0
            button[i][j].config(bg="lightgrey")
    print("toggle is {}".format(toggle))

def OpenCam():
    global pTime,cTime,mpDraw,hands,mphands,cap,prev,toggle,button,row,col,a,cx,cy
    start = time.time()
    for x in range(10):
        while True:
            success, img = cap.read()
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    landmarks = hand.landmark
                    for id, lm in enumerate(handLms.landmark):
                        x = int(landmark.x*frame_width)
                        y = int(landmark.y*frame_height)
                        if id == 8:
                            cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                            index_x = screen_width/frame_width*x
                            index_y = screen_height/frame_height*y

                        if id == 4:
                            cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                            thumb_x = screen_width/frame_width*x
                            thumb_y = screen_height/frame_height*y
                            print('outside', abs(index_y - thumb_y))
                            if abs(index_y - thumb_y) < 20:
                                pyautogui.click()
                                pyautogui.sleep(1)
                            elif abs(index_y - thumb_y) < 100:
                                pyautogui.moveTo(index_x, index_y)
                #print(id,lm)
                        h, w, c = img.shape
                        cx, cy = int(lm.x *w), int(lm.y*h)
                        print(cx,cy)
                        
                #if id ==0:
                        cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)
                        pyautogui.moveTo(cx,cy)

                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
                
                time.sleep(0.5)
            if time.time() - start > 5:
                return 

def Clearcanvas():
    global toggle, button,h,a,colorRow,canvas
    canvas.delete("all")
    for i in range(row):
        for j in range(col):
            toggle[i][j] = 0
            button[i][j].config(bg="lightgrey")
    
def click(click_event):
    global prev
    prev = click_event


def move(move_event):
    global prev, toggle,button,row,col,a,cx,cy
    canvas.create_line(prev.x, prev.y, move_event.x, move_event.y, width=2)
    prev = move_event
    canvasx = int(prev.x/152)
    canvasy = int(prev.y/62)
    #y = width
    #x = height
    print("X is {} and Y is {}".format(canvasx,canvasy))
    h = [canvasy, canvasx]
    i = h[0]; j = h[1]
    print("y is {} and x is {}".format(i,j))
    if toggle[i][j]== 0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=1


#Creating Tkinker Popup

my_notebook = ttk.Notebook(main)
my_notebook.grid()

frame1 = Frame(my_notebook)
frame2 = Frame(my_notebook)

frame1.grid()
frame2.grid()

my_notebook.add(frame1, text="Keyboard Mode")
my_notebook.add(frame2, text="Draw Mode")

a=0
##grid layout
row=15
col=8


##toggle
toggle = [i for i in range(row)]
for i in range(row):
    toggle[i] = [j for j in range(col)]
for i in range(row):
    for j in range(col):
        toggle[i][j] = 0

    
##grid generation
button = [i for i in range(row)]
for i in range(row):
    button[i]= [j for j in range(col)]
   
for i in range(row):
    for j in range(col):
        button[i][j] = Button(frame1, command = lambda hello = [i,j]:btnpress(hello),
                              width=13,pady=17 ,bg="lightgrey",font=("Arial",15))
        button[i][j].grid(row=i,column=j) 

#Row grid
colorRow = [i for i in range(15)]
for i in range(15):
    colorRow[i]= [j for j in range(1)]
   
for i in range(15):
    for j in range(1):
        colorRow[i][j] = Button(frame1, command = lambda hello = [i,j]:Lightup(hello),
                              width=13,pady=21 ,bg="lightgrey")
        colorRow[i][j].grid(row=i,column=17)
        colorRow[i][j].invoke()
##creating sound array
option= ["pluck","sine","square","triangle","trapezium","sawtooth"]
variable = StringVar(frame1)
variable.set(option[0])

Noteoption= ["C1","C2","C3","C4","C5","C6"]
Notevariable = StringVar(frame1)
Notevariable.set(Noteoption[3])

##creating Slider for BPM
BPM= Scale(frame1 , from_=350, to=360, orient = HORIZONTAL, label = "BPM", font=("Arial",12))
BPM.grid(row=0, column=19)

BPM= Scale(frame2 , from_=350, to=360, orient = HORIZONTAL, label = "BPM", font=("Arial",12))
BPM.grid(row=0, column=4)

##Creating drop down menu
Sound = OptionMenu(frame1, variable, *option)
Sound.grid(row=2, column=19)

Note = OptionMenu(frame1, Notevariable, *Noteoption)
Note.grid(row=2, column=18)

##creating button for Playing sound and clearing

Play = Button(frame1, text = "Play" ,command = play, width =10, pady = 19, bg="green",fg="white",font=("Arial",13))
Play.grid(row=0, column=18)

Play = Button(frame2, text = "Play" ,command = play, width =10, pady = 19, bg="green",fg="white",font=("Arial",13))
Play.grid(row = 0 , column=2)

Clear = Button(frame1, text= "Clear", command = Clear, width =10, pady = 19, bg="red",fg="white",font=("Arial",13))
Clear.grid(row=1, column=18)

Clear2 = Button(frame2, text= "Clear", command = Clearcanvas, width =10, pady = 19, bg="red",fg="white",font=("Arial",13))
Clear2.grid(row=0, column=3)


main.bind('1',apressed)
main.bind('2',spressed)
main.bind('3',dpressed)
main.bind('4',fpressed)
main.bind('5',gpressed)
main.bind('6',hpressed)
main.bind('7',jpressed)
main.bind('8',kpressed)
main.bind('<Down>',downpressed)
main.bind('<Down>',Lightdown)
main.bind('<Up>',uppressed)
main.bind('<Up>',Lightup)
main.bind('<Return>',lambda event:play())
main.bind('<C>',lambda event:Clear())
main.geometry("1920x1080")

canvas = Canvas(frame2, width = col*150, height=row*60, bg='white')
canvas.grid( row = 0 ,column=1)
canvas.bind('<Button-1>', click)
canvas.bind('<B1-Motion>',move)

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=4,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0



#     cTime = time.time()
#     fps = 1/(cTime-pTime)
#     pTime = cTime

#     cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    
#     cv2.imshow("Image", img)
#     cv2.waitKey(1)

    
Opencam = Button(frame2, text= "OpenCam", command = OpenCam, width =10, pady = 19, bg="red",fg="white",font=("Arial",13))
Opencam.grid(row=0, column=6)
main.mainloop()






from tkinter import *
from tkinter import ttk
from pix2music import *
from goodtracker import *
import os
import cv2
import mediapipe as mp
import time
##creating toggle function

def btnpress(h):
    global toggle, button
    i = h[0]; j = h[1]
    print("i is {} and j is {}".format(i,j))
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
#         print("ON  toggle is {}".format(toggle))
        print("ON  button is {}".format(button))
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
        colorRow[0][0].config(bg="grey")
        
    if a==a and a != 14:
        colorRow[a][j].config(bg="grey")
        a=a+1
        colorRow[a][j].config(bg="yellow")
    else:
        a=14
        colorRow[a][j].config(bg="yellow")
def Lightup(h):
    global a
    if a==a and a !=0:
        colorRow[a][j].config(bg="grey")
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
           


def onepressed (event):
    global h,toggle,button,a
    h=[a,0]
    i = h[0]; j = h[1]
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=0
        button[i][j].config(bg="lightgrey")
def twopressed (event):
    global h,toggle,button,a
    h=[a,1]
    i = h[0]; j = h[1]
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=0
        button[i][j].config(bg="lightgrey")
def threepressed (event):
    global h,toggle,button,a
    h=[a,2]
    i = h[0]; j = h[1]
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=0
        button[i][j].config(bg="lightgrey")
def fourpressed (event):
    global h,toggle,button,a
    h=[a,3]
    i = h[0]; j = h[1]
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=0
        button[i][j].config(bg="lightgrey")
def fivepressed (event):
    global h,toggle,button
    h=[a,4]
    i = h[0]; j = h[1]
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=0
        button[i][j].config(bg="lightgrey")
def sixpressed (event):
    global h,toggle,button
    h=[a,5]
    i = h[0]; j = h[1]
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=0
        button[i][j].config(bg="lightgrey")
def sevenpressed (event):
    global h,toggle,button
    h=[a,6]
    i = h[0]; j = h[1]
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=0
        button[i][j].config(bg="lightgrey")
def eightpressed (event):
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

def play2():
    global toggle, button,h,a,colorRow
    pix2music(variable.get(), BPM2.get(), Notevariable.get() , toggle)
##clearing all keys
def Clear ():
    global toggle, button,h,a,colorRow,canvas
    canvas.delete("all")
    for i in range(row):
        for j in range(col):
            toggle[i][j] = 0
            button[i][j].config(bg="lightgrey")
    print("toggle is {}".format(toggle))
    


def Clearcanvas():
    global toggle, button,h,a,colorRow,canvas,updatecanvas
    canvas.delete("all")
    for i in range(row):
        for j in range(col):
            toggle[i][j] = 0
            button[i][j].config(bg="lightgrey")
    
    
def click(click_event):
    global prev
    prev = click_event


def OpenCam():
    global prev, toggle,button,row,col,cx,cy,move_event,e,f,Beat
    z=1
    a=1
    c=0
    flag = 0
    
    while True:
        
        c= c+1
        t = goodtracker(a)

        if flag == 0:
            print("c is {}".format(c))
           
            x = t[0]
            y = t[1]
            cx = t[0]
            cy = t[1]
            flag = 1; print("Flag is {}".format(flag));
            cxp = cx
            cyp = cy
        else:
            time.sleep(0.5)
            x = cxp
            y = cyp
            cx = t[0]
            cy = t[1]
            cxp = cx
            cyp = cy
            print("Flag is {}".format(flag))
        print("x is {} and y is {}".format(x,y))
        print("cx is {} and cy is {}".format(cx,cy))
        canvas.create_line(x,y,cx,cy,width=2)
        canvasx = int(x/152) 
        canvasy = int(y/62)
            #y = width
            #x = height
        h = [canvasy, canvasx]
        i = h[0]; j = h[1]
        print("canx is {} and cany is {}".format(j,i))
        if toggle[i][j]== 0:
            toggle[i][j]=1
            button[i][j].config(bg="green")
        else:
            toggle[i][j]=1
        if c == 0:
            pix2music("Pluck", 180, "C4",Beat)
        elif c == 1:
            time.sleep(1)
            pix2music("Pluck", 180, "C4",Beat)
        elif c == 2:
            time.sleep(1)
            pix2music("Pluck", 180, "C4",Beat)
        elif c == 3:
            time.sleep(1)
            pix2music("Pluck", 180, "C4",Beat)
        elif c == 4:
            time.sleep(1)
            pix2music("Pluck", 180, "C4",Beat)
        elif c == 5:
            time.sleep(1)
            pix2music("Pluck", 180, "C4",Beat)
        else:
            return
                        
def move(move_event):
    global prev, toggle,button,row,col,a,cx,cy
    canvas.create_line(prev.x, prev.y, move_event.x, move_event.y, width=2)
    prev = move_event
    canvasx = int(prev.x/152)
    canvasy = int(prev.y/62)
    #y = width
    #x = height
    print ("prevX is {} prevY is {}".format(prev.x,prev.y))
    print ("moveX is {} moveY is {}".format(move_event.x,move_event.y))
#     print("X is {} and Y is {}".format(canvasx,canvasy))
    h = [canvasy, canvasx]
    i = h[0]; j = h[1]
    print("x is {} and y is {}".format(j,i))
    if toggle[i][j]== 0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=1


# start function
def start():
    global running, toggle, button,h,a,colorRow,canvas
    canvas.delete("all")
    for i in range(row):
        for j in range(col):
            toggle[i][j] = 0
            button[i][j].config(bg="lightgrey")
    print("toggle is {}".format(toggle))
    if not running:
        update()
        running = True
    else:
        stopwatch_label.after_cancel(update_time)
        running = True
        update()
    # set variables back to zero
    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0
    # set label back to zero
    stopwatch_label.config(text='00:00:00')

# pause function
def pause():
    global running
    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False

def update():
    # update seconds with (addition) compound assignment operator
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    # format time to include leading zeros
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    # update timer label after 1000 ms (1 second)
    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    # after each second (1000 milliseconds), call update function
    # use update_time variable to cancel or pause the time using after_cancel
    global update_time
    update_time = stopwatch_label.after(1000, update)

def preset():
    global toggle,button,h,Button
    toggle = [[1, 0, 0, 1, 0, 0, 0, 0],
              [1, 1, 0, 1, 0, 0, 0, 0],
              [1, 0, 1, 1, 0, 0, 0, 0],
              [1, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 1, 0, 0],
              [0, 0, 1, 0, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 1, 1, 1],
              [0, 0, 0, 1, 0, 1, 0, 1],
              [0, 0, 0, 1, 0, 1, 1, 1],
              [0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]
    preset_row = [0,1,2,3,1,2,0,1,2,3,5,5,6,6,7,8,9,10,11,8,8,8,9,9,10,10,10,11,12,13]
    preset_col =[0,0,0,0,1,2,3,3,3,3,1,5,2,4,3,3,3,3,3,7,6,5,7,5,7,6,5,5,5,5]
    for i in range(len(preset_row)):
        button[preset_row[i]][preset_col[i]].config(bg = "green")
      
# #Creating Tkinker Popup
# stopwatch_label = main.Label(text='00:00:00', font=('Arial', 80))
# stopwatch_label.grid(row= 6, col=17)

main = Tk()

my_notebook = ttk.Notebook(main)
my_notebook.grid()

frame1 = Frame(my_notebook)
frame2 = Frame(my_notebook)

frame1.grid()
frame2.grid()

my_notebook.add(frame1, text="Keyboard Mode")
my_notebook.add(frame2, text="Draw Mode")

a=0
# use a boolean variable to help control state of time (running or not running)
running = False
# time variables initially set to 0
hours, minutes, seconds = 0, 0, 0
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
##Beat
Beat = [i for i in range(1)]
for i in range(1):
    Beat[i] = [j for j in range(1)]
for i in range(1):
    for j in range(1):
        Beat[i][j] = 1
    
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
                              width=13,pady=21 ,bg="grey")
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
BPM= Scale(frame1 , from_=60, to=180, orient = HORIZONTAL, label = "BPM", font=("Arial",12))
BPM.grid(row=0, column=19)

BPM2= Scale(frame2 , from_=60, to=180, orient = HORIZONTAL, label = "BPM", font=("Arial",12))
BPM2.grid(row=0, column=4)

##Creating drop down menu
Sound = OptionMenu(frame1, variable, *option)
Sound.grid(row=2, column=19)

Note = OptionMenu(frame1, Notevariable, *Noteoption)
Note.grid(row=2, column=18)

##creating button for Playing sound and clearing

preset = Button(frame1, text = "NYP" ,command = preset, width =10, pady = 19, bg="green",fg="white",font=("Arial",13))
preset.grid(row=4, column=18)

Play = Button(frame1, text = "Play" ,command = play, width =10, pady = 19, bg="green",fg="white",font=("Arial",13))
Play.grid(row=0, column=18)

Play = Button(frame2, text = "Play" ,command = play2, width =10, pady = 19, bg="green",fg="white",font=("Arial",13))
Play.grid(row = 0 , column=2)

Clear = Button(frame1, text= "Clear", command = Clear, width =10, pady = 19, bg="red",fg="white",font=("Arial",13))
Clear.grid(row=1, column=18)

Clear2 = Button(frame2, text= "Clear", command = Clearcanvas, width =10, pady = 19, bg="red",fg="white",font=("Arial",13))
Clear2.grid(row=0, column=3)


main.bind('1',onepressed)
main.bind('2',twopressed)
main.bind('3',threepressed)
main.bind('4',fourpressed)
main.bind('5',fivepressed)
main.bind('6',sixpressed)
main.bind('7',sevenpressed)
main.bind('8',eightpressed)
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
Opencam.grid(row=1, column=4)

# label to display time
stopwatch_label = Label(frame1,text='00:00:00', font=('Arial', 25))
stopwatch_label.grid(row = 7 , column = 18)

keyboardtiming_label = Label(frame1,text='Keyboard Avg:', font=('Arial', 15))
keyboardtiming_label.grid(row = 5 , column = 18)

mousetiming_label = Label(frame1,text='Mouse Avg:', font=('Arial', 15))
mousetiming_label.grid(row = 5 , column = 19)

keyboardtimingNo_label = Label(frame1,text='22', font=('Arial', 15))
keyboardtimingNo_label.grid(row = 6 , column = 18)

mousetimingNo_label = Label(frame1,text='18', font=('Arial', 15))
mousetimingNo_label.grid(row = 6 , column = 19)

TrackerStop_label = Label(frame2,text='LOOK HERE', font=('Arial', 15))
TrackerStop_label.grid(row = 1 , column = 3)
# start, pause, reset, quit buttons
start_button = Button(frame1, text='start', width =10, pady = 19, font=('Arial', 10),bg="green",fg="white", command=start)
start_button.grid(row = 8 , column = 18)
pause_button = Button(frame1, text='stop', width =10, pady = 19, font=('Arial', 10),bg="red",fg="white"  , command=pause)
pause_button.grid(row = 8 , column = 19)

main.mainloop()






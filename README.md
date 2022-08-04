# Table of Contents:
* [Our Purpose](#our-purpose)
* [Hardware Used](#hardware-used)
* [Sodtware Used](#software-used)
* [Features Added](#features-added)
* [GUI](#gui)
* [Installation Process](#installation-process)
* [Code](#code)

# Our Purpose
Our group was interested in what different art drawings would sound like. We wanted to create GUI that is able to audibly hear drawings and paintings and have a way to listen to what their own art sounds like.

# Hypothesis 
The hypothesis of our project is the raspberry pi is able to create a working GUI that has a grid mode that can play different notes in a sequence. Have a draw mode that can accurately represent on the grid.

# GUI
<h2>Keyboard Mode</h2>

![Keyboard Mode GUI](https://media.discordapp.net/attachments/965809568808575027/1004398042348257291/Annotation_Keyboard_Mode.png?width=1215&height=587)

<h2>Draw Mode</h2>

![Drawing Mode GUI](https://media.discordapp.net/attachments/965809568808575027/1004398042834813088/Annotation_Draw_Mode.png?width=1014&height=597)

# Installation Process
<h2>Step 1: Open terminal and update the Pi using the code below.

```
sudo apt-get update

sudo apt-get upgrade
```
<h2>Step 2: Ensure the GPU has 128MB of memory

```
sudo raspi-config
```
<h2>Go down to Performance Options and hit Enter</h2>

![Step 2 Pt 1](https://media.discordapp.net/attachments/965809568808575027/1004404511969914921/unknown.png)
<h2> Then go down to GPU Memory and hit Enter</h2>

![Step 2 Pt 2](https://media.discordapp.net/attachments/965809568808575027/1004404864631189634/unknown.png)
<h2> Then type in 128 and click Ok and reboot</h2>

![Step 2 Pt 3](https://media.discordapp.net/attachments/965809568808575027/1004418923766218782/unknown.png)

<h2> Then proceed to install the required items with the code below </h2>

```
sudo apt-get install build-essential cmake git unzip pkg-config

sudo apt-get install libjpeg-dev libpng-dev libtiff-dev

sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev

sudo apt-get install libgtk2.0-dev libcanberra-gtk*

sudo apt-get install libxvidcore-dev libx264-dev libgtk-3-dev

sudo apt-get install python3-dev python3-numpy python3-pip

sudo apt-get install python-dev python-numpy

sudo apt-get install libtbb2 libtbb-dev libdc1394-22-dev

sudo apt-get install libv4l-dev v4l-utils

sudo apt-get install libjasper-dev libopenblas-dev libatlas-base-dev

sudo apt-get install libblas-dev liblapack-dev gfortran

sudo apt-get install gcc-arm*

sudo apt-get install protobuf-compiler
```

<h2>Step 3: Install OpenCV</h2>

```
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.5.zip

wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.2.0.zip

unzip opencv.zip

unzip opencv_contrib.zip


```
Step 4: Install Mediapipe

```
sudo apt install ffmpeg python3-opencv python3-pip

sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1 libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23

sudo pip3 install mediapipe-rpi4
```

## Hardware Used  
- We are using raspberry pi as it uses Linux OS, which is open source, which makes users able to create their own software while still having great security as well as get codes from other sources and it can still be changed to the user's liking. Using Linux Os devices is also more cost efficient in both the hardware and software side as well as less maintenance cost as much as other OS Software. Raspberry Pi also has many component interfaces such as HDMI, Ethernet, Many GPIOs, and USB 2.0 and 3.0.
 
- We  used a monitor for our display out and for the user to see what they are clicking on. And lastly a pair of speakers for the user to be able to hear the sounds that are playing from the notes they clicked on in the program on screen.

## Software used 
- The main coding platform we are using is Thonny Python IDE. Thonny is useful especially more towards beginners as it is a free integrated development environment. As compared to other coding languages as well as python 3, Thonny is a more suitable coding platform for learning.

 - For our camera feature, we are using OpenCv for hand tracking. OpenCV is an open source computer vision and machine learning software library. For our purpose, OpenCV is the best machine learning software as compared to other softwares such as tensorflow as OpenCV processes based on images and videos, while tensorflow builds machine learning models and is more used for deep learning applications.

## Features Added
- Keyboard Mode
-- On the GUI, you will be able to use the keys 1 to 8 to press the different buttons on the GUI, there will be a yellow rectangle at the side to indicate which row would is active for the user to press on.

- Canvas Mode
-- There is another tab that will switch over to a canvas where the user will be able to use the mouse cursor and draw on it. The drawing will then be accurately represented back on the grid in order to play the sound that the drawing makes.

- Draw using your own hands
-- Using a USB webcam, the user will be able to draw shapes or objects using the motion on their hands which will reflect back on the grid and creates a shape that will play a set of sound notes.

# Code

```
from  tkinter  import  *
from  tkinter  import  ttk
from pix2music import  *
from  goodtracker  import  *
import  os
import  cv2
import  mediapipe  as  mp
import  time
```
Implementing the toggle function which will activate and change the color of a button when pressed to show whether a button is active or not. 
```
def btnpress(h):
    global toggle, button
    i = h[0]; j = h[1]
    print("i is {} and j is {}".format(i,j))
    if toggle[i][j]==0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=0
        button[i][j].config(bg="lightgrey")

```

This implements a function that highlights a box in yellow to indicate which row you are on
```
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
```

This defines the button presses using the up and down arrow keys
```
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
```
This creates the function to take the input from pressing the numbers 1-8 on the keyboard
```
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
```
Takes the different Sounds from the sound library from pix2music file and implements the sounds into the program which can be played when selected
```
def play():
    global toggle, button,h,a,colorRow
    pix2music(variable.get(), BPM.get(), Notevariable.get() , toggle)

def play2():
    global toggle, button,h,a,colorRow
    pix2music(variable.get(), BPM2.get(), Notevariable.get() , toggle)
```
Creates a clear function for the keyboard page
```
def Clear ():
    global toggle, button,h,a,colorRow,canvas
    canvas.delete("all")
    for i in range(row):
        for j in range(col):
            toggle[i][j] = 0
            button[i][j].config(bg="lightgrey")
```

Creates a clear function for the drawing page
```
def Clearcanvas():
    global toggle, button,h,a,colorRow,canvas,updatecanvas
    canvas.delete("all")
    for i in range(row):
        for j in range(col):
            toggle[i][j] = 0
            button[i][j].config(bg="lightgrey")
```

On mouse left click get the X & Y coordinates
```
def click(click_event):
    global prev
    prev = click_event
```

As the mouse cursor moves get the X & Y coordinates of the mouse from click function and draw it out on the canvas 
```
def move(move_event):
    global prev, toggle,button,row,col,a,cx,cy
    canvas.create_line(prev.x, prev.y, move_event.x, move_event.y, width=2)
    prev = move_event
    canvasx = int(prev.x/152)
    canvasy = int(prev.y/62)
    #y = width
    #x = height
    h = [canvasy, canvasx]
    i = h[0]; j = h[1]
    if toggle[i][j]== 0:
        toggle[i][j]=1
        button[i][j].config(bg="green")
    else:
        toggle[i][j]=1
```

This will  run the camera function and have it track the hands of the user for 5 seconds
every 1 second there will be a sound played by the speakers to represent that the camera have taken a picture of your current location of user hands and input it as 1 X & Y coordinates repeated 5 times to draw 5 lines in a continuous line
```
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
```

Creates a preset for the users to replicate as fast as they can
```
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
```
Creating the Tkinter pop up and making the window have 2 tabs, also set a to 0
```
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
```
Setting the timer into a not running state and hour minutes and seconds are set to 0
```
running = False

hours, minutes, seconds = 0, 0, 0
```

Gives the grid the number of rows and columns and gives each button its own X and Y value. 
```

row=15
col=8

toggle = [i for i in range(row)]
for i in range(row):
    toggle[i] = [j for j in range(col)]
for i in range(row):
    for j in range(col):
        toggle[i][j] = 0

```

A constant on state toggle for pix2music to call upon so that it will always play sound with out user inputs
used for the sound produce when the camera is turn on
```

Beat = [i for i in range(1)]
for i in range(1):
    Beat[i] = [j for j in range(1)]
for i in range(1):
    for j in range(1):
        Beat[i][j] = 1
```
The grid generation for the GUI to properly align and arrange the button physical position
```
button = [i for i in range(row)]
for i in range(row):
    button[i]= [j for j in range(col)]

for i in range(row):
    for j in range(col):
        button[i][j] = Button(frame1, command = lambda hello = [i,j]:btnpress(hello),
                              width=13,pady=17 ,bg="lightgrey",font=("Arial",15))
button[i][j].grid(row=i,column=j)

```
The grid for the yellow button to show the user what row they are on
```
colorRow = [i for i in range(15)]
for i in range(15):
    colorRow[i]= [j for j in range(1)]
   
for i in range(15):
    for j in range(1):
        colorRow[i][j] = Button(frame1, command = lambda hello = [i,j]:Lightup(hello),
                              width=13,pady=21 ,bg="grey")
        colorRow[i][j].grid(row=i,column=17)
        colorRow[i][j].invoke()
```

Creating sound array taken from the sound library
```
option= ["pluck","sine","square","triangle","trapezium","sawtooth"]
variable = StringVar(frame1)
variable.set(option[0])

Noteoption= ["C1","C2","C3","C4","C5","C6"]
Notevariable = StringVar(frame1)
Notevariable.set(Noteoption[3])
```
Creating Slider for BPM taken from the sound library
```
BPM= Scale(frame1 , from_=60, to=180, orient = HORIZONTAL, label = "BPM", font=("Arial",12))
BPM.grid(row=0, column=19)

BPM2= Scale(frame2 , from_=60, to=180, orient = HORIZONTAL, label = "BPM", font=("Arial",12))
BPM2.grid(row=0, column=4)
``` 
Creating drop down menu for the sound profile
```
Sound = OptionMenu(frame1, variable, *option)
Sound.grid(row=2, column=19)
``` 
Creating drop down menu for which pitch to start at

```
Note = OptionMenu(frame1, Notevariable, *Noteoption)
Note.grid(row=2, column=18)
```	
Creating button for activating the preset,  playing sound and clearing for both keyboard and draw modes
```	
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
```
To bind the buttons on the GUI to the keyboard button presses
```
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
```

Setting the size of the tkinter pop up
```
main.geometry("1920x1080")
```

Creating canvas size and position 
```
canvas = Canvas(frame2, width = col*150, height=row*60, bg='white')
canvas.grid( row = 0 ,column=1)
```

binding the left click of the mouse and the move motion of the mouse to canvas
```
canvas.bind('<Button-1>', click)
canvas.bind('<B1-Motion>',move)
```

Setting up the camera 

```
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=4,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
```
Creating the OpenCam button on the tkinter GUI on the draw mode page
```
Opencam = Button(frame2, text= "OpenCam", command = OpenCam, width =10, pady = 19, bg="red",fg="white",font=("Arial",13))
Opencam.grid(row=1, column=4)
```
Creating the Stopwatch time label on the keyboard page and the label for avg timing of other users
```
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
```
The start and pause button for the stopwatch timer
```
start_button = Button(frame1, text='start', width =10, pady = 19, font=('Arial', 10),bg="green",fg="white", command=start)
start_button.grid(row = 8 , column = 18)

pause_button = Button(frame1, text='stop', width =10, pady = 19, font=('Arial', 10),bg="red",fg="white"  , command=pause)
pause_button.grid(row = 8 , column = 19)
```
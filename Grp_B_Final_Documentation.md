# Table of Contents:
* [Our Purpose](#Our-purpose)
* [Why we need this product](#why-we-need-this-product)
* [Ideation](#ideation)
* [Hardware Used](#hardware-used)
* [Sodtware Used](#software-used)
* [GUI](#gui)
* [Block Diagram](#Installation-Process)
* [Code](#Code)

# Our Purpose
Our group was interested in what different art drawings would sound like. We wanted to create GUI that is able to audibly hear drawings and paintings and have a way to listen to what their own art sounds like.
# Hypothesis 
The hypothesis of our project is the raspberry pi is able to create a working GUI that has a grid mode that can play different notes in a sequence. Have a draw mode that can accurately represent on the grid.
# Installation Process
Step 1: Open terminal and update the Pi using the code below.
```
sudo apt-get update

sudo apt-get upgrade
```
Step 2: Ensure the GPU has 128MB of memory
```
sudo raspi-config
```
![enter image description here](https://media.discordapp.net/attachments/965809568808575027/1004404511969914921/unknown.png)
Go down to Performance Options and hit Enter
![enter image description here](https://media.discordapp.net/attachments/965809568808575027/1004404864631189634/unknown.png)
Then go down to GPU Memory and hit Enter
![enter image description here](https://media.discordapp.net/attachments/965809568808575027/1004418923766218782/unknown.png)
Then type in 128 and click Ok and reboot
=======

## Hardware Used  
We are using raspberry pi as it uses Linux OS, which is open source, which makes users able to create their own software while still having great security as well as get codes from other sources and it can still be changed to the user's liking. Using Linux Os devices is also more cost efficient in both the hardware and software side as well as less maintenance cost as much as other OS Software. Raspberry Pi also has many component interfaces such as HDMI, Ethernet, Many GPIOs, and USB 2.0 and 3.0.
 
We  used a monitor for our display out and for the user to see what they are clicking on. And lastly a pair of speakers for the user to be able to hear the sounds that are playing from the notes they clicked on in the program on screen.

## Software used 
The main coding platform we are using is Thonny Python IDE. Thonny is useful especially more towards beginners as it is a free integrated development environment. As compared to other coding languages as well as python 3, Thonny is a more suitable coding platform for learning. 

## Features Added
- Keyboard Mode
-- On the GUI, you will be able to use the keys 1 to 8 to press the different buttons on the GUI, there will be a yellow rectangle at the side to indicate which row would is active for the user to press on.

- Canvas Mode
-- There is another tab that will switch over to a canvas where the user will be able to use the mouse cursor and draw on it. The drawing will then be accurately represented back on the grid in order to play the sound that the drawing makes.

- Draw using your own hands
-- Using a USB webcam, the user will be able to draw shapes or objects using the motion on their hands which will reflect back on the grid and creates a shape that will play a set of sound notes.

  -- This is done by using a software called Opencv, which is an open source computer vision and machine learning program.+

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
    print("toggle is {}".format(toggle))
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
*click code*
On mouse left click get the X & Y coordinates
```
def click(click_event):
    global prev
    prev = click_event
```
*move code*
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
```
*open cam code*


*start code*

*pause code*

*update code*

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
Gives the grid the number of rows and columns and gives each button its own X and Y value
```
row=15
col=8

toggle = [i for i in range(row)]
for i in range(row):
    toggle[i] = [j for j in range(col)]
for i in range(row):
    for j in range(col):
        toggle[i][j] = 0

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



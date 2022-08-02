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
import autopy
import  pyautogui
import  subprocess
```
Implementing the toggle function which will activate and change the color of a button when pressed to show whether a button is active or not. 
```
def  btnpress(h):

global  toggle, button

i  = h[0]; j  = h[1]

print("i is {} and j is {}".format(i,j))

if  toggle[i][j]==0:

toggle[i][j]=1

button[i][j].config(bg="green")

print("ON button is {}".format(button))

else:

toggle[i][j]=0

button[i][j].config(bg="lightgrey")

print("OFF toggle is {}".format(toggle))
```

This implements a function that highlights a box in yellow to indicate which row you are on
```
def  Lightdown(h):

global  a

if  a==0:

colorRow[0][0].config(bg="yellow")

else:

colorRow[0][0].config(bg="grey")

if  a==a  and  a  !=  14:

colorRow[a][j].config(bg="grey")

a=a+1

colorRow[a][j].config(bg="yellow")

else:

a=14

colorRow[a][j].config(bg="yellow")

def  Lightup(h):

global  a

if  a==a  and  a  !=0:

colorRow[a][j].config(bg="grey")

a=a-1

colorRow[a][j].config(bg="yellow")

else:

a=0

colorRow[a][j].config(bg="yellow")
```

This defines the button presses using the up and down arrow keys
```
def  downpressed (event):

global  h,toggle,button,a

if  a==a  and  a  !=  14:

a=a+1

else:

a=14

def  uppressed (event):

global  h,toggle,button,a

if  a==a  and  a  !=  0:

a=a-1

else:

a=0
```
This creates the function to take the input from pressing the numbers 1-8 on the keyboard
```
def  onepressed (event):

global  h,toggle,button,a

h=[a,0]

i  =  h[0]; j  =  h[1]

if  toggle[i][j]==0:

toggle[i][j]=1

button[i][j].config(bg="green")

else:

toggle[i][j]=0

button[i][j].config(bg="lightgrey")

def  twopressed (event):

global  h,toggle,button,a

h=[a,1]

i  =  h[0]; j  =  h[1]

if  toggle[i][j]==0:

toggle[i][j]=1

button[i][j].config(bg="green")

else:

toggle[i][j]=0

button[i][j].config(bg="lightgrey")

def  threepressed (event):

global  h,toggle,button,a

h=[a,2]

i  =  h[0]; j  =  h[1]

if  toggle[i][j]==0:

toggle[i][j]=1

button[i][j].config(bg="green")

else:

toggle[i][j]=0

button[i][j].config(bg="lightgrey")

def  fourpressed (event):

global  h,toggle,button,a

h=[a,3]

i  =  h[0]; j  =  h[1]

if  toggle[i][j]==0:

toggle[i][j]=1

button[i][j].config(bg="green")

else:

toggle[i][j]=0

button[i][j].config(bg="lightgrey")

def  fivepressed (event):

global  h,toggle,button

h=[a,4]

i  =  h[0]; j  =  h[1]

if  toggle[i][j]==0:

toggle[i][j]=1

button[i][j].config(bg="green")

else:

toggle[i][j]=0

button[i][j].config(bg="lightgrey")

def  sixpressed (event):

global  h,toggle,button

h=[a,5]

i  =  h[0]; j  =  h[1]

if  toggle[i][j]==0:

toggle[i][j]=1

button[i][j].config(bg="green")

else:

toggle[i][j]=0

button[i][j].config(bg="lightgrey")

def  sevenpressed (event):

global  h,toggle,button

h=[a,6]

i  =  h[0]; j  =  h[1]

if  toggle[i][j]==0:

toggle[i][j]=1

button[i][j].config(bg="green")

else:

toggle[i][j]=0

button[i][j].config(bg="lightgrey")

def  eightpressed (event):

global  h,toggle,button

h=[a,7]

i  =  h[0]; j  =  h[1]

if  toggle[i][j]==0:

toggle[i][j]=1

button[i][j].config(bg="green")

else:

toggle[i][j]=0

button[i][j].config(bg="lightgrey")
```
Takes the different Sounds from the sound library from pix2music file and implements the sounds into the program which can be played when selected
```
def  play():

global  toggle, button,h,a,colorRow

pix2music(variable.get(), BPM.get(), Notevariable.get() , toggle)
```
Creates a clear function for the keyboard page
```
def  Clear ():

global  toggle, button,h,a,colorRow,canvas

canvas.delete("all")

for  i  in  range(row):

for  j  in  range(col):

toggle[i][j] =  0

button[i][j].config(bg="lightgrey")

print("toggle is {}".format(toggle))
```

Creates a clear function for the drawing page
```
def  Clearcanvas():

global  toggle, button,h,a,colorRow,canvas,updatecanvas

canvas.delete("all")

for  i  in  range(row):

for  j  in  range(col):

toggle[i][j] =  0

button[i][j].config(bg="lightgrey")
```
*click code*

*open cam code*

*move code*

*start code*

*pause code*

*update code*

Creates a preset for the users to replicate as fast as they can
```
def  preset():

global  toggle,button,h,Button

toggle  = [[1, 0, 0, 1, 0, 0, 0, 0],

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

button[0][0].config(bg="green")

button[1][0].config(bg="green")

button[2][0].config(bg="green")

button[3][0].config(bg="green")

button[1][1].config(bg="green")

button[2][2].config(bg="green")

button[0][3].config(bg="green")

button[1][3].config(bg="green")

button[2][3].config(bg="green")

button[3][3].config(bg="green")

print("button is {}".format(button))
```
Gives the grid the number of rows and columns and gives each button its own X and Y value
```
row=15

col=8

toggle  = [i  for  i  in  range(row)]

for  i  in  range(row):

toggle[i] = [j  for  j  in  range(col)]

for  i  in  range(row):

for  j  in  range(col):

toggle[i][j] =  0
```
The grid generation for the GUI to properly align and arrange the button physical position
```
button = [i  for  i  in  range(row)]

for  i  in  range(row):

button[i]= [j  for  j  in  range(col)]

for  i  in  range(row):

for  j  in  range(col):

button[i][j] = Button(main,text=("(",i,",",j,")"), command = lambda  hello = [i,j]:btnpress(hello),

width=5,height=2 ,bg="lightgrey")

button[i][j].grid(row=i,column=j)
```
Creating sound array taken from the sound library
```
option= ["pluck","sine","square","triangle","trapezium","sawtooth"]

variable = StringVar(main)

variable.set(option[0])

Noteoption= ["C1","C2","C3","C4","C5","C6"]

Notevariable = StringVar(main)

Notevariable.set(Noteoption[3])
```
Creating Slider for BPM taken from the sound library
```
BPM= Scale(main , from_=60, to=180, orient = HORIZONTAL, label = "BPM", font=("Arial",10))

BPM.grid(row=0, column=17)
``` 
Creating drop down menu for the sound profile
```
Sound = OptionMenu(main, variable, *option)

Sound.grid(row=2, column=17)
``` 
 Creating drop down menu for which pitch to start at
```
Note = OptionMenu(main, Notevariable, *Noteoption)

Note.grid(row=2, column=16)
```
Creating button for activating the preset,  playing sound and clearing for both keyboard and draw modes
```	
preset  =  Button(frame1, text =  "NYP" ,command =  preset, width =10, pady =  19, bg="green",fg="white",font=("Arial",13))

preset.grid(row=4, column=18)

Play  =  Button(frame1, text =  "Play" ,command =  play, width =10, pady =  19, bg="green",fg="white",font=("Arial",13))

Play.grid(row=0, column=18)

Play  =  Button(frame2, text =  "Play" ,command =  play, width =10, pady =  19, bg="green",fg="white",font=("Arial",13))

Play.grid(row =  0 , column=2)

Clear  =  Button(frame1, text=  "Clear", command =  Clear, width =10, pady =  19, bg="red",fg="white",font=("Arial",13))

Clear.grid(row=1, column=18)

Clear2  =  Button(frame2, text=  "Clear", command =  Clearcanvas, width =10, pady =  19, bg="red",fg="white",font=("Arial",13))

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

main.bind('<C>',lambda event:Clear())
```



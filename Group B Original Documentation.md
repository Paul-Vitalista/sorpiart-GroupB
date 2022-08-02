# POC Document
Table of Contents:
* [Target audience](#target-audience)
* [Why we need this product](#why-we-need-this-product)
* [Ideation](#ideation)
* [Hardware Used](#hardware-used)
* [Sodtware Used](#software-used)
* [GUI](#gui)
* [Block Diagram](#block-diagram)
* [Code](#code)

## Target audience 
 Kids aged 7-17 and adults aged 18-25

##  Why we need this product
Because we want to show users a simple way to send secret messages through sound waves and decoding those messages by viewing the sound waves on a spectrogram

## Ideation 
Using Raspberry Pi and an integrated sound library with different sound profiles(pluck, sine, square, triangle, trapezium ,sawtooth) we are able to create a General User Interface(GUI) with buttons corresponding to musical notes(C, D, E, F, G, A, B, C), a slider to change the Beats Per Minute(BPM), and different pitches(C1, C2, C3, C4, C5, C6) to generate an image on the GUI and play sounds based on what buttons were selected and the speed set from the BPM.

## Hardware Used  
We are using raspberry pi as it uses Linux OS, which is open source, which makes users able to create their own software while still having great security as well as get codes from other sources and it can still be changed to the user's liking. Using Linux Os devices is also more cost efficient in both the hardware and software side as well as less maintenance cost as much as other OS Software. Raspberry Pi also has many component interfaces such as HDMI, Ethernet, Many GPIOs, and USB 2.0 and 3.0. 

We used a keyboard and mouse for the user to input which notes they want to click and input. We also used a monitor for our display out and for the user to see what they are clicking on. And lastly a pair of speakers for the user to be able to hear the sounds that are playing from the notes they clicked on in the program on screen.

## Software used 
The main coding platform we are using is Thonny Python IDE. Thonny is useful especially more towards beginners as it is a free integrated development environment. As compared to other coding languages as well as python 3, Thonny is a more suitable coding platform for learning.

## GUI 
The GUI will be the source that our audience will be able to view and interact with. By selecting the white tiles and activating it on the grid, the users can play the sound according to row order. The user can also select the different pitch and instrument notes by the dropdown menu next to the third row, a slider above to change the beats per minute in the sequence, a play and a clear to play and clear the grid respectively.

## Block Diagram
[Block Diagram Image](https://drive.google.com/file/d/1-kV42KhKw3Q5RIe435vX34I6stEaQiRd/view?usp=sharing)

![enter image description here](https://media.discordapp.net/attachments/772331726122385419/983279576450994206/unknown.png)
[GUI Image 1](https://drive.google.com/file/d/1Xpyf9LJJhRdqUZOvK_ZRCcPqF_suQXgf/view?usp=sharing)
![enter image description here](https://cdn.discordapp.com/attachments/965809568808575027/981735469937221672/unknown.png)
[GUI Image 2](https://drive.google.com/file/d/1_pDPBJFr4gqitkuSsbUljAc1yhCLvFZe/view?usp=sharing)
![enter image description here](https://cdn.discordapp.com/attachments/965809568808575027/981735540015640576/unknown.png)

# Code 

`from  tkinter  import *`

`from pix2music import *`

Implementing the toggle function in which will activate and change the color of a button when pressed to show whether a button is active or not. 

```
def  btnpress(h):

global  toggle, button

i = h[0]; j = h[1]

print("i is {} and j is {}".format(i,j))

if  toggle[i][j]==0:

toggle[i][j]=1

button[i][j].config(bg="green")

#print("ON toggle is {}".format(toggle))

else:

toggle[i][j]=0

button[i][j].config(bg="lightgrey")

#print("OFF toggle is {}".format(toggle))
```
Takes the different Sounds from the sound library from pix2music file and implements the sounds into the program which can be played when selected
```
def  play():

pix2music(variable.get(), BPM.get(), Notevariable.get() , toggle)
```
Clearing all active buttons to return to its original state of idle
```
def  Clear ():

global  toggle, button,h,a

for  i  in  range(row):

for  j  in  range(col):

toggle[i][j] = 0

button[i][j].config(bg="lightgrey")

print("toggle is {}".format(toggle))

```
Gives the grid the number of rows and columns and gives each button its own X and Y value 
```
row=15

col=8

##toggle

toggle = [i  for  i  in  range(row)]

for  i  in  range(row):

toggle[i] = [j  for  j  in  range(col)]

for  i  in  range(row):

for  j  in  range(col):

toggle[i][j] = 0

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
  

 Creating button for Playing sound and clearing
```	
Clear = Button(main, text= "Clear", command = Clear, padx = 10, pady = 2, bg="red")

Clear.grid(row=1, column=16)

Play = Button(main, text = "Play" ,command = play, padx = 10, pady = 2, bg="green")

Play.grid(row=0, column=16)
```

# Dilation Graph

this project is just a graph where you put a polygon and see how dilation affects it

## Tech stack

this project is made entirely using python and matplotlib library

## How to use

### Download

firstly enter this link

https://github.com/zezo386/dilation-graph

and find the release and download the exe

### Controls

- right click -> if you right click into a place with no point, a new point gets added in this place, if there is a point already there it removes it except for the dilation center which you cannot move

- left click drag -> if you drag a point it moves with you, you can move original polygon points and the dilation center but you can not move a dilated point

- Reset button -> it removes all points and resets the dilation center to (0,0)

- dilation slider -> it controls the dilation factor

## Features

### points

there are 3 types of points

1- original polygon points -> these are points that you add, remove move and do whatever you want with and represent the polygon that you will dilate

2- dilated polygon points -> these points are only for visualization and they represent the polygon after dilation

3- dilation center -> you can move this center but you can not add a new one or remove it since you need it to find the dilated polygon

### polygons

after putting atleast 2 points a line will form between them and once you put atleast 3 you make a polygon

a polygon will get filled with a color that represents a different thing

if the polygon is blue this means it is the original polygon that you put in

if it is green this means it is the dilated polygon

### Lines

after putting any point a line will appear between the dilation center and each dilated point

this line is called the dilation line and its colored in light green and dashed

## Math stuff

come here if you have problems with the math

### Dilation

so basically dilation is the change of the position along the same line as the dilation center

its just like changing prespective

its formula is

`cx + (px - cx) * k, cy + (py - cy) * k`

where cx is the x value of the dilation center

px is the x value of the point

cy is the y value of the dilation center

py is the y value of the point

k is the dilation factor

from my prespective i like to think of it as connecting a line between the point and the dilation center and then multiplying the distance by the dilation factor

## How to clone

you should be profeccient at this at this point but here it is

`git clone https://github.com/zezo386/dilation-graph`

just paste this into your terminal and voalla you got it

## Contributions

this project is made entirely by Ziad Elhusiny

the **GOAT OF PROGRAMMING**

#AUTHOR: Jamie Wyatt
#COURSE: Software Development
#DATE: 9/21/2018
#ASSIGNMENT: HW4 Pyramid Game
#RESOURCES: https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
#RESOURCE DESCRIPTION: Needed help with understanding python lists in 2D 

#FILES ASSOCIATED:  HW4wyattOutfile.txt
#HW4wyattOutfile.txt:   This file is the output file, essentially a copy of the screen output of this program
#####################   It starts with a description of this program, shows the game number, shows the move order,
#####################   and then ends with the stats from all the runs of the game.

#HWinfile.txt           Inside that file there will be four rows with two integers in each row, separated by a blank.
#####################   L. The number of levels to simulate,
#####################   T. Another integer, this one between 10 and 50 inclusive, that tells how many times you
#####################   should simulate the pyramid game with this sized pyramid. 

#IMPORT LIBRARIES
from __future__ import print_function
import random
import turtle
import time


#Start Program
print("Starting Program...")

#PROJECT DESCRIPTION
print("A pyramid exists with numbers increasing left to right, 1 is at the top. Each level has 1 more number than the above level\n",
"Whenever you make a move, and when you start the game on the number 1\n",
"you put a dot next to the number where you are. You put a new dot on the number even if the move forces\n",
"you to stay on the same number. You keep playing this strange game until every\n",
"number has at least one dot. At that point, the game is over.After the game is over\n",
"you will record the total number of moves it took to finish the game, the average number of dots on the numbers\n",
"and the largest number of dots on any number. More than one number may have exactly that number of dots.")


#Input/ Output File Definition
output_file = "HW4wyattOutfile.txt"
input_file = "HWinfile.txt"


#Read data from input file

V = []
with open(input_file) as f:
    V = [line.split() for line in f]
#Initialize 2D Array Sizes via User Input
level_value = -1
repeat_value_T = -1

#Get the user to display text or not
answer = "a"
show_output = True
while(answer != "yes" and answer != "no"):
    try:
        answer = str(input("Do you want to see each spot printed, yes/no:"))
    except ValueError:
        answer = "a"
    if answer == "no":
        show_output = False

#Define vectors.
M = [0,0,0,0]
D = [0,0,0,0]

#Open Output File          
f = open(output_file, "w");

#Write Project Description to the Output File
f.write("A pyramid exists with numbers increasing left to right, 1 is at the top. Each level has 1 more number than the above level\n \
Whenever you make a move, and when you start the game on the number 1\n \
you put a dot next to the number where you are. You put a new dot on the number even if the move forces\n \
you to stay on the same number. You keep playing this strange game until every\n \
number has at least one dot. At that point, the game is over.After the game is over\n \
you will record the total number of moves it took to finish the game, the average number of dots on the numbers\n \
and the largest number of dots on any number. More than one number may have exactly that number of dots.")
        
for v in range(-1,4,1):
    if v!= -1:
        level_value = int(V[v][0])
        repeat_value_T = int(V[v][1])
    else:
        level_value = 6
        repeat_value_T = 1
        print("::::::::::::::::BEGIN DEMO SIMULATION:::::::::::::::::")
    if v==0:
        print("::::::::::::::::::END DEMO SIMULATION:::::::::::::::::")

    print("SIMULATION " + str(v+1) + ": " + str(level_value) + " LEVELS, " + str(repeat_value_T) + " REPEATS")
    f.write("SIMULATION " + str(v+1) + ": " + str(level_value) + " LEVELS, " + str(repeat_value_T) + " REPEATS\n")
    print("______________________________________________________")
    f.write("______________________________________________________\n")
    
    turtle.clear()

    #PLACE NUMBER OF LEVELS INTO 2D LIST SIZES
    array_x_size = level_value
    array_y_size = level_value

    #Initialize Values for Empty Pyramid
    pyramid_value_init = 0

    #Initialize Values for Dot Counter
    dot_value_init = 0

    #Generate Empty Pyramid, Set to Pyramid Initial Value
    Pyramid = [[pyramid_value_init for x in range(array_x_size)] for y in range(array_y_size)]

    #Generate Dot Counter for Pyramid, Set to Dot Initial Value
    Pyramid_Dot_Count = \
    [[dot_value_init for x in range(array_x_size)] for y in range(array_y_size)]

    #Initialize Bounds for Pyramid
    lower_bound = 1
    upper_bound = 0
    filler = lower_bound

    #DEFINE FUNCTIONS:
    Scale = 200/array_x_size
    X_Shift = -50
    Y_Shift = 100
    turtle.hideturtle()
    turtle.speed("fastest")
    turtle.colormode(255)

    txt = turtle.Turtle()
    
    txt.hideturtle()
    def drawGameText(i,move_count):
        txt.clear()
        txt.penup()
        txt.setpos(X_Shift-250, Y_Shift+50)
        txt.write(str(i)+":"+str(move_count), False, align="center", font=("Arial",16,"normal"))

    def drawSummary(moves, avgd, maxd):
        txt.speed("slow")
        txt.clear()
        txt.penup()
        txt.setpos(X_Shift-250, Y_Shift+50)
        txt.write("GAMEOVER\nMoves:" + str(moves) +"\nAvgDot:" + str(avgd) + "\nMaxDot:" + str(maxd), False, align="center", font=("Arial",12,"normal"))
        time.sleep(5)
        txt.clear()
    def getColor(dot_count, x, y):
        if dot_count == 0:
            return (0,0,0)
        elif dot_count < 25:
            return (dot_count*10,255-dot_count*10, 0)
        else:
            return (255, 0, 0)
    def drawCircle(dot_count, x, y):
        x = -x*Scale*2
        y = -y*Scale*2
        x = x-(y)+X_Shift
        y = y+(x/2)+Y_Shift
        y = y*2
        if dot_count=="current":
            turtle.color("cyan")
            turtle.fillcolor("cyan")
        else:
            turtle.color(getColor(dot_count, x, y))
            turtle.fillcolor(getColor(dot_count,x,y))
        turtle.penup()
        turtle.setpos(x,y)
        turtle.begin_fill()
        turtle.circle(Scale)
        turtle.end_fill()


    #Fill Pyramid Values
    for x in range(array_x_size):
        for y in range(array_y_size):
            Pyramid[x][y] = filler
            filler += (x+1) + (y+1)
            if(x==0 and y==level_value-2):
                upper_bound = filler
        filler = Pyramid[x][0] + x + 1

    #Trim Pyramid Values
    for x in range(array_x_size):
        for y in range(array_y_size):
            if Pyramid[x][y] > upper_bound:
                Pyramid[x][y] = pyramid_value_init

    def drawPyramid():
        for x in range(array_x_size):
            for y in range(array_y_size):
                if(Pyramid[x][y]!=pyramid_value_init):
                    drawCircle(Pyramid_Dot_Count[x][y], x, y)


    #Initialize variables for calculating program statistics
    total_move_count=0
    total_min = 0
    total_max = 0
    min_max_dot = 0
    max_max_dot = 0
    avg_max_dot = 0
    max_total = 0





    #Loop that places dots on spots, and randomly picks Up left, up right, down left, or down right
    for t in range(repeat_value_T):

        #Show the Game Number
        print("")
        print("Playing Game " + str(t+1))
        f.write("\nGame " + str(t+1) + "\n")

        #Generate Dot Counter for Pyramid, Set to Dot Initial Value
        Pyramid_Dot_Count = \
        [[dot_value_init for x in range(array_x_size)] for y in range(array_y_size)]

        #Draw Pyramid
        drawPyramid()

        #Initialze Start Location in Pyramid
        x_location = 0
        y_location = 0

        #To return if going out of bounds
        x_prev_location = 0
        y_prev_location = 0

        #Set a dot to include the starting position
        Pyramid_Dot_Count[x_location][y_location] = Pyramid_Dot_Count[x_location][y_location] + 1
        drawCircle(Pyramid_Dot_Count[x_location][y_location],x_location,y_location)
        #Initialize Loop Control and Counter Number of Loops
        move_count = 0

        #Boolean for whether each spot has a dot or not, Initializer
        complete = False

        #Begin Game, Loop Until complete is true, meaning every spot has at least one dot
        while complete is False:
            drawGameText(t+1,move_count)

            #Add to move total
            move_count = move_count + 1
            total_move_count = total_move_count + 1 

            #Pick a random direction to move in 2D
            next_move = random.randint(1,5)

            drawCircle(Pyramid_Dot_Count[x_location][y_location], x_location, y_location)
        
            #Move either left, right, up, or down
            if next_move == 1:
                x_location = x_location + 1
            elif next_move == 2:
                x_location = x_location - 1
            elif next_move == 3:
                y_location = y_location + 1
            elif next_move == 4:
                y_location = y_location - 1
        
            #Check if move is possible (or out of bounds)
            try:
                return_value=Pyramid[x_location][y_location]
                if return_value == 0 or x_location <0 or y_location<0:
                    raise IndexError("Out of Bounds")
        
            #Catch Out of Bounds And reset
            except IndexError:
                #Zero value return implies out of bounds, go back to same position
                x_location = x_prev_location
                y_location = y_prev_location
                return_value=Pyramid[x_location][y_location]

            
            
            #Increment Dot Count    
            Pyramid_Dot_Count[x_location][y_location] = Pyramid_Dot_Count[x_location][y_location] + 1
            drawCircle(Pyramid_Dot_Count[x_location][y_location], x_location, y_location)

            #Draw Circle for Current Position
            drawCircle("current",x_location, y_location)
            #Check if Pyramid is Full of Dots or not
            complete = True
            for x in range(array_x_size):
                for y in range(array_y_size):
                    if Pyramid_Dot_Count[x][y] == 0 and Pyramid[x][y] != 0:
                        complete = False

            #Once a game is completed, calculate statistics
            if(complete==True):
                if(t==0):
                    total_min = total_move_count
                    total_max = total_move_count
                if(total_move_count>total_max):
                    total_max = total_move_count
                if(total_move_count<total_min):
                    total_min = total_move_count
                max_spot = 0;
                max_count = 0;

                #Calculate max dot count and compare to previous games
                for x in range(array_x_size):
                        for y in range(array_y_size):
                                if(Pyramid_Dot_Count[x][y] > max_count):
                                        max_count = Pyramid_Dot_Count[x][y]
                                        max_spot = Pyramid[x][y]
                if(max_max_dot<max_count):
                    max_max_dot = max_count
                if(t==0):
                    min_max_dot = max_count

                if(min_max_dot>max_count):
                    min_max_dot = max_count
                max_total = max_total + max_count

                drawSummary(move_count, max_count/upper_bound, max_count)

            #Show User the Landing Spot
            if move_count % 10 == 0:
                if show_output == True:
                    print("")
                f.write("\n")

            #If a game is over, use a period, else use a commma to show the user what spot we are on
            if complete == True:
                if show_output == True:
                    print(str(Pyramid[x_location][y_location]) + ".\t ",end='')
                f.write(str(Pyramid[x_location][y_location]) + ".\t ")
            else:
                if show_output == True:
                    print(str(Pyramid[x_location][y_location]) + ",\t ",end= '')
                f.write(str(Pyramid[x_location][y_location]) + ",\t ")
        
            #Set Location for Next Iteration
            x_prev_location = x_location
            y_prev_location = y_location

            #END CORE GAME LOOP


    #Calculate average move count
    print("")
    f.write("\n")
    avg_move_count = total_move_count/repeat_value_T
    
    print("Average Move Count for each game: " + str(avg_move_count))
    f.write("Average Move Count for each game: " + str(avg_move_count) + "\n")

    #Simulation totals
    if(v>=0):
        M[v] = avg_move_count
        D[v] = max_max_dot

    #Print Max and Min move counts
    print("Minimum Move Count:  " + str(total_min))
    f.write("Minimum Move Count: " + str(total_min) + "\n")
    print("Maximum Move count: " + str(total_max))
    f.write("Maximum Move Count: " + str(total_max) + "\n")


    #Print Max Max Dot count, Min Max Dot count, and Average Max dot count
    avg_max_dot = max_total/repeat_value_T
    print("Minimum Max Dot count was : " + str(min_max_dot))
    f.write("Minimum Max Dot count was : " + str(min_max_dot) + "\n")
    print("Maximum Max Dot count was : " + str(max_max_dot))
    f.write("Maximum Max Dot count was : " + str(max_max_dot) + "\n")
    print("Average Max Dot count was : " + str(avg_max_dot))
    f.write("Average Max Dot count was : " + str(avg_max_dot)+ "\n")

    #New Line
    print("")
    f.write("\n")



print("Game Finish.")

print("[ L , T , M , D]")
for v in range(0,4,1):
    V[v][0] = int(V[v][0])
    V[v][1] = int(V[v][1])
    V[v].append(M[v])
    V[v].append(D[v])
    print(V[v])

#Close Output File
f.close()

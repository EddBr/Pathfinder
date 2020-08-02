import numpy as np 
import pygame  

#Sets the grid dimensions
x_length = 25 #int(input("Enter the width of the grid: "))
y_length = 25 #int(input("Enter the height of the grid: "))
grid =[["[ ]"]*x_length]*y_length
grid = np.array(grid)

#Pygame global variables
width = 20
height = 20
margin = 5
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
orange = (255,165,0)
yellow = (255,255,0)
purple = (128,0,128)
gameDisplay = pygame.display.set_mode((25*x_length, 25*y_length))
gameDisplay.fill(black)
    
"""
KEY
---

Starting Position (sp) - /
Current Position (cp) - *
Blocked Position (bp) - +
Finish Position (fp) - =

"""
sp = {
    "x": 24,
    "y": 24
}

fp = {
    "x": 0,
    "y": 0
}

cp = {
    "x": sp["x"],
    "y": sp["y"]
}
bp = []
direct = []

def setup():
    pygame.init()
    pygame.display.set_caption("Pathfinder")
    for row in range(x_length):
        for column in range(y_length):
            try:
                if row == fp["x"] and column == fp["y"]:
                    drawblock(green, row, column)
                elif row == sp["x"] and column == sp["y"]:
                    drawblock(orange, row, column)
                elif checked.index([row,column]) != -1:
                    drawblock(red, row, column)
                else:
                    drawblock(white, row, column)
            except:
                drawblock(white, row, column)
    pygame.display.flip()

    closed = False
    first = True
    while not closed:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT: 
                closed = True 
                pygame.display.quit()
                pygame.quit()
            elif pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                column = pos[0] / 25
                row = pos[1] / 25
                column = round(column)
                row = round(row)
                drawblock(black, row, column)
                print(row, column, pos)
                #print("Click ", pos, "Grid coordinates: ", row, column)
                bp.append([row, column])
                pygame.display.flip()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if first == True:
                    complete()
                    first = False

path = [[cp["x"],cp["y"]]]
checked = []
direct_checked = []
weights = []

def surrounding(cp_x, cp_y, output_array, destination):
    #Checks all 8 surrounding blocks from cp
    #Creates a weight for all 8, to be compared
    for i in range(9):
        if i == 0:
            try:
                optionx = cp_x - 1
                optiony = cp_y - 1
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except Exception as e:
                pass
        elif i == 1:
            try:
                optionx = cp_x
                optiony = cp_y + 1
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except Exception as e:
                pass
        elif i == 2:
            try:
                optionx = cp_x + 1
                optiony = cp_y + 1
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except Exception as e:
                pass
        elif i == 3:
            try:
                optionx = cp_x - 1
                optiony = cp_y
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except Exception as e:
                pass
        elif i == 4:
            try:
                optionx = cp_x + 1
                optiony = cp_y
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except Exception as e:
                pass
        elif i == 5:
            try:
                optionx = cp_x - 1
                optiony = cp_y - 1
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except Exception as e:
                pass
        elif i == 6:
            try:
                optionx = cp_x
                optiony = cp_y - 1
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except Exception as e:
                pass
        elif i == 7:
            try:
                optionx = cp_x + 1
                optiony = cp_y - 1
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except Exception as e:
                pass
        elif i == 8:
            try:
                optionx = cp_x - 1
                optiony = cp_y + 1
                option_test = grid[optionx][optiony]
                option = [optionx, optiony]
            except Exception as e:
                pass
        try:
            if checked.index(option) != -1:
                pass
        except Exception as e:
            try:
                if bp.index(option) != -1:
                    pass
            except:
                if destination == "sp":
                    try:
                        if path.index(option) > -1:
                            print(path.index(option))
                            print(option)
                            #This calculates the weight of a node, dependent on the distance from both the 
                            #Starting Point and Finishing Point, using Pythagorus' Theorem
                            spd = (( (sp["x"]*10 - optionx*10)**2 + (sp["y"]*10 - optiony*10)**2 )** 0.5)
                            fpd = (( (fp["x"]*10 - optionx*10)**2 + (fp["y"]*10 - optiony*10)**2 )** 0.5)
                            if destination == "sp":
                                spd *= 10
                            else:
                                fpd *= 10
                            weight = spd + fpd
                            if (optionx == fp["x"]) and (optiony == fp["y"]):
                                weight = 0
                            weights.append([weight, optionx, optiony])
                            output_array.append(option)
                    except:       
                        pass
                else:
                    #This calculates the weight of a node, dependent on the distance from both the 
                    #Starting Point and Finishing Point, using Pythagorus' Theorem
                    spd = (( (sp["x"]*10 - optionx*10)**2 + (sp["y"]*10 - optiony*10)**2 )** 0.5)
                    fpd = (( (fp["x"]*10 - optionx*10)**2 + (fp["y"]*10 - optiony*10)**2 )** 0.5)
                    if destination == "sp":
                        spd *= 10
                    else:
                        fpd *= 10
                    weight = spd + fpd
                    if (optionx == fp["x"]) and (optiony == fp["y"]):
                        weight = 0
                    weights.append([weight, optionx, optiony])
                    output_array.append(option)


    """
    KEY
    ---
    lowest[0] = weight
    lowest[1] = index

    weights[i][0] = weight
    weights[i][1] = x
    weights[i][2] = y
    """

    lowest = [0,0]
    for i in range(len(weights)):
        if i == 0:
            lowest[0] = weights[i][0]
            lowest[1] = i
        if weights[i][0] == 0:
            lowest[0] = weights[i][0]
            lowest[1] = i
        try:
            if weights[i][0] <= lowest[0]:
                lowest[0] = weights[i][0]
                lowest[1] = i
        except:
            pass
    try:
        path.append([weights[lowest[1]][1], weights[lowest[1]][2]])
    except:
        print("No possible path found")

    cp_x = weights[lowest[1]][1]
    cp_y = weights[lowest[1]][2]
    del weights[lowest[1]]
    return cp_x, cp_y

def complete():
    while (cp["x"] != fp["x"]) or (cp["y"] != fp["y"]):
        output()
        cp["x"], cp["y"] = surrounding(cp["x"],cp["y"], checked, "fp")   
    output() 
    pygame.display.flip()
    pygame.event.pump()
    #direct_path()
    endgame()
    
def drawblock(colour, row, column):
    pygame.draw.rect(gameDisplay, #The screen it's using
                                    colour, #The colour of the blocks
                                    [(margin + width) * column + margin, #Its x position
                                    (margin + height) * row + margin, #Its y position
                                    width, #The width of the blocks
                                    height]) #The height of the blocks

def direct_path():
    direct.append([fp["x"],fp["y"]])
    weights = []
    i = 0

    while (direct[len(direct)-1][0] != sp["x"]) or (direct[len(direct)-1][1] != sp["y"]):
        direct_checking = [direct[i][0], direct[i][1]]
        direct_checking = surrounding(direct_checking[0], direct_checking[1], direct_checked, "sp")
        direct.append(direct_checking)
        i += 1
        print(direct)
            

        for i in range(len(direct)):
            drawblock(purple, direct[i][0], direct[i][0])

def output():
    #This is the output grid (oGrid)
    #Console Output
    oGrid = ""
    for i in range(x_length):
        for j in range(y_length):
            try:
                try:
                    if bp.index([i,j]) != -1:
                        oGrid += "[+]"
                except:
                    if i == cp["x"] and j == cp["y"]:
                        oGrid += "[*]"
                    elif (i == fp["x"] and j == fp["y"]):
                        oGrid += "[=]"
                    elif i == sp["x"] and j == sp["y"]:
                        oGrid += "[/]"
                    elif checked.index([i,j]) != -1:
                        oGrid += "[X]"
                    else:
                        oGrid += "[ ]"
            except:
                oGrid += "[ ]"
        oGrid += "\n"
    print(oGrid)

    #Pygame Updated Output
    for i in range(len(checked)):
        try:
            if bp.index([checked[i][0], checked[i][1]]) != -1:
                pass
        except:
            drawblock(red, checked[i][0], checked[i][1])
    for i in range(len(path)):
        drawblock(blue, path[i][0], path[i][1])
    drawblock(blue, cp["x"], cp["y"])
    pygame.display.flip()

def endgame():
    font = pygame.font.Font('freesansbold.ttf', 32) 
    msg = ("Finished in " + str(len(path))+ " moves.")
    print(msg)
    text = font.render(msg, True, black, white) 
    textRect = text.get_rect()  
    textRect.center = (x_length * 12, y_length * 12) 
    gameDisplay.blit(text, textRect) 
    pygame.display.flip() 
setup()

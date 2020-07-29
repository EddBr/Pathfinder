import numpy as np 

#Sets the grid dimensions
x_length = 10 #int(input("Enter the width of the grid: "))
y_length = 10 #int(input("Enter the height of the grid: "))
grid =[["[ ]"]*x_length]*y_length
grid = np.array(grid)
    
"""
KEY
---

Starting Position (sp) - /
Current Position (cp) - *
Blocked Position (bp) - +
Finish Position (fp) - =

"""
sp = {
    "x": 9,
    "y": 9
}

fp = {
    "x": 0,
    "y": 0
}

cp = {
    "x": sp["x"],
    "y": sp["y"]
}

#This calculates the weight of a node, dependent on the distance from both the 
#Starting Point and Finishing Point, using Pythagorus' Theorem
def weight(x,y,arr):
    spd = (( (sp["x"]*10 - x*10)**2 + (sp["y"]*10 - y*10)**2 )** 0.5)
    fpd = (( (fp["x"]*10 - x*10)**2 + (fp["y"]*10 - y*10)**2 )** 0.5) * 2
    weight = spd + fpd
    if x == fp["x"] and y == fp["y"]:
        weight = 0
    arr.append([weight, x, y])

path = [[cp["x"],cp["y"]]]
checked = []
weights = []

def main():
    while cp["x"] != fp["x"] and cp["y"] != fp["y"]:
        output()
        #Checks all 8 surrounding blocks from cp
        #Creates a weight for all 8, to be compared
        for i in range(8):
            if i == 0:
                try:
                    optionx = cp["x"] - 1
                    optiony = cp["y"] - 1
                    option_test = grid[optionx][optiony]
                    option = [optionx, optiony]
                except Exception as e:
                    pass
            elif i == 1:
                try:
                    optionx = cp["x"]
                    optiony = cp["y"] + 1
                    option_test = grid[optionx][optiony]
                    option = [optionx, optiony]
                except Exception as e:
                    pass
            elif i == 2:
                try:
                    optionx = cp["x"] + 1
                    optiony = cp["y"] + 1
                    option_test = grid[optionx][optiony]
                    option = [optionx, optiony]
                except Exception as e:
                    pass
            elif i == 3:
                try:
                    optionx = cp["x"] - 1
                    optiony = cp["y"] 
                    option_test = grid[optionx][optiony]
                    option = [optionx, optiony]
                except Exception as e:
                    pass
            elif i == 4:
                try:
                    optionx = cp["x"] + 1
                    optiony = cp["y"]
                    option_test = grid[optionx][optiony]
                    option = [optionx, optiony]
                except Exception as e:
                    pass
            elif i == 5:
                try:
                    optionx = cp["x"] - 1
                    optiony = cp["y"] - 1
                    option_test = grid[optionx][optiony]
                    option = [optionx, optiony]
                except Exception as e:
                    pass
            elif i == 6:
                try:
                    optionx = cp["x"]
                    optiony = cp["y"] - 1
                    option_test = grid[optionx][optiony]
                    option = [optionx, optiony]
                except Exception as e:
                    pass
            elif i == 7:
                try:
                    optionx = cp["x"] + 1
                    optiony = cp["y"] - 1
                    option_test = grid[optionx][optiony]
                    option = [optionx, optiony]
                except Exception as e:
                    pass
            try:
                if checked.index(option) != -1:
                    pass
            except Exception as e:
                checked.append(option)
                weight(option[0] ,option[1],weights)
        """
        KEY
        ---
        lowest[0] = weight
        lowest[1] = index

        weights[0] = weight
        weights[1] = x
        weights[2] = y
        """
        #Compares the weights of the 8 surrounding options and finds the lowest one,
        #Lowest weight becomes the next position
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
        path.append([weights[lowest[1]][1], weights[lowest[1]][2]])  
        cp["x"] = weights[lowest[1]][1]
        cp["y"] = weights[lowest[1]][2]
        del weights[lowest[1]] 
    output()
    print("Finished in " + str(len(path))+ " moves.")

def output():
    #This is the output grid (oGrid)
    oGrid = ""
    for i in range(x_length):
        for j in range(y_length):
            try:
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

main()
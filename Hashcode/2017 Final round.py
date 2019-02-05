from random import *

file = open('charleston_road.in', 'r')

first_line = file.readlines(1)[0].strip().split(' ')
second_line = file.readlines(2)[0].strip().split(' ')
third_line = file.readlines(3)[0].strip().split(' ')

# Height(rows), Width(columns), Radius of the router
H = first_line[0]
W = first_line[1]
R = first_line[2]

# Price for placing 1 router, Price for connecting 1 cell to backbone, Total budget
PR = second_line[0]
PB = second_line[1]
BUDGET = second_line[2]

# x and y index of initial cell connected to backbone
BX = third_line[0]
BY = third_line[1]

# Rest of the input(characters representation of building cells)
building = file.readlines()

file.close()

# ############# Done reading inputs ####################################

new_building = []

for string in building:
    new_string = []
    for char in string.strip():
        new_string.append(char)

    new_building.append(new_string)

backbone_cells = []
routers_cells = []

output = open('pont_output', 'a')

output.writelines(str(100) + "\n")

for i in range(100):
    num1 = randint(1, 9)
    num2 = randint(1, 9)
    output.write(str(num1) + " " + str(num2) + "\n")

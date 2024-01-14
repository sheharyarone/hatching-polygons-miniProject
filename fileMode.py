# Import necessary modules and functions from other files
from shared_modules import turtle, vertices, screen, my_turtle
import os


# Function to get a valid filename input from the user
def file_name_input():
    wrong_entry = False
    prompt = "Enter the file name:"
    while True:
        filename = turtle.textinput("Filename", prompt)
        if not filename.endswith('.txt'):
            filename += '.txt'
        if os.path.isfile(filename):
            return filename
        else:
            if not wrong_entry:
                prompt = 'FILE NOT FOUND\n' + prompt
                wrong_entry = True


def read_file(file_name):
    global vertices
    vertices = []
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            index = int(parts[0])
            coordinates_str = parts[1]
            coordinates_list = coordinates_str.split('|')

            coordinates = []
            for coord_set in coordinates_list:
                if coord_set:  # Check if the string is not empty
                    coord_tuple = tuple(
                        map(float, coord_set.strip('()').split(', ')))
                    coordinates.append(coord_tuple)
            if len(coordinates) == 3:
                vertices.append(
                    (index, coordinates[0], coordinates[1], coordinates[2]))
            else:
                vertices.append((index, coordinates[0]))


# Function to read polygon data from a file
def read_polygon():
    global vertices
    file_name = file_name_input()
    read_file(file_name)


# Function to visualize the polygon based on its vertices
def visualize_polygon(vertices):
    turtle.clearscreen()
    for i in range(len(vertices)):
        start = (vertices[i][1])
        end = (vertices[(i + 1) % len(vertices)][1])

        # If there are three coordinates, assume it's a cubic Bezier curve
        if len(vertices[(i + 1) % len(vertices)]) == 4:
            control_point1 = vertices[(i + 1) % len(vertices)][2]
            control_point2 = vertices[(i + 1) % len(vertices)][3]
            draw_cubic_bezier_curve(
                start, end, control_point1, control_point2)
        else:
            draw_straight_line(start, end)


# Function to draw a cubic Bezier curve based on control points
def draw_cubic_bezier_curve(start, end, control_point1, control_point2):
    my_turtle.pencolor("red")
    my_turtle.penup()
    my_turtle.goto(start)
    my_turtle.pendown()
    # Draw the control points
    my_turtle.goto(control_point1)
    my_turtle.dot(5, "red")  # Mark Control Point 1 in red
    my_turtle.goto(control_point2)
    my_turtle.dot(5, "red")  # Mark Control Point 2 in green
    my_turtle.goto(end)
    my_turtle.dot(5, "black")  # Mark End Point in blue
    my_turtle.pendown()

    # Draw the cubic Bezier curve
    t = 0
    my_turtle.pencolor("black")

    my_turtle.penup()
    my_turtle.goto(start)
    my_turtle.pendown()
    while t <= 1:
        x_t = ((1 - t) ** 3) * start[0] + 3 * t * ((1 - t) ** 2) * control_point1[0] + 3 * (
            t ** 2) * (1 - t) * control_point2[0] + (t ** 3) * end[0]
        y_t = ((1 - t) ** 3) * start[1] + 3 * t * ((1 - t) ** 2) * control_point1[1] + 3 * (
            t ** 2) * (1 - t) * control_point2[1] + (t ** 3) * end[1]

        my_turtle.goto(x_t, y_t)
        t += 0.01


# Function to draw a straight line between two points
def draw_straight_line(start, end):
    global order
    my_turtle.penup()
    my_turtle.goto(start)
    my_turtle.dot(5, "black")
    my_turtle.pendown()
    my_turtle.color("black")
    my_turtle.goto(end)
    my_turtle.dot(5, "black")


# Function to handle the file mode, reading and visualizing the polygon
def handleFileMode():
    global vertices
    read_polygon()
    visualize_polygon(vertices)


def handleDirecotryMode():
    global vertices
    wrong_entry = False
    description = "Enter the Folder name : "
    while True:
        folder_name = turtle.textinput(
            'FOLDER NAME', description)

        folder_path = os.path.join(os.getcwd(), folder_name)
        if (os.path.exists(folder_path) and os.path.isdir(folder_path)):
            files = os.listdir(folder_path)
            files = [
                file_name for file_name in files if file_name.endswith(".txt")]
            if not files:
                description = 'FOLDER NOT FOUND OR NO FILES ARE IN THE FOLDER\n'+description
                wrong_entry = True
            else:
                break
        else:
            if not wrong_entry:
                description = 'FOLDER NOT FOUND OR NO FILES ARE IN THE FOLDER\n'+description
                wrong_entry = True
    files = os.listdir(folder_path)
    files.sort(key=len)

    for file in files:
        file = folder_path+'\\'+file
        read_file(file)
        turtle.clearscreen()
        visualize_polygon(vertices)

    user_input = turtle.textinput(
        "Input", 'Do you like to read another folder ?\n1-> to read again\nPress any key to close the program')
    if user_input == '1':
        handleDirecotryMode()

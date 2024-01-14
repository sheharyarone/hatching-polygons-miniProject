# Import necessary modules and functions from other files
from shared_modules import turtle, my_turtle, screen, vertices, order, polygon_complete, get_user_input
import transformations


# Function to draw a straight line between the last two vertices
def draw_straight_line():
    global order
    my_turtle.penup()
    my_turtle.goto(vertices[-2][1])
    my_turtle.dot(5, "black")
    my_turtle.pendown()
    my_turtle.color("black")
    my_turtle.goto(vertices[-1][1])
    my_turtle.dot(5, "black")

    # Set up click event handling again after drawing a straight line
    check_and_continue_or_terminate()


# Function to check the number of vertices and continue or terminate
def check_and_continue_or_terminate():

    global num_vertices_desired, order, polygon_complete, vertices
    order += 1

    if order == num_vertices_desired:

        if not polygon_complete:
            polygon_complete = True
            choice = get_user_input('0 for straight edge\n1 for cubic bezier:')

            if choice == '0':
                draw_first_and_last_edges()
            elif choice == '1':
                turtle.textinput(
                    "Control Point 1", f"Select coordinates for Control Point 1 :")
                screen.onscreenclick(control_point_1_inp)
        else:
            save_or_transformation(vertices)
    else:
        turtle.textinput("OK", f"Click 'OK' to select VERTEX {order}")
        screen.onscreenclick(set_origin)


# Function to draw the first and last edges together
def draw_first_and_last_edges():

    global order, num_vertices_desired, vertices
    my_turtle.penup()
    my_turtle.goto(vertices[-1][1])
    my_turtle.pendown()
    my_turtle.color("black")
    # Draw the last edge
    my_turtle.goto(vertices[0][1])

    save_or_transformation(vertices)


# Function to get user input for the number of vertices
def get_number_of_vertices():
    wrong_entry = False
    prompt = "Enter the number of vertices you need:"
    while True:
        num_vertices = (turtle.textinput(
            "Number of Vertices", prompt))
        if int(num_vertices) >= 3:  # Minimum of 3 vertices required for a polygon
            return int(num_vertices)
        else:
            if not wrong_entry:
                prompt = ("Please enter a valid number (at least 3).\n") + prompt
                wrong_entry = True


# Function to set the origin
def set_origin(x, y):
    global order, vertices
    if vertices:
        # After setting the origin, ask for the type of line
        choice = get_user_input('0 for straight edge\n1 for cubic bezier:')

        if choice == '0':
            vertices.append((order, (x, y)))
            draw_straight_line()
        elif choice == '1':
            vertices.append((order, (x, y)))
            cubic_bezier_curve_prompt()
        else:
            screen.onscreenclick(set_origin)
    else:
        vertices.append((order, (x, y)))
        order += 1

        turtle.textinput("OK", "Click 'OK' to select VERTEX 1.")
        screen.onscreenclick(set_origin)


# Function to handle the second control point input for a cubic Bezier curve
def control_point_2_inp(x, y):
    global vertices
    if (order != num_vertices_desired):
        vertices[-1] = vertices[-1] + ((x, y),)
        draw_cubic_bezier_curve(
            vertices[-2][1], vertices[-1][1], vertices[-1][2], vertices[-1][3])
    else:
        vertices[0] = vertices[0] + ((x, y),)
        draw_cubic_bezier_curve(
            vertices[-1][1], vertices[0][1], vertices[0][2], vertices[0][3])


# Function to handle the first control point input for a cubic Bezier curve
def control_point_1_inp(x, y):
    global vertices
    if (order != num_vertices_desired):
        vertices[-1] = vertices[-1] + ((x, y),)
    else:
        vertices[0] = vertices[0] + ((x, y),)
    turtle.textinput(
        "Control Point 2", f"Select coordinates for Control Point 2 :")
    screen.onscreenclick(control_point_2_inp)


# Function to prompt user for control points and initiate cubic Bezier curve drawing
def cubic_bezier_curve_prompt():
    turtle.textinput(
        "Control Point 1", f"Select coordinates for Control Point 1 :")
    screen.onscreenclick(control_point_1_inp)


# Function to draw a cubic Bezier curve based on user input for control points
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
    check_and_continue_or_terminate()


# Function to store the polygon vertices in a file
def store_polygon(vertices):
    file_name = turtle.textinput("Store Polygon", "Enter the file name:")
    if file_name:
        if not file_name.endswith('.txt'):
            file_name += '.txt'
    with open(file_name, 'w') as file:
        for vertex in vertices:
            for i in range(0, len(vertex)):
                if i == 0:
                    file.write(f"{vertex[i]}:")
                else:
                    file.write(f"{vertex[i]}")
                if i != len(vertex) and i != 0:
                    file.write(f"|")
            file.write(f"\n")


# Function to prompt user for saving the polygon or applying transformations
def save_or_transformation(vertices):
    choice = turtle.textinput(
        "Choice", "Enter 0->DON'T SAVE FILE\n1->SAVE FILE:")
    if choice == '0':
        transformations.transformation_mode()
    else:
        store_polygon(vertices)
        transformations.transformation_mode()


# Function to handle interactive mode
def handleInteractiveMode():
    global num_vertices_desired, vertices
    num_vertices_desired = get_number_of_vertices()
    num_vertices_desired = int(num_vertices_desired)
    turtle.textinput("Starting Point Input",
                     "Click 'OK' to select Starting Point.")
    screen.onscreenclick(set_origin)

    turtle.mainloop()

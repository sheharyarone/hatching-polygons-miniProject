# Import necessary modules and functions from other files
from shared_modules import turtle, my_turtle, screen, vertices, order, polygon_complete, transformed_vertices, get_user_input
import fileMode
import interactiveMode
import math
import random

# Global variables
current_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


# Function to create a translation matrix
def translation_matrix(dx, dy):
    return [[1, 0, dx],
            [0, 1, dy],
            [0, 0, 1]]


# Function to create a rotation matrix
def rotation_matrix(theta):
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    return [[cos_theta, -sin_theta, 0],
            [sin_theta, cos_theta, 0],
            [0, 0, 1]]


# Function to create a scaling matrix
def scaling_matrix(sx, sy):
    return [[sx, 0, 0],
            [0, sy, 0],
            [0, 0, 1]]


# Function to create a shearing matrix
def shearing_matrix(sx, sy):
    return [[1, sx, 0],
            [sy, 1, 0],
            [0, 0, 1]]


# Function to create a reflection matrix
def reflection_matrix(axis):
    if axis.lower() == 'x':
        return [[1, 0, 0],
                [0, -1, 0],
                [0, 0, 1]]
    elif axis.lower() == 'y':
        return [[-1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]]
    else:
        raise ValueError("Invalid axis. Use 'x' or 'y'.")


# Function to multiply two matrices
def multiply_matrices(X, Y):
    result = [[0], [0], [0]]

    result = [[sum(a * b for a, b in zip(X_row, Y_col))
               for Y_col in zip(*Y)] for X_row in X]
    return result


# Function to apply a transformation to the vertices
def apply_transformation(transformation_matrix):
    global vertices, transformed_vertices

    transformed_vertices = vertices[:]

    for i in range(len(vertices)):
        if (len(vertices[i]) == 4):
            x1, y1 = transformed_vertices[i][1]
            x2, y2 = transformed_vertices[i][2]
            x3, y3 = transformed_vertices[i][3]

            result1 = multiply_matrices(
                transformation_matrix, [[x1], [y1], [1]])
            result2 = multiply_matrices(
                transformation_matrix, [[x2], [y2], [1]])
            result3 = multiply_matrices(
                transformation_matrix, [[x3], [y3], [1]])

            transformed_vertices[i] = (
                transformed_vertices[i][0], (result1[0][0], result1[1][0]), (result2[0][0], result2[1][0]), (result3[0][0], result3[1][0]))
        else:
            x1, y1 = transformed_vertices[i][1]
            result1 = multiply_matrices(
                transformation_matrix, [[x1], [y1], [1]])
            transformed_vertices[i] = (
                transformed_vertices[i][0], (result1[0][0], result1[1][0]))

    return transformed_vertices


# Function to enter the transformation mode
def transformation_mode():
    global transformed_vertices
    choice = get_user_input(
        'Enter 0->NO TRANSFORMATION\n1->YES TO TRANSFORMATION:')
    if choice == '0':
        random_pattern()  # will add another function here
    elif choice == '1':
        global current_matrix
        while True:
            choice = turtle.textinput(
                "Transformation", "Choose a transformation: \nT(translation)\n/R(rotation)\n/S(scaling)\n/H(shearing)\n/F(reflection)\n/Quit")
            if choice.lower() == 'quit':
                break
            elif choice.lower() == 't':
                dx = float(turtle.textinput("Translation",
                                            "Enter translation along x-axis (dx):"))
                dy = float(turtle.textinput("Translation",
                                            "Enter translation along y-axis (dy):"))
                transformation_matrix = translation_matrix(dx, dy)
            elif choice.lower() == 'r':
                angle = math.radians(float(turtle.textinput(
                    "Rotation", "Enter rotation angle (degrees):")))
                transformation_matrix = rotation_matrix(angle)
            elif choice.lower() == 's':
                sx = float(turtle.textinput(
                    "Scaling", "Enter scaling factor along x-axis (sx):"))
                sy = float(turtle.textinput(
                    "Scaling", "Enter scaling factor along y-axis (sy):"))
                transformation_matrix = scaling_matrix(sx, sy)
            elif choice.lower() == 'h':
                sx = float(turtle.textinput(
                    "Shearing", "Enter shearing factor along x-axis (sx):"))
                sy = float(turtle.textinput(
                    "Shearing", "Enter shearing factor along y-axis (sy):"))
                transformation_matrix = shearing_matrix(sx, sy)
            elif choice.lower() == 'f':
                axis = turtle.textinput(
                    "Reflection", "Choose axis for reflection (x/y):")
                transformation_matrix = reflection_matrix(axis)
            else:
                continue

            current_matrix = multiply_matrices(
                current_matrix, transformation_matrix)
            apply_transformation(current_matrix)

        choice = get_user_input(
            "Enter 0->NO TRANSFORMATION VISUALIZATION\n1->YES TO TRANSFORMATION VISUALIZATION:")

        if choice == '1':
            # will add another function here
            fileMode.visualize_polygon(transformed_vertices)
        choice = get_user_input(
            "Enter 0->DON'T SAVE TRANSFORMED POINTS\n1->SAVE TRANSFORMED POINTS:")
        if choice == '1':
            # will add another function here
            interactiveMode.store_polygon(transformed_vertices)

        random_pattern()


# Function to generate a random pattern
def random_pattern():

    choice = get_user_input(
        "Enter 0->SKIP RANDOM PATTERN\n1->TRY RANDOM PATTERN:")

    if choice == '1':
        num_vertices = interactiveMode.get_number_of_vertices()
        points = [(i, (random.uniform(-300, 300), random.uniform(-300, 300)))
                  for i in range(num_vertices)]
        turtle.clearscreen()
        fileMode.visualize_polygon(points)  # will add another function here
        choice = get_user_input(
            "Enter 0->DON'T SAVE RANDOM PATTERN\n1->SAVE RANDOM PATTERN:")

        if choice == '1':
            # will add another function here
            interactiveMode.store_polygon(points)
    exit()

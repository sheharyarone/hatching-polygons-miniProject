import turtle

vertices = []

transformed_vertices = []
order = 0
polygon_complete = False
num_vertices_desired = 0

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle
my_turtle = turtle.Turtle()

my_turtle.hideturtle()


def get_user_input(description):
    description = description+'\n exit -> to close the program'
    wrong_entry = False
    while True:
        user_input = turtle.textinput("Input", description)
        if user_input in ['0', '1']:
            return (user_input)
        elif user_input == 'exit':
            exit()
        else:
            if not wrong_entry:
                description = "Invalid input. Please enter either 0 or 1.\n"+description
                wrong_entry = True

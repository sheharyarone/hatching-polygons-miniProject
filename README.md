# User Manual

- Open a terminal and navigate to the directory where your `main.py` file is located.
- Execute the following command to start your program:
```
python main.py
```

- The program will prompt you to choose a mode by entering a number. Enter 0 for file reading mode or 1 for interactive mode.

**Directory Mode:**

- If you choose this mode, the program will ask for the folder name in which 3 files will be stored or any number of files can be there.
- Program will make sure to check folder existence and .txt file existence within it.
- Then it will visualize all the polygons present in that file.
- After visualization, the program will ask for repeating this mode.

**File Reading Mode:**

- If you chose File Reading Mode, the program will ask for the filename. Enter the filename with the extension (e.g., `input_file.txt`).
- The program will check if the file exists. If it does, it will draw the vertices and prompt you for transformations.
- After transformations, the program will ask if you want to visualize the transformed vertices.
- Finally, the program will ask if you want to save the transformed vertices to a file. If you choose "yes," the program will prompt you for the output filename.

**Interactive Mode:**

- If you chose Interactive Mode, the program will guide you through selecting coordinates based on mouse clicks.
- After selecting coordinates, the program will proceed with the transformations.
- It will then ask if you want to visualize the transformed vertices and if you want to save them to a file.

Regardless of the mode chosen, the program may offer an option to generate a random polygon pattern.
If you choose "yes," the program will generate a polygon and ask if you want to visualize it through the grid.
If you choose "yes," the program will draw the points on the plane and ask for saving these vertices in a file.
If you choose "yes," the program will prompt you for the output filename. After saving the data points, the program will close automatically.

**Exit Operation:**

User can exit any time by typing `exit` in the input dialogue box.

# Program Capabilities

**Input Capabilities:**

1. **File Reading Mode:**
 - Users can provide input data by reading from a file.
 - The program prompts the user to enter the filename for reading.

2. **Interactive Mode:**
 - Users can provide input interactively through mouse clicks.
 - The program guides the user to select coordinates by clicking on the screen.
 - Pressing 'q' finishes the coordinate selection.

**Transformations:**

3. **Transformation Functionality:**
 - After input is provided (either from file or interactively), the program allows users to perform transformations on the vertices.
 - The transformations may include translation, rotation, scaling, etc.

**Visualization:**

4. **Visualization of Vertices:**
 - After performing transformations, the program offers the option to visualize the transformed vertices.
 - Users can see the updated positions of vertices on the screen.

**File Output Capabilities:**

5. **Save Transformed Vertices to File:**
 - Users have the option to save the transformed vertices to a file after performing transformations.
 - The program prompts users to enter the filename for saving the transformed vertices.

6. **Save Generated Polygon to File:**
 - If the user chooses to generate a random polygon pattern, there is an option to save the generated polygon to a file.
 - The program prompts users to enter the filename for saving the generated polygon.

**Random Polygon Pattern Generation:**

7. **Random Polygon Pattern Generation:**
 - The program may offer the option to generate a random polygon pattern.
 - Users can choose to generate a random polygon with a specified number of vertices.

**User Interaction:**

8. **Interactive Menu:**
 - The program presents an interactive menu for users to choose between file reading mode and interactive mode.
 - Users can navigate through the program using numerical inputs to select different functionalities.

**Miscellaneous:**

9. **Error Handling:**
 - The program checks for the existence of the specified input file and provides appropriate messages if the file is not found.
 - Error handling for invalid inputs during file reading or interactive mode.

10. **Program Continuity:**
  - The program allows users to perform multiple operations in sequence or exit the program after completing the desired tasks.

These capabilities provide users with flexibility in providing input, transforming data, visualizing results, and saving outputs, making the program versatile and user-friendly.

# Data Structure for Vertices

The data structure used to store the vertices is a list of tuples. Each tuple in the list represents a vertex and its associated information. Let's break down the structure:

python
vertices = [
(1, (x1, y1)),  # Vertex 1 with coordinates (x1, y1)
(2, (x2, y2)),  # Vertex 2 with coordinates (x2, y2)
# ... more vertices ...
]

# Contributing

We welcome contributions to improve this project! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/new-feature` or `git checkout -b bugfix/fix-issue`.
3. Make your changes and commit them: `git commit -m 'Description of your changes'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Submit a pull request.

We appreciate your help!

# License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.



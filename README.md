[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/f_6PzPyj)
# ds-graphical-recursive

Let's get creative. On this lab, you will be creating a recursive program that generates the base for a graphical recursive algorithm. Since we haven't seen any graphics library, you don't need to worry about the visualization, the professor will provide the mechanism ro visualize your data.

From the _Essential Algorithms: A Practical Approach to Computer Algorithms_ book, in [Chapter 9: Recursion](https://learning.oreilly.com/library/view/essential-algorithms-a/9781118612101/17_chapter09.html#c09-5), implement one of the following 3 graphical recursive algorithms

- Koch Curves
- Hilbert Curve
- Sierpiński Curve

# Implementation Requirements

- Each algorithm has its own parameters, make sure you document them in the [following section](#how-to-compile--run-you-program)
- Parameters must be sent through the command line. Example below:
    ```
    ./your-program <param1> <param2> ... 
    ```
- The output of your program will be a list of line segments in a file called `lines.txt`. The `lines.txt` file must follow the following format. Each pair represents a point in a 2D plane
    ```
    (1,2)(33,3)
    (3,5)(3,43)
    (2,1)(3,3)
    ```
- There's a 1024x1024 canvas, make sure that your generated points are inside that limited space. 
- The progressor will provide the mechanism to visualize your data, just make sure you generate the proper `lines.txt` file




# How to compile & run you program

The following instructions will compile and run a program that generates a Koch Curve at a specified depth. The end result is a text file that contains the pair of point coordinates for each line segment that comprise the Koch Curve. The execution command must contian the desired depth and the pair of point coordinates for the first line segment (think of it as the limits of the curve).

**Compilation:**
```
g++ main.cpp
```

**Execution:**
```
./a.out <int depth> <int x1> < int y1> <int x2> <int y2>
```

**Running Graph Generator:**
```
python3 graph_generator.py
```


**Example of final result:**
![alt text](example_figure_1.png)
<center>Parameters: 5, 100, 600, 1000, 600</center>

![alt text](example_figure_2.png)
<center>Parameters: 3, 100, 700, 600, 700</center><br>



# Grading Policy

| **Rubric**                             | **Points** |
|----------------------------------------|------------|
| Successful Compilation                 | 25%        |
| Coding Practices                       | 5%         |
| Well formed `lines.txt` file           | 35%        |
| Proper Algorithm's graphics rendering  | 35%        |
| **Total**                              | 100%       |
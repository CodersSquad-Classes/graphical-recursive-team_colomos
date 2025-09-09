#!/usr/bin/env python3
"""
Graph Generator for Koch Curve Visualization

This script reads line segment data from a text file and displays the resulting
Koch curve using matplotlib. The file format expected is:
(x1,y1)(x2,y2)
where each line represents a line segment with start and end coordinates.

Requirements:
- matplotlib library (install with: pip install matplotlib)

Usage:
    python3 graph_generator.py [filename]

If no filename is provided, it defaults to 'lines.txt'.

Author: Team Colomos
Date: 2025
"""

import ast
import matplotlib.pyplot as plt
import sys
from typing import List, Tuple, Optional

# Type alias for better code readability
Point = Tuple[int, int]
LineSegment = Tuple[Point, Point]

def get_lines_from_file(filepath: str) -> List[LineSegment]:
    """
    Parse line segments from a text file.
    
    Expected file format:
    (x1,y1)(x2,y2)
    (x3,y3)(x4,y4)
    ...
    
    Args:
        filepath: Path to the input file containing line segments
        
    Returns:
        List of line segments, where each segment is a tuple of two points
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist
        ValueError: If the file format is invalid
    """
    lines = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            line_number = 0
            for line in file.readlines():
                line_number += 1
                line = line.strip()
                
                # Skip empty lines
                if not line:
                    continue
                    
                try:
                    # Parse the line format: (x1,y1)(x2,y2)
                    if line.count('(') != 2 or line.count(')') != 2:
                        raise ValueError(f"Invalid format at line {line_number}: {line}")
                    
                    # Split by ')(' to separate the two points
                    parts = line.split(')(')
                    if len(parts) != 2:
                        raise ValueError(f"Invalid format at line {line_number}: {line}")
                    
                    # Parse first point: remove opening '(' if present
                    p1_str = parts[0].lstrip('(') + ')'
                    p1 = ast.literal_eval(p1_str)
                    
                    # Parse second point: add opening '(' and remove closing ')' if needed
                    p2_str = '(' + parts[1].rstrip(')')
                    p2 = ast.literal_eval(p2_str)
                    
                    # Validate that points are tuples of two numbers
                    if not (isinstance(p1, tuple) and len(p1) == 2 and 
                            isinstance(p2, tuple) and len(p2) == 2):
                        raise ValueError(f"Points must be tuples of two numbers at line {line_number}")
                    
                    lines.append((p1, p2))
                    
                except (ValueError, SyntaxError) as e:
                    print(f"Warning: Skipping invalid line {line_number}: {line} - {e}")
                    continue
                    
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        print("Make sure to run the Koch curve generator first to create the file.")
        
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{filepath}'.")
        
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        
    return lines

def plot_lines(lines: List[LineSegment]) -> None:
    """
    Create a matplotlib plot displaying the line segments.
    
    Args:
        lines: List of line segments to plot
    """
    if not lines:
        print("No valid line segments found to plot.")
        return
    
    # Create the plot with proper styling
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_title("Koch Curve Visualization", fontsize=16, fontweight='bold')
    ax.set_xlabel("X-axis (pixels)", fontsize=12)
    ax.set_ylabel("Y-axis (pixels)", fontsize=12)
    
    # Calculate bounds for better visualization
    all_x_coords = []
    all_y_coords = []
    
    for line in lines:
        p1, p2 = line
        all_x_coords.extend([p1[0], p2[0]])
        all_y_coords.extend([p1[1], p2[1]])
    
    # Set axis limits with some padding
    if all_x_coords and all_y_coords:
        x_margin = (max(all_x_coords) - min(all_x_coords)) * 0.05
        y_margin = (max(all_y_coords) - min(all_y_coords)) * 0.05
        
        ax.set_xlim(min(all_x_coords) - x_margin, max(all_x_coords) + x_margin)
        ax.set_ylim(min(all_y_coords) - y_margin, max(all_y_coords) + y_margin)
    
    # Plot each line segment
    print(f"Plotting {len(lines)} line segments...")
    
    for line in lines:
        p1, p2 = line
        line_x = [p1[0], p2[0]]
        line_y = [p1[1], p2[1]]
        
        # Draw the line segment in red with appropriate thickness
        ax.plot(line_x, line_y, color='red', linestyle='-', linewidth=1.5)
    
    # Add grid for better visualization
    ax.grid(True, alpha=0.3)
    
    # Equal aspect ratio to prevent distortion
    ax.set_aspect('equal', adjustable='box')
    
    # Add some statistics as text
    stats_text = f"Total segments: {len(lines)}"
    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
            verticalalignment='top', fontsize=10)
    
    plt.tight_layout()
    plt.show()

def main(file_name: str) -> None:
    """
    Main function to load and visualize Koch curve data.
    
    Args:
        file_name: Path to the file containing line segment data
    """
    print(f"Loading Koch curve data from '{file_name}'...")
    
    # Get the lines from the file
    lines_from_file = get_lines_from_file(file_name)
    
    if not lines_from_file:
        print("No line segments were loaded. Please check the file format and content.")
        return
    
    print(f"Successfully loaded {len(lines_from_file)} line segments.")
    
    try:
        # Plot the Koch curve
        plot_lines(lines_from_file)
    except ImportError as e:
        print(f"Error: matplotlib is required but not installed.")
        print("Install it using: pip install matplotlib")
        sys.exit(1)
    except Exception as e:
        print(f"Error during plotting: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Default filename
    default_file = "lines.txt"
    
    # Check if a custom filename was provided
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        print(f"Using custom file: {file_name}")
    else:
        file_name = default_file
        print(f"No filename provided, using default: {file_name}")
    
    # Validate file extension
    if not file_name.endswith('.txt'):
        print(f"Warning: File '{file_name}' doesn't have .txt extension")
    
    main(file_name)
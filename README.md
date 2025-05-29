# Bubble Sort — Algorithm Explained with Visualization

Welcome to this educational repository where the **Bubble Sort algorithm** is both explained in detail and brought to life through an interactive **Python-based visualization** using OpenCV.

---

## Overview

**Bubble Sort** is a fundamental comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process continues until no further swaps are required — resulting in a sorted array.

This repository demonstrates:
- A clear explanation of how Bubble Sort works.
- A step-by-step animated visualization using Python and OpenCV.
- An educational tool for students and professionals alike.

---

## Algorithm Description

### How it works:
1. Iterate over the array multiple times.
2. During each pass, compare adjacent elements.
3. Swap the elements if they are in the wrong order.
4. Each pass places the next largest unsorted element in its correct position — like a bubble rising to the surface.
5. Repeat until no swaps occur in a complete pass.

### Pseudocode:
```python
for i in range(len(array)):
    for j in range(0, len(array) - i - 1):
        if array[j] > array[j + 1]:
            swap(array[j], array[j + 1])
```
### Time & Space Complexity
| Scenario     | Time Complexity |
| ------------ | --------------- |
| Best Case    | O(n)            |
| Average Case | O(n²)           |
| Worst Case   | O(n²)           |
| Space        | O(1)            |


Note: The best case occurs when the input array is already sorted. The worst case is when the array is sorted in reverse order.

## Visualization
This project includes a Python script that generates an MP4 video showing how the Bubble Sort algorithm works step-by-step. It uses OpenCV to draw bars representing array elements and highlights swaps and comparisons with colors and annotations.

## Features:
- Color-coded comparisons (e.g. red bars during swaps).

- Annotated explanations rendered on each frame.

- Progress tracked through outer loop passes.

- Suitable for classroom use or personal study.

## Installation
- Python 3.x
- OpenCV (cv2)
- NumPy

## Getting Started
1. Clone the repository:
```bash
git clone https://github.com/Mordekai66/bubble-sort-visualizer.git
cd bubble-sort-visualizer
```
3. Install dependencies:
```python
pip install opencv-python numpy
```
3. Run the script:
```python
python bubble_sort_visualizer.py
```
**You can customize the data array in the script to visualize your own set of numbers.**

## Repository Structure
```bash
bubble-sort-visualizer/
├── bubble_sort_visualizer.py     # Main script to generate the video
├── bubble_sort_visualization.mp4 # Output video
└── README.md                     # You're reading it
```
## Educational Purpose
This repository is primarily intended for:

Computer Science students learning sorting algorithms.

Educators creating course materials.

Developers exploring data visualization with OpenCV.

## Feedback & Contributions
Contributions are welcome! If you'd like to add new features (like color themes, more algorithms, or sound effects 🎵), feel free to fork the repo and submit a pull request.

If you found this project helpful, don’t forget to star 🌟 the repository!

## Preview Snapshot

## License
This project is open-source and available under the MIT License.

#  Sorting Algorithm Visualizer

A terminal-based Sorting Algorithm Visualizer built in Python.

---

##  Features

-  Real-time sorting visualization in the terminal
-  Adjustable visualization speeds
-  Built-in sound feedback using `winsound.Beep()`
-  Multiple sorting algorithms:
  - Bubble Sort
  - Selection Sort
  - Quick Sort
-  Simple menu-driven interface
-  Dynamic bar visualization based on element ranking

---

---

##  Language and Modules Used

| Tool | Purpose |
|------|---------|
| Python | Core language |
| `os` | Terminal control |
| `time` | Animation delays |
| `winsound` | Sound feedback |

---

##  Requirements

- Python 3.x
- Windows OS *(uses the built-in `winsound` module)*

> No additional packages need to be installed.

---

##  Getting Started

**Clone the Repository**
```bash
git clone https://github.com/your-username/sorting-algorithm-visualizer.git
```

**Navigate to the Project Directory**
```bash
cd sorting-algorithm-visualizer
```

**Run the Program**
```bash
python sorting_visualizer.py
```

---

## Best Viewing Experience

For the visualization to display properly:

- **Maximize** your terminal or output window.
- If the bars wrap onto the next line in VS Code, increase the terminal zoom using:

```
Ctrl + +
```
or
```
Ctrl + Mouse Wheel Up
```

This ensures all bars remain visible on a single line and improves the overall viewing experience.

---

## Usage

**Step 1 — Enter numbers separated by spaces:**
```
- 9 22 98 21 19 97 6 1 55 51
- 4 25 12 22 11 78 91 3 45 56 19 88 72 34 67 5 99 41 28 60 14 83 7 52 30 95 1 48 76 20 69 9 37 58 81 16 97 24 43 62 10 85 32 74 6 93 27 50 18 71
```

**Step 2 — Choose a sorting algorithm:**
```
1. Selection Sort
2. Bubble Sort
3. Quick Sort
4. Exit
```

**Step 3 — Choose a visualization speed:**
```
1. Fast
2. Medium
3. Slow
```

**Step 4 — Watch the sorting process unfold in real time** as the bars rearrange themselves into sorted order. 

---

## Algorithms Implemented

###  Bubble Sort
Repeatedly compares adjacent elements and swaps them if they are in the wrong order. Simple but intuitive — great for seeing how "heavy" elements bubble to the end.

###  Selection Sort
Finds the smallest element in the unsorted portion of the list and places it in its correct position. Clean and easy to follow visually.

###  Quick Sort
Uses a pivot element to partition the array and recursively sorts the resulting subarrays. Fast in practice and fascinating to watch unfold.

---

---

## Future Improvements

- [ ] Adding more algorithms
- [ ] Highlight comparisons and swaps with color
- [ ] Display sorting statistics (comparisons, swaps, time)
- [ ] Create a GUI version using Pygame

---

## Authors

**Aravind R** and **Aalwin Rajesh** 

> Built during our semester break as a fun learning project — and an excuse to do something more productive than endlessly scrolling through social media. 😄

---

## Show Your Support

If you found this project interesting or useful, consider giving it a **star** on GitHub!  
It motivates us to keep building and improving. 🙌

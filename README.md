# python-line-profiler

🚀 **Optimizing Python Code with `line_profiler`**

This repository contains examples of how to use the `line_profiler` Python tool to analyze and optimize code performance. The examples demonstrate two real-world scenarios: 

1. **File I/O Operations** - Writing and reading large amounts of data to/from a file.
2. **API Calls** - Making requests to an external API and handling JSON responses.

---

## 📂 Project Structure
. ├── script.py # Main Python file with profiled functions └── README.md # Documentation for the repository
---

## 📦 Requirements

- Python 3.7 or higher
- `line_profiler` library

### Install `line_profiler`

```bash
pip install line-profiler
```

🚀 How to Run
1. Execute the script with kernprof:

```python
kernprof -l -v script.py
```
- The -l flag enables the @profile decorator.
- The -v flag outputs the profiling results to the terminal.

📊 Example Output
Here’s an example of the profiling output for the file_io_operations function:

```bash
Timer unit: 1e-06 s

Total time: 0.012345 s
File: script.py
Function: file_io_operations at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
=============================================================
     5         1          3.0      3.0      0.0      with open(file_name, "w") as file:
     6      1000       8765.0      8.8     70.0          file.write(content)
```
From this output, you can identify which lines of code are performance bottlenecks and focus on optimizing them.

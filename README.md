
---

# 🧬✨ Job Shop Scheduling with Genetic Algorithm

An elegant and interactive Python implementation of the **Job Shop Scheduling Problem (JSSP)** using a **Genetic Algorithm (GA)**. Optimize job assignments across multiple machines and visualize your solution with a stunning Gantt chart 📊.

---

## 🚀 Overview

In manufacturing or production systems, scheduling jobs efficiently across different machines is crucial. This project applies a **Genetic Algorithm** to intelligently search for the optimal or near-optimal schedule that **minimizes the makespan** (total completion time).

> ✅ Ideal for researchers, students, and engineers exploring evolutionary algorithms or production planning problems.

---

## 🧠 Problem Description

Given:
- `n` jobs, each consisting of a sequence of operations.
- Each operation must be processed on a **specific machine** for a fixed amount of time.
- No two operations can run on the same machine at the same time.

🎯 **Goal**: Find the best job schedule that **minimizes the total completion time (makespan)**.

---

## 🛠️ Features

✅ Interactive job and operation input  
✅ Customizable Genetic Algorithm parameters  
✅ Intelligent selection, crossover & mutation  
✅ Makespan evaluation for fitness  
✅ Gantt chart visualization of the best schedule  

---

## ⚙️ How to Run

### 1. 💾 Install Dependencies

```bash
pip install matplotlib numpy
```

### 2. 🧪 Run the Script

```bash
python jobshop_ga.py
```

### 3. 📥 Input Example

You'll be prompted to enter job and operation details:

```
Enter the number of jobs: 2
Enter the number of machines: 3

Enter operations for job 1:
  Operation 1 machine: 0
  Operation 1 processing time: 3
  Operation 2 machine: 1
  Operation 2 processing time: 2
  Operation 3 machine: 2
  Operation 3 processing time: 4

Enter operations for job 2:
  Operation 1 machine: 1
  Operation 1 processing time: 2
  Operation 2 machine: 0
  Operation 2 processing time: 1
  Operation 3 machine: 2
  Operation 3 processing time: 5
```

### 🧾 Output

```
Best Schedule: [1, 0]
Best Makespan: 10
```

✨ A Gantt chart is automatically displayed, showing task distribution across machines.

---


## 📁 Project Structure

```
code.py      # Main script with GA logic
README.md          # Project documentation
```

---

## 🧠 Concepts Involved

- Genetic Algorithms (Selection, Crossover, Mutation)
- Scheduling Theory
- Gantt Chart Visualization
- Constraint Satisfaction
- Python Programming

---
## ✍️ Authors

- **Yara Khattab**
-  
  📧 [yarakhattab16@gmail.com](mailto:yarakhattab16@gmail.com)


 
  🔗 [GitHub: @yarakhattab](https://github.com/yarakhattab)

- **Saja Asfour**

- 
  🔗 [GitHub: @SajaAsfour](https://github.com/SajaAsfour)



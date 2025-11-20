# Computational Dynamics — Numerical ODE Solvers (Euler, RK2, RK4)

This repository contains a simple Python implementation of several numerical integration methods for ordinary differential equations (ODEs): **Euler**, **Runge–Kutta 2nd order (RK2)**, and **Runge–Kutta 4th order (RK4)**.
The code visualizes the results using matplotlib and allows solving ODEs of **arbitrary order** using a dynamically constructed system.

The full accompanying report is written **in Polish** and included as *projekt.pdf*. 

---

## 📁 Project contents

The repository contains:

```
projektDO.py     # Main (and only) source code file with numerical ODE solvers
projekt.pdf      # Polish-language course report explaining the methods and results
```

## 🚀 Features

* Solves ODEs of **any order**, using a symbolic expression for the highest derivative.
* Supports three explicit integration schemes:

  * **Euler method**
  * **RK2 midpoint method**
  * **RK4 classical method**
* Allows specifying:

  * derivative order,
  * initial conditions,
  * time step `h`,
  * number of iterations,
  * equation as a Python expression (`"sin(y)"`, `"cos(y)"`, `"y"`, etc.).
* Plots all methods on one graph for comparison.

---

## 📦 Requirements (complete and accurate)

The following packages are required to run `projektDO.py`:

### **Python version**

* **Python 3.9+** (recommended)

### **Python dependencies**

Based directly on imports in the file:

* `matplotlib`
* `collections` (standard library)
* `math` (standard library)

*(All other imports come from the standard Python library and require no installation.)*

---

## ▶️ How to run

Simply execute:

```bash
python projektDO.py
```

This will run all example simulations already included at the bottom of the script:

* First-order ODEs (`y' = y`, `y' = cos(x)`)
* Second-order ODEs (`y'' = sin(y)`, `y'' = -sin(y)`, `y'' = cos(y)`, etc.)
* Comparisons of stability for various time steps `h`

Each call generates a plot comparing **Euler**, **RK2**, and **RK4**.

---

## 🧠 How it works

### Equation definition

Example:

```python
Solve("sin(y)", 2, 0, [0, 1], 0.05, 800)
```

Meaning:

* `sin(y)` → the highest derivative (`y''`)
* `2` → order of the ODE
* `0` → initial x
* `[0,1]` → initial conditions (`y(0)=0`, `y'(0)=1`)
* `0.05` → step size
* `800` → number of iterations

The solver internally builds a first-order system and applies Euler, RK2, and RK4.

---

## 📊 Example output

The script generates plots comparing method accuracy.
A typical output shows:

* **Euler** diverging for larger `h`
* **RK2** moderately stable
* **RK4** very accurate for most `h`

This matches the discussion in the report.

---

## 📘 Course report

The project includes a full written report (in **Polish**) that discusses:

* properties of each integration method,
* numerical stability depending on time step,
* results for nonlinear equations such as ( y'' = -\sin(y) ),
* comparison of energy preservation for various methods.

Report file: *projekt.pdf* 

---

## 🙌 Acknowledgements

Project created as coursework for the university subject
**“Dynamika obliczeniowa” – Computational Dynamics**.


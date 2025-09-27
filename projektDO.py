import matplotlib.pyplot as plt
from math import sin, cos,tan, atan, exp, log, pi
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

def Solve(f_expr, n, x0, initial_conditions, step, num_of_iterations):
    def make_system(expr, order):
        def f_system(x, Y):
            dY = [0] * order
            for i in range(order - 1):
                dY[i] = Y[i + 1]
            local_vars = {"x": x, "y": Y[0], "sin": sin, "cos": cos, "exp": exp, "log": log}
            dY[order - 1] = eval(expr, {}, local_vars)
            return dY
        return f_system

    def euler():
        x = x0
        y_vals = initial_conditions[:]
        results = {x: y_vals[0]}
        for _ in range(num_of_iterations):
            dY = system(x, y_vals)
            y_vals = [y + step * dy for y, dy in zip(y_vals, dY)]
            x = round(x + step, 10)
            results[x] = y_vals[0]
        return results

    def rk2():
        x = x0
        y_vals = initial_conditions[:]
        results = {x: y_vals[0]}
        for _ in range(num_of_iterations):
            k1 = system(x, y_vals)
            y_predict = [y + step * dy for y, dy in zip(y_vals, k1)]
            k2 = system(x + step, y_predict)
            y_vals = [y + step/2 * (a + b) for y, a, b in zip(y_vals, k1, k2)]
            x = round(x + step, 10)
            results[x] = y_vals[0]
        return results

    def rk4():
        x = x0
        y_vals = initial_conditions[:]
        results = {x: y_vals[0]}
        for _ in range(num_of_iterations):
            k1 = system(x, y_vals)
            k2 = system(x + step/2, [y + step/2 * dy for y, dy in zip(y_vals, k1)])
            k3 = system(x + step/2, [y + step/2 * dy for y, dy in zip(y_vals, k2)])
            k4 = system(x + step, [y + step * dy for y, dy in zip(y_vals, k3)])
            y_vals = [y + step/6 * (a + 2*b + 2*c + d) for y, a, b, c, d in zip(y_vals, k1, k2, k3, k4)]
            x = round(x + step, 10)
            results[x] = y_vals[0]
        return results


    def format_initial_conditions():
        terms = []
        for i, val in enumerate(initial_conditions):
            primes = "'" * i
            terms.append(f"y{primes}({x0}) = {val}")
        return ", ".join(terms)

    def function(f, x0, step, num_of_iterations):
      x = x0
      y = f(x)
      Points = [Point(x, y)]
      for _ in range(num_of_iterations):
          x = x + step
          y = f(x)
          Points.append(Point(x, y))
      return Points

    system = make_system(f_expr, n)

    euler_res = euler()
    rk2_res = rk2()
    rk4_res = rk4()

    plt.figure(figsize=(10, 6))
    plt.title(f"$y^{{({n})}} = {f_expr}$\n{format_initial_conditions()}\n h = {step}, ilość iteracji = {num_of_iterations}", fontsize=11)

    plt.plot(euler_res.keys(), euler_res.values(), 'red', label='Euler',marker='o', markersize=3, zorder=2)
    plt.plot(rk2_res.keys(), rk2_res.values(), 'orange', label='RK2', marker='o', markersize=6, zorder=1)
    plt.plot(rk4_res.keys(), rk4_res.values(), 'blue', label='RK4' ,marker='o',markersize=3, zorder=3)


    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

Solve("y", 1, 0,[8.71975], 1, 50)
Solve("y", 1, 0,[8.71975], 0.1, 500)

Solve("sin(y)", 2, 0,[0,1], 0.05, 800)
Solve("sin(y)", 2, 0,[0,1], 0.2, 200)

Solve("-sin(y)", 2, 0,[0,1], 0.001, 80000)
Solve("-sin(y)", 2, 0,[0,1], 0.01, 8000)
Solve("-sin(y)", 2, 0,[0,1], 0.05, 1600)
Solve("-sin(y)", 2, 0,[0,1], 0.2, 400)
Solve("-sin(y)", 2, 0,[0,1], 2, 40)
Solve("-sin(y)", 2, 0,[0,1], 3, 27)
Solve("-sin(y)", 2, 0,[0,1], 5, 16)

Solve("cos(y)", 2, 0,[0,1], 0.02, 2000)
Solve("cos(y)", 2, 0,[0,1], 0.08, 500)
Solve("cos(y)", 2, 0,[0,1], 0.1, 400)
Solve("cos(y)", 2, 0,[0,1], 0.2, 200)
Solve("cos(y)", 2, 0,[0,1], 0.5, 80)
Solve("cos(y)", 2, 0,[0,1], 1, 40)


Solve("cos(x)", 1, 0,[0], 0.1, 100)
Solve("cos(x)", 1, 0,[0], 0.5, 20)

Solve("-sin(x)", 2, 0,[0,0], 0.5, 50)


#Można zauważyć, że im wyższy rząd metody, tym lepiej "znosi" ona zmiany parametru h. . Na przyład, dla rówania y''=-sin(y) (Będziemy rozpatrywać tutaj
#wyniki otrzyamne na długości przedziału = 80 ) można zaobserwować, że  metoda Eulera działa całkiem dobrze dla h=0.01, jednak przy h=0.05 zaczyna
#odbiegać, a dla h>0.02 już bardzo szybko zachodzi znaczna utrata energii. Im większe wartości h, tym szybciej wynik zaczyna odbiegać od rozwiązania.
#Jeśli chodzi o metodę RK4, widzimy, że radzi sobie ona znacznie lepiej niż metoda Eulera, jest ona dokładna w niemalże każdym przypadku, błędne wyniki
#daje dla dużych h, większych od 3. Z kolei metoda RK2, na podanych przykładach, radzi sobie dosyć dobrze dla h < 1. Oczywiście "odpowiednie" wartości h
#zależą od długości przedziału, jaki rozpatrujemy.    
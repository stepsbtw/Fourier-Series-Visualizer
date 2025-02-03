import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def f(x):
    if -2 < x < -1:
        return 0
    if -1 < x < 1:
        return -np.abs(x)
    if 1 < x < 2:
        return 0
    return None # undefined 

def function_visualizer(f, intervals, n=1000):
    for i, (a,b) in enumerate(intervals):
        x = np.linspace(a, b, n)
        y = [f(xi) for xi in x]
        plt.plot(x, y)

    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.show()

def main():
    intervals = [(-2, -1), (-1, 1), (1, 2)]
    function_visualizer(f, intervals)
    
    x = np.linspace(-2,2)
    I = integrate.simpson(f, x)
    print(I)

if __name__ == "__main__":
    main()

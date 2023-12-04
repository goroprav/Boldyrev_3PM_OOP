import numpy as np
from abc import ABC, abstractmethod

class Integral(ABC):
    def __init__(self, num_points, step, precision):
        self.num_points = num_points
        self.step = step
        self.precision = precision

    @abstractmethod
    def calc(self, func, lower_bound, upper_bound):
        pass

class TrapezoidalIntegral(Integral):
    def calc(self, func, lower_bound, upper_bound):
        x = np.linspace(lower_bound, upper_bound, self.num_points)
        y = func(x)
        integral = self.step * (0.5*y[0] + 0.5*y[-1] + np.sum(y[1:-1]))
        return integral

class SimpsonIntegral(Integral):
    def calc(self, func, lower_bound, upper_bound):
        x = np.linspace(lower_bound, upper_bound, self.num_points)
        y = func(x)
        integral = self.step / 3 * (y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]))
        return integral

def f(x):
    return x**2

trapezoidal_integral = TrapezoidalIntegral(num_points=1000, step=0.001, precision=0.0001)
print(trapezoidal_integral.calc(f, 0, 1))

simpson_integral = SimpsonIntegral(num_points=1000, step=0.001, precision=0.0001)
print(simpson_integral.calc(f, 0, 1))


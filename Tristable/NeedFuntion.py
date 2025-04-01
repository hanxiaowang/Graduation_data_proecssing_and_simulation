import sympy as sp
import os
import numpy as np
import datetime
import matplotlib.pyplot as plt
import json
from tqdm import tqdm

hbar = 6.626e-34 / (2 * np.pi)

def solve_equation(A, B, C, D):
    x = sp.Symbol('x')
    f = ((A + x) ** 2 + B ** 2) * x - C * D
    t = sp.solve(f, x)
    return t
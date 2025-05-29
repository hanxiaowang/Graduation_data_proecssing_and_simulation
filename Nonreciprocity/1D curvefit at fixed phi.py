import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *
import math as m
import cmath
from matplotlib import cm
import skrf as rf
import os
import json
voltage=70
S12=np.loadtxt(f'F:\\Nonreciprocity\\20210701\\S12\\20-110\\S\\S12 of coupling(experiment) with A={round(voltage)}.0 mV 2D.txt',delimiter=',')
S21=np.loadtxt(f'F:\\Nonreciprocity\\20210701\\S21\\20-110\\S\\S21 of coupling(experiment) with A={round(voltage)}.0 mV 2D.txt',delimiter=',')

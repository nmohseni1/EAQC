import time
from pylab import*
import numpy as np
from qutip import *
from math import sqrt
from scipy import *
#import matplotlib.pyplot as plt
##*******************************      set up the parapeteres

vac = basis(5, 0)
one = basis(5, 1)
c = create(5)
N = num(5)
print(expect(N, vac)) 

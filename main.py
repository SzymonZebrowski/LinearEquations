from Analyzer import Analyzer
from Solver import Solver
import multiprocessing as mul
import threading
import matplotlib.pyplot as plt
import sys


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        if arg == 'A':
            Analyzer.A()
        elif arg == 'B':
            Analyzer.B()
        elif arg == 'C':
            Analyzer.C()
        elif arg == 'D':
            Analyzer.D()
        elif arg == 'E':
            Analyzer.E()
    #Analyzer.A()
    #Analyzer.B()
    #Analyzer.C()
    #Analyzer.D()
    #Analyzer.E()







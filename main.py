from Analyzer import Analyzer
import matplotlib.pyplot as plt

e = 1

#Analyzer.A()
Analyzer.B()
Analyzer.C()
Analyzer.D()
Analyzer.E()
exit(12321)

equations = [Solver(N=100, e=e, f=2, a1=5+e, a2=-1, a3=-1, method="Jacobi"),
             Solver(N=500, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi"),
             Solver(N=1000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi"),
             Solver(N=2000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi"),
             Solver(N=5000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi")]

times = []
Ns = [100, 500, 1000, 2000, 5000]
for eq in equations:
    eq.jacobi_method(bound=10e-3)
    times.append(eq.time_solved)
    eq.info()


plt.plot(Ns, times)
plt.show()






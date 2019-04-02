from Solver import Solver
import matplotlib.pyplot as plt

e = 1

zad1 = Solver(N=965, e=e, f=2, a1=5+e, a2=-1, a3=-1, method="Jacobi")
zad2 = Solver(N=965, e=e, f=2, a1=5+e, a2=-1, a3=-1, method="Gauss-Seidl")

zad1.solve(10e-9)
zad2.solve(10e-9)

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






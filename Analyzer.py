from Solver import Solver
import matplotlib.pyplot as plt
import multiprocessing as mp


e = 1
c = 6
d = 5


class Analyzer:

    @staticmethod
    def A():
        equation = Solver(N=900 + 10*c + d, e=e, f=2, a1=5+e, a2=-1, a3=-1, method="")
        print(equation.A)
        print(equation.x)
        print(equation.b)

    @staticmethod
    def B():
        equation1 = Solver(N=900 + 10*c + d, e=e, f=2, a1=5+e, a2=-1, a3=-1, method="Jacobi")
        equation2 = Solver(N=900 + 10*c + d, e=e, f=2, a1=5+e, a2=-1, a3=-1, method="Gauss-Seidl")

        equation1.solve(bound=10e-9)
        equation2.solve(bound=10e-9)

    @staticmethod
    def C():
        equation1 = Solver(N=900 + 10 * c + d, e=e, f=2, a1=3, a2=-1, a3=-1, method="Jacobi")
        equation2 = Solver(N=900 + 10 * c + d, e=e, f=2, a1=3, a2=-1, a3=-1, method="Gauss-Seidl")

        equation1.solve(bound=10e-9)
        equation2.solve(bound=10e-9)

    @staticmethod
    def D():
        equation = Solver(N=900 + 10 * c + d, e=e, f=2, a1=3, a2=-1, a3=-1, method="LU")
        equation.solve(bound=10e-9)

    @staticmethod
    def E():
        Ns = [100, 500, 1000, 2000, 5000]
        time_jacobi = []
        time_gauss_seidl = []
        time_lu = []

        equations_jacobi = [Solver(N=100, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi"),
                             Solver(N=500, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi"),
                             Solver(N=1000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi"),
                             Solver(N=2000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi"),
                             Solver(N=5000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi")]

        equations_gauss_seidl = [Solver(N=100, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss_Seidl"),
                            Solver(N=500, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss_Seidl"),
                            Solver(N=1000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss_Seidl"),
                            Solver(N=2000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss_Seidl"),
                            Solver(N=5000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss_Seidl")]

        equations_lu = [Solver(N=100, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="LU"),
                            Solver(N=500, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="LU"),
                            Solver(N=1000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="LU"),
                            Solver(N=2000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="LU"),
                            Solver(N=5000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="LU")]


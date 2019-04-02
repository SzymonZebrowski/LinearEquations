from Solver import Solver
import matplotlib.pyplot as plt
import multiprocessing as mp

def s(x):
    return x.solve()

e = 1
c = 6
d = 5


class Analyzer:


    @staticmethod
    def A():
        equation = Solver(N=900 + 10*c + d, e=e, f=2, a1=5+e, a2=-1, a3=-1, method="")
        print("="*16+"A"+"="*16)
        print(equation.A)
        print(equation.x)
        print(equation.b)

    @staticmethod
    def B():
        print("="*16+"B"+"="*16)

        equation1 = Solver(N=900 + 10*c + d, e=e, f=2, a1=5+e, a2=-1, a3=-1, method="Jacobi")
        equation2 = Solver(N=900 + 10*c + d, e=e, f=2, a1=5+e, a2=-1, a3=-1, method="Gauss-Seidl")

        equation1.solve(bound=10e-9)
        equation2.solve(bound=10e-9)

    @staticmethod
    def C():
        print("="*16+"C"+"="*16)

        equation1 = Solver(N=900 + 10 * c + d, e=e, f=2, a1=3, a2=-1, a3=-1, method="Jacobi")
        equation2 = Solver(N=900 + 10 * c + d, e=e, f=2, a1=3, a2=-1, a3=-1, method="Gauss-Seidl")

        equation1.solve(bound=10e-9)
        equation2.solve(bound=10e-9)

    @staticmethod
    def D():
        print("="*16+"D"+"="*16)

        equation = Solver(N=900 + 10 * c + d, e=e, f=2, a1=3, a2=-1, a3=-1, method="LU")
        equation.solve(bound=10e-9)
    @staticmethod
    def E():

        Ns = [100, 500, 1000, 2000, 5000]
        time_jacobi = []
        time_gauss_seidl = []
        time_lu = []
        e = 1




        results_100 = []

        print(f(11))
        #eq for eq in zipped[0]
        pool = mp.Pool(processes=3)
        r = pool.map(f, [1, 2, 3])
        pool.close()

        pool.close()
        pool.join()



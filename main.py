#from Analyzer import Analyzer
from Solver import Solver
import multiprocessing as mul
import threading
import matplotlib.pyplot as plt
import time

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

        equation1 = Solver(N=900 + 10 * c + d, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi_non_matrix")
        equation2 = Solver(N=900 + 10 * c + d, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss-Seidl_non_matrix")

        equation1.solve(bound=10e-9)
        equation2.solve(bound=10e-9)

        equation1 = Solver(N=900 + 10 * c + d, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi")
        equation2 = Solver(N=900 + 10 * c + d, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss-Seidl")

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
        #equation = Solver(965, e=e, f=2, a1=5+e, a2=-1, a3=-1, method="LU")
        equation.solve(bound=10e-9)



    @staticmethod
    def E():
        print("="*16+"E"+"="*16)

        Ns = [100, 500, 1000, 2000, 3000, 5000]
        e = 1

        equations_jacobi = [Solver(N=100, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi_non_matrix"),
                            Solver(N=500, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi_non_matrix"),
                            Solver(N=1000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi_non_matrix"),
                            Solver(N=2000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi_non_matrix"),
                            Solver(N=3000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi_non_matrix"),
                            Solver(N=5000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi_non_matrix")]

        equations_gauss_seidl = [Solver(N=100, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss-Seidl_non_matrix"),
                                 Solver(N=500, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss-Seidl_non_matrix"),
                                 Solver(N=1000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss-Seidl_non_matrix"),
                                 Solver(N=2000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss-Seidl_non_matrix"),
                                 Solver(N=3000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss-Seidl_non_matrix"),
                                 Solver(N=5000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss-Seidl_non_matrix")]

        equations_lu = [Solver(N=100, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="LU"),
                        Solver(N=500, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="LU"),
                        Solver(N=1000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="LU"),
                        Solver(N=2000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="LU"),
                        Solver(N=3000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="LU"),
                        Solver(N=5000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="LU")]

        zipped = list(zip(equations_jacobi, equations_gauss_seidl, equations_lu))

        times_jacobi = []
        times_gauss_seidl = []
        times_lu = []
        for i in range(6):
            for eq in zipped[i]:
                eq.solve(bound=1e-9)
            times_jacobi.append(zipped[i][0].time_solved)
            times_gauss_seidl.append(zipped[i][1].time_solved)
            times_lu.append(zipped[i][2].time_solved)

        plt.plot(Ns, times_jacobi, label='Jacobi method')
        plt.plot(Ns, times_gauss_seidl, label='Gauss-Seidl method')
        plt.plot(Ns[:-1], times_lu[:-1], label='LU method')
        plt.title('Time of solving equation')
        plt.xlabel('Size of matrix')
        plt.ylabel('Time [s]')
        plt.legend(loc='best')
        plt.savefig("wykresy.jpg")
        plt.show()

    @staticmethod
    def E_parallel():

        Ns = [100, 500, 1000, 2000, 3000, 5000]
        e = 1

        equations_jacobi = [Solver(N=100, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi"),
                            Solver(N=500, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi"),
                            Solver(N=1000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi"),
                            Solver(N=2000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi"),
                            Solver(N=3000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi"),
                            Solver(N=5000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Jacobi")]

        equations_gauss_seidl = [Solver(N=100, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss-Seidl"),
                                 Solver(N=500, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss-Seidl"),
                                 Solver(N=1000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss-Seidl"),
                                 Solver(N=2000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss-Seidl"),
                                 Solver(N=3000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss-Seidl"),
                                 Solver(N=5000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="Gauss-Seidl")]

        equations_lu = [Solver(N=100, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="LU"),
                        Solver(N=500, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="LU"),
                        Solver(N=1000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="LU"),
                        Solver(N=2000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="LU"),
                        Solver(N=3000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="LU"),
                        Solver(N=5000, e=e, f=2, a1=5 + e, a2=-1, a3=-1, method="LU")]

        zipped = list(zip(equations_jacobi, equations_gauss_seidl, equations_lu))

        times_jacobi = []
        times_gauss_seidl = []
        times_lu = []
        for i in range(6):
            thread0 = threading.Thread(target=s, args=(zipped[i][0],))
            thread1 = threading.Thread(target=s, args=(zipped[i][1],))
            thread2 = threading.Thread(target=s, args=(zipped[i][2],))
            thread0.start()
            thread1.start()
            thread2.start()
            thread0.join()
            thread1.join()
            thread2.join()

            times_jacobi.append(zipped[i][0].time_solved)
            times_gauss_seidl.append(zipped[i][1].time_solved)
            times_lu.append(zipped[i][2].time_solved)

        plt.plot(Ns, times_jacobi, label='Jacobi method')
        plt.plot(Ns, times_gauss_seidl, label='Gauss-Seidl method')
        plt.plot(Ns[:-1], times_lu[:-1], label='LU method')
        plt.title('Time of solving equation')
        plt.xlabel('Size of matrix')
        plt.ylabel('Time [s]')
        plt.legend(loc='best')
        plt.savefig("wykresy.jpg")
        plt.show()




if __name__ == '__main__':
    #Analyzer.A()
    #Analyzer.B()
    #Analyzer.C()
    #Analyzer.D()
    Analyzer.E()






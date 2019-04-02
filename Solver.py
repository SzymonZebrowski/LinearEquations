import numpy as np
import time


class Solver:
    def __init__(self, N, e, f, a1, a2, a3, method):
        self.N = N
        self.e = e
        self.f = f
        self.A = self.create_band_matrix(N, a1, a2, a3)
        self.b = self.create_b_vector(N, f)
        self.x = np.zeros((N, 1))
        self.norm_res = 0
        self.iterations = 0
        self.method = method
        self.time_solved = 0

    def create_band_matrix(self, n, a1, a2, a3):
        band_matrix = np.zeros((n, n))

        for i in range(n - 2):
            band_matrix[i][i] = a1
            band_matrix[i + 1][i] = a2
            band_matrix[i + 2][i] = a3
            band_matrix[i][i + 1] = a2
            band_matrix[i][i + 2] = a3

        band_matrix[n - 2][n - 2] = a1
        band_matrix[n - 1][n - 1] = a1
        band_matrix[n - 2][n - 1] = a2
        band_matrix[n - 1][n - 2] = a2

        return band_matrix

    def create_b_vector(self, n, f):
        vec = np.zeros((n, 1))
        for i in range(n):
            vec[i][0] = np.sin(i*(f+1))
        return vec

    def solve(self, bound=10e-6):
        func = None
        if self.method == "Jacobi":
            func = self.jacobi_method
        elif self.method == "Gauss-Seidl":
            func = self.gauss_seidl_method
        elif self.method == "LU":
            func = self.lu_method
        else:
            exit('Unknown solving method')

        try:
            func(bound)
            self.info()
        except Exception as e:
            print(e)

        return self.x

    def jacobi_method(self, bound=10e-6):
        D = np.diag(self.A)
        R = self.A - np.diagflat(D)

        i = 0
        start = time.time()
        while np.linalg.norm(np.dot(self.A, self.x) - self.b) > bound:
            # x(k+1) = (b/D) - ( (L+U)*x(k) )/D
            # L+U = R
            s1 = time.time()
            prev_residuum = np.linalg.norm(np.dot(self.A, self.x) - self.b)
            e1 = time.time()

            self.x = np.dot(np.linalg.inv(np.diagflat(D)), (self.b - np.dot(R, self.x)))

            s2 = time.time()
            actual_residuum = np.linalg.norm(np.dot(self.A, self.x) - self.b)
            e2 = time.time()

            start -= ((e1 - s1)+(e2 - s2))

            i += 1
            if actual_residuum > prev_residuum:
                raise Exception("Residuum doesn't convergence!")
        end = time.time()

        self.x = self.x[:, 0].reshape((self.N, 1))
        self.iterations = i
        self.time_solved = end - start
        self.norm_res = np.linalg.norm(np.dot(self.A, self.x) - self.b)
        return self.x

    def gauss_seidl_method(self, bound=10e-6):
        D = np.diag(self.A)
        L = np.tril(self.A, -1)
        U = np.triu(self.A, 1)

        i = 0
        start = time.time()
        while np.linalg.norm(np.dot(self.A, self.x) - self.b) > bound:
            # x(k+1) = -(U * x(k) )/(D+L) + b / (D+L)
            s1 = time.time()
            prev_residuum = np.linalg.norm(np.dot(self.A, self.x) - self.b)
            e1 = time.time()

            self.x = np.dot(np.linalg.inv(L + np.diagflat(D)), (self.b - np.dot(U, self.x)))

            s2 = time.time()
            actual_residuum = np.linalg.norm(np.dot(self.A, self.x) - self.b)
            e2 = time.time()

            start -= ((e1 - s1) + (e2 - s2))

            i += 1
            if actual_residuum > prev_residuum:
                raise Exception("Residuum doesn't convergence!")
        end = time.time()

        self.x = self.x[:, 0].reshape((self.N, 1))
        self.iterations = i
        self.time_solved = end - start
        self.norm_res = np.linalg.norm(np.dot(self.A, self.x) - self.b)
        return self.x

    def lu_method(self, bound):
        L = np.tril(self.A)
        U = np.triu(self.A)
        #Lz = b
        #Ux = z


    def info(self):
        print("#" * 30)
        print("Equation solved!")
        print("Matrix size: " + str(self.N))
        print("Solving method: " + self.method)
        print("Residuum norm: " + str(self.norm_res))
        print("Number of iterations: " + str(self.iterations))
        print("Time: " + str(self.time_solved))
        print("#" * 30)

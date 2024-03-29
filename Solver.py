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
            vec[i][0] = np.sin((i+1)*(f+1))
        return vec

    def solve(self, bound=1e-9):
        func = None
        if self.method == "Jacobi_inv":
            func = self.jacobi_method
        elif self.method == "Gauss-Seidl_inv":
            func = self.gauss_seidl_method
        elif self.method == "Jacobi":
            func = self.jacobi_method_non_matrix
        elif self.method == "Gauss-Seidl":
            func = self.gauss_seidl_method_non_matrix
        elif self.method == "LU":
            func = self.lu_method
        else:
            exit('Unknown solving method')

        try:
            func(bound)
            self.info()
        except Exception as e:
            print(e)

        return self

    def jacobi_method(self, bound=1e-9):
        '''bad implementation, we shouldn't inverse matrix'''
        #matrix version
        D = np.diag(self.A)
        R = self.A - np.diagflat(D)
        D_inv = np.linalg.inv(np.diagflat(D))
        i = 0
        actual_residuum = np.linalg.norm(np.dot(self.A, self.x) - self.b) > bound
        start = time.time()

        while actual_residuum > bound:
            # x(k+1) = (b/D) - ( (L+U)*x(k) )/D
            # L+U = R
            s1 = time.time()
            prev_residuum = np.linalg.norm(np.dot(self.A, self.x) - self.b)
            e1 = time.time()

            self.x = np.dot(D_inv, (self.b - np.dot(R, self.x)))

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

    def gauss_seidl_method(self, bound=1e-9):
        '''bad implementation, we shouldn't inverse matrix'''
        #matrix version

        D = np.diag(self.A)
        L = np.tril(self.A, -1)
        U = np.triu(self.A, 1)
        LU_inv = np.linalg.inv(L + np.diagflat(D))
        i = 0
        start = time.time()
        while np.linalg.norm(np.dot(self.A, self.x) - self.b) > bound:
            # x(k+1) = -(U * x(k) )/(D+L) + b / (D+L)
            s1 = time.time()
            prev_residuum = np.linalg.norm(np.dot(self.A, self.x) - self.b)
            e1 = time.time()

            self.x = np.dot(LU_inv, (self.b - np.dot(U, self.x)))

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

    def jacobi_method_non_matrix(self, bound=1e-9):
        '''good version without inversing matrix'''
        x_n = np.ones((self.N, 1))

        x = 0
        start = time.time()
        while np.linalg.norm(np.dot(self.A, self.x) - self.b) > bound:

            s1 = time.time()
            prev_residuum = np.linalg.norm(np.dot(self.A, self.x) - self.b)
            e1 = time.time()

            for i in range(self.N):
                p1 = np.dot(self.A[i, :i], self.x[:i])
                p2 = np.dot(self.A[i, i + 1:], self.x[i + 1:])
                x_n[i, 0] = (self.b[i] - p1 - p2) / self.A[i, i]

            self.x = np.copy(x_n)

            s2 = time.time()
            actual_residuum = np.linalg.norm(np.dot(self.A, self.x) - self.b)
            e2 = time.time()

            start -= ((e1 - s1)+(e2 - s2))

            x += 1
            if x>1000:
                raise Exception(f"Residuum doesn't convergence after {x} iterations!")
        end = time.time()
        self.iterations = x
        self.time_solved = end - start
        self.norm_res = np.linalg.norm(np.dot(self.A, self.x) - self.b)
        return self.x

    def gauss_seidl_method_non_matrix(self, bound=1e-9):
        '''good version without inversing matrix'''
        x_n = np.ones((self.N, 1))

        x = 0
        start = time.time()
        while np.linalg.norm(np.dot(self.A, self.x) - self.b) > bound:

            s1 = time.time()
            prev_residuum = np.linalg.norm(np.dot(self.A, self.x) - self.b)
            e1 = time.time()

            for i in range(self.N):
                p1 = np.dot(self.A[i, :i], x_n[:i])
                p2 = np.dot(self.A[i, i + 1:], self.x[i + 1:])
                x_n[i, 0] = (self.b[i] - p1 - p2) / self.A[i, i]

            self.x = np.copy(x_n)

            s2 = time.time()
            actual_residuum = np.linalg.norm(np.dot(self.A, self.x) - self.b)
            e2 = time.time()

            start -= ((e1 - s1) + (e2 - s2))

            x += 1
            if x>1000:
                raise Exception(f"Residuum doesn't convergence after {x} iterations!")
        end = time.time()
        self.iterations = x
        self.time_solved = end - start
        self.norm_res = np.linalg.norm(np.dot(self.A, self.x) - self.b)
        return self.x

    def lu_method(self, bound):
        U = np.copy(self.A)
        L = np.eye(self.N)

        start = time.time()
        #decomposition


        for k in range(self.N-1):
            for j in range(k+1, self.N):
                L[j,k] = U[j,k]/U[k,k]
                U[j, k:self.N] -= L[j, k]*U[k, k:self.N]


        #solving
        #forward substitution Ly = b
        y = np.zeros(self.N)
        y[0] = self.b[0]/L[0, 0]
        #y[0, 0] = self.b[0, 0] / L[0, 0]
        for i in range(1, self.N):
            sum = 0
            for j in range(0, i):
                sum += L[i, j] * y[j]
            y[i] = (self.b[i]) - sum / L[i, i]

        #backward substitution Ux = y

        for i in range(self.N-1, -1, -1):
            sum = y[i]
            for j in range(i, self.N):
                if i!=j:
                    sum -= U[i, j] * self.x[j]
            self.x[i] = sum / U[i, i]

        end = time.time()
        self.time_solved = end - start
        self.norm_res = np.linalg.norm(np.dot(self.A, self.x) - self.b)
        return self.x

    def info(self):
        print("#" * 30)
        print("Equation solved!")
        print("Matrix size: " + str(self.N))
        print("Solving method: " + self.method)
        print("Residuum norm: " + str(self.norm_res))
        print("Number of iterations: " + str(self.iterations))
        print("Time: " + str(self.time_solved))
        print("#" * 30)

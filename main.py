import numpy as np
from scipy.linalg import solve
N = 965
e = 1


class Solver:
    def __init__(self, N, e, f, a1, a2, a3):
        self.N = N
        self.e = e
        self.f = f
        self.A = self.create_band_matrix(N, a1, a2, a3)
        self.b = self.create_b_vector(N, f)
        self.x = np.zeros((N, 1))

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

    def jacobi_method(self, bound=10e-6):
        D = np.diag(self.A)
        R = self.A - np.diagflat(D)

        i = 0
        while np.linalg.norm(np.dot(self.A, self.x) - self.b) > bound:

            self.x = (self.b - np.dot(R, self.x))/D
            i+=1

        print(i)
        return self.x[:, 0].reshape((self.N, 1))


zad1 = Solver(N=5, e=e, f=2, a1=5+e, a2=-1, a3=-1)
x = zad1.jacobi_method(bound=10e-9)
print(zad1.A)

print(x)

import numpy as np
N = 965
e = 1


class Solver:
    def __init__(self, N, e, f, a1, a2, a3):
        self.N = N
        self.e = e
        self.f = f
        self.A = self.create_band_matrix(N, a1, a2, a3)
        self.b = self.create_b_vector(N, f)

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
        vec = np.zeros((1, n))
        for i in range(n):
            vec[0][i] = np.sin(i*(f+1))
        return vec


zad1 = Solver(N=5, e=e, f=2, a1=5+e, a2=-1, a3=-1)

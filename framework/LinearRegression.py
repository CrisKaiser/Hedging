
import numpy as np

class LinearRegression:

    @staticmethod
    def calcSolutionVector(matrix, result_vec):
        pinv = LinearRegression.getPenroseInverse(matrix)
        return np.dot(pinv, result_vec)

    @staticmethod
    def getPenroseInverse(matrix):
        return np.linalg.pinv(matrix)
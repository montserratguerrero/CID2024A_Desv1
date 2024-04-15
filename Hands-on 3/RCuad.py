from typing import List
import numpy as np

class RCuad:
    def __init__(self):
        # Coeficientes y estadísticas iniciales
        self.__private_a_0: float = 0.0
        self.__private_a_1: float = 0.0
        self.__private_a_2: float = 0.0
        self.__private_coefficient_determination: float = 0.0
        self.__private_coefficient_correlation: float = 0.0

    # Getters para los coeficientes de determinación y correlación
    def get_coefficient_determination(self) -> float:
        return self.__private_coefficient_determination

    def get_coefficient_correlation(self) -> float:
        return self.__private_coefficient_correlation

    # Método para calcular la ecuación de regresión cuadrática
    def to_compute_equation(self, n: int, sum_x: float, sum_x_quad: float, sum_x_cub: float, sum_x_fourth: float, sum_y: float, sum_xy: float, sum_x_quad_y: float) -> None:
        # Matriz X
        x_matrix = np.array([[n, sum_x, sum_x_quad], [sum_x, sum_x_quad, sum_x_cub], [sum_x_quad, sum_x_cub, sum_x_fourth]])

        # Array B
        b_array = np.array([sum_y, sum_xy, sum_x_quad_y])

        # Inversa de la matriz X * Array B
        results = np.dot(np.linalg.inv(x_matrix), b_array)

        # Asignación de los coeficientes calculados
        self.__private_a_0 = round(results[0], 6)
        self.__private_a_1 = round(results[1], 6)
        self.__private_a_2 = round(results[2], 6)

    # Método para calcular el coeficiente de determinación
    def to_compute_coefficient_determination(self, data_x: List[float], data_y: List[float], n: int):
        avg = 0
        sse = 0
        sst = 0

        # Promedio de los valores de Y
        for i in range(n):
            avg += data_y[i]
        avg /= n

        # SSE (Suma de errores cuadráticos)
        for i in range(n):
            sse += ((data_y[i] - self.to_predict(data_x[i])) ** 2)

        # SST (Suma total de cuadrados)
        for i in range(n):
            sst += ((data_y[i] - avg) ** 2)

        # Cálculo del coeficiente de determinación
        self.__private_coefficient_determination = round(1 - (sse / sst), 4)

    # Método para calcular el coeficiente de correlación
    def to_compute_coefficient_correlation(self) -> None:
        # Cálculo del coeficiente de correlación como la raíz cuadrada del coeficiente de determinación
        self.__private_coefficient_correlation = round(np.sqrt(self.__private_coefficient_determination), 4)

    # Método para imprimir la ecuación de regresión calculada
    def to_print_regression_eq(self) -> None:
        print(f' \nY = {self.__private_a_0} + {self.__private_a_1}x + {self.__private_a_2}x^2')

    # Método para predecir un valor utilizando la ecuación de regresión
    def to_predict(self, independent_var: float) -> float:
        return round(self.__private_a_0 + (self.__private_a_1 * independent_var) + (self.__private_a_2 * (independent_var ** 2)), 2)

    # Método para imprimir la predicción de un valor utilizando la ecuación de regresión
    def print_prediction(self, independent_var: float) -> None:
        print(f'X = {independent_var}, Y = {self.to_predict(independent_var)}')

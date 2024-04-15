from typing import List

class Mate:
    def __init__(self, n: int):
        # Inicialización de la clase con el número de observaciones (n)
        self.__private_n: int = n

    # Suma de los valores de X
    def sum_x(self, data: List[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i]
        return total

    # Suma de los valores de Y
    def sum_y(self, data: List[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i]
        return total

    # Suma de los valores de X al cuadrado
    def sum_x_quad(self, data: List[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i] ** 2
        return total

    # Suma de los valores de X al cubo
    def sum_x_cub(self, data: List[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i] ** 3
        return total

    # Suma de los valores de X a la cuarta potencia
    def sum_x_fourth(self, data: List[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i] ** 4
        return total

    # Suma de los valores de X a la quinta potencia
    def sum_x_fifth(self, data: List[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i] ** 5
        return total

    # Suma de los valores de X a la sexta potencia
    def sum_x_sixth(self, data: List[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i] ** 6
        return total

    # Suma de los cuadrados de los valores de Y
    def sum_y_quad(self, data: List[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data[i] * data[i]
        return total

    # Suma de los productos de los valores de X y Y
    def sum_xy(self, data_x: List[float], data_y: List[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += data_x[i] * data_y[i]
        return total

    # Suma de los cuadrados de los valores de X multiplicados por Y
    def sum_x_quad_y(self, data_x: List[float], data_y: List[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += (data_x[i] ** 2) * data_y[i]
        return total

    # Suma de los cubos de los valores de X multiplicados por Y
    def sum_x_cub_y(self, data_x: List[float], data_y: List[float]) -> float:
        total = 0.0
        for i in range(self.__private_n):
            total += (data_x[i] ** 3) * data_y[i]
        return total

    # Suma del producto de la suma de los valores de X consigo misma
    def sum_x_sum_x(self, data: List[float]) -> float:
        return self.sum_x(data) * self.sum_x(data)

    # Suma del producto de la suma de los valores de Y consigo misma
    def sum_y_sum_y(self, data: List[float]) -> float:
        return self.sum_y(data) * self.sum_y(data)

    # Suma del producto de la suma de los valores de X y la suma de los valores de Y
    def sum_x_sum_y(self, data_x: List[float], data_y: List[float]) -> float:
        return self.sum_x(data_x) * self.sum_y(data_y)


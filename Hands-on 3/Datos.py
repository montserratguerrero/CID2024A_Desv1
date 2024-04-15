from typing import List

class Datos:
    def __init__(self):
        # Datos codificados
        self.__private_x: List[float] = [108.0, 115.0, 106.0, 97.0, 95.0, 91.0, 97.0, 83.0, 83.0, 78.0, 54.0, 67.0, 56.0, 53.0, 61.0, 115.0, 81.0, 78.0, 30.0, 45.0, 99.0, 32.0, 25.0, 28.0, 90.0, 89.0]
        # Datos de la variable dependiente (Y)
        self.__private_y: List[float] = [95.0, 96.0, 95.0, 97.0, 93.0, 94.0, 95.0, 93.0, 92.0, 86.0, 73.0, 80.0, 65.0, 69.0, 77.0, 96.0, 87.0, 89.0, 60.0, 63.0, 95.0, 61.0, 55.0, 56.0, 94.0, 93.0]
        # Número de observaciones en los datos
        self.__private_n: int = len(self.__private_x)

    # Método para obtener los valores de la variable independiente (X)
    def get_x(self) -> List[float]:
        return self.__private_x

    # Método para obtener los valores de la variable dependiente (Y)
    def get_y(self) -> List[float]:
        return self.__private_y

    # Método para obtener el número de observaciones
    def get_n(self) -> int:
        return self.__private_n

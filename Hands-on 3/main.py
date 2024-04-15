from Datos import Datos  # Importa la clase Datos desde el archivo Datos.py
from Mate import Mate  # Importa la clase Mate desde el archivo Mate.py
from RLineal import RLineal  # Importa la clase RLineal desde el archivo RLineal.py
from RCuad import RCuad  # Importa la clase RCuad desde el archivo RCuad.py
from RCub import RCub  # Importa la clase RCub desde el archivo RCub.py

# Instancias de objetos
data_set = Datos()  # Crea una instancia de la clase Datos
discrete_maths = Mate(data_set.get_n())  # Crea una instancia de la clase Mate con el número de datos
RLineal = RLineal()  # Crea una instancia de la clase RLineal
RCuad = RCuad()  # Crea una instancia de la clase RCuad
RCub = RCub()  # Crea una instancia de la clase RCub

# Operaciones e impresiones de RLineal
def RLineal_operations():
    # Calculando beta_1 y beta_0
    RLineal.to_compute_beta_1(discrete_maths.sum_xy(data_set.get_x(), data_set.get_y()), discrete_maths.sum_x_sum_y(data_set.get_x(), data_set.get_y()), discrete_maths.sum_x_quad(data_set.get_x()), discrete_maths.sum_x_sum_x(data_set.get_x()), data_set.get_n())

    RLineal.to_compute_beta_0(discrete_maths.sum_y(data_set.get_y()), discrete_maths.sum_x(data_set.get_x()), data_set.get_n())

    # Imprimir la ecuación de regresión
    RLineal.to_print_regression_eq()

    # Predicciones
    print('\nPREDICCIONES')
    RLineal.print_prediction(62)
    RLineal.print_prediction(67)  # Valor del conjunto de datos
    RLineal.print_prediction(77)
    RLineal.print_prediction(83)  # Valor del conjunto de datos

    print('\nCOEFICIENTES')

    # Coeficiente de Determinación
    RLineal.to_compute_coefficient_determination(data_set.get_x(), data_set.get_y(), data_set.get_n())
    print(f'R^2 / DETERMINACIÓN = {RLineal.get_coefficient_determination()}')

    # Coeficiente de Correlación
    RLineal.to_compute_coefficient_correlation()
    print(f'R   / CORRELACIÓN   = {RLineal.get_coefficient_correlation()}')

# Operaciones e impresiones de RCuad
def RCuad_operations():
    RCuad.to_compute_equation(data_set.get_n(), discrete_maths.sum_x(data_set.get_x()), discrete_maths.sum_x_quad(data_set.get_x()), discrete_maths.sum_x_cub(data_set.get_x()), discrete_maths.sum_x_fourth(data_set.get_x()), discrete_maths.sum_y(data_set.get_y()), discrete_maths.sum_xy(data_set.get_x(), data_set.get_y()), discrete_maths.sum_x_quad_y(data_set.get_x(), data_set.get_y()))

    RCuad.to_print_regression_eq()

    print('\nPREDICCIONES')
    RCuad.print_prediction(62)
    RCuad.print_prediction(67)  # Valor del conjunto de datos
    RCuad.print_prediction(77)
    RCuad.print_prediction(83)  # Valor del conjunto de datos

    print('\nCOEFICIENTES')
    RCuad.to_compute_coefficient_determination(data_set.get_x(), data_set.get_y(), data_set.get_n())
    print(f'R^2 / DETERMINACIÓN = {RCuad.get_coefficient_determination()}')

    RCuad.to_compute_coefficient_correlation()
    print(f'R   / CORRELACIÓN   = {RCuad.get_coefficient_correlation()}')

# Operaciones e impresiones de RCub
def RCub_operations():
    RCub.to_compute_equation(data_set.get_n(), discrete_maths.sum_x(data_set.get_x()), discrete_maths.sum_x_quad(data_set.get_x()), discrete_maths.sum_x_cub(data_set.get_x()), discrete_maths.sum_x_fourth(data_set.get_x()), discrete_maths.sum_x_fifth(data_set.get_x()), discrete_maths.sum_x_sixth(data_set.get_x()), discrete_maths.sum_y(data_set.get_y()), discrete_maths.sum_xy(data_set.get_x(), data_set.get_y()), discrete_maths.sum_x_quad_y(data_set.get_x(), data_set.get_y()), discrete_maths.sum_x_cub_y(data_set.get_x(), data_set.get_y()))

    RCub.to_print_regression_eq()

    print('\nPREDICCIONES')
    RCub.print_prediction(62)
    RCub.print_prediction(67)  # Valor del conjunto de datos
    RCub.print_prediction(77)
    RCub.print_prediction(83)  # Valor del conjunto de datos

    print('\nCOEFICIENTES')

    RCub.to_compute_coefficient_determination(data_set.get_x(), data_set.get_y(), data_set.get_n())
    print(f'R^2 / DETERMINACIÓN = {RCub.get_coefficient_determination()}')

    RCub.to_compute_coefficient_correlation()
    print(f'R   / CORRELACIÓN   = {RCub.get_coefficient_correlation()}')

# Función Principal
def main():
    print("\n")
    print(f'{"(" * 2} Ecuación de Regresión Lineal Simple {")" * 2}')
    RLineal_operations()
    print("\n")
    print(f'{"(" * 2} Ecuación de Regresión Cuadrática {")" * 2}')
    RCuad_operations()
    print("\n")
    print(f'{"(" * 2} Ecuación de Regresión Cúbica {")" * 2}')
    RCub_operations()
    print("\n")
    print(f'{"MILAGROS MONTSERRAT GUERRERO SOLANO" * 1}')

if __name__ == "__main__":
    main()

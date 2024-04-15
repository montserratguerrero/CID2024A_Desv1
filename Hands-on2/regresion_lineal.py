class RegresionLineal:
    def __init__(self, X_train, y_train):
        # Inicialización de la clase con los datos de entrenamiento
        self.X_train = X_train  # Conjunto de valores X
        self.y_train = y_train  # Conjunto de valores Y
        self.Bo = None  # Coeficiente Bo (intercepto)
        self.Bi = None  # Coeficiente Bi (pendiente)

    def entrenar_modelo(self):
        # Método para entrenar el modelo de regresión lineal
        n = len(self.X_train)  # Número de muestras
        sum_x = sum(self.X_train)  # Suma de valores X
        sum_y = sum(self.y_train)  # Suma de valores Y
        sum_xy = sum(x * y for x, y in zip(self.X_train, self.y_train))  # Suma de productos XY
        sum_x_squared = sum(x**2 for x in self.X_train)  # Suma de valores X al cuadrado

        # Calculando los coeficientes Bo y Bi de la regresión lineal
        self.Bi = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
        self.Bo = (sum_y - self.Bi * sum_x) / n

    def ecuacion_regresion(self):
        # Método para obtener la ecuación de regresión
        return f"Ecuación de regresión: y = {self.Bo} + {self.Bi} * x"

    def predecir_valor(self, X_pred):
        # Método para predecir un valor de Y para un valor dado de X
        return self.Bo + self.Bi * X_pred

    def coeficiente_correlacion(self):
        # Método para calcular el coeficiente de correlación
        x_mean = sum(self.X_train) / len(self.X_train)  # Media de valores X
        y_mean = sum(self.y_train) / len(self.y_train)  # Media de valores Y
        numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(self.X_train, self.y_train))  # Numerador
        denominator = (sum((x - x_mean)**2 for x in self.X_train) * sum((y - y_mean)**2 for y in self.y_train)) ** 0.5  # Denominador
        return numerator / denominator  # Coeficiente de correlación

    def coeficiente_determinacion(self):
        # Método para calcular el coeficiente de determinación (R^2)
        y_pred = [self.predecir_valor(x) for x in self.X_train]  # Valores predichos de Y
        y_mean = sum(self.y_train) / len(self.y_train)  # Media de valores Y
        ss_total = sum((y - y_mean)**2 for y in self.y_train)  # Suma de cuadrados total
        ss_res = sum((y - yp)**2 for y, yp in zip(self.y_train, y_pred))  # Suma de cuadrados de la regresión
        return 1 - (ss_res / ss_total)  # Coeficiente de determinación (R^2)

# Datos de entrada
X_train = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Valores de X
y_train = [2, 4, 6, 8, 10, 12, 14, 16, 18]  # Valores de Y

# Crear objeto de regresión lineal
regresion = RegresionLineal(X_train, y_train)

# Entrenar el modelo
regresion.entrenar_modelo()

# Imprimir ecuación de regresión
print(regresion.ecuacion_regresion())

# Calcular y predecir un valor de X
X_pred = 20
print(f"Valor predicho para x={X_pred}: {regresion.predecir_valor(X_pred)}")

# Calcular coeficiente de correlación
print(f"Coeficiente de correlación: {regresion.coeficiente_correlacion()}")

# Calcular coeficiente de determinación
print(f"Coeficiente de determinación (R^2): {regresion.coeficiente_determinacion()}")


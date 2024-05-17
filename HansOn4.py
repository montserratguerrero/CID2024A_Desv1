class KNN:
    def __init__(self, k=3):
        """
        Inicializa el clasificador kNN.

        Parámetros:
        - k: Número de vecinos a considerar (por defecto es 3).
        """
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X_train, y_train):
        """
        Entrena el modelo kNN.

        Parámetros:
        - X_train: Datos de entrenamiento, una lista de listas de tamaño (n_samples, n_features).
        - y_train: Etiquetas de los datos de entrenamiento, una lista de tamaño (n_samples,).
        """
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        """
        Realiza predicciones sobre nuevos datos.

        Parámetros:
        - X_test: Datos de prueba, una lista de listas de tamaño (n_samples, n_features).

        Retorna:
        - predictions: Predicciones para los datos de prueba, una lista de tamaño (n_samples,).
        """
        if self.X_train is None or self.y_train is None:
            raise ValueError("El modelo no ha sido entrenado. Utilice el método fit primero.")

        predictions = []
        for sample in X_test:
            distances = [self.euclidean_distance(sample, x) for x in self.X_train]
            nearest_indices = sorted(range(len(distances)), key=lambda i: distances[i])[:self.k]
            nearest_labels = [self.y_train[i] for i in nearest_indices]
            most_common = self.most_common_label(nearest_labels)
            predictions.append(most_common)
        return predictions

    def euclidean_distance(self, p1, p2):
        """
        Calcula la distancia euclidiana entre dos puntos.

        Parámetros:
        - p1: Primer punto, una lista de coordenadas.
        - p2: Segundo punto, una lista de coordenadas.

        Retorna:
        - distance: La distancia euclidiana entre los dos puntos.
        """
        distance_squared = sum((a - b) ** 2 for a, b in zip(p1, p2))
        return self.sqrt(distance_squared)

    def sqrt(self, x, epsilon=1e-6):
        """
        Calcula la raíz cuadrada de un número usando el método de Newton.

        Parámetros:
        - x: Número del cual se quiere calcular la raíz cuadrada.
        - epsilon: Precisión deseada.

        Retorna:
        - La raíz cuadrada de x.
        """
        guess = x
        while True:
            guess_squared = guess * guess
            diff = abs(guess_squared - x)
            if diff <= epsilon:
                return guess
            guess = (guess + x / guess) / 2

    def most_common_label(self, labels):
        """
        Encuentra la etiqueta más común en una lista de etiquetas.

        Parámetros:
        - labels: Lista de etiquetas.

        Retorna:
        - most_common_label: La etiqueta más común.
        """
        label_count = {}
        for label in labels:
            if label in label_count:
                label_count[label] += 1
            else:
                label_count[label] = 1
        most_common_label = max(label_count, key=label_count.get)
        return most_common_label

    def accuracy(self, X_test, y_test):
        """
        Calcula la precisión del modelo sobre datos de prueba.

        Parámetros:
        - X_test: Datos de prueba, una lista de listas de tamaño (n_samples, n_features).
        - y_test: Etiquetas verdaderas de los datos de prueba, una lista de tamaño (n_samples,).

        Retorna:
        - accuracy: La precisión del modelo.
        """
        predictions = self.predict(X_test)
        correct = sum(predictions[i] == y_test[i] for i in range(len(predictions)))
        total = len(y_test)
        accuracy = correct / total
        return accuracy

# Ejemplo de uso:
if __name__ == "__main__":
    # Datos de ejemplo
    X_train = [[1, 2], [2, 3], [3, 4], [4, 5]]
    y_train = [0, 0, 1, 1]
    X_test = [[3, 3], [1, 1]]
    y_test = [1, 0]

    # Crear instancia de kNN
    knn = KNN(k=2)

    # Entrenar el modelo
    knn.fit(X_train, y_train)

    # Predecir
    predictions = knn.predict(X_test)
    print("Predicciones:", predictions)

    # Calcular precisión
    accuracy = knn.accuracy(X_test, y_test)
    print("Precisión:", accuracy)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree

# ==========================================
# DATOS DE ENTRENAMIENTO
# ==========================================

datos = {
    "horas_estudio": [1, 2, 3, 4, 5, 6, 7, 8, 2, 5],
    "asistencia": [50, 60, 65, 70, 80, 85, 90, 95, 55, 88],
    "tareas": [1, 2, 3, 4, 5, 5, 5, 5, 2, 4],
    "resultado": [
        "Reprueba",
        "Reprueba",
        "Reprueba",import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree

# ==========================================
# DATOS DE ENTRENAMIENTO
# ==========================================

datos = {
    "horas_estudio": [1, 2, 3, 4, 5, 6, 7, 8, 2, 5],
    "asistencia": [50, 60, 65, 70, 80, 85, 90, 95, 55, 88],
    "tareas": [1, 2, 3, 4, 5, 5, 5, 5, 2, 4],
    "resultado": [
        "Reprueba",
        "Reprueba",
        "Reprueba",
        "Aprueba",
        "Aprueba",
        "Aprueba",
        "Aprueba",
        "Aprueba",
        "Reprueba",
        "Aprueba"
    ]
}

df = pd.DataFrame(datos)

# Variables de entrada y salida
X = df[["horas_estudio", "asistencia", "tareas"]]
y = df["resultado"]

# División de datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Crear y entrenar modelo
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

# ==========================================
# INGRESO DE DATOS DEL USUARIO
# ==========================================

print("===== INGRESO DE DATOS =====")

horas = float(input("Ingrese horas de estudio: "))
asistencia = float(input("Ingrese porcentaje de asistencia: "))
tareas = float(input("Ingrese cantidad de tareas realizadas: "))

nuevo_estudiante = pd.DataFrame({
    "horas_estudio": [horas],
    "asistencia": [asistencia],
    "tareas": [tareas]
})

# ==========================================
# MOSTRAR DATOS INGRESADOS
# ==========================================

print("\n===== DATOS DEL ESTUDIANTE =====")
print("Horas de estudio:", horas)
print("Asistencia:", asistencia, "%")
print("Tareas realizadas:", tareas)

# ==========================================
# PREDICCIÓN
# ==========================================

prediccion = modelo.predict(nuevo_estudiante)

print("\n===== PREDICCIÓN =====")
print("Resultado predicho:", prediccion[0])

# ==========================================
# EVALUACIÓN DEL MODELO
# ==========================================

y_pred = modelo.predict(X_test)
precision = accuracy_score(y_test, y_pred)

print("\n===== EVALUACIÓN =====")
print("Precisión del modelo:", round(precision * 100, 2), "%")

# ==========================================
# DIBUJAR ÁRBOL
# ==========================================

plt.figure(figsize=(12, 8))

tree.plot_tree(
    modelo,
    feature_names=X.columns,
    class_names=modelo.classes_,
    filled=True,
    rounded=True,
    fontsize=10
)

plt.title("Árbol de Decisión - Aprobación de Estudiantes")

plt.show()
        "Aprueba",
        "Aprueba",
        "Aprueba",
        "Aprueba",
        "Aprueba",
        "Reprueba",
        "Aprueba"
    ]
}

df = pd.DataFrame(datos)

# Variables de entrada y salida
X = df[["horas_estudio", "asistencia", "tareas"]]
y = df["resultado"]

# División de datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Crear y entrenar modelo
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

# ==========================================
# INGRESO DE DATOS DEL USUARIO
# ==========================================

print("===== INGRESO DE DATOS =====")

horas = float(input("Ingrese horas de estudio: "))
asistencia = float(input("Ingrese porcentaje de asistencia: "))
tareas = float(input("Ingrese cantidad de tareas realizadas: "))

nuevo_estudiante = pd.DataFrame({
    "horas_estudio": [horas],
    "asistencia": [asistencia],
    "tareas": [tareas]
})

# ==========================================
# MOSTRAR DATOS INGRESADOS
# ==========================================

print("\n===== DATOS DEL ESTUDIANTE =====")
print("Horas de estudio:", horas)
print("Asistencia:", asistencia, "%")
print("Tareas realizadas:", tareas)

# ==========================================
# PREDICCIÓN
# ==========================================

prediccion = modelo.predict(nuevo_estudiante)

print("\n===== PREDICCIÓN =====")
print("Resultado predicho:", prediccion[0])

# ==========================================
# EVALUACIÓN DEL MODELO
# ==========================================

y_pred = modelo.predict(X_test)
precision = accuracy_score(y_test, y_pred)

print("\n===== EVALUACIÓN =====")
print("Precisión del modelo:", round(precision * 100, 2), "%")

# ==========================================
# DIBUJAR ÁRBOL
# ==========================================

plt.figure(figsize=(12, 8))

tree.plot_tree(
    modelo,
    feature_names=X.columns,
    class_names=modelo.classes_,
    filled=True,
    rounded=True,
    fontsize=10
)

plt.title("Árbol de Decisión - Aprobación de Estudiantes")

plt.show()
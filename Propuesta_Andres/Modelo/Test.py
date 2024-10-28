import modeloEconomia as ec
from grammar2 import text_to_tuple

# Parámetros del modelo
parameters = {
    "dotacion_X": 10,
    "dotacion_Y": 10,
    "dotacion_Z": 10,
    "steps": 2,  # Ejecutar el modelo durante 2 pasos
    "switch": 3,  # Definir funcion
}


### Se crea el modelo con los parámetros
modelo = ec.EconomiaIntercambio(parameters)


# Llama al método setup para inicializar los agentes
modelo.setup()


cadena_transacciones_test2 = "Trade(Alice,Bob,Xvalue(78.7),Yvalue(64.5))Trade(Alice,Charles,Xvalue(46.0),Yvalue(94.5))Trade(Charles,Alice,Xvalue(32.6),Yvalue(15.9))Trade(Charles,Alice,Xvalue(21.4),Yvalue(51.9))"
cadena_1 = "Trade(Alice,Bob,Xvalue(78.7),Yvalue(64.5))"

lista_transacciones = text_to_tuple(cadena_transacciones_test2)


modelo.ejecutar_lista_transacciones(lista_transacciones)

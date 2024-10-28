### Módulo para Registrar Transacciones

#! Métodos diseñados para ser implementados en una clase ap.model


#! Método para inicializar la matriz de transacciones entre agentes


"""
El método toma como entrada el modelo y genera la matriz de transacciones entre agentes con "nombre propio".
El modelo esta diseñado para que al realizar el setup se realice un setup de un diccionario con los nombres propios de los agentes , después usando ese diccionario
se genera la matriz de transacciones con los nombres de los agentes relevantes.

Args:
    self (ap.model): esta diseñado para ser llamado como método de la clase ap.Model que represente la economía de Intercambio
    dict_agentes: el diccionario con los nombres propios para cada agente , luego: Key: Nombre:agente y value: Nombre del agente como objeto dentro del modelo
"""


def generar_matriz_transacciones(self):
    # Crear la lista de agentes involucrados a partir del diccionario de agentes
    lista_involucrados = list(self.dict_agentes.keys())

    # Crear la matriz de transacciones con los nombres de los agentes como claves
    self.matriz_transacciones = {
        a1: {a2: 0 for a2 in lista_involucrados} for a1 in lista_involucrados
    }


#! Método para inicializar la matriz de transacciones entre agentes


"""
El método toma como entrada el modelo y registra la transferencia de cantidades entre agentes".
Ubica a los agentes involucrados, los ubica en la matriz y registra en la casilla correspondiente la trasnferencia de bienes 
Asimismop, genera una matriz unica para la transacción y la anexa a una lista qeu va guardando las matrices de cada paso 


Args:
    self (ap.model): esta diseñado para ser llamado como método de la clase ap.Model que represente la economía de Intercambio
    transaccion (tuple): recibe la tupla que define la transacción
"""


def registrar_matriz_transacciones(self, transaccion):
    # lista de los agentes
    lista_involucrados = list(self.dict_agentes.keys())

    # Procesar y ejecutar la transacción que viene como tupla
    matriz_transaccion_unica = {
        a1: {a2: 0 for a2 in lista_involucrados} for a1 in lista_involucrados
    }

    agente1, agente2, bien1, cantidad1, bien2, cantidad2 = transaccion

    # Encontrar los nombres de los agentes
    nombre_agente_1 = [
        key for key, value in self.dict_agentes.items() if key is agente1
    ][0]
    nombre_agente_2 = [
        key for key, vaue in self.dict_agentes.items() if key is agente2
    ][0]

    # Obtener las instancias de los agentes desde el diccionario self.dict_agentes
    agente_1 = self.dict_agentes[agente1_nombre]
    agente_2 = self.dict_agentes[agente2_nombre]

    # Sumar la transacción a la matriz Acumulada
    self.matriz_transacciones[nombre_agente_1][nombre_agente_2] += cantidad1
    self.matriz_transacciones[nombre_agente_2][nombre_agente_1] += cantidad2

    self.transacciones_por_paso.append(matriz_transaccion_unica)

import numpy as np


"""
    El método valorar calcula la utilidad social del sistema basado en las utilidades individuales 
    de cada agente, utilizando una función de utilidad social específica.

    Args:
    self (ap.Model): Método de la clase `EconomiaIntercambio`.
    switch (int): Un parámetro que determina qué función de utilidad social se utiliza:
        - 1: Función Rawlsiana, maximiza la utilidad del agente con menor utilidad.
        - 2: Función de Nash, maximiza la productoria de las utilidades individuales.
        - Otro valor: Función utilitarista, maximiza la suma de las utilidades.

    Returns:
    float: El valor de la utilidad social calculada, según la función de utilidad especificada.

    Funcionamiento:
    - Primero, se actualiza la utilidad de cada agente llamando a su método `valorar()`.
    - Luego, se recogen las utilidades de los agentes en una lista.
    - Dependiendo del valor del parámetro `switch`, se calcula la utilidad social utilizando 
      una de las tres funciones disponibles: Rawlsiana, Nash o utilitarista.
    - Finalmente, se actualiza la variable `utilidad_social` del modelo con el valor calculado.
    """


# Método para valorar la utilidad social en función de las utilidades de los agentes
def valorar(self):
    # Se llama a switch de los parámetros del modelo

    switch = self.p["switch"]

    # Actualizar la utilidad de cada agente
    for agente in self.dict_agentes.values():
        agente.valorar()  # Recalcular la utilidad basada en las nuevas dotaciones.

    """ Valorar el resultado de las transacciones usando una función de utilidad social. """
    lista_utilidades = [agente.utilidad for agente in self.dict_agentes.values()]

    # Funciones de valoración social basadas en el valor de "switch"
    if switch == 1:
        # Función Rawlsiana: Maximizar la utilidad del agente más desfavorecido (mínima utilidad)
        funcion = min(lista_utilidades)

    elif switch == 2:
        # Función de Nash: Maximizar la productoria de las utilidades
        funcion = np.prod(lista_utilidades)

    else:
        # Función utilitarista: Maximizar la suma de las utilidades
        funcion = sum(lista_utilidades)

    # Actualizar la utilidad social en el modelo
    self.utilidad_social = funcion
    #!TODO Definir si la función de valoracion debe ser definida en un módulo aparte y luego ser instanciada.

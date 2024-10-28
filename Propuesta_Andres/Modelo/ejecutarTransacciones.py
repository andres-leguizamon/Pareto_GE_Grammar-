### Módulo para ejecutar Transacciones

#! Este módulo esta diseñado para ser implementado en una clase ap.model


#! Método para ejecutar una transaccion entre dos agentes


def realizar_intercambio(
    self, agente_1, agente_2, bien_1, bien_2, cantidad_1, cantidad_2
):
    """
    Método para realizar el intercambio entre dos agentes.
    Actualiza las dotaciones de bienes para ambos agentes.

    El agente_1 pierde cantidad_1 de bien_1 y gana cantidad_2 de bien_2.
    El agente_2 gana cantidad_1 de bien_1 y pierde cantidad_2 de bien_2.

    Args:
        self (ap.Model): Modelo de la economía de intercambio.
        agente_1 (ap.Agent): Primer agente que participa en el intercambio.
        agente_2 (ap.Agent): Segundo agente que participa en el intercambio.
        bien_1 (str): Nombre del bien que ofrece el agente_1.
        bien_2 (str): Nombre del bien que ofrece el agente_2.
        cantidad_1 (float): Cantidad del bien_1 que ofrece el agente_1.
        cantidad_2 (float): Cantidad del bien_2 que ofrece el agente_2.
    """
    # Actualizar las dotaciones del agente_1
    agente_1.dotacion[bien_1] -= cantidad_1
    agente_1.dotacion[bien_2] += cantidad_2

    # Actualizar las dotaciones del agente_2
    agente_2.dotacion[bien_1] += cantidad_1
    agente_2.dotacion[bien_2] -= cantidad_2


def aplicar_transaccion(self, transaccion):
    """
    Método para procesar y ejecutar una transacción que viene como una tupla.

    Args:
        self (ap.Model): Modelo de la economía de intercambio.
        transaccion (tuple): Tupla con la información de la transacción a realizar.
            Formato de la tupla: (agente1_nombre, agente2_nombre, bien1, cantidad1, bien2, cantidad2)
            donde agente1_nombre y agente2_nombre son nombres (str) de los agentes,
            bien1 y bien2 son los nombres (str) de los bienes a transar,
            cantidad1 y cantidad2 son las cantidades (float) de los bienes.
    """
    # Desempaquetar la transacción
    agente1_nombre, agente2_nombre, bien1, cantidad1, bien2, cantidad2 = transaccion

    # Realizar la transacción
    self.realizar_intercambio(agente_1, agente_2, bien1, bien2, cantidad1, cantidad2)

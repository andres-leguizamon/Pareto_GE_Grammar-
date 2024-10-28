import numpy as np
import scipy as sp
import agentpy as ap


### Creación de la clase AgenteIntercambio, que modela un agente en la economía de intercambio.


class AgenteIntercambio(ap.Agent):
    ### Método setup: Inicializa los agentes asignándoles sus dotaciones y su utilidad base.

    def setup(self):
        # Inicializar las dotaciones de los bienes (X, Y, Z) a partir de los parámetros del modelo.
        self.dotacion = {
            "X": self.model.p[
                "dotacion_X"
            ],  # Asigna la dotación inicial de X desde los parámetros del modelo.
            "Y": self.model.p["dotacion_Y"],  # Asigna la dotación inicial de Y.
            "Z": self.model.p["dotacion_Z"],  # Asigna la dotación inicial de Z.
        }

        # Establecer la utilidad inicial en 0.
        self.utilidad = 0

    ### Método intercambiar: Permite que dos agentes realicen un intercambio de bienes.
    # Args:
    #   otro_agente (AgenteIntercambio): El agente con el que se realiza el intercambio.
    #   bien_enviado (str): El bien que este agente envía en el intercambio.
    #   bien_recibido (str): El bien que este agente recibe en el intercambio.
    #   cantidad_enviada (float): La cantidad de bien_enviado que este agente ofrece.
    #   cantidad_recibida (float): La cantidad de bien_recibido que este agente recibe.

    def intercambiar(
        self,
        otro_agente,
        bien_enviado,
        bien_recibido,
        cantidad_enviada,
        cantidad_recibida,
    ):
        # Actualiza las dotaciones de bienes para ambos agentes.
        # El agente actual pierde la cantidad de bien_enviado y gana la cantidad de bien_recibido.
        self.dotacion[bien_enviado] -= cantidad_enviada
        self.dotacion[bien_recibido] += cantidad_recibida

        # El otro agente gana la cantidad de bien_enviado y pierde la cantidad de bien_recibido.
        otro_agente.dotacion[bien_enviado] += cantidad_enviada
        otro_agente.dotacion[bien_recibido] -= cantidad_recibida

    ### Método valorar: Devuelve las cantidades actuales de los bienes X, Y, Z que posee el agente.
    # Este método puede ser heredado y modificado en otras clases de agentes que utilicen diferentes formas de valoración.
    def valorar(self):
        """Método para obtener las cantidades de los bienes X, Y, Z del agente.
        Puede ser sobrescrito en clases derivadas para diferenciar las utilidades de cada agente."""

        # Obtener las cantidades actuales de los bienes X, Y, Z.
        cantidad_x = self.dotacion["X"]
        cantidad_y = self.dotacion["Y"]
        cantidad_z = self.dotacion["Z"]

        # Retornar las cantidades de los tres bienes.
        return cantidad_x, cantidad_y, cantidad_z

    ### Agente tipo 1 "Alice"


class Agente1(AgenteIntercambio):
    def valorar(self):
        cantidad_x, cantidad_y, cantidad_z = super().valorar()

        # Definir la utilidad como la cantidad de bien X
        self.utilidad = cantidad_x
        return self.utilidad

    ### Agente tipo 2 "Bob"


class Agente2(AgenteIntercambio):
    def valorar(self):
        cantidad_x, cantidad_y, cantidad_z = super().valorar()

        # Definir la utilidad como la cantidad de bien Y
        self.utilidad = cantidad_y
        return self.utilidad


### Agente tipo 3 "Charles"


class Agente3(AgenteIntercambio):
    def valorar(self):
        cantidad_x, cantidad_y, cantidad_z = super().valorar()

        # Definir la utilidad como la cantidad de bien Z
        self.utilidad = cantidad_z
        return self.utilidad

    # TODO Ver si hay una mejor forma o una forma más eficiente de incorporar la heterogenidad en las funciones de utilidad en la clase agente

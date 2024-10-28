import numpy as np
import scipy as sp
import agentpy as ap


### Creación de la clase AgenteIntercambio, que modela un agente en la economía de intercambio.


class AgenteIntercambio(ap.Agent):
    # Método setup: Inicializa los agentes asignándoles sus dotaciones y su utilidad base.
    def setup(self):
        # Inicializar las dotaciones de los bienes (X, Y, Z) a partir de los parámetros del modelo.
        self.dotacion = {
            "X": self.model.p["dotacion_X"],  # Asigna la dotación inicial de X.
            "Y": self.model.p["dotacion_Y"],  # Asigna la dotación inicial de Y.
            "Z": self.model.p["dotacion_Z"],  # Asigna la dotación inicial de Z.
        }

        # Establecer la utilidad inicial en 0.
        self.utilidad = 0

        # Lista de Utilidades históricas

        self.historial_utilidad = []

        # Historial de inventario: se inicializa con la dotación inicial.
        self.historial_inventario = {
            "X": [self.dotacion["X"]],
            "Y": [self.dotacion["Y"]],
            "Z": [self.dotacion["Z"]],
        }

    # Método para registrar el estado del inventario después de cada transacción.
    def registrar_inventario(self):
        # Añadir el estado actual del inventario al historial.
        self.historial_inventario["X"].append(self.dotacion["X"])
        self.historial_inventario["Y"].append(self.dotacion["Y"])
        self.historial_inventario["Z"].append(self.dotacion["Z"])

    # Este método accede a la utilidad del agente actual y la añade a la lista
    def registrar_utilidad(self):
        u = self.utilidad
        self.historial_utilidad.append(u)

    # Método valorar: Devuelve las cantidades actuales de los bienes X, Y, Z que posee el agente.
    def valorar(self):
        """Método para obtener las cantidades de los bienes X, Y, Z del agente.
        Puede ser sobrescrito en clases derivadas para diferenciar las utilidades de cada agente."""

        # Obtener las cantidades actuales de los bienes X, Y, Z.
        cantidad_x = self.dotacion["X"]
        cantidad_y = self.dotacion["Y"]
        cantidad_z = self.dotacion["Z"]

        # Retornar las cantidades de los tres bienes.
        return cantidad_x, cantidad_y, cantidad_z


#!  Agente tipo 1 "Alice"


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

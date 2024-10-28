import agentpy as ap
from types import MethodType

# Importar los módulos del modelo
import agentes
import ejecutarTransacciones
import registroTransacciones
import valorarTransacciones
# import analizarTransacciones


### Nuevo modelo con los métodos
class EconomiaIntercambio(ap.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Asignar funciones importadas como métodos de la clase usando MethodType
        self.aplicar_transaccion = MethodType(
            ejecutarTransacciones.aplicar_transaccion, self
        )
        self.realizar_intercambio = MethodType(
            ejecutarTransacciones.realizar_intercambio, self
        )
        self.registrar_matriz_transacciones = MethodType(
            registroTransacciones.registrar_matriz_transacciones, self
        )
        self.generar_matriz_transacciones = MethodType(
            registroTransacciones.generar_matriz_transacciones, self
        )
        self.valorar = MethodType(valorarTransacciones.valorar, self)

    def setup(self):
        # ! Generar los agentes , identificarlos y  crear su estado base
        # * Crear los tres agentes: Alice, Bob, Charles
        alice = agentes.Agente1(self)
        bob = agentes.Agente2(self)
        charles = agentes.Agente3(self)

        # * Almacenar los agentes en un diccionario para acceso fácil
        self.dict_agentes = {"Alice": alice, "Bob": bob, "Charles": charles}

        # * Configurar cada agente
        for agente in self.dict_agentes.values():
            agente.setup()

        # ! Generar todos los atributos de registro
        self.generar_matriz_transacciones()  # Generar  Matriz acumulada de transacciones

        # Inicializar variables de registro
        self.historial_utilidad_social = []  # Registro de la utilidad social para cada transacción

        self.transacciones_por_paso = []  # Lista con las matrices de cada transacción

        self.utilidad_social = (
            self.valorar()
        )  # Utilidad social del estado actual de los inventarios de los agentes

        # Valoración inicial de las dotaciones de los agentes

        utilidad_social_inicial = self.valorar()  # Valora las dotaciones iniciales

        # Añadir la utilidad inicial al historial
        self.historial_utilidad_social.append(utilidad_social_inicial)

    #! Método para ejecutar una transacción y registrarla

    """
    El método ejecutar_transaccion aplica el intercambio de mercancías entre dos agentes del modelo, 
    alterando sus inventarios. Además, se encarga de valorar y registrar la transacción.

    Args:
    self (ap.model): Método de la clase ap.Model que representa la economía de intercambio.
    transaccion (objeto): Representa una transacción con los agentes involucrados y los bienes intercambiados.
    """

    def ejecutar_transaccion(self, transaccion):
        # Aplicar la transacción y alterar los inventarios de los agentes
        self.aplicar_transaccion(transaccion)  # Llamar al método asignado

        # Registrar la transacción en la matriz acumulada
        # self.registrar_matriz_transacciones(transaccion)  # Registrar la transacción

        # Valorar el resultado de la transacción - En esta etapa ya se actualizó el inventario de todos los agentes
        utilidad_transaccion = self.valorar()

        # Agregar la utilidad social de la transacción al historial
        self.historial_utilidad_social.append(utilidad_transaccion)

    # Método para ejecutar una lista de transacciones secuencialmente
    def ejecutar_lista_transacciones(self, lista_transacciones):
        for transaccion in lista_transacciones:
            self.ejecutar_transaccion(transaccion)

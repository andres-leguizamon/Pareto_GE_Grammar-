from lark import Lark, Transformer


### Definir Gramatica
""""
La gramatica representa posibles intercambios
de cantidades enteras y no enteras de los 3 bienes
"""

grammar = """
    ?start: trades
    trades: trade+
    trade: "Trade(" ENTITY "," ENTITY "," asset "," asset ")"
    ENTITY: "Alice" | "Bob" | "Charles"
    asset: x | y | z
    x: "Xvalue(" value ")"
    y: "Yvalue(" value ")"
    z: "Zvalue(" value ")"
    value: SIGNED_NUMBER
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS
    """


### Definir el parser
parser = Lark(grammar)


#! Creación del Transformer

""""
El objeto Parser genera un árbol de jerarquía con los terminales, tokens y reglas de producción a partir de la línea de texto
Finalmente el objeto Transformer convertirá el árbol en la tupla que interpreta el módulo Interpreter
"""


class TradeTransformer(Transformer):
    # Este método toma un token que representa una entidad (agente)
    # y devuelve su nombre como cadena de texto.

    def ENTITY(self, token):
        return token.value

    # Este método convierte el valor de un token a un número de tipo float.
    # args es una lista con los elementos del árbol de sintaxis. Tomamos el primer elemento.
    def value(self, args):
        token = args[0]
        return float(token.value)  # Convierte el valor a float y lo retorna.

    # Procesa el subárbol que representa el valor 'x'.
    # Se espera que 'args' contenga un subárbol 'value' que es procesado primero.
    def x(self, args):
        value = self.transform(
            args[0]
        )  # Llama al método 'value' para obtener el valor.
        return ("X", value)  # Devuelve una tupla con 'X' y el valor correspondiente.

    # Procesa el subárbol que representa el valor 'y'.
    # Se utiliza el mismo método que para 'x', pero devuelve una tupla con 'Y'.
    def y(self, args):
        value = self.transform(args[0])
        return ("Y", value)

    # Procesa el subárbol que representa el valor 'z'.
    # Misma lógica que 'x' y 'y', devuelve una tupla con 'Z'.
    def z(self, args):
        value = self.transform(args[0])
        return ("Z", value)

    # Este método transforma un activo, el cual puede ser 'x', 'y' o 'z'.
    # Llama al transformador correspondiente dependiendo del activo.
    def asset(self, args):
        return self.transform(args[0])

    # Este método procesa una transacción completa.
    # args: [agente1, agente2, asset1, asset2]

    def trade(self, args):
        agente1 = args[0]  # Primer agente involucrado en la transacción.
        agente2 = args[1]  # Segundo agente involucrado en la transacción.

        # Procesa los activos de los agentes
        asset1 = self.transform(args[2])  # Transforma el primer activo.
        asset2 = self.transform(args[3])  # Transforma el segundo activo.

        # Desempaqueta los activos (bien, cantidad).
        bien1, cantidad1 = asset1
        bien2, cantidad2 = asset2

        # Retorna la transacción como una tupla con los agentes y los detalles de los activos.
        return (agente1, agente2, bien1, cantidad1, bien2, cantidad2)

    # Método para procesar una lista de transacciones.
    # Retorna la lista completa de transacciones procesadas.
    def trades(self, trades):
        return trades

    # Método de inicio que espera la lista de transacciones ya procesadas.
    # Esencialmente, devuelve la lista tal como llega.
    def start(self, trades):
        return trades


# ! Crear una función para realizar el Parsing de texto.
"""
La función `parse_text` toma una cadena de texto como entrada, la procesa utilizando
el objeto `parser` y devuelve un árbol sintáctico que el transformer pueda procesar.

Args:
    text (str): La cadena de texto que contiene las instrucciones o transacciones a procesar.

Returns:
    tree: El árbol de análisis sintáctico (parsing tree) generado a partir del texto.
          Este árbol será procesado posteriormente por un transformer para extraer la información relevante.
"""


def parse_text(text):
    # Se utiliza el objeto parser para analizar el texto de entrada y generar el árbol sintáctico.
    tree = parser.parse(text)

    # Devuelve el árbol generado, que representa la estructura jerárquica del texto procesado.
    return tree


#! Crear una función para generar tuplas a partir del árbol generado
"""
La función `transform_tree` toma un arbol como argumento, instancia el objeto transformer 
lo procesa siguiendo y luego usando el transfomer procesa el arbol conviertiendolo en la 
lista de tuplas que el modulo Interpreter puede utilizar 

Args:
    tree(tree): El parse tree que representa la transacción en términos de objetos terminales, tokens y reglas de producción 

Returns:
   list_tuple : Lista de tuplas que representan las transacciones que el módulo intepreter puede utilizar. 

"""


def transform_tree(tree):
    ### Apuntar al Transformer
    transformer_trade = TradeTransformer()

    list_tuple = transformer_trade.transform(tree)

    return list_tuple


# ! Crear una función para convertir texto en tuplas procesables por el módulo Interpreter.
"""
La función `text_to_tuple` toma una cadena de texto, la convierte en un árbol de análisis sintáctico
usando la función `parse_text`, y luego transforma ese árbol en una lista de tuplas utilizando 
`transformar_arbol`. Las tuplas resultantes representan transacciones que pueden ser procesadas por 
el módulo Interpreter.

Args:
    text (str): La cadena de texto que describe la transacción o conjunto de transacciones en términos legibles.

Returns:
    transacciones (list): Una lista de tuplas que representan las transacciones extraídas del texto.
"""


def text_to_tuple(text):
    # Genera el árbol de análisis sintáctico a partir del texto.
    tree = parse_text(text)

    # Transforma el árbol en una lista de tuplas utilizables.
    transacciones = transform_tree(tree)

    # Devuelve la lista de transacciones.
    return transacciones

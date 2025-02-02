# Objetivo


El objetivo de este ejercicio de modelado es realizar el ciclo completo de módulos necesarios para modelar el problema de evasión fiscal en Zonas Francas. 

En particular, se ha elegido representar una economía de intercambio puro junto al mecanismo de Edgeworth para así tener un caso base que permita realizar la construcción de los módulos necesarios.

# Descripción del Entorno

La idea es modelar a tres tipos de agentes: Alice, Bob y Charles, que reciben cada uno una dotación de tres bienes y deben llevar a cabo una serie de transacciones (Intercambios) que serán posteriormente evaluados por una función objetivo.

En este caso, la función objetivo será una función de bienestar social creciente en las utilidades de los agentes. Debido a que la función es creciente en las utilidades de los agentes, sus argumentos maximizadores corresponderán a asignaciones que sean óptimos de Pareto de la economía.

Se ha escogido este entorno ya que bajo ciertas condiciones sobre las funciones de utilidad, se podría comprobar si el intercambio escogido corresponde a un Pareto de forma analítica, lo cual puede servir como benchmark del proceso de Grammar Evolution.

De hecho, puede que lo que encuentre el algoritmo no sea un óptimo de Pareto, pero, idealmente, debería ser al menos una asignación dentro del núcleo de la economía.

# Descripción de Módulos Propuestos

## Módulo de Gramática

El módulo de gramática se encuentra en el archivo `grammar.py` y su objetivo es generar una gramática en formato BNF (Backus-Naur Form) que represente las posibles acciones en las que pueden incurrir los agentes dentro de una economía de intercambio. La BNF es una notación utilizada comúnmente para describir la sintaxis de lenguajes formales, lo que nos permite especificar de manera clara las reglas que rigen el comportamiento de estos agentes.

Una vez definida la gramática, se utiliza la biblioteca Lark de Python para interpretar líneas de texto que describen posibles transacciones. Lark convierte estas descripciones en Parsing Trees, que representan la estructura jerárquica del texto según las reglas de la gramática. A través de un proceso de transformación (usando transformers), estas estructuras se pueden manipular y, finalmente, convertir en tuplas que son interpretadas por un módulo interpretador, permitiendo que Python las procese como instrucciones válidas.

Este enfoque modular garantiza que las transacciones descritas puedan ser traducidas de manera precisa y eficiente a un formato que el programa pueda ejecutar.

## Módulo Interpretador

El módulo interpretador utiliza el paradigma de programación orientada a objetos (OOP) y la biblioteca `Agentpy` para modelar tanto a los agentes económicos como la estructura de la economía de intercambio. Este módulo tiene como objetivo interpretar las tuplas generadas por el módulo de gramática (`grammar.py`), las cuales representan transacciones potenciales entre los agentes.

Cada agente económico es modelado como un objeto que sigue reglas específicas de comportamiento, las cuales se definen dentro de la estructura del simulador. La biblioteca `Agentpy` facilita la creación de estos agentes y sus interacciones, permitiendo la simulación de dinámicas complejas de intercambio.

El módulo interpretador recibe las tuplas de transacciones, que contienen las instrucciones derivadas de las acciones posibles de los agentes. A partir de estas tuplas, el módulo ejecuta dichas transacciones dentro del modelo, actualizando el estado de los agentes involucrados. Al final del proceso, se calcula la utilidad social resultante de la secuencia de transacciones, evaluando cómo las interacciones afectan el bienestar colectivo dentro de la economía simulada.

Este enfoque modular permite analizar de manera detallada las interacciones entre agentes, obtener resultados sobre la eficiencia del sistema de intercambio, y evaluar cómo diferentes secuencias de transacciones impactan el bienestar global.

## Módulo Generador

Este módulo tiene como objetivo generar listas de transacciones en forma de frases, partiendo de listas de enteros, utilizando la gramática definida previamente en el archivo `grammar.py`. Este proceso es fundamental para implementar la evolución gramatical (Grammar Evolution), un enfoque que aplica técnicas evolutivas para explorar y generar posibles soluciones dentro de un espacio de búsqueda definido por la gramática.

El módulo toma listas de enteros como entrada, donde cada entero corresponde a una opción o decisión dentro de la estructura de la gramática. Estas listas son traducidas a secuencias de transacciones (frases), siguiendo las reglas definidas en el sistema BNF. A medida que los enteros se interpretan, el módulo selecciona las producciones gramaticales correspondientes, generando así una representación en lenguaje natural de las transacciones económicas.

Este proceso permite que las transacciones generadas sirvan de insumo para evaluaciones posteriores, como la simulación en el módulo interpretador. Además, al estar diseñado como parte del proceso de evolución gramatical, las listas de enteros pueden ser ajustadas y optimizadas mediante algoritmos genéticos u otros métodos evolutivos, buscando maximizar un objetivo predefinido, como la eficiencia del sistema o la utilidad social.

De este modo, el módulo actúa como un puente entre la representación abstracta de los enteros y las transacciones que pueden ser interpretadas dentro del marco de la economía de intercambio modelada.

## Módulo de Búsqueda

Work in Progress.

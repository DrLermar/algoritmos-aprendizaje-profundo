# Control Difuso

El control difuso es una forma de control basado en una mimetización de como toma decisiones el ser humano, donde en ocaciones las decisiones no son basadas en la determinación absoluta de una o varias opciones.

Es utilizado para modelar sistemas de decisión complejos que son dificiles de describir con otros modelos.

## Conceptos fundamentales

* **Reglas difusas**: se basan en oraciones condicionales estructuradas con if-then (si-entonces) las cuales rigen el comportamiento del control.

* **Variables lingüisticas**: son las variables representadas a través de los conjuntos posibles. Por ejemplo: se tiene la variable "edad" la cual representa a tres conjuntos: joven, adulto, anciano junto con la variable "actividad física" la cual representa a otros tres conjuntos: bajo, medio, alto.

* **Valor crisp**: es una magnitud numérica de la variable estudiada. Por ejemplo, para la misma valiable "edad" un valor crisp es 24 años.

* **Funcion de membresía**: es la función que define porcentualmente los conjuntos a través de las varaibles lingüisticas que los representa. Estas funciones pueden tener diversas formas dependiendo de las necesidades del control, pueden ser triangulares, trapezoidales, Gaussinas o Singleton. Se caracterízan por generar traslapamientos entre los conjuntos.

Funcion triangular

<div align="center">
  <img src="imagenes/funcion triangular.png" alt="funcion triangular" width="500">
</div>

Funcion trapezoidal

<div align="center">
  <img src="imagenes/funcion trapezoidal.png" alt="funcion trapezoidal" width="500">
</div>

Funcion Gaussiana

<div align="center">
  <img src="imagenes/funcion gaussiana.png" alt="funcion gaussiana" width="500">
</div>

* **Defuzificación**: es el paso final del sistema de control difuso, traduce los resultados de la lógica difusa, obtenidos por las funciones de membresía, en un valor numérico exato y utilizable. El método más es el método por centroide en el que se obtiene el centroide de las areas involucradas porcentualmente de los conjuntos definidos por la variable lingüistica.

## Proceso de lógica difusa

La lógica difusa comienza con un dato crisp, un dato numérico de la variable de entrada, esta es sometida a ser una variable difusa o variable lingüistica la cual genera conjuntos traslapados. Teniendo este resultado difuso de la variable de entrada, se pasa este resultado por la variable difusa de la variable de salida que se desea, con esto se obtiene un resultado difuso de la variable de salida. Por ultimo se somete a la defuzificación (por el método del centroido por ejemplo) para obtener un valor crisp de la variable de salida.

<div align="center">
  <img src="imagenes/logica difusa.png" alt="Logica difusa" width="500">
</div>

## Operadores en logica difusa

Al aplicar la lógica difusa a problemas más complejos se vuleve necesario que las reglas difusas usen operadores como or, and o not.

Los operadores funcionan de la misma manera que funcionan con valores binarios.

* OR: para trabajar con OR en logica difusa se usa el valor máximo de las variables de entrada que se tienen [`max(A,B)`].

* AND: para trabajar con AND en logica difusa se usa el valor mínimo de las variables de entrada que se tienen [`min(A,B)`].

* NOT: para trabajar con NOT en logica difusa se usa el valor de 1 menos el valor de la entrada que se niega [`1-A`].

## Tuning de la inferencia en lógica difusa

Es un problema de optimización en el que se deben de encontrar los parámetros que generen el resultado más óptimo. Se hace mediante una función de costo a la cual se le encuentra el mínimo.

Para obtener una respuesta ideal de un sistema controlado con lógica difusa se pueden probar diferentes configuraciones del controlador minimizando la función de costo planteada al comparar la salida de el sistema controlado contra la respuesta ideal esperada.

Se pueden modificar todos los parámetros de un controlador difuso para realizar el tuning, como el número de funciones de membresía, las formas de las funciones de membresía los parámetros de las funciones de membresía, las reglas o el defuzificador, pero esto debe de ser realizado mediante el conocimiento que se tenga del problema y la experiencia, no de una forma sistemática ya que las permutaciones que se pueden generar crecen exponencialmente. Sin embargo, en lo que se debe de centrar el tuning es en encontrar el arreglo óptimo de las reglas difusas.

Pero para obtener el mejor arreglo de reglas no basta con hacer permutaciones de las todos los escenarios posibles ya que de igual manera resultan ser demasiadas. Por ello se utilizan diferentes algoritmos:

* **Algoritmo genético**: el cual muestrea aleatoriamente un número de puntos en el espacio de soluciones generado por los parámetros que se modifican, a esos puntos se les calcula el costo y solo permanecen los que tengan un menor costo, a partir de esos puntos se realiza una busqueda de puntos cercanos en diferentes direcciones y se vuelve a realizar el descate de los puntos que tengan un mayor costo, este proceso se repite hasta que se converge en el arreglo que tiene el menor costo.

* **Pattern Search**: en este algoritmo se muestrea un punto aleatorio en el espacio de soluciones, a partir de ese punto se muestrean puntos en diferentes direcciones, se mantiene el punto con el menor costo y se vuelve a realizar el mismo proceso hasta obtener el menor costo. Sin embargo, si ninguno de los puntos nuevos muestreados tienen un menor costo, el rango de muestreo se acorta para obtener una mejor precisión.

Otra cosa que ayuda sustancialmente a encontrar los parámetros óptimos es reducir el espacio de soluciones. Esto se puede realizar mediante **Fuzzy Trees** la cual plantea una técnica en la que se separa un sistema de inferencia difusa en varios sistemas, por ejemplo: si se tiene un sistema de 3 entradas, este se puede realizar como dos sistemas, uno con una entrada y otro con dos. Esta estructura de árbol en los sistemas difusos reduce el número posible de configuraciones y resulta ser más facil de interpretar.

<div align="center">
  <img src="imagenes/Fuzzy Trees.png" alt="Fuzzy Trees" width="500">
</div>

Esto se puede ver aplicado al modelado de un pancreas en el siguiente link: [Lógica difusa en pancreas](https://www.mathworks.com/help/fuzzy/design-fuzzy-logic-controller-for-artificial-pancreas.html)
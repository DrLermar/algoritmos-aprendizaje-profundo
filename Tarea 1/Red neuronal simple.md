# Función NAND con perceptrón

Un perceptrón aprende a realizar la función binaria NAND con entradas $x_1$ y $x_2$.
* Entradas: $x_0$, $x_1$ y $x_2$, donde $x_0$ se mantiene constante en $1$.
* Umbral ($t$): $0.5$
* Bias ($b$): $0$
* Tasa de aprendizaje ($r$): $0.1$
* Conjunto de entrenamiento: ${((1,0,0),1),((1,0,1),1),((1,1,0),1),((1,1,1),0)}$

En lo que sigue, los pesos finales de la iteración se convierten en los pesos iniciales de la siguiente.

**Fórmula:** $w(Nuevo) = w(Anterior) + (r * e)(Xentrada)$

| $x_0$ | $x_1$ | $x_2$ | $z$ (Deseada) | $w_0$ (Inic) | $w_1$ (Inic) | $w_2$ (Inic) | $c_0$ | $c_1$ | $c_2$ | $s$ (Suma) | $n$ (Red) | $e$ (Error) | $d$ (Corr) | $w_0$ (Fin) | $w_1$ (Fin) | $w_2$ (Fin) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | +0.1 | 0.1 | 0 | 0 |
| 1 | 0 | 1 | 1 | 0.1 | 0 | 0 | 0.1 | 0 | 0 | 0.1 | 0 | 1 | +0.1 | 0.2 | 0 | 0.1 |
| 1 | 1 | 0 | 1 | 0.2 | 0 | 0.1 | 0.2 | 0 | 0 | 0.2 | 0 | 1 | +0.1 | 0.3 | 0.1 | 0.1 |
| 1 | 1 | 1 | 0 | 0.3 | 0.1 | 0.1 | 0.3 | 0.1 | 0.1 | 0.5 | 0 | 0 | 0 | 0.3 | 0.1 | 0.1 |
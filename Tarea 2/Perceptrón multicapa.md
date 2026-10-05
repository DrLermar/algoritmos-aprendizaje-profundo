# Cálculo de un perceptrón multicapa

## Definición de red

* Entradas: $[2, 3]$
* Salida: $1$

**Pesos iniciales**
* $w_1=0.11$
* $w_2=0.21$
* $w_3=0.12$
* $w_4=0.08$
* $w_5=0.14$
* $w_6=0.15$
* $a=0.05$

<div align="center">
  <img src="imagenes/Perceptron multicapa.png" alt="Perceptron" width="500">
</div>

## Cálculo de red

### Epoca 1

1. Valor de salida con pesos actuales

$$
\begin{bmatrix} 2 & 3 \end{bmatrix}
\begin{bmatrix} 0.11 & 0.12 \\ 0.21 & 0.08 \end{bmatrix} = \begin{bmatrix} 0.85 & 0.48 \end{bmatrix}
$$

$$
\begin{bmatrix} 0.85 & 0.48 \end{bmatrix}
\begin{bmatrix} 0.14 \\ 0.15 \end{bmatrix} = 0.191
$$

2. Error cuadrado medio

$$
e = \frac{1}{2} (0.191 - 1)^2 = 0.327
$$

3. Obtención de nuevos pesos

$$
\begin{bmatrix} W_5 \\ W_6 \end{bmatrix} = 
\begin{bmatrix} 0.14 \\ 0.15 \end{bmatrix} - 
\begin{bmatrix} (0.05)(0.85)(0.191 - 1) \\ (0.05)(0.48)(0.191 - 1) \end{bmatrix} = 
\begin{bmatrix} 0.17 \\ 0.17 \end{bmatrix}
$$

$$
\begin{bmatrix} W_1 & W_3 \\ W_2 & W_4 \end{bmatrix} = 
\begin{bmatrix} 0.11 & 0.12 \\ 0.21 & 0.08 \end{bmatrix} - 
(0.05)(0.191 - 1) \begin{bmatrix} 2 \\ 3 \end{bmatrix} \begin{bmatrix} 0.14 & 0.15 \end{bmatrix}
$$

$$
= \begin{bmatrix} 0.11 & 0.12 \\ 0.21 & 0.08 \end{bmatrix} + 0.04 \begin{bmatrix} 0.28 & 0.3 \\ 0.42 & 0.45 \end{bmatrix} = 
\begin{bmatrix} 0.11 & 0.12 \\ 0.21 & 0.08 \end{bmatrix} + \begin{bmatrix} 0.011 & 0.012 \\ 0.017 & 0.018 \end{bmatrix}
$$

$$
\begin{bmatrix} W_1 & W_3 \\ W_2 & W_4 \end{bmatrix} = \begin{bmatrix} 0.12 & 0.13 \\ 0.23 & 0.10 \end{bmatrix}
$$

4. Se repiten los pasos 1, 2 y 3 con nuevos pesos hasta bajar el error

---

### Epoca 2

**Valor de salida:**

$$
\begin{bmatrix} 2 & 3 \end{bmatrix} \begin{bmatrix} 0.12 & 0.13 \\ 0.23 & 0.1 \end{bmatrix} = 
\begin{bmatrix} 0.92 & 0.56 \end{bmatrix} \begin{bmatrix} 0.17 \\ 0.17 \end{bmatrix} = 0.26
$$

**Error cuadrado medio:**

$$
e = \frac{1}{2} (0.26 - 1)^2 = 0.27
$$

**Actualización de $W_5$ y $W_6$:**

$$
\begin{bmatrix} W_5 \\ W_6 \end{bmatrix} = \begin{bmatrix} 0.17 \\ 0.17 \end{bmatrix} - (0.05)(0.26 - 1) \begin{bmatrix} 0.92 \\ 0.56 \end{bmatrix} = 
\begin{bmatrix} 0.17 \\ 0.17 \end{bmatrix} + 0.037 \begin{bmatrix} 0.92 \\ 0.56 \end{bmatrix}
$$

$$
= \begin{bmatrix} 0.17 \\ 0.17 \end{bmatrix} + \begin{bmatrix} 0.034 \\ 0.021 \end{bmatrix} = \begin{bmatrix} 0.2 \\ 0.19 \end{bmatrix}
$$

**Actualización de $W_1$ a $W_4$:**

$$
\begin{bmatrix} W_1 & W_3 \\ W_2 & W_4 \end{bmatrix} = 
\begin{bmatrix} 0.12 & 0.13 \\ 0.23 & 0.1 \end{bmatrix} - (0.05)(0.26 - 1) \begin{bmatrix} 2 \\ 3 \end{bmatrix} \begin{bmatrix} 0.17 & 0.17 \end{bmatrix}
$$

$$
= \begin{bmatrix} 0.12 & 0.13 \\ 0.23 & 0.1 \end{bmatrix} + 0.037 \begin{bmatrix} 0.34 & 0.34 \\ 0.51 & 0.51 \end{bmatrix} = 
\begin{bmatrix} 0.12 & 0.13 \\ 0.23 & 0.1 \end{bmatrix} + \begin{bmatrix} 0.013 & 0.013 \\ 0.02 & 0.02 \end{bmatrix}
$$

$$
\begin{bmatrix} W_1 & W_3 \\ W_2 & W_4 \end{bmatrix} = \begin{bmatrix} 0.13 & 0.14 \\ 0.25 & 0.12 \end{bmatrix}
$$

### Época 3

**Valor de salida:**

$$
\begin{bmatrix} 2 & 3 \end{bmatrix} \begin{bmatrix} 0.13 & 0.14 \\ 0.25 & 0.12 \end{bmatrix} = \begin{bmatrix} 1.01 & 0.64 \end{bmatrix} \begin{bmatrix} 0.2 \\ 0.19 \end{bmatrix} = 0.3236
$$

**Error cuadrado medio:**

$$
e = \frac{1}{2} (0.3236 - 1)^2 = 0.23
$$

**Actualización de $W_5$ y $W_6$:**

$$
\begin{bmatrix} W_5 \\ W_6 \end{bmatrix} = \begin{bmatrix} 0.2 \\ 0.19 \end{bmatrix} - (0.05)(0.3236 - 1) \begin{bmatrix} 1.01 \\ 0.64 \end{bmatrix} = \begin{bmatrix} 0.2 \\ 0.19 \end{bmatrix} + 0.03382 \begin{bmatrix} 1.01 \\ 0.64 \end{bmatrix}
$$

$$
= \begin{bmatrix} 0.2 \\ 0.19 \end{bmatrix} + \begin{bmatrix} 0.034 \\ 0.02 \end{bmatrix} = \begin{bmatrix} 0.23 \\ 0.21 \end{bmatrix}
$$

**Actualización de $W_1$ a $W_4$:**

$$
\begin{bmatrix} W_1 & W_3 \\ W_2 & W_4 \end{bmatrix} = \begin{bmatrix} 0.13 & 0.14 \\ 0.25 & 0.12 \end{bmatrix} - (0.05)(0.3236 - 1) \begin{bmatrix} 2 \\ 3 \end{bmatrix} \begin{bmatrix} 0.2 & 0.19 \end{bmatrix}
$$

$$
= \begin{bmatrix} 0.13 & 0.14 \\ 0.25 & 0.12 \end{bmatrix} + 0.03382 \begin{bmatrix} 0.4 & 0.38 \\ 0.6 & 0.57 \end{bmatrix} = \begin{bmatrix} 0.13 & 0.14 \\ 0.25 & 0.12 \end{bmatrix} + \begin{bmatrix} 0.01 & 0.01 \\ 0.02 & 0.02 \end{bmatrix}
$$

$$
\begin{bmatrix} W_1 & W_3 \\ W_2 & W_4 \end{bmatrix} = \begin{bmatrix} 0.14 & 0.15 \\ 0.27 & 0.14 \end{bmatrix}
$$

---

### Época 4

**Valor de salida:**

$$
\begin{bmatrix} 2 & 3 \end{bmatrix} \begin{bmatrix} 0.14 & 0.15 \\ 0.27 & 0.14 \end{bmatrix} = \begin{bmatrix} 1.09 & 0.72 \end{bmatrix} \begin{bmatrix} 0.23 \\ 0.21 \end{bmatrix} = 0.4
$$

**Error cuadrado medio:**

$$
e = \frac{1}{2} (0.4 - 1)^2 = 0.18
$$

**Actualización de $W_5$ y $W_6$:**

$$
\begin{bmatrix} W_5 \\ W_6 \end{bmatrix} = \begin{bmatrix} 0.23 \\ 0.21 \end{bmatrix} - (0.05)(0.4 - 1) \begin{bmatrix} 1.09 \\ 0.72 \end{bmatrix} = \begin{bmatrix} 0.23 \\ 0.21 \end{bmatrix} + 0.03 \begin{bmatrix} 1.09 \\ 0.72 \end{bmatrix}
$$

$$
= \begin{bmatrix} 0.23 \\ 0.21 \end{bmatrix} + \begin{bmatrix} 0.03 \\ 0.02 \end{bmatrix} = \begin{bmatrix} 0.26 \\ 0.23 \end{bmatrix}
$$

**Actualización de $W_1$ a $W_4$:**

$$
\begin{bmatrix} W_1 & W_3 \\ W_2 & W_4 \end{bmatrix} = \begin{bmatrix} 0.14 & 0.15 \\ 0.27 & 0.14 \end{bmatrix} - (0.05)(-0.6) \begin{bmatrix} 2 \\ 3 \end{bmatrix} \begin{bmatrix} 0.23 & 0.21 \end{bmatrix}
$$

$$
= \begin{bmatrix} 0.14 & 0.15 \\ 0.27 & 0.14 \end{bmatrix} + 0.03 \begin{bmatrix} 0.46 & 0.42 \\ 0.69 & 0.63 \end{bmatrix} = \begin{bmatrix} 0.14 & 0.15 \\ 0.27 & 0.14 \end{bmatrix} + \begin{bmatrix} 0.013 & 0.012 \\ 0.02 & 0.02 \end{bmatrix}
$$

$$
\begin{bmatrix} W_1 & W_3 \\ W_2 & W_4 \end{bmatrix} = \begin{bmatrix} 0.15 & 0.16 \\ 0.29 & 0.16 \end{bmatrix}
$$

---

### Época 5

**Valor de salida:**

$$
\begin{bmatrix} 2 & 3 \end{bmatrix} \begin{bmatrix} 0.15 & 0.16 \\ 0.29 & 0.16 \end{bmatrix} = \begin{bmatrix} 1.17 & 0.8 \end{bmatrix} \begin{bmatrix} 0.26 \\ 0.23 \end{bmatrix} = 0.4882
$$

**Error cuadrado medio:**
$$
e = \frac{1}{2} (0.4882 - 1)^2 = 0.13
$$

**Actualización de $W_5$ y $W_6$:**

$$
\begin{bmatrix} W_5 \\ W_6 \end{bmatrix} = \begin{bmatrix} 0.26 \\ 0.23 \end{bmatrix} - (0.05)(0.4882 - 1) \begin{bmatrix} 1.17 \\ 0.8 \end{bmatrix} = \begin{bmatrix} 0.26 \\ 0.23 \end{bmatrix} + 0.026 \begin{bmatrix} 1.17 \\ 0.8 \end{bmatrix}
$$

$$
= \begin{bmatrix} 0.26 \\ 0.23 \end{bmatrix} + \begin{bmatrix} 0.03 \\ 0.02 \end{bmatrix} = \begin{bmatrix} 0.29 \\ 0.25 \end{bmatrix}
$$

**Actualización de $W_1$ a $W_4$:**

$$
\begin{bmatrix} W_1 & W_3 \\ W_2 & W_4 \end{bmatrix} = \begin{bmatrix} 0.15 & 0.16 \\ 0.29 & 0.16 \end{bmatrix} + 0.026 \begin{bmatrix} 2 \\ 3 \end{bmatrix} \begin{bmatrix} 0.26 & 0.23 \end{bmatrix}
$$

$$
= \begin{bmatrix} 0.15 & 0.16 \\ 0.29 & 0.16 \end{bmatrix} + 0.026 \begin{bmatrix} 0.52 & 0.46 \\ 0.78 & 0.69 \end{bmatrix} = \begin{bmatrix} 0.15 & 0.16 \\ 0.29 & 0.16 \end{bmatrix} + \begin{bmatrix} 0.01 & 0.01 \\ 0.02 & 0.02 \end{bmatrix}
$$

$$
\begin{bmatrix} W_1 & W_3 \\ W_2 & W_4 \end{bmatrix} = \begin{bmatrix} 0.16 & 0.17 \\ 0.31 & 0.18 \end{bmatrix}
$$

---


### Época 6

**Valor de salida:**

$$
\begin{bmatrix} 2 & 3 \end{bmatrix} \begin{bmatrix} 0.16 & 0.17 \\ 0.31 & 0.18 \end{bmatrix} = \begin{bmatrix} 1.25 & 0.88 \end{bmatrix} \begin{bmatrix} 0.29 \\ 0.25 \end{bmatrix} = 0.5825
$$

**Error cuadrado medio:**

$$
e = \frac{1}{2} (0.5825 - 1)^2 = 0.087
$$
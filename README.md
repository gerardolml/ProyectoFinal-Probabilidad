# Proyecto Final — Probabilidad 📊

Este proyecto explora formas de aproximar el cálculo de la distribución normal estándar $\phi(x)$.  
Los métodos que estaremos utilizando para este cálculo son la **expansión de Taylor centrada en 0** y el **método de Montecarlo**.



## Cálculo por expansión de Taylor

### Distribución Normal Estándar

La función de distribución acumulada para la variable aleatoria $\mathcal{N}(0,1)$ se define como:

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\phi(x)=\int_{-\infty}^x\frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}}\,dt" />
</p>

Ahora, si $\(x \geq 0\)$:

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\phi(x)=\frac{1}{2}+\int_{0}^x\frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}}\,dt" />
</p>

También sabemos que la función  $e^{-\frac{x^2}{2}}$  se puede expresar como:

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?e^{-\frac{x^2}{2}}=\sum_{n=0}^\infty\frac{(-1)^n}{2^n\,n!}x^{2n}" />
</p>

Sustituyendo $e^{-\frac{x^2}{2}}$  en la integral anterior, y considerando únicamente el caso donde $\(x \geq 0\)$, tenemos:

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\phi(x)=\frac{1}{2}+\int_{0}^x\frac{1}{\sqrt{2\pi}}\sum_{n=0}^\infty\frac{(-1)^n}{2^n\,n!}t^{2n}\,dt" />
</p>

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\phi(x)=\frac{1}{2}+\frac{1}{\sqrt{2\pi}}\sum_{n=0}^\infty\frac{(-1)^n}{2^n\,n!}\int_{0}^xt^{2n}\,dt" />
</p>

Con este desarrollo, tenemos una integral que es más fácil de resolver que la expresión original. Por lo tanto, obtenemos la siguiente expresión:

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\phi(x)=\frac{1}{2}+\frac{1}{\sqrt{2\pi}}\sum_{n=0}^\infty\frac{(-1)^nx^{2n+1}}{2^n\,n!(2n+1)}" />
</p>

Esta fórmula solo funciona cuando $\(x \geq 0\)$. Para $\(x < 0\)$, se puede usar la simetría:

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\phi(-x)=1-\phi(x)" />
</p>

### Implementación

Se creó una implementación en Python y C donde se aplica la fórmula desarrollada para calcular el valor de $\phi(x)$.  
A continuación, se muestra gráficamente cómo funciona la aproximación:

![aproximacion_normal-ezgif com-loop-count](https://github.com/user-attachments/assets/57d11a80-5084-46fe-b9a5-56d4b955049a)

La función que hicimos calcula muy bien $\(\phi(x)\)$, pero el error se hace más evidente en las colas de la función.  
Esto se observa en el siguiente gráfico, que representa cómo evoluciona el error conforme se incluyen más términos en el polinomio:

![error_phi-ezgif com-loop-count](https://github.com/user-attachments/assets/b18b4618-b7d3-4dca-b6f5-e279a34bfecd)

---

## Método Montecarlo

El **método de Montecarlo** es una técnica numérica que utiliza **números aleatorios** para aproximar soluciones a problemas matemáticos complejos, especialmente cuando no se pueden resolver de forma exacta.

### ¿Cómo funciona?
1. Se simulan muchos casos posibles usando valores aleatorios.
2. Se observa cuántos de esos casos cumplen cierta condición.
3. Se calcula una proporción y se utiliza para aproximar el resultado deseado.

### Ejemplo clásico: área del círculo

Para estimar el valor de $\(\pi\)$, se puede inscribir un círculo dentro de un cuadrado y generar puntos aleatorios dentro del cuadrado:

- Si el círculo tiene radio 1, el área del cuadrado será $\(4\)$ (de lado 2).
- Se generan $\(N\)$ puntos aleatorios en el cuadrado.
- Se cuenta cuántos caen dentro del círculo (distancia al origen menor que 1).
- Entonces:

$\[
\pi \approx 4 \times \frac{\text{número de puntos dentro del círculo}}{\text{número total de puntos}}
\]$

### Ventajas
- Sencillo de implementar.
- Muy útil cuando no hay una solución analítica.
- Mejora su precisión al aumentar el número de simulaciones.

## Implementación

Las siguientes gráficas muestran cómo se ve este método aplicado a la función:

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}" />
</p>

![montecarlo2-ezgif com-loop-count](https://github.com/user-attachments/assets/01740c96-146e-4dfd-b809-9f4a475ab5a0)  
![montecarlo1-ezgif com-loop-count](https://github.com/user-attachments/assets/a84083bd-de10-4a5f-bf02-bdfc45eaee00)

---
#### Conclusión

A lo largo de este proyecto, exploramos dos métodos distintos para aproximar la función de distribución normal estándar $\phi(x)$: la expansión en serie de Taylor y el método de Montecarlo.

La **expansión de Taylor** demostró ser una forma precisa y eficiente para calcular $\phi(x)$, especialmente cerca del origen. Sin embargo, su precisión disminuye en las **colas de la distribución**, donde se requieren muchos más términos para lograr una buena aproximación.

Por otro lado, el **método de Montecarlo** ofrece una alternativa más general, basada en simulaciones aleatorias. Aunque es conceptualmente sencillo y muy versátil, **su precisión depende en gran medida del número de simulaciones**. Esto puede implicar un alto costo computacional si se busca una aproximación muy precisa.

En resumen:
- La expansión de Taylor es más **eficiente y precisa** para valores cercanos a cero.
- El método de Montecarlo es más **flexible y generalizable**, pero menos eficiente para funciones suaves como $\phi(x)$.

Este ejercicio ilustra cómo distintas herramientas numéricas pueden ser útiles en diferentes contextos, y resalta la importancia de elegir el método adecuado según las características del problema.

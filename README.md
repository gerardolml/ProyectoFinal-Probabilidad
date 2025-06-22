# Proyecto Final — Probabilidad 📊

Este proyecto explora formas de aproximar el calculo de distribución normal estándar $\phi(x)$ Los metodos con los que estarmos trabajando para este calculo es usando la expansion de taylor centrada en 0 y el metodo Montecarlo

---

## Calculo por expansion de taylor

### Distribución Normal Estándar

La función de distribución acumulada para la variable aleatoria $\( X \sim \mathcal{N}(0,1) \)$ se define como:

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\phi(x)=\int_{-\infty}^x\frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}}\,dt" />
</p>

Ahora si $x\geq 0$
<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\phi(x)=\frac{1}{2}+\int_{0}^x\frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}}\,dt" />
</p>

Tambien sabemos que la funcion $e^{-\frac{x^2}{2}}$ se puede expresar de la siguiente manera:
<p align="center">
  <img src="https://latex.codecogs.com/svg.image?e^{-\frac{x^2}{2}}=\sum_{n=0}^\infty\frac{(-1)^n}{2^n\,n!}x^{2n}" />
</p>

Sustituyendo los $e^{-\frac{t^2}{2}}$ tenemos el siguiente desarrollo y tomando solamente la parte donde $x\geq 0$
<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\phi(x)=\frac{1}{2}+\int_{0}^x\frac{1}{\sqrt{2\pi}}\sum_{n=0}^\infty\frac{(-1)^n}{2^n\,n!}t^{2n}\,dt" />
</p>

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\phi(x)=\frac{1}{2}+\frac{1}{\sqrt{2\pi}}\sum_{n=0}^\infty\frac{(-1)^n}{2^n\,n!}\int_{0}^xt^{2n}\,dt" />
</p>

Con este desarrollo tenemos una integral que es mas facil de resolver que la expresion original. por lo que tenemos la siente expresion 

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\phi(x)=\frac{1}{2}+\frac{1}{\sqrt{2\pi}}\sum_{n=0}^\infty\frac{(-1)^nx^{2n+1}}{2^n\,n!(2n+1)}" />
</p>

Ahora esta formula solo funciona si si $x\geq 0$, la solucion si $x < 0$ 
<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\phi(-x)=1-\phi(x)" />
</p>

### Implementacion 
Se creo una implementacion en python y C donde se aplica la formula desarroya y esta funcion va a calcualar el valor de $\phi(x)$ Aqui se muestra graficamente como funciona la aproximacion de la funcion:

![aproximacion_normal-ezgif com-loop-count](https://github.com/user-attachments/assets/57d11a80-5084-46fe-b9a5-56d4b955049a)


La funcion que hicimos calcula muy bien a $\phi(x)$ solo que el erro se va presentando en las colas de funcion, esto lo vemos con el siguiente grafico que representa la evolucion del error a medida de como se van incluyendo mas terminos en los polinomios 

![error_phi-ezgif com-loop-count](https://github.com/user-attachments/assets/b18b4618-b7d3-4dca-b6f5-e279a34bfecd)


---

## Metodo Montecarlo

El **método de Montecarlo** es una técnica numérica que utiliza **números aleatorios** para aproximar soluciones a problemas matemáticos complejos, especialmente cuando no es posible resolverlos de forma exacta.

### ¿Cómo funciona?
1. Se simulan muchos casos posibles usando valores aleatorios.
2. Se observa cuántos de esos casos cumplen cierta condición.
3. Se calcula una proporción y se usa para aproximar el resultado deseado.

### Ejemplo clásico: área del círculo

Para estimar el valor de $\pi$, se puede inscribir un círculo dentro de un cuadrado y generar puntos aleatorios dentro del cuadrado:

- Si el círculo tiene radio 1, el área del cuadrado será \(4\) (de lado 2).
- Generamos \(N\) puntos aleatorios en el cuadrado.
- Contamos cuántos caen dentro del círculo (distancia al origen < 1).
- Entonces:

\[
$\pi$ $\approx$ 4 $\times$ $\frac{\text{número de puntos dentro del círculo}}{\text{número total de puntos}}$
\]

### Ventajas
- Sencillo de implementar.
- Muy útil cuando no hay una solución analítica.
- Mejora su precisión al aumentar el número de simulaciones

## Implementacion 
Las siguientes graficas representan como se ve este metodo aplicandolo sobre la funcion 
<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}\" />
</p


![montecarlo2-ezgif com-loop-count](https://github.com/user-attachments/assets/01740c96-146e-4dfd-b809-9f4a475ab5a0)
![montecarlo1-ezgif com-loop-count](https://github.com/user-attachments/assets/a84083bd-de10-4a5f-bf02-bdfc45eaee00)

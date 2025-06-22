# Proyecto Final — Probabilidad 📊

Este proyecto explora formas de aproximar el calculo de distribución normal estándar $\phi(x)$ Los metodos con los que estarmos trabajando para este calculo es usando la expansion de taylor centrada en 0 y el metodo Montecarlo



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

![aproximacion_normal](./Imagenes/aproximacion_normal.gif)


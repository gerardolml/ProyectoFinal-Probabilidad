# Proyecto Final — Probabilidad 📊

Este proyecto explora el desarrollo de la función de distribución normal estándar $\( \phi(x) \)$, su forma integral y su aproximación mediante el desarrollo en serie de Taylor de su núcleo exponencial.

---

## Distribución Normal Estándar

La función de distribución acumulada para la variable aleatoria $\( X \sim \mathcal{N}(0,1) \)$ se define como:

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\phi(x)=\int_{-\infty}^x\frac{1}{\sqrt{2\pi}}e^{-\frac{t^2}{2}}\,dt" />
</p>

---

## Desarrollo de Taylor de \( e^{-\frac{x^2}{2}} \)

La función dentro de la integral no tiene una antiderivada elemental. Sin embargo, podemos aproximarla utilizando una serie de Taylor centrada en 0:

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?e^{-\frac{x^2}{2}}=\sum_{n=0}^\infty\frac{(-1)^n}{2^n\,n!}x^{2n}" />
</p>

Desarrollando los primeros términos:

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?e^{-\frac{x^2}{2}}\approx1-\frac{x^2}{2}+\frac{x^4}{8}-\frac{x^6}{48}+\cdots" />
</p>

---

## Aplicaciones

Usando esta expansión, podemos aproximar numéricamente la función \( \phi(x) \) integrando término a término:

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\phi(x)\approx\int_{-\infty}^x\frac{1}{\sqrt{2\pi}}\left(1-\frac{t^2}{2}+\frac{t^4}{8}-\cdots\right)\,dt" />
</p>

---

## Conclusión

Esta aproximación permite obtener valores de la función de distribución normal sin usar tablas, y es útil en simulaciones o contextos donde no se dispone de funciones especiales predefinidas.

---

## Créditos

Este trabajo fue realizado por **Luis Ayala** como parte del proyecto final de la materia de Probabilidad.

import numpy as np
import matplotlib.pyplot as plt
import imageio
from io import BytesIO
import base64
from IPython.display import HTML, display
import math

# Función factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Aproximación a la función de distribución normal estándar
def normal_aprox(x, n_terminos):
    suma = 0.0
    for n in range(n_terminos):
        numerador = (-1)**n * x**(2 * n + 1)
        denominador = (2 * n + 1) * (2**n) * factorial(n)
        suma += numerador / denominador
    return 0.5 + (1.0 / math.sqrt(2 * math.pi)) * suma

# Generar y mostrar GIF con comparación teórica y error
def generar_gif_aproximacion(x, max_terminos=20, duration=0.7, save_path=None, decimals=6):
    x_vals = np.linspace(-4, 4, 400)
    frames = []

    # Valor teórico usando función de error
    valor_teorico = 0.5 * (1 + math.erf(x / math.sqrt(2)))

    for n in range(1, max_terminos + 1):
        y_aprox = [normal_aprox(xi, n) for xi in x_vals]
        y_real = [0.5 * (1 + math.erf(xi / math.sqrt(2))) for xi in x_vals]

        valor_aproximado = normal_aprox(x, n)
        error = abs(valor_aproximado - valor_teorico)

        fig, ax = plt.subplots(figsize=(10, 6), dpi=110)
        ax.plot(x_vals, y_aprox, label=f'Aproximación con {n} términos', lw=2.5, color="#3498db")
        ax.plot(x_vals, y_real, label='Función Normal Teórica', color='#2c3e50', linestyle='--')
        ax.axvline(x, color='#e74c3c', linestyle=':', lw=2, label=f'x = {x:.2f}')
        ax.set_title(f"Aproximación de Φ({x}) usando {n} términos", fontsize=16)
        ax.set_xlabel("x", fontsize=14)
        ax.set_ylabel("Φ(x)", fontsize=14)
        ax.set_ylim(0, 1.05)
        ax.grid(True)
        ax.legend(fontsize=11, loc='lower right')

        # Mostrar valores comparativos
        ax.text(-3.8, 0.9, f"Φ({x:.2f}) ≈ {valor_aproximado:.{decimals}f}", fontsize=12)
        ax.text(-3.8, 0.83, f"Teórico     = {valor_teorico:.{decimals}f}", fontsize=12)
        ax.text(-3.8, 0.76, f"Error abs   = {error:.{decimals}f}", fontsize=12)

        buf = BytesIO()
        fig.savefig(buf, format='png')
        plt.close(fig)
        buf.seek(0)
        frames.append(imageio.v2.imread(buf))

    # Crear buffer del GIF
    gif_buffer = BytesIO()
    imageio.mimsave(gif_buffer, frames, format='GIF', duration=duration)
    gif_buffer.seek(0)

    # Guardar si se solicita
    if save_path:
        with open(save_path, 'wb') as f:
            f.write(gif_buffer.read())
        gif_buffer.seek(0)  # Para mostrarlo también

    # Mostrar en el notebook
    gif_base64 = base64.b64encode(gif_buffer.read()).decode("utf-8")
    display(HTML(f'<img src="data:image/gif;base64,{gif_base64}">'))
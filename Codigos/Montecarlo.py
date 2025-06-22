import numpy as np
import matplotlib.pyplot as plt
import imageio
from io import BytesIO
import base64
from IPython.display import HTML, display
from math import exp, sqrt, pi
from scipy.stats import norm  # Valor teórico

plt.style.use('seaborn-v0_8-muted')

def normal_pdf(t):
    return (1 / sqrt(2 * pi)) * exp(-t**2 / 2)

def monte_carlo_cdf_visual(x=None, a=None, b=None, n_points=10000, step=500, L=4, decimals=6, save_path=None):
    assert (x is not None) or (a is not None and b is not None), "Debes especificar x o (a y b)."

    x_min = -L
    x_max = L
    max_pdf = normal_pdf(0)

    accepted_under_curve = []
    accepted_above_curve = []

    frames = []

    if x is not None:
        theoretical = norm.cdf(x)
        range_check = lambda t: t <= x
    else:
        a_, b_ = min(a, b), max(a, b)
        theoretical = norm.cdf(b_) - norm.cdf(a_)
        range_check = lambda t: a_ <= t <= b_

    for i in range(1, n_points + 1):
        t = np.random.uniform(x_min, x_max)
        y = np.random.uniform(0, max_pdf)

        if y <= normal_pdf(t):
            accepted_under_curve.append((t, y))
        else:
            accepted_above_curve.append((t, y))

        if i % step == 0 or i == n_points:
            fig, ax = plt.subplots(figsize=(11, 6), dpi=110)
            ax.grid(False)

            t_vals = np.linspace(x_min, x_max, 500)
            y_vals = [normal_pdf(ti) for ti in t_vals]
            ax.plot(t_vals, y_vals, color='#2c3e50', lw=3, label='Densidad normal')

            if x is not None:
                count = sum(1.0 for t_, _ in accepted_under_curve if t_ <= x)
                estimate = count / len(accepted_under_curve) if accepted_under_curve else 0
                ax.axvline(x, color='#e74c3c', linestyle='--', lw=3, label=f'x = {x:.2f}')
                t_fill = np.linspace(x_min, x, 500)
            else:
                count = sum(1.0 for t_, _ in accepted_under_curve if a_ <= t_ <= b_)
                estimate = count / len(accepted_under_curve) if accepted_under_curve else 0
                ax.axvline(a_, color='#e67e22', linestyle='--', lw=3, label=f'a = {a_:.2f}')
                ax.axvline(b_, color='#e74c3c', linestyle='--', lw=3, label=f'b = {b_:.2f}')
                t_fill = np.linspace(a_, b_, 500)

            # RECTÁNGULO de simulación en lugar del área bajo la curva
            ax.fill_between(t_fill, 0, max_pdf, color='#95a5a6', alpha=0.3, label='Rectángulo de simulación')

            under_filtered = [(t_, y_) for t_, y_ in accepted_under_curve if range_check(t_)]
            above_filtered = [(t_, y_) for t_, y_ in accepted_above_curve if range_check(t_)]

            if under_filtered:
                t_u, y_u = zip(*under_filtered)
                ax.scatter(t_u, y_u, color='#3498db', s=10, alpha=0.7, label='Bajo la curva')

            if above_filtered:
                t_o, y_o = zip(*above_filtered)
                ax.scatter(t_o, y_o, color='#e74c3c', s=10, alpha=0.5, label='Fuera de la curva')

            error = abs(theoretical - estimate)

            if x is not None:
                title = (
                    f"Φ({x}) ≈ {estimate:.{decimals}f} | Teórico = {theoretical:.{decimals}f} "
                    f"| Error = {error:.{decimals}f}"
                )
            else:
                title = (
                    f"P({a_} ≤ Z ≤ {b_}) ≈ {estimate:.{decimals}f} | Teórico = {theoretical:.{decimals}f} "
                    f"| Error = {error:.{decimals}f}"
                )

            ax.set_title(f'{title}\n({i} puntos)', fontsize=18, fontweight='bold', pad=25)
            ax.set_xlabel('t', fontsize=15, labelpad=15)
            ax.set_ylabel('Densidad', fontsize=15, labelpad=15)
            ax.set_xlim(x_min, x_max)
            ax.set_ylim(0, max_pdf * 1.1)
            ax.tick_params(labelsize=12)

            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)

            plt.tight_layout()

            buf = BytesIO()
            fig.savefig(buf, format='png')
            plt.close()
            buf.seek(0)
            frames.append(imageio.v2.imread(buf))

    gif_buffer = BytesIO()
    imageio.mimsave(gif_buffer, frames, format='GIF', duration=0.7)
    gif_buffer.seek(0)

    if save_path is not None:
        with open(save_path, 'wb') as f:
            f.write(gif_buffer.read())
        gif_buffer.seek(0)

    gif_base64 = base64.b64encode(gif_buffer.read()).decode("utf-8")
    display(HTML(f'<img src="data:image/gif;base64,{gif_base64}">'))
import numpy as np

from bokeh.models import Label
from bokeh.plotting import figure, show

x = np.arange(0.0, 1.0 + 0.01, 0.01)
y = np.cos(2 * 2 * np.pi * x) + 2

p = figure(title="$$f = \\sum_{n=1}^\\infty\\frac{-e^{i\\pi}}{2^n}!$$", plot_width=500, plot_height=500)
p.line(x, y)

# Note: must set ``render_mode="css"``
latex = Label(
    text="$$f = \\sum_{n=1}^\\infty\\frac{-e^{i\\pi}}{2^n}!$$",
    x=40,
    y=420,
    x_units="screen",
    y_units="screen",
    render_mode="css",
    text_font_size="21px",
    background_fill_alpha=0,
)

p.add_layout(latex)

show(p)
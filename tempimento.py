import numpy
import bokeh
from bokeh.plotting.figure import figure

seno = numpy.sin(numpy.pi)

p = figure(width=1280, height=720)
p.line(x=[-64,64], y=numpy.linspace(-numpy.pi, numpy.pi, 255))

show(p)

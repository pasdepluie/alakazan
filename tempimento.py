import numpy
import bokeh
from cassandra.cluster import Cluster
from bokeh.plotting.figure import figure

cosseno = numpy.cos(numpy.pi)

p = figure(width=1280, height=720)
p.line(x=[-64,64], y=numpy.linspace(-numpy.pi, numpy.pi, 255))

cluster = Cluster()

show(p)

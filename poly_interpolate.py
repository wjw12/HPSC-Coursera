'''
quadratic polynomial interpolation
p(x) = c0 + c1*x + c2*x**2

and general polynomial interpolation
'''
from numpy import *
import matplotlib.pyplot as plt

def quad_interp(xi,yi):
	A = vstack([ones(3), xi, xi**2]).T
	b = array(yi)
	return linalg.solve(A,b)

def plot_quad(xi,yi):
	xi, yi = array(xi), array(yi)
	c = quad_interp(xi,yi)
	x = linspace(xi.min()-1, xi.max()+1, 500)
	plt.plot(x,c[0]+c[1]*x+c[2]*x**2)
	plt.show()

def test_quad():
	x1 = [1.,2.,3.]
	y1 = [4.,7.,9.]
	x2 = array([3.,5.,6.])
	y2 = array([1.,-1.,7.])
	plot_quad(x1,y1)
	plot_quad(x2,y2)
	pass

def poly_interp(xi,yi):
	assert len(xi)==len(yi), 'xi and yi should be of same length'
	n = len(xi)
	A = ones(n)
	for deg in range(1,n):
		A = vstack([A,xi**deg])
	A = A.T
	return linalg.solve(A,yi)
	
def plot_poly(xi,yi):
	xi, yi = array(xi), array(yi)
	x = linspace(xi.min()-2,xi.max()+2,500)
	c = poly_interp(xi,yi)
	n = len(xi)
	y = c[n-1]
	for j in range(n-1,0,-1):
		y = y*x + c[j-1]
	plt.plot(x,y)
	plt.show()

def test_poly():
	x1 = [1.,2.,3.,4.]
	y1 = [4.,7.,9.,6.]
	x2 = array([3.,5.,6.,8.,10.])
	y2 = array([1.,-1.,7.,9.,55.])
	x3 = random.random(20)
	y3 = random.random(20)
	plot_poly(x1,y1)
	plot_poly(x2,y2)
	plot_poly(x3,y3)
	

import math #importo la libreria de math

#funciones que devuelven el area y perimetro de un figura
def rectangulo(base,altura):
	area = base * altura
	perimetro = 2 * (base + altura)
	return area, perimetro

def triangulo(base,altura):
	lado = ((altura**2)+((base/2)**2))**(1/2)
	area = (base*altura)/2
	perimetro = base + 2*lado
	return area,perimetro

def circulo(radio):
	area = math.pi * (radio**2)
	perimetro = math.pi *2*radio
	return area, perimetro



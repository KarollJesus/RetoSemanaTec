
import pandas as pd
#importar las funciones que calculan el perimetro y area
#de cada figura
from figuras import rectangulo, triangulo, circulo
df = pd.read_csv("figuras.csv")
print("El archivo ha sido cambiado")

for index, row in df.iterrows():
	if  row['FIGURA'] == 'c':
		calculos = circulo(row['MEDIDA1'])
		print(f"fila{index}, Figura = Circulo, , MEDIDA1 = {row['MEDIDA1']} , MEDIDA2 = {row['MEDIDA2']}, AREA = {calculos[0]}, PERIMETRO = {calculos[1]}")
	elif row['FIGURA'] == 't':
		calculos = triangulo(row['MEDIDA1'],row['MEDIDA2'])
		print(f"fila{index}, Figura = Triangulo, MEDIDA1 = {row['MEDIDA1']} , MEDIDA2 = {row['MEDIDA2']}, AREA = {calculos[0]}, PERIMETRO = {calculos[1]}")
	else:
		calculos = rectangulo(row['MEDIDA1'],row['MEDIDA2'])
		print(f"fila{index}, Figura = Rectangulo,  MEDIDA1 = {row['MEDIDA1']} , MEDIDA2 = {row['MEDIDA2']}, AREA = {calculos[0]}, PERIMETRO = {calculos[1]}")
	



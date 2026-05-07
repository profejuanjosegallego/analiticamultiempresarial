#Codigo principal que ejecutara la ETL (Encargado de ejecutar el analisis de datos)

from notebook.simulaciones.simulacionUsuario import simular_usuarios
#TAREA: importar en esta linea su funcion simuladora de gastos

usuarios=simular_usuarios(100000)
print(usuarios)

#TAREA: Cree la variable gastos=a su funcion
#print(gastos)
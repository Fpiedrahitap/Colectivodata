import pandas as pd

usuariosdf = pd.read_excel("./data/usuarios_sistema_completo.xlsx")
#print(usuariosdf)

print(usuariosdf.isnull().sum())


#CONSULTAS DETALLADAS

#1. necesito listado de aprendices
#2. necesito listado de instructores o profesores
#3. necesito listado de especialistas en desarollo web o sistemas
#4. necesito listado de solo usuarios con direccion en medellin
#5. necesito listado de solo usuarios cuyas direcciones terminen en sur
#6. necesito listado de especialitas que contengan la palabra datos
#7. necesito profesores de itagui
#8. necesito una lista de nacidos en los 90s
#9. necesito una lista de profesores mayores
#10. necesito una lista de profesores y estudiantes nacidos en el nuevo milenio  
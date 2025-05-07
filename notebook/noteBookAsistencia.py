import pandas as pd

#Leyendo los datos de asistencia

asistenciadf = pd.read_csv("./data/asistencia_estudiantes_completo.csv")
#print(asistenciadf)

#obteniendo informacion basica del dataframe

#print(asistenciadf.describe())

#print(asistenciadf.isnull().sum())

#print(asistenciadf['estrato'].value_counts().head(2))


#FILTROS O CONSULTAS DETALLADAS

#1. necesito encontrar los estudiantes que si asistieron
estudiantesQueAsistieron = asistenciadf.query('estado == "asistio"')
#2. necesito encontrar los estudiantes que no asistieron
estudiantesNoQueAsistieron = asistenciadf.query('estado == "inasistencia"')
#3. necesito encontrar los estudiantes que llegaron tarde
estudiantesQueLlegaronTarde = asistenciadf.query('estado == "justificado"')
#4. necesito encontrar los estudiantes de estrato 1
estudiantesEstratoBajo = asistenciadf.query('estrato == 1')
#5. necesito encontrar los estudiantes de estratos altos
estudiantesEstratoAlto = asistenciadf.query('estrato >= 5')
#6. necesito encontrar estudiantes que llegan en metro
estudiantesMetro = asistenciadf.query('medio_transporte == "metro"')
#7. necesito encontrar estudiantes que llegaron en bicicleta
estudiantesBicicleta = asistenciadf.query('medio_transporte == "bicicleta"')
#8. necesito encontrar todos los estudiantes menos los que llegaron a pie
estudiantesNoAPie = asistenciadf.query('medio_transporte != "a pie"')
#9. necesito todos los registros de asistencia de junio
registrosJunio = asistenciadf.loc[(asistenciadf['fecha'] >= '2025-06-01') & (asistenciadf['fecha'] <= '2025-07-30')]

#10. necesito todos los estudiantes que usan trasporte ecologico
Ecologico = asistenciadf.query('medio_transporte == "bicicleta" or medio_transporte == "a pie"')

#11. necesito todos los estudiantes que usan bus y son estrato alto
estudiantesBusEstratoAlto = asistenciadf.query('medio_transporte == "bus" and estrato >= 5')

#12. necesito todos los estudiantes que usan bus y son estrato bajo
estudiantesBusEstratobajo = asistenciadf.query('medio_transporte == "bus" and estrato <= 2')

#13. necesito estudiantes caminan para llegar a clase
estudiantesAPie = asistenciadf.query('medio_transporte == "a pie"')


#CONTEOS POR AGRUPACIONES

#1. necesito conteo de registros por estado de asistencia
conteo = asistenciadf.groupby('estado').size()
#2. necesito obtener el numero de registros por estrato
conteoEstrato = asistenciadf.groupby('estrato').size()

#3. necesito la cantidad de estudiantes por medio de trasporte 
conteoMedioTransporte = asistenciadf.groupby('medio_transporte').size()

#4. necesito promedio de estrato por estado de asistencia
promedioEstrato = asistenciadf.groupby('estado')['estrato'].mean()
#5. necesito maximo estrato por estado
maximoEstrato = asistenciadf.groupby('estado')['estrato'].max()
#6. necesito minimo estrato por estado
minimoEstrato = asistenciadf.groupby('estado')['estrato'].min()
#7. necesito conteo de asistencia por grupo y estado
ConteoAsistenciaGrupo = asistenciadf.loc[(asistenciadf['estado'] == 'asistio') | (asistenciadf['estado'] == 'inasistencia')].groupby(['grupo', 'estado']).size()





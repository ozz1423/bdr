# Datos dummy y funciones de agregación

## Inserción de datos ficticios para la base de datos LigaMX

Se utilizó un script con el uso de diferentes librerías para generar registros aleatorios para las tablas.

Este [script](insertar_dummy.py) conecta a una base de datos PostgreSQL y utiliza la librería Faker junto con funciones aleatorias para insertar datos simulados en tres tablas: crea 10 equipos, luego genera 100 jugadores asignados aleatoriamente a esos equipos, y finalmente crea 100 partidos distribuidos en 20 semanas con información variada como fechas, marcadores y asistencia.

## Funciones de agregación

### Consulta 1: Edad promedio de los equipos
```sql
SELECT AVG(edad) AS media_edad_equipos
FROM equipo;
```

Esta consulta calcula la edad promedio de los equipos registrados en la tabla EQUIPO. La columna EDAD representa la edad promedio de los jugadores de cada equipo, y esta consulta devuelve la media general de todas esas edades.

### Consulta 2: Máximo de minutos jugados por un jugador
```sql
SELECT MAX(minutos) AS max_minutos
FROM jugador;
```

Esta consulta obtiene el valor máximo de minutos jugados por un jugador en la tabla JUGADOR. Esto identifica al jugador con mayor participación en el campo en términos de tiempo.

### Consulta 3: Percentil 75 de goles anotados
```sql
SELECT PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY goles) AS percentil_75_goles
FROM jugador;
```

Esta consulta calcula el percentil 75 de la cantidad de goles anotados por los jugadores. Es decir, el número de goles que supera al 75% de los jugadores, ayudando a entender la distribución del rendimiento goleador.

### Consulta 4: Resultado local más frecuente
```sql
SELECT marcador_local as golesLocal, COUNT(*) AS veces
FROM partido
GROUP BY marcador_local
ORDER BY COUNT(*) DESC
LIMIT 1;
```

Esta consulta identifica el marcador local más frecuente en los partidos. Agrupa los partidos según los goles anotados por el equipo local, cuenta cuántas veces se repite cada resultado y devuelve el más común.
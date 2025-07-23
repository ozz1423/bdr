# Subconsultas de la base de datos LigaMX

## Consulta 1: Jugadores que pertenecen al equipo con más goles anotados en total
```sql
SELECT nombre
FROM jugador
WHERE equipo_id = (
    SELECT equipo_local_id
    FROM partido
    GROUP BY equipo_local_id
    ORDER BY SUM(marcador_local) DESC
    LIMIT 1
);
```

Esta consulta busca a todos los jugadores cuyo equipo es el que más goles ha anotado como local.

## Consulta 2: Equipos que tienen más de 5 jugadores con más de 1000 minutos jugados
```sql
SELECT nombre_equipo
FROM equipo
WHERE id_equipo IN (
    SELECT equipo_id
    FROM jugador
    WHERE minutos > 1000
    GROUP BY equipo_id
    HAVING COUNT(*) > 5
);
```

Encuentra los equipos que tienen más de 5 jugadores que han jugado más de 1000 minutos.

## Consulta 3: Jugadores cuyo total de goles es mayor al promedio de todos los jugadores
```sql
SELECT nombre, goles
FROM jugador
WHERE goles > (
    SELECT AVG(goles)
    FROM jugador
);
```

Muestra a los jugadores que han anotado más goles que el promedio de todos los jugadores.

## Consulta 4: Partidos en los que participó el equipo con mayor promedio de posesión (PL)
```sql
SELECT *
FROM partido
WHERE equipo_local_id = (
    SELECT id_equipo
    FROM equipo
    ORDER BY pl DESC
    LIMIT 1
)
OR equipo_visitante_id = (
    SELECT id_equipo
    FROM equipo
    ORDER BY pl DESC
    LIMIT 1
);
```

Muestra todos los partidos donde jugó el equipo que tiene el mayor valor de posesión (PL).

## Consulta 5: Jugadores cuyo equipo haya jugado un partido con más de 50,000 asistentes
```sql
SELECT nombre
FROM jugador
WHERE equipo_id IN (
    SELECT equipo_local_id
    FROM partido
    WHERE asistencia > 50000
    UNION
    SELECT equipo_visitante_id
    FROM partido
    WHERE asistencia > 50000
);
```

Busca jugadores cuyos equipos hayan jugado algún partido (como local o visitante) con más de 50,000 asistentes.
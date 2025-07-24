# Creación de vistas y trigger

## Vista con JOIN
```sql
CREATE OR REPLACE VIEW vista_jugador_equipo AS
SELECT 
    j.ID_JUGADOR,
    j.NOMBRE AS nombre_jugador,
    j.PAIS,
    j.POSC,
    e.NOMBRE_EQUIPO,
    e.PL,
    e.EDAD
FROM 
    JUGADOR j
JOIN 
    EQUIPO e ON j.EQUIPO_ID = e.ID_EQUIPO;
```

Esta vista combina información de las tablas JUGADOR y EQUIPO usando un INNER JOIN, es decir, solo mostrará los jugadores que están asignados a un equipo existente.

## Vista con LEFT JOIN
```sql
CREATE OR REPLACE VIEW vista_equipo_jugador_left AS
SELECT 
    e.ID_EQUIPO,
    e.NOMBRE_EQUIPO,
    j.ID_JUGADOR,
    j.NOMBRE AS nombre_jugador
FROM 
    EQUIPO e
LEFT JOIN 
    JUGADOR j ON e.ID_EQUIPO = j.EQUIPO_ID;
```

Esta vista muestra todos los equipos, y si tienen jugadores, también muestra los datos de los jugadores.
Pero si un equipo no tiene ningún jugador asignado, igualmente aparecerá en el resultado, con los datos del jugador en NULL.

## Vista con RIGHT JOIN
```sql
CREATE OR REPLACE VIEW vista_jugador_equipo_right AS
SELECT 
    j.ID_JUGADOR,
    j.NOMBRE AS nombre_jugador,
    e.ID_EQUIPO,
    e.NOMBRE_EQUIPO
FROM 
    EQUIPO e
RIGHT JOIN 
    JUGADOR j ON e.ID_EQUIPO = j.EQUIPO_ID;
```

Esta vista muestra todos los jugadores, y si están asignados a un equipo, también muestra los datos del equipo.
Si algún jugador no tiene un equipo asignado (es decir, EQUIPO_ID es NULL o no coincide con ningún ID_EQUIPO), de todas formas aparece en la vista, pero los datos del equipo saldrán como NULL.

## Vista con subconsulta
```sql
CREATE OR REPLACE VIEW vista_jugador_con_goles_equipo AS
SELECT 
    j.ID_JUGADOR,
    j.NOMBRE AS nombre_jugador,
    j.EQUIPO_ID,
    e.NOMBRE_EQUIPO,
    
    (
        SELECT SUM(j2.GOLES)
        FROM JUGADOR j2
        WHERE j2.EQUIPO_ID = j.EQUIPO_ID
    ) AS total_goles_equipo
FROM 
    JUGADOR j
JOIN 
    EQUIPO e ON j.EQUIPO_ID = e.ID_EQUIPO;
```

Esta vista muestra los datos de cada jugador junto con el total de goles marcados por todos los jugadores de su mismo equipo.

## Creación de trigger

### Función para ejecutar el trigger
```sql
CREATE OR REPLACE FUNCTION actualizar_goles_mas_asist()
RETURNS TRIGGER AS $$
BEGIN
    -- Actualiza la columna GOLES_MAS_ASIST del jugador
    UPDATE JUGADOR
    SET GOLES_MAS_ASIST = GOLES + COALESCE(ASISTENCIAS, 0)
    WHERE ID_JUGADOR = NEW.ID_JUGADOR;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

### Trigger
```sql
CREATE TRIGGER trigger_actualizar_goles_mas_asist
AFTER INSERT OR UPDATE OF GOLES, ASISTENCIAS ON JUGADOR
FOR EACH ROW
EXECUTE FUNCTION actualizar_goles_mas_asist();
```

Cada vez que se inserte o se actualicen los campos GOLES o ASISTENCIAS de un jugador:
Se actualiza automáticamente su campo GOLES_MAS_ASIST con la suma GOLES + ASISTENCIAS.
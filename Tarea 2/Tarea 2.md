# Modelo Entidad - Relación de la Liga MX

## Descripción general de la base de datos

Este sistema de base de datos modela información de la **Liga MX**. Compuesta por las siguientes tablas:

---

### Tabla: `EQUIPO`

Contiene información sobre los clubes participantes en la Liga MX.

| Atributo             | Tipo de Dato     | Descripción                            |
|----------------------|------------------|----------------------------------------|
| ID_EQUIPO            | SERIAL (PK)      | Identificador único del equipo         |
| NOMBRE_EQUIPO        | VARCHAR(100)     | Nombre oficial del club                |
| PL                   | INTEGER          | Número de jugadores en los partidos    |
| EDAD                 | NUMERIC(4,1)     | Edad promedio del equipo               |
| POS                  | INTEGER          | Porcentaje de posesión del balón       |
| PJ                   | INTEGER          | Total de partidos jugados              |
| TITULAR              | INTEGER          | Jugadores de titular                   |
| MINUTOS              | INTEGER          | Minutos jugados por el equipo          |

---

### Tabla: `JUGADOR`

Contiene información sobre jugadores activos en la Liga MX.

| Atributo             | Tipo de Dato     | Descripción                            |
|----------------------|------------------|----------------------------------------|
| ID_JUGADOR           | SERIAL (PK)      | Identificador único del jugador        |
| NOMBRE               | VARCHAR(100)     | Nombre completo del jugador            |
| PAIS                 | VARCHAR(50)      | Nacionalidad del jugador               |
| POSC                 | VARCHAR(50)      | Posición en el campo                   |
| EQUIPO_ID            | INTEGER (FK)     | Relación con el equipo actual          |
| NACIMIENTO           | DATE             | Fecha de nacimiento                    |
| PJ                   | INTEGER          | Partidos jugados                       |
| TITULAR              | INTEGER          | Partidos como titular                  |
| MINUTOS              | INTEGER          | Minutos totales jugados                |
| NOVENTAS             | NUMERIC(5,2)     | Equivalente en "partidos completos"    |
| GOLES                | INTEGER          | Goles anotados                         |
| ASISTENCIAS          | INTEGER          | Asistencias realizadas                 |
| GOLES_MAS_ASIST      | INTEGER          | Suma de goles y asistencias (G+A)      |
| PENALES              | INTEGER          | Tiros penales                          |
| TARJETAS_AMARILLAS   | INTEGER          | Tarjetas amarillas recibidas           |
| TARJETAS_ROJAS       | INTEGER          | Tarjetas rojas recibidas               |


---

### Tabla: `PARTIDO`

Contiene información de cada partido jugado en la liga.

| Atributo             | Tipo de Dato     | Descripción                            |
|----------------------|------------------|----------------------------------------|
| ID_PARTIDO           | SERIAL (PK)      | Identificador único del partido        |
| SEMANA               | INTEGER          | Semana de la competencia (jornada)               |
| DIA                  | VARCHAR(15)      | Día del partido                        |
| FECHA                | DATE             | Fecha del encuentro                    |
| HORA                 | TIME             | Hora del partido                       |
| EQUIPO_LOCAL_ID      | INTEGER (FK)     | ID del equipo local                    |
| XG                   | NUMERIC(4,2)     | Goles esperados                        |
| MARCADOR_LOCAL       | INTEGER          | Goles anotados por el equipo local     |
| EQUIPO_VISITANTE_ID  | INTEGER (FK)     | ID del equipo visitante                |
| MARCADOR_VISITANTE   | INTEGER          | Goles anotados por el equipo visitante |
| ASISTENCIA           | INTEGER          | Asistencia del público                 |
| SEDE                 | VARCHAR(100)     | Estadio donde se jugó el partido       |
| ARBITRO              | VARCHAR(100)     | Nombre del árbitro                     |

---

## Relaciones entre tablas

- **De la tabla JUGADOR, en al atributo EQUIPO_ID a la tabla EQUIPO, en el atributo ID_EQUIPO**
  Cada jugador pertenece a un único equipo.

- **De la tabla PARTIDO, en el atributo EQUIPO_LOCAL_ID (o equipo visitante) a la tabla EQUIPO, en el atributo ID_EQUIPO**  
  Cada partido tiene dos equipos relacionados (local y visitante).


## Modelo E-R
![Modelo Entidad-Relación](/Tarea%203/diagrama%20er.png)

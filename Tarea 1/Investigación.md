# Base de Datos: Liga MX

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
| SEMANA               | INTEGER          | Semana de la competencia               |
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

---

## Investigación sobre Sistemas Gestores de Bases de Datos (SGBD)

Un Sistema Gestor de Base de Datos (SGBD) es un software que permite crear, mantener y manipular bases de datos. Los SGBD modernos permiten el manejo eficiente de datos mediante características como control de concurrencia, integridad de datos, transacciones y recuperación ante fallos.

Existen distintos tipos de SGBD:

- **Relacionales**: Basados en tablas y relaciones (ej. MySQL, PostgreSQL, Oracle).
- **No relacionales**: Como MongoDB, que trabaja con documentos JSON.

> **Referencia**: Coronel, C., & Morris, S. (2015). *Database Systems: Design, Implementation, & Management*. Cengage Learning.

---

## Justificación del uso de PostgreSQL

PostgreSQL es un SGBD relacional de código abierto reconocido por su potencia, fiabilidad y cumplimiento del estándar SQL. Las razones por las que se elige PostgreSQL para este proyecto son:

- Compatibilidad con tipos de datos avanzados.
- Comunidad activa y documentación completa.
- Es multiplataforma y gratuito.

> PostgreSQL ha sido clasificado como uno de los SGBD más completos en informes de Stack Overflow y DB-Engines (2024).
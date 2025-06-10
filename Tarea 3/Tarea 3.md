# Modelo Entidad - Relación de la Liga MX

## Diagrama relacional

```mermaid
  erDiagram

  EQUIPO {
    SERIAL ID_EQUIPO PK
    VARCHAR NOMBRE_EQUIPO
    INTEGER PL
    NUMERIC EDAD
    INTEGER POS
    INTEGER PJ
    INTEGER TITULAR
    INTEGER MINUTOS
  }

  JUGADOR {
    SERIAL ID_JUGADOR PK
    VARCHAR NOMBRE
    VARCHAR PAIS
    VARCHAR POSC
    INTEGER EQUIPO_ID FK
    DATE NACIMIENTO
    INTEGER PJ
    INTEGER TITULAR
    INTEGER MINUTOS
    NUMERIC NOVENTAS
    INTEGER GOLES
    INTEGER ASISTENCIAS
    INTEGER GOLES_MAS_ASIST
    INTEGER PENALES
    INTEGER TARJETAS_AMARILLAS
    INTEGER TARJETAS_ROJAS
  }

  PARTIDO {
    SERIAL ID_PARTIDO PK
    INTEGER SEMANA
    VARCHAR DIA
    DATE FECHA
    TIME HORA
    INTEGER EQUIPO_LOCAL_ID FK
    NUMERIC XG
    INTEGER MARCADOR_LOCAL
    INTEGER EQUIPO_VISITANTE_ID FK
    INTEGER MARCADOR_VISITANTE
    INTEGER ASISTENCIA
    VARCHAR SEDE
    VARCHAR ARBITRO
  }

  EQUIPO ||--o{ JUGADOR : tiene
  EQUIPO ||--o{ PARTIDO : juega_como_local
  EQUIPO ||--o{ PARTIDO : juega_como_visitante
  ```

## Operaciones usando álgebra relacional

### Operación 1
Obtiene todos los jugadores que han marcado por lo menos un gol.
Álgebra relacional: σ_GOLES > 0 (JUGADOR)

### Operación 2
Obtiene los jugadores más consistentes en cuanto a tiempo jugado.
Álgebra relacional: σ_MINUTOS > 1000 (JUGADOR)

### Operación 3
Obtiene las goleadas más fuertes de local.
Álgebra relacional: σ_(MARCADOR_LOCAL - MARCADOR_VISITANTE) ≥ 3 (PARTIDO)

### Operación 4
Obtiene los jugadores con más partidos de titular.
Álgebra relacional: τ_DESC(TITULAR)(π_ID_JUGADOR, NOMBRE, EQUIPO_ID, TITULAR (JUGADOR))
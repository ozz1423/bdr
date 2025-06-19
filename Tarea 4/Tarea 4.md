# Creación de la base de datos - PostgreSQL

## Script SQL para el modelo de la [Tarea 2](/Tarea%202/Tarea%202.md)

### Creación de tablas

```sql
CREATE TABLE EQUIPO (
    ID_EQUIPO SERIAL PRIMARY KEY,
    NOMBRE_EQUIPO VARCHAR(100),
    PL INTEGER,
    EDAD NUMERIC(4,1),
    POS INTEGER,
    PJ INTEGER,
    TITULAR INTEGER,
    MINUTOS INTEGER
);

CREATE TABLE JUGADOR (
    ID_JUGADOR SERIAL PRIMARY KEY,
    NOMBRE VARCHAR(100),
    PAIS VARCHAR(50),
    POSC VARCHAR(50),
    EQUIPO_ID INTEGER REFERENCES EQUIPO(ID_EQUIPO),
    NACIMIENTO DATE,
    PJ INTEGER,
    TITULAR INTEGER,
    MINUTOS INTEGER,
    NOVENTAS NUMERIC(5,2),
    GOLES INTEGER,
    ASISTENCIAS INTEGER,
    GOLES_MAS_ASIST INTEGER,
    PENALES INTEGER,
    TARJETAS_AMARILLAS INTEGER,
    TARJETAS_ROJAS INTEGER
);

CREATE TABLE PARTIDO (
    ID_PARTIDO SERIAL PRIMARY KEY,
    SEMANA INTEGER,
    DIA VARCHAR(15),
    FECHA DATE,
    HORA TIME,
    EQUIPO_LOCAL_ID INTEGER REFERENCES EQUIPO(ID_EQUIPO),
    XG NUMERIC(4,2),
    MARCADOR_LOCAL INTEGER,
    EQUIPO_VISITANTE_ID INTEGER REFERENCES EQUIPO(ID_EQUIPO),
    MARCADOR_VISITANTE INTEGER,
    ASISTENCIA INTEGER,
    SEDE VARCHAR(100),
    ARBITRO VARCHAR(100)
);

INSERT INTO EQUIPO (NOMBRE_EQUIPO, PL, EDAD, POS, PJ, TITULAR, MINUTOS) VALUES
  ('América', 40, 26.8, 56, 34, 34, 3060),
  ('Atlas', 31, 28.1, 46, 34, 34, 3060),
  ('Atlético de San Luis', 30, 26.5, 37, 34, 34, 3060),
  ('Cruz Azul', 33, 27.5, 63, 34, 34, 3060),
  ('FC Juárez', 34, 27.4, 26, 34, 34, 3060),
  ('Guadalajara', 34, 26.8, 51, 34, 34, 3060),
  ('León', 33, 27.4, 41, 34, 34, 3060),
  ('Mazatlán FC', 31, 27.6, 36, 34, 34, 3060),
  ('Monterrey', 37, 27.4, 64, 34, 34, 3060),
  ('Necaxa', 33, 27.2, 29, 34, 34, 3060),
  ('Pachuca', 35, 25.3, 40, 34, 34, 3060),
  ('Puebla', 31, 27.6, 45, 34, 34, 3060),
  ('Pumas UNAM', 34, 26.6, 56, 34, 34, 3060),
  ('Querétaro', 35, 27.1, 39, 34, 34, 3060),
  ('Santos Laguna', 35, 25.3, 53, 34, 34, 3060),
  ('Tijuana', 31, 26.9, 37, 34, 34, 3060),
  ('Toluca', 34, 27.4, 59, 34, 34, 3060),
  ('UANL', 35, 27.4, 70, 34, 34, 3060);

INSERT INTO JUGADOR
  (NOMBRE, PAIS, POSC, EQUIPO_ID, NACIMIENTO, PJ, TITULAR, MINUTOS, NOVENTAS, GOLES, ASISTENCIAS, GOLES_MAS_ASIST, PENALES, TARJETAS_AMARILLAS, TARJETAS_ROJAS)
VALUES
  ('Saminu Abdullahi', 'NGA', 'CC', 5, '2001-01-01', 3, 0, 48, 0.50, 0, 1, 1, 0, 0, 0),
  ('José Abella', 'MEX', 'DF', 15, '1994-01-01', 17, 17, 1510, 16.80, 0, 2, 2, 0, 0, 0),
  ('José Abella', 'MEX', 'DF', 5, '1994-01-01', 11, 11, 1014, 11.30, 0, 1, 1, 0, 0, 0),
  ('Diego Abitia', 'MEX', 'DL', 3, '2003-01-01', 11, 3, 320, 3.60, 0, 0, 0, 0, 0, 0),
  ('Carlos Acevedo', 'MEX', 'PO', 15, '1996-01-01', 33, 33, 2970, 33.00, 0, 0, 0, 0, 0, 0),
  ('Alonso Aceves', 'MEX', 'DF', 11, '2001-01-01', 17, 14, 1334, 14.80, 0, 0, 0, 0, 0, 0),
  ('Gilberto Adame', 'MEX', 'DF,CC', 8, '2004-01-01', 12, 3, 417, 4.60, 0, 0, 0, 0, 0, 0),
  ('Sergio Aguayo', 'USA', 'DL', 11, '2002-01-01', 6, 0, 162, 1.80, 1, 0, 1, 1, 0, 0),
  ('Eduardo Águila', 'MEX', 'DF', 3, '2002-01-01', 31, 30, 2701, 30.00, 0, 0, 0, 0, 0, 0),
  ('Eduardo Aguirre', 'MEX', 'DL,CC', 2, '1998-01-01', 30, 25, 2195, 24.40, 8, 3, 11, 8, 0, 0),
  ('Mauro Aguirre', 'ARG', 'CC', 10, '1999-01-01', 1, 0, 13, 0.10, 0, 0, 0, 0, 0, 0),
  ('Jorge Aguirre', 'MEX', 'DL', 2, '1999-01-01', 7, 2, 178, 2.00, 0, 0, 0, 0, 1, 0),
  ('Brian Aguilar', 'MEX', 'DL', 8, '2003-01-01', 11, 2, 269, 3.00, 1, 0, 1, 0, 1, 0),
  ('Francisco Aguilar', 'MEX', 'DL', 9, '2005-01-01', 1, 0, 1, 0.00, 0, 0, 0, 0, 0, 0),
  ('Kevin Álvarez', 'MEX', 'DF', 1, '1999-01-01', 27, 19, 1753, 19.50, 1, 1, 2, 0, 3, 0),
  ('Luis Malagón', 'MEX', 'PO', 1, '1996-01-01', 30, 30, 2700, 30.00, 0, 0, 0, 0, 2, 0),
  ('Emilio Lara', 'MEX', 'DF', 1, '2002-01-01', 14, 12, 1042, 11.60, 1, 1, 2, 0, 2, 1),
  ('Israel Reyes', 'MEX', 'DF', 1, '2000-01-01', 36, 31, 2817, 31.30, 1, 1, 2, 0, 6, 0),
  ('Ramón Juárez', 'MEX', 'DF', 1, '2001-01-01', 34, 34, 3035, 33.70, 1, 1, 2, 0, 4, 0),
  ('Jesús Alberto Moreno', 'MEX', 'DL', 1, '2004-01-01', 1, 0, 8, 0.10, 0, 0, 0, 0, 0, 0);

INSERT INTO PARTIDO
  (SEMANA, DIA, FECHA, HORA, EQUIPO_LOCAL_ID, XG, MARCADOR_LOCAL, EQUIPO_VISITANTE_ID, MARCADOR_VISITANTE, ASISTENCIA, SEDE, ARBITRO)
VALUES
  (1, 'Vie', '2024-07-05', '16:45', 12, 1.50, 1, 14, 0, 8331, 'Estadio Cuauhtémoc', 'Jorge Camacho'),
  (1, 'Sáb', '2024-07-06', '17:00', 3, 1.20, 2, 1, 1, 21480, 'Estadio Alfonso Lastras Ramírez', 'Iván López'),
  (1, 'Vie', '2024-07-05', '19:00', 13, 0.80, 1, 15, 2, 9237, 'Estadio La Corregidora', 'Luis García'),
  (1, 'Vie', '2024-07-05', '21:10', 5, 1.10, 2, 2, 2, 7046, 'Estadio Olímpico Benito Juárez', 'Óscar Macías'),
  (1, 'Dom', '2024-07-07', '13:00', 18, 2.10, 4, 7, 1, 19950, 'Estadio Olímpico de Universitario', 'Maximiliano Quintero'),
  (1, 'Sáb', '2024-07-06', '19:00', 6, 1.30, 0, 16, 0, 37251, 'Estadio Akron', 'Jesús López'),
  (1, 'Sáb', '2024-07-06', '19:00', 17, 1.70, 1, 10, 0, 40371, 'Estadio Universitario de Nuevo León', 'Vicente Arce'),
  (1, 'Sáb', '2024-07-06', '21:00', 4, 2.00, 1, 8, 0, 15206, 'Estadio de la Ciudad de los Deportes', 'Karen Hernández'),
  (1, 'Dom', '2024-07-07', '19:06', 11, 0.90, 0, 9, 1, 18262, 'Estadio Hidalgo', 'Ismael López'),
  (2, 'Sáb', '2024-07-13', '17:00', 7, 0.30, 0, 11, 0, 13279, 'Estadio León', 'Salvador Pérez Villalobos');
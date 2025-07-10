import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password=""
)
cur = conn.cursor()

equipos_ids = []
for _ in range(10):
    nombre = fake.company()
    pl = random.randint(0, 38)
    edad = round(random.uniform(22, 30), 1)
    pos = random.randint(1, 20)
    pj = random.randint(0, pl)
    titular = random.randint(0, pj)
    minutos = titular * 90
    cur.execute("""
        INSERT INTO EQUIPO (NOMBRE_EQUIPO, PL, EDAD, POS, PJ, TITULAR, MINUTOS)
        VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING ID_EQUIPO
    """, (nombre, pl, edad, pos, pj, titular, minutos))
    equipos_ids.append(cur.fetchone()[0])

for _ in range(100):
    nombre = fake.name()
    pais = fake.country()
    posc = random.choice(["Delantero", "Mediocampista", "Defensa", "Portero"])
    equipo_id = random.choice(equipos_ids)
    nacimiento = fake.date_between(start_date='-35y', end_date='-18y')
    pj = random.randint(0, 38)
    titular = random.randint(0, pj)
    minutos = titular * 90
    noventas = round(minutos / 90.0, 2)
    goles = random.randint(0, 20)
    asistencias = random.randint(0, 15)
    goles_mas_asist = goles + asistencias
    penales = random.randint(0, 5)
    tarjetas_amarillas = random.randint(0, 10)
    tarjetas_rojas = random.randint(0, 2)

    cur.execute("""
        INSERT INTO JUGADOR (
            NOMBRE, PAIS, POSC, EQUIPO_ID, NACIMIENTO, PJ, TITULAR, MINUTOS, NOVENTAS,
            GOLES, ASISTENCIAS, GOLES_MAS_ASIST, PENALES, TARJETAS_AMARILLAS, TARJETAS_ROJAS
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        nombre, pais, posc, equipo_id, nacimiento, pj, titular, minutos, noventas,
        goles, asistencias, goles_mas_asist, penales, tarjetas_amarillas, tarjetas_rojas
    ))

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

for semana in range(1, 21):
    for _ in range(5):
        equipos = random.sample(equipos_ids, 2)
        dia = random.choice(dias_semana)
        fecha = datetime(2024, 8, 1) + timedelta(weeks=semana)
        hora = datetime.strptime(f"{random.randint(13, 21)}:{random.choice(['00','30'])}", "%H:%M").time()
        xg = round(random.uniform(0.5, 3.5), 2)
        marcador_local = random.randint(0, 5)
        marcador_visitante = random.randint(0, 5)
        asistencia = random.randint(5000, 80000)
        sede = fake.city()
        arbitro = fake.name()

        cur.execute("""
            INSERT INTO PARTIDO (
                SEMANA, DIA, FECHA, HORA, EQUIPO_LOCAL_ID, XG, MARCADOR_LOCAL,
                EQUIPO_VISITANTE_ID, MARCADOR_VISITANTE, ASISTENCIA, SEDE, ARBITRO
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            semana, dia, fecha.date(), hora, equipos[0], xg, marcador_local,
            equipos[1], marcador_visitante, asistencia, sede, arbitro
        ))

conn.commit()
cur.close()
conn.close()
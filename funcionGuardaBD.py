# Importando las librarías SQLite3 y Pandas.

import sqlite3
import pandas as pd
import shutil
import os

def inserta_registros(df):
  # Creando una conección a la base de datos SQLite.
  connection = sqlite3.connect(os.path.join('database','enfermedades_db.db'))

  nombre_base_datos_original = os.path.join('database','enfermedades_db.db')

  # Nombre del archivo de respaldo
  nombre_base_datos_respaldo = os.path.join('database','enfermedades_db_respaldo.db')

  # Copiando el archivo de la base de datos para crear un respaldo
  shutil.copy2(nombre_base_datos_original, nombre_base_datos_respaldo)

  # Creando un objeto Cursor para ejecutar instrucciones en SQL.
  cursor = connection.cursor()

  cursor.execute("DELETE FROM registro")
  connection.commit()

  df.to_sql('registro', connection, index=False, if_exists='replace')

  connection.close()

folder_path_data = os.path.join('data','dengue_2022.csv')
dengue_data = pd.read_csv(folder_path_data)

inserta_registros(dengue_data)
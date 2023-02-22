import pandas as pd
import sqlite3

def ff():
    file = "quran.xlsx"
    xls = pd.ExcelFile("quran.xlsx")
    df = pd.read_excel(xls, sheet_name="Sheet1")
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    for index, row in df.iterrows():
        values = (row['Gender'], row['Name'], row['Family'], row['Juz'], row['Salavat'], row['Phone'], row['Groupe'])
        c.execute('INSERT OR REPLACE INTO quran (gender, name, family, juz, salavat, phone, groupe) VALUES (?, ?, ?, ?, ?, ?, ?)', values)
    conn.commit()
    conn.close()
    return 'Data imported successfully!'

ff ()
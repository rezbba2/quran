import sqlite3


def create_table():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE quran (gender text, name text, family text, juz integer, salavat integer,Phone CHAR(11) UNIQUE ,groupe integer)''')
    c.execute("INSERT INTO quran VALUES ('Male', 'Ahmed', 'Ali', 1, 7, '01234567891',3)")
    c.execute("INSERT INTO quran VALUES ('Female', 'Fatima', 'Saeedi', 3, 5, '01112223334',3)")
    c.execute("INSERT INTO quran VALUES ('Male', 'Ali', 'Hassan', 12, 3, '01020304050',4)")
    c.execute("INSERT INTO quran VALUES ('Female', 'Zainab', 'Saleem', 17, 4, '01555555555',4)")
    c.execute("INSERT INTO quran VALUES ('Male', 'Hassan', 'Nouri', 26, 2, '01111111111',4)")
    c.execute("INSERT INTO quran VALUES ('Female', 'Maryam', 'Jalal', 6, 9, '01234567890',4)")
    c.execute("INSERT INTO quran VALUES ('Male', 'Mahdi', 'Alavi', 17, 10, '01122334455',3)")
    c.execute("INSERT INTO quran VALUES ('Female', 'Aisha', 'Khalid', 16, 1, '01987654321',5)")
    c.execute("INSERT INTO quran VALUES ('Male', 'Khalid', 'Ala', 13, 13, '01777777777',5)")
    c.execute("INSERT INTO quran VALUES ('Female', 'Nadia', 'Safi', 11, 8, '01666666666',3)")
    conn.commit()
    conn.close()

create_table()
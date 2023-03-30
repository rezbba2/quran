import sqlite3


def create_table():
    conn = sqlite3.connect('storage/mydatabase.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE quran
                 (gender text, name text, family text, juz integer, salavat integer,phone CHAR(11) UNIQUE , groupe integer)''')
    c.execute("INSERT INTO quran VALUES ('Male', 'Ahmed', 'Ali', '3', 7, '01234567891',3)")
    c.execute("INSERT INTO quran VALUES ('Female', 'Fatima', 'Saeedi', '15', 5, '01112223334',3)")
    c.execute("INSERT INTO quran VALUES ('Male', 'Ali', 'Hassan', '16', 3, '01020304050',4)")
    c.execute("INSERT INTO quran VALUES ('Female', 'Zainab', 'Saleem', '9', 4, '01555555555',3)")
    c.execute("INSERT INTO quran VALUES ('Male', 'Hassan', 'Nouri', '18', 2, '01111111111',3)")
    c.execute("INSERT INTO quran VALUES ('Female', 'Maryam', 'Jalal', '29', 9, '01234567890',4)")
    c.execute("INSERT INTO quran VALUES ('Male', 'Mahdi', 'Alavi', '24', 10, '01122334455',5)")
    c.execute("INSERT INTO quran VALUES ('Female', 'Aisha', 'Khalid', '30', 1, '01987654321',3)")
    c.execute("INSERT INTO quran VALUES ('Male', 'Khalid', 'Ala', '11', 6, '01777777777',3)")
    c.execute("INSERT INTO quran VALUES ('Female', 'Nadia', 'Safi', '6', 8, '01666666666',4)")
    conn.commit()
    conn.close()
create_table()
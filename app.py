from flask import Flask, render_template, request
import pandas as pd
import sqlite3

app = Flask(__name__, static_folder='static')


@app.route('/v')
def index_v():
    return render_template('quran/land/index.html')
def pri():
    print("ddddd")



@app.route('/')
def index():
    # Connect to the database
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    # Retrieve the unique groups from the table
    c.execute('SELECT DISTINCT groupe FROM quran ORDER BY juz DESC')
    groups = c.fetchall()

    # Close the database connection
    conn.close()

    # Render the HTML template with the groups and an empty list of rows
    return render_template('week.html', groups=groups, rows=[])
# اینو در رند اول داره ولی پس از فشردن دکمه از تابع بعدی می زنه
@app.route('/get_data', methods=['POST','GET'])
def get_data():
    # Retrieve the selected group from the dropdown
    selected_group = request.form['group']
    # Connect to the database
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    # Retrieve the rows from the table that match the selected group
    c.execute('SELECT * FROM quran WHERE groupe = ? ORDER BY juz ASC', (selected_group,))
                
    rows = c.fetchall()

    # Close the database connection
    conn.close()

    # Render the HTML template with the selected group and matching rows
    return render_template('week_view.html', groups=[], rows=rows, selected_group=selected_group)    

    
# این تابعی که در اپدیت ایجکس داره استفاده میشه    
@app.route('/update_data', methods=['POST'])
def update_data():
    juz = request.json['new_juz']
    groupe = request.json['group']
    print (juz + "  "+groupe)
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    query = f"UPDATE quran SET juz = juz + '{juz}'"
    query2 = f"UPDATE quran SET juz =  1 WHERE juz > 30"  
    
    print (query)
    c.execute(query)
    c.execute(query2)
    conn.commit()
    conn.close()
    return {'status':'success'}

    
@app.route('/get_data/group', methods=['GET'])
def get_data_group():
    conn = get_db_connection()
    cursor = conn.execute("SELECT DISTINCT groupe FROM quran")
    groups = [row['groupe'] for row in cursor.fetchall()]
    conn.close()
    return jsonify(groups)


# import sqlite data from excel file

@app.route('/import', methods=['GET'])
def index_import():
    # Render the HTML template with the groups and an empty list of rows
    return render_template('import.html')

@app.route('/import-data', methods=['POST'])
def import_data():
    file = request.files['file']
    if file.filename.endswith('.xlsx'):
        df = pd.read_excel(file, sheet_name="Sheet1")
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        for index, row in df.iterrows():
            values = (row['Gender'], row['Name'], row['Family'], row['Juz'], row['Salavat'], row['Phone'], row['Groupe'])
            c.execute('INSERT OR REPLACE INTO quran (gender, name, family, juz, salavat, phone, groupe) VALUES (?, ?, ?, ?, ?, ?, ?)', values)
        conn.commit()
        conn.close()
        return 'Data imported successfully!'
    else:
        return 'Invalid file type. Please upload an Excel file.'






# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0', port=8000)

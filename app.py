from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # Connect to the database
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    # Retrieve the unique groups from the table
    c.execute('SELECT DISTINCT groupe FROM quran ORDER BY chapter DESC')
    groups = c.fetchall()

    # Close the database connection
    conn.close()

    # Render the HTML template with the groups and an empty list of rows
    return render_template('week.html', groups=groups, rows=[])

@app.route('/get_data', methods=['POST','GET'])
def get_data():
    # Retrieve the selected group from the dropdown
    selected_group = request.form['group']

    # Connect to the database
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()

    # Retrieve the rows from the table that match the selected group
    c.execute('SELECT * FROM quran WHERE groupe = ? ORDER BY chapter DESC', (selected_group,))
    # c.execute('SELECT * FROM quran WHERE groupe = ?  ORDER BY chapter DESC', (selected_group,))               
    rows = c.fetchall()

    # Close the database connection
    conn.close()

    # Render the HTML template with the selected group and matching rows
    return render_template('week_view.html', groups=[], rows=rows, selected_group=selected_group)    

    
    
@app.route('/update_data', methods=['POST'])
def update_data():
    chapter = request.json['chapter']
    groupe = request.json['group']
    print (chapter + "  "+groupe)
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    query = f"UPDATE quran SET chapter = chapter + '{chapter}'"
    query2 = f"UPDATE quran SET chapter =  1 WHERE chapter > 30"  
    
    print (query)
    c.execute(query)
    c.execute(query2)
    conn.commit()
    conn.close()
    return 'Success'

    
@app.route('/get_data/group', methods=['GET'])
def get_data_group():
    conn = get_db_connection()
    cursor = conn.execute("SELECT DISTINCT groupe FROM quran")
    groups = [row['groupe'] for row in cursor.fetchall()]
    conn.close()
    return jsonify(groups)

if __name__ == '__main__':
    app.run(debug=True)

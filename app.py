from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

try:
    conn = psycopg2.connect(
        dbname="whizz75_nzgk",
        user="whizz75_nzgk_user",
        password="0ycwbcpqtmMOd4Qw3p3px0YANWZy5GM1",
        host="dpg-cvrru42li9vc739n4140-a",
        port="5432",
        sslmode="require"
    )
except Exception as e:
    print("Database connection failed:", e)

@app.route('/api/records')
def getData():
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM financialRecords;")
        rows = cur.fetchall()
        cur.close()

        print("Fetched rows:", rows)

if __name__ == '__main__':
    app.run(debug=True)

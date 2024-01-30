# api.py

from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Ganti dengan informasi koneksi PostgreSQL Anda
db_params = {
    'dbname': 'mbkm',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost',
    'port': '5432',
}

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        # Membuat koneksi ke database
        connection = psycopg2.connect(**db_params)

        # Membuat kursor
        cursor = connection.cursor()

        # Mendapatkan hasil query
        results = cursor.fetchall()

        # Menutup kursor dan koneksi
        cursor.close()
        connection.close()

        # Mengirimkan hasil sebagai JSON
        return jsonify({'data': results})

    except psycopg2.Error as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=8080)
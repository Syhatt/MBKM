import psycopg2

# Ganti parameter koneksi sesuai dengan konfigurasi PostgreSQL Anda
db_params = {
    'dbname': 'mbkm',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost',
    'port': '5432',
}

try:
    # Membuat koneksi ke database
    connection = psycopg2.connect(**db_params)

    # Membuat kursor
    cursor = connection.cursor()

    # Melakukan commit untuk menyimpan perubahan
    connection.commit()

except psycopg2.Error as e:
    print(f"Error: {e}")

finally:
    # Menutup kursor dan koneksi
    cursor.close()
    connection.close()
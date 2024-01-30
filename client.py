# client.py

import requests

api_url = 'http://127.0.0.1:8080/get_data'  # Ganti dengan URL API Anda

try:
    # Mengirimkan permintaan GET ke API
    response = requests.get(api_url)

    # Mendapatkan hasil respons sebagai JSON
    data = response.json()

    # Menampilkan hasil
    print(data)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
<?php
$host = 'localhost';
$dbname = 'mbkm';
$user = '1234';
$password = '1234';
$port = "5432";

$conn = pg_connect("host=$host dbname=$dbname user=$user password=$password");

if (!$conn) {
    echo "Koneksi gagal.\n";
    die();
} else {
    echo "Koneksi berhasil.\n";
}

// Lakukan operasi database di sini

// Tutup koneksi
pg_close($conn);
?>
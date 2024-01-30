<?php
$host = 'db'; // Gunakan nama layanan yang didefinisikan di dalam Docker Compose
$port = 5432; // Port default PostgreSQL
$dbname = "mbkm"; // Nama basis data
$user = "postgres"; // Nama pengguna
$password = "1234"; // Kata sandi

try {
    $conn = new PDO("pgsql:host=$host;port=$port;dbname=$dbname;user=$user;password=$password");
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Koneksi sukses!";
} catch (PDOException $e) {
    echo "Koneksi gagal: " . $e->getMessage();
}
?>

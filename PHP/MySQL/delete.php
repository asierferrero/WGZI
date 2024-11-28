<?php
// Erroreak erakusteko
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$conn = new mysqli("localhost", "root", "Admin123", "php");

if ($conn->connect_errno) {
    die("Errorea: (" . $conn->connect_errno . ") " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['delete'])) {
    $delete = $_POST['delete'];

    $placeholders = implode(',', array_fill(0, count($delete), '?'));
    $query = "DELETE FROM eraikuntza WHERE id IN ($placeholders)";

    if ($stmt = $conn->prepare($query)) {
        $stmt->bind_param(str_repeat('i', count($delete)), ...$delete);

        if ($stmt->execute()) {
            echo "Etxebizitzak ezabatu dira.";
        } else {
            echo "Errorea etxebizitzak ezabatzerako orduan: " . $stmt->error;
        }

        $stmt->close();
    } else {
        echo "Errorea kontsulta prestatzerakoan: " . $conn->error;
    }
} else {
    echo "Ez da etxebizitzarik aukeratu ezabatzeko.";
}

$conn->close();

header("Location: index.php");
exit();
?>

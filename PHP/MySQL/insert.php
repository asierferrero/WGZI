<?php
// Erroreak erakusteko
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$conn = new mysqli("localhost", "root", "Admin123", "php");

if ($conn->connect_errno) {
    die("Error: (" . $conn->connect_errno . ") " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $mota = $_POST['mota'];
    $zonaldea = $_POST['zonaldea'];
    $helbidea = $_POST['helbidea'];
    $logelak = $_POST['logelak'];
    $prezioa = $_POST['prezioa'];
    $tamaina = $_POST['tamaina'];
    $extrak = isset($_POST['extrak']) ? implode(', ', $_POST['extrak']) : '';
    $oharrak = $_POST['oharrak'];

    $irudia = '';
    if (isset($_FILES['irudia']) && $_FILES['irudia']['error'] == 0) {
        $irudia = basename($_FILES['irudia']['name']);
        move_uploaded_file($_FILES['irudia']['tmp_name'], $irudia);
    }

    $valid_extraks = ['Igerilekua', 'Lorategia', 'Garajea'];
    $extrak = isset($_POST['extrak']) ? array_intersect($_POST['extrak'], $valid_extraks) : [];
    $extrak = implode(',', $extrak);

    $query = "INSERT INTO eraikuntza (mota, zonaldea, helbidea, logelak, prezioa, tamaina, extrak, irudia, oharrak) 
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)";
    $stmt = $conn->prepare($query);

    $stmt->bind_param("ssssddsss", $mota, $zonaldea, $helbidea, $logelak, $prezioa, $tamaina, $extrak, $irudia, $oharrak);

    if ($stmt->execute()) {
        header("Location: index.php");
        exit();
    } else {
        echo "Errorea: " . $stmt->error;
    }

    $stmt->close();

} else {
    echo "Errorea etxebizitza sartzerako orduan: " . $conn->error;
}


$conn->close();
?>
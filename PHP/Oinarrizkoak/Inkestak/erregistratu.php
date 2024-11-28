<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['aukeratu'])) {
    $vote = $_POST['aukeratu'];

    $file = "aukerak.json";

    if (!file_exists($file)) {
        $data = ["bai" => 0, "ez" => 0];
    } else {
        $data = json_decode(file_get_contents($file), true);
    }

    if (isset($data[$vote])) {
        $data[$vote]++;
    }

    if (file_put_contents($file, json_encode($data, JSON_PRETTY_PRINT)) === false) {
        echo "Error al guardar el archivo JSON";
        exit;
    }

    $_SESSION['aukeratuak'] = true;

    header("Location: konfirmatu.php");
    exit;
} else {
    header("Location: index.php");
    exit;
}
?>

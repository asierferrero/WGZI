<html>

<body>
    <h1>Fitxategiak igo. Formularioaren emaitza</h1>

    <?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $izenburua = $_POST['izenburua'] ?? '';
        $testua = $_POST['testua'] ?? '';
        $modua = $_POST['modua'] ?? 'Eskaintzak';
        $fitxategia = $_FILES['fitxategia'] ?? null;

        if (empty($izenburua) || empty($testua)) {
            die("Errorea: Izenburua eta testua derrigorrezkoak dira.");
        }

        $fitxategiaIzena = "Ez dago irudirik";

        if ($fitxategia && $fitxategia['error'] === UPLOAD_ERR_OK) {
            $fitxategiaIzena = basename($fitxategia['name']);
        }

        echo "<ul>";
        echo "<li>Izenburua: " . htmlspecialchars($izenburua) . "</li>";
        echo "<li>Testua: " . htmlspecialchars($testua) . "</li>";
        echo "<li>Modua: " . htmlspecialchars($modua) . "</li>";

        if ($fitxategia && $fitxategia['error'] === UPLOAD_ERR_OK) {
            echo "<li>Irudia: <a href='uploads/" . htmlspecialchars($fitxategiaIzena) . "' download>" . htmlspecialchars($fitxategiaIzena) . "</a></li>";
        } else {
            echo "<li>Irudia: Ez dago irudirik</li>";
        }

        echo "</ul>";
        echo '<br><a href="index.php">[ Beste berri bat gehitu ]</a>';
    } else {
        die("Errorea: Metodo okerra.");
    }
    ?>
</body>

</html>

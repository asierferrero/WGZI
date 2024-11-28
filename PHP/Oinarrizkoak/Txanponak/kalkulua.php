<html>

<body>
    <h1>Irudiaren azalera</h1>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $kantitatea = $_POST['kantitatea'];
        $dirua = $_POST['dirua'];
        if ($kantitatea != '') {
            if ($dirua == "dolar") {
                $bihurketa = $kantitatea * 1.08;
                echo "<p>$kantitatea euro $bihurketa $dirua dira.</p>";
            } elseif ($dirua == "libera") {
                $bihurketa = $kantitatea * 0.83;
                echo "<p>$kantitatea euro $bihurketa $dirua dira.</p>";
            } elseif ($dirua == "yen") {
                $bihurketa = $kantitatea * 164.3;
                echo "<p>$kantitatea euro $bihurketa $dirua dira.</p>";
            } elseif ($dirua == "franko") {
                $bihurketa = $kantitatea * 0.94;
                echo "<p>$kantitatea euro $bihurketa $dirua dira.</p>";
            }
        }
        echo '<a href="index.php">Itzuli</a>';

    } else {
        echo "<p>Ez da daturik bidali.</p>";
        echo '<a href="index.php">Itzuli</a>';
    }
    ?>
</body>

</html>
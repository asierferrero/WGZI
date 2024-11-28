<html>

<body>
    <h1>Irudiaren azalera</h1>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $aldea = $_POST['aldea'];
        $irudia = $_POST['irudia'];
        if ($aldea != '') {
            if ($irudia == "karratua") {
                $azalera = $aldea * $aldea;
                echo "<p>$aldea-ko aldea daukan karratu baten azalera $azalera da.</p>";
            } elseif ($irudia == "zirkulua") {
                $azalera = pi() * ($aldea * $aldea);
                echo "<p>$aldea-ko erradioa daukan zirkulu baten azalera " . round($azalera, 2) . " da.</p>";
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
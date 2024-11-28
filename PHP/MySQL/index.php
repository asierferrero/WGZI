<?php
$conn = new mysqli("localhost", "root", "Admin123", "php");

if ($conn->connect_errno) {
    die("Errorea: (" . $conn->connect_errno . ") " . $conn->connect_error);
}

$query = "SELECT * FROM eraikuntza";
$result = $conn->query($query);

if (!$result) {
    die("Errorea kontsultan: " . $conn->error);
}

$conn->close();
?>

<html>

<head>
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <h1>Etxebizitzen Kontsultak</h1>
    <form action="delete.php" method="POST">
        <table>
            <thead>
                <tr>
                    <th>Mota</th>
                    <th>Zonaldea</th>
                    <th>Logelak</th>
                    <th>Prezioa (€)</th>
                    <th>Tamaina (m²)</th>
                    <th>Extrak</th>
                    <th>Irudia</th>
                    <th>Oharrak</th>
                    <th>Ezabatu</th>
                </tr>
            </thead>
            <tbody>
                <?php
                if ($result->num_rows > 0) {
                    while ($row = $result->fetch_assoc()) {
                        echo "<tr>";
                        echo "<td>" . $row["mota"] . "</td>";
                        echo "<td>" . $row["zonaldea"] . "</td>";
                        echo "<td>" . $row["logelak"] . "</td>";
                        echo "<td>" . $row["prezioa"] . "</td>";
                        echo "<td>" . $row["tamaina"] . "</td>";
                        echo "<td>" . $row["extrak"] . "</td>";
                        if (!empty($row["irudia"])) {
                            echo "<td><a href='" . $row["irudia"] . "'>Irudia ikusi</a></td>";
                        } else {
                            echo "<td></td>";
                        }
                        echo "<td>" . $row["oharrak"] . "</td>";
                        echo "<td><input type='checkbox' name='delete[]' value='" . $row["id"] . "'></td>";
                    }
                } else {
                    echo "<tr><td colspan='10'>Ez dago emaitzarik.</td></tr>";
                }
                ?>
            </tbody>
        </table><br>
        <button type="submit">Etxebizitza/k ezabatu</button><br><br>
    </form>
    <a href="form.php">[ Beste berri bat gehitu ]</a>
</body>

</html>
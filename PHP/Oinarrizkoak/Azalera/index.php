<html>

<body>
    <h1>Irudien azalera kalkulatu</h1>
    <form action="kalkulua.php" method="post">
        <label for="aldea">Aldea/Erradioa:</label>
        <input type="number" id="aldea" name="aldea" step="any">
        <br><br>
        <label for="irudia">Irudia:</label>
        <select id="irudia" name="irudia" required>
            <option value="karratua">Karratua</option>
            <option value="zirkulua">Zirkulua</option>
        </select>
        <br><br>
        <button type="submit">Kalkulatu</button>
    </form>
</body>

</html>
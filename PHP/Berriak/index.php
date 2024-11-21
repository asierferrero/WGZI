<html>

<body>
    <h1>Fitxategiak igo</h1>
    <form action="erantzuna.php" method="POST">
        <label for="izenburua">Izenburua*:</label>
        <input type="text" name="izenburua" id="izenburua" required><br><br>

        <label for="testua">Testua*:</label>
        <textarea name="testua" id="testua" required></textarea><br><br>

        <label for="mota">Mota:</label>
        <select name="mota" id="mota">
            <option value="Eskaintzak">Eskaintzak</option>
        </select><br><br>

        <label for="fitxategia">Irudia:</label>
        <input type="file" name="fitxategia" id="fitxategia" accept="image/*"><br><br>

        <button type="submit">Bidali</button>
    </form>
</body>
</html>
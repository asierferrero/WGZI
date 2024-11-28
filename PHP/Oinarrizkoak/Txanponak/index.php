<html>

<body>
    <h1>Txanpon bihurgailua</h1>
    <form action="kalkulua.php" method="post">
        <label for="kantitatea">Euro kantitatea:</label>
        <input type="number" id="kantitatea" name="kantitatea" step="any">
        <br><br>
        <select id="dirua" name="dirua" required>
            <option value="dolar">AEBetako dolar</option>
            <option value="libera">Libera britaniar</option>
            <option value="yen">Yen japoniar</option>
            <option value="franko">Franko suitzar</option>
        </select>
        <br><br>
        <button type="submit">Kalkulatu</button>
    </form>
</body>

</html>
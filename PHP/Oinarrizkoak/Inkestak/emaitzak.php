<?php
$file = "aukerak.json";
$data = ["bai" => 0, "ez" => 0];

if (file_exists($file)) {
    $data = json_decode(file_get_contents($file), true);
}

$totalVotes = $data["bai"] + $data["ez"];
$baiPercent = $totalVotes > 0 ? ($data["bai"] / $totalVotes) * 100 : 0;
$ezPercent = $totalVotes > 0 ? ($data["ez"] / $totalVotes) * 100 : 0;
?>

<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>Inkesta. Inkestaren emaitzak.</h1>
    <div style="width: 300px; height: 300px;">
        <canvas id="resultsChart"></canvas>
    </div>
    <script>
        const ctx = document.getElementById('resultsChart').getContext('2d');
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Bai', 'Ez'],
                datasets: [{
                    data: [<?= $baiPercent ?>, <?= $ezPercent ?>],
                    backgroundColor: ['#4caf50', '#f44336'],
                }]
            }
        });
    </script>
    <p>Jasotako bozkak guztira: <?= $totalVotes ?></p>
    <a href="index.php">[ Bueltatu bozkatzeko orrira ]</a>
</body>
</html>


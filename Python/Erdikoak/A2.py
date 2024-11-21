def hiriak_ordenatzen(hiriak):
    # 200.000 pertsona baino gehiago dituzten hiriak gehitu
    hiriak_filtratuak = {}
    for hiri, populazioa in hiriak.items():
        if populazioa > 200000:
            hiriak_filtratuak[hiri] = populazioa

    # Hiriak populazioaren arabera handienetik txikienera ordenatu
    hiriak_ordenatuak = sorted(hiriak_filtratuak, key=hiriak_filtratuak.get, reverse=True)

    return hiriak_ordenatuak

hiriak = {
    "Gasteiz": 250000,
    "Donostia": 190000,
    "Bilbo": 350000,
    "Eibar": 27000
}

emaitza = hiriak_ordenatzen(hiriak)
print(emaitza)

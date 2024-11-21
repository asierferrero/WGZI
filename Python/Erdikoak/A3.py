def gehiengo_absolutua(botoak):
    # Boto guztien gehiketa
    botoakGuztira = sum(botoak.values())

    # Gehiengo absolutua botoen erdia
    absolutua = botoakGuztira / 2

    for alderdia, boto in botoak.items():
        if boto > absolutua:
            return f"{alderdia} irabazlea da."
    return "Inork ez dauka gehiengo absoluturik."

botoak = {
    "THL": 23,
    "DEW": 65,
    "PLO": 23
}

print(gehiengo_absolutua(botoak))
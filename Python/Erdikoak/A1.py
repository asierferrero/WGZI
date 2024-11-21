# Hitzak ordenatzeko eta emaitza erakusteko programa

testua = input("Sartu testu bat: ")

# Testua banandu
hitzak = testua.split()

# Letra larriz jarri
hitzak_unique = sorted(set([hitz.upper() for hitz in hitzak]))

print("Emaitza:", " ".join(hitzak_unique))
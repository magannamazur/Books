# nested
nested = ["pierwszy", ("drugi", "trzeci"), ["czwarty", "piąty", "szósty"]] # 3 elementy
print(nested)

# dostęp poprzez indeksy
scores = [("Muniek", 1000), ("Lilka", 1500), ("Kajtek", 3000)]
print(scores[0])
print(scores[1])
print(scores[2])

# dostęp do dokladnego elementu:
# 1 index
print(scores[2][0])
# 2 przypisanie krotki
a_score = scores[2]
print(a_score[0])

# rozpakowywanie
name, score = ("Szymek", 175)
print(name, score)
#Vytvorte skrip, ktery mi bude hodnotit pravdivost jednotlivych promennych.
#Vytvorte slovnik, který bude mít jako klíč pozici prvku a jako hodnoty bude mít tuple(prvek,pravdivost)
#{0: (6,True)}


# zadání a)
list_promennych =  [6,"text", "", [], {6,7,8}, dict(), True]

vyskyt_pravdivosti = dict()
for i, object in enumerate(list_promennych):
    vyskyt_pravdivosti.setdefault(i, (object, bool(object)))

print(vyskyt_pravdivosti)


# zadání b)
list_promennych =  '[6,"text", "", [], {6,7,8}, dict(), True]'
# upraveny_list_promennych = list_promennych.strip('][').split(',')
upraveny_list_promennych = eval(list_promennych)

vyskyt_pravdivosti = dict()
for i, object in enumerate(upraveny_list_promennych):
    vyskyt_pravdivosti.setdefault(i, (object, bool(object)))

print(vyskyt_pravdivosti)

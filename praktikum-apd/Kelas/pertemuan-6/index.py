# Biodata = {
# print(f"nama saya adalah {Biodata['Nama']}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get["Nama"]}")
# print(Biodata.get("Nama"))
# }

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})
# #Setelah Ditambah
# print(Film)
# #Sebelum Ditambah
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery',
# 'The Conjuring': 'Horror'}
# #Setelah Ditambah
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery',
# 'The Conjuring': 'Horror', 'Zombieland': 'Comedy', 'Hours':
# 'Thriller'}

Musik = {
    "The Chainsmoker": ["All we Know", "The Paris"],
    "Alan Walker": ["Alone", "Lily"],
    "Neffex": ["Best of Me",['tes','halo'], "Memories"],
    'Paramore' : ["Misery Business", "Ain't It Fun", 
                ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
}

print(Musik['Paramore'][2][1][1])
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "LOSER":"Se refiere a alguien o algo que perdidio en alguna cosa"
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(meme_dict[word])
else:
    print("Esa Palabra no se encuentra en nuestro diccionario")
    # ¿Qué hacer si no se encuentra la palabra?

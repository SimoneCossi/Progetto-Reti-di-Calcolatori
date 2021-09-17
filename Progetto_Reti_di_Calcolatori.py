import Instagram

# nel caso in cui l'utente digiti 1 viene chiesto all'utente di inserire un username di cui effettuare la ricerca
def opzioneUno():
    
    account = input("\n\tInserire il nome utente di instagram dell'account di cui si vogliono visualizzare i dati:\n\t")
    print("\tACCOUNT:\t"+account.replace(" ", ""))
    instagram = Instagram.Instagram(account)
    instagram = instagram.PrendiDati()
    
# nel caso in cui l'utente digiti 2 viene chiesto di inserire un tag di cui si effettuera' la ricerca
def opzioneDue():
    
    hashtag = input("\n\tInserire l'hashtag di cui si vogliono vedere i post:\n\t")
    print("\tHASHTAG:\t"+hashtag.replace(" ", ""))
    instagram = Instagram.Instagram(hashtag)
    instagram = instagram.HashTag()



print("\t########################################################################################################")
print("\tTool che effettua lo scraping dati da instagram tramite instagram.com")
print("\t########################################################################################################")
print("\n\n\n")

# variabile di controllo per il programma principale
res = "s"

# Programma Principale
while (res != "n"):
    
    print("\tCosa si desidera effettuare?")
    print("\t1) Ricercare le iformazioni base di un account")
    print("\t2) Ricercare tutti i post di un hashtag")
    print("\n")

    #validazione input
    n = input("\t")
    if n.isdecimal():
        if int(n) == 1:
            opzioneUno()
         
        elif int(n) == 2:
            opzioneDue()

        else:
         print("\n\tSONO AMMESSI SOLO I VALORI '1' E '2'")

    else:
         print("\n\tSONO AMMESSI SOLO I VALORI '1' E '2'")
    
    res = input("\n\n\n\tVuoi continuare? [s/n]\t")


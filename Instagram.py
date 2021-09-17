import http.client
import json

class Instagram(object):
# CHIAVE PER LE API    
#76bdd04ce3mshc552f063f4ce6fdp15c528jsn2c6b337fcc9b

        def __init__(self, search):
            self.hashtag = search
            self.account = search
        
        # Metodo che legge alcune informazioni tramite username e le stampa a video su console
        def PrendiDati(self):

            # Connessione a Instagram API
            conn = http.client.HTTPSConnection("instagram40.p.rapidapi.com")
        

            headers = {
                'x-rapidapi-host': "instagram40.p.rapidapi.com",
                'x-rapidapi-key': "76bdd04ce3mshc552f063f4ce6fdp15c528jsn2c6b337fcc9b"
                }

            conn.request("GET", "/account-info?username="+self.account.replace(" ", "")+"&wrap=0", headers=headers)

            res = conn.getresponse()
            data = res.read()            

            # Carico la risposta API in un oggetto python, codificato come una stringa utf-8
            json_dictionary = json.loads(data.decode("utf-8"))
        
            # PRINT MOLTO IMPORTANTE
            # SE IL PROGRAMMA DOVESSE DARE ERRORI DURANTE L'ESACUZIONE DI QUESTA PARTE TOGLIERE IL CANCELLETTO DALLA PRINT E OSSERVARE SE È STATO RAGGIUNTO
            # IL LIMITE DI RICHIESTE MENSILE.
            #print(json_dictionary)


            ############ da controllare ma lavorare sulla seonda funzione ( non esaurire i tentativi qui
            try:
                # Prendo le informazioni desiderate, le memorizzo in delle variabili e le stampo a video tramite console
                fullname = json_dictionary['full_name']
                print("\n\n\tNome completo\n\n",fullname)
            
                biography = json_dictionary['biography']
                print("\n\n\tBio\n\n",biography)

                followers = json_dictionary['edge_followed_by']['count']
                print("\n\n\tNr di Followers\n\n",followers)

                following = json_dictionary['edge_follow']['count']
                print("\n\n\tNr di persone/pagine seguite\n\n",following)

                profile_pic = json_dictionary['profile_pic_url_hd']
                print("\n\n\tLink per l'immagine di profilo\n\n",profile_pic)

            except:
                print("!!! NOME UTENTE NON TROVATO !!!")


        # Metodo che ricerca tutti i post tramite hashtag e genera un file HTML con tutti i post con lo stesso hashtag
        def HashTag(self):
       

            #Connessione a Instagram API
            conn = http.client.HTTPSConnection("instagramdimashirokovv1.p.rapidapi.com")

            headers = {
                'x-rapidapi-host': "InstagramdimashirokovV1.p.rapidapi.com",
                'x-rapidapi-key': "76bdd04ce3mshc552f063f4ce6fdp15c528jsn2c6b337fcc9b"
                }

            conn.request("GET", "/tag/"+self.hashtag.replace(" ", "")+"/optional", headers=headers)

            res = conn.getresponse()
            data = res.read()

            # Carico la risposta API in un oggetto python, codificato come una stringa utf-8
            json_dictionary = json.loads(data.decode("utf-8"))
            
            # PRINT MOLTO IMPORTANTE
            # SE IL PROGRAMMA DOVESSE DARE ERRORI DURANTE L'ESACUZIONE DI QUESTA PARTE TOGLIERE IL CANCELLETTO DALLA PRINT E OSSERVARE SE È STATO RAGGIUNTO
            # IL LIMITE DI RICHIESTE GIORNAGLIERE.
            #print(json_dictionary)
            
            
            # Preparazione dell'HTML 
            # Utilizzo del meta charset per riuscire a visualizzare correttamente le emoji
            #outputHTML = "<html><head><meta charset='utf-8'><style>.instagram-wrapper{display:grid;grid-template-columns: 300px 300px 300px;post-wrapper{padding:10px;}.post-wrapper img {max-width:180px;}.post-likes{font-weight:bold;}</style></head><body><div class='instagram-wrapper'>"
            outputHTML = "<html><head><meta charset='utf-8'><style>.instagram-wrapper{display:grid;grid-template-columns: 33% 34% 33%;post-wrapper{padding:10px;}.post-wrapper img {max-width:180px;}.post-likes{font-weight:bold;}</style></head><body><div class='instagram-wrapper'>"
            # Il file generato andra'salvato in questo file (nella directory locale)
            outputFile = "instagram.html"
            

            
            try:
                # Loop per andare a trovare tutti i post
                for item in json_dictionary['edges']:

                    # Prendo la descrizione, l'immagine, e il numero di like di ogni post e li salvo in delle variabili
               
                    descrizione = item['node']['edge_media_to_caption']['edges'][0]['node']['text']
                
                    URL = item['node']['display_url']

                    likes = item['node']['edge_liked_by']['count']

                    # Viene aggiunta una sezione(post) per ogni ciclo del loop
                    outputHTML+='<div class="post-wrapper"><img src="'+str(URL)+'" /><div class="post-caption">'+str(descrizione)+'</div><div class="post-likes">'+str(likes)+' likes</div></div>'
                    
                # Chiusura dell'HTML
                outputHTML+='</div></body></html>'
    
                #Inserisco l'HTML generato all'interno del file
                with open(outputFile, "w", encoding="utf-8") as f:
                    f.write(outputHTML)

                print("\n\tFile creato...\nControllare il file\n")\

            except:
                print('#HashTag non trovato')
                print('\noppure\n')
                print('Numero di richieste giornaliero esaurito')


            
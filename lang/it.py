# it.py
#Italian

encrypt1 = 'Chiave di cifratura in corso...'

config1 = "Il file di configurazione esiste: "
config2 = "Aggiorna file esistente: "
config3 = "La cartella esiste gia: "
config4 = "Controlla gli aggiornamenti? [Y/n]: ⤷ "
config5 = "Modificare la configurazione? [Y/n]: ⤷ "
config6 = "Cosa vuoi cambiare? ⤷ "
config7 = "Creazione cartella: "
config8 = "La cartella esiste già: "

configOption1 = "[1] Controlla aggiornamenti: " 
configOption2 = "[2] Mostra suggerimenti: " 
configOption3 = "[3] Percorso di download del sito: "
configOption4 = "[4] Browser: " 
configOption5 = "[5] Lingua: "
configOptionA = "[A] Ripulisci Alfred. (In questo modo vengono rimossi i file temporanei)"
configOptionB = "[B] Strumenti per sviluppatori."

configOption1Message = "Ok! [verificareaggiornamenti] È impostato per Sì. Passando a No"
configOption2Message = "Ok! [suggerimenti] È impostato per Sì. Passando a No"
configOption3Message = "Nuovo percorso: ⤷ "
configOption4Message = """Tipi supportati:
                         Firefox
                         Edge
                         Chrome
                         """
configOption5Message = """
            Inserisci il codice della tua lingua
            Lingua supportata:
                it = italiano
                en = Inglese
                         """
configOptionAMessage = "Fatto!"
configOptionBMessage = "Benvenuto nel menu sviluppatore!"

configOption1Message2 = "Va bene! [verificareaggiornamenti] È impostato per No. Passando a Sì"
configOption2Message2 = "Ok! [suggerimenti] È impostato per No. Passando a Sì"
configOptionBMessage2 = "NON dare le seguenti chiavi a nessuno se non a uno sviluppatore Alfred."
configOptionBMessage3 = "chiave privata: "
configOptionBMessage4 = "syscrypt: "

target = "Obiettivo del: ⤷ "
browser = "Browser: "

file_not_found = "File not found: {filename}"
permission_denied = "Permission denied for {operation} on {path}"

note = 'Nota! '
path = "PERCORSO: ⤷ "
warning1 = "Molti siti non consentono di scaricare i file del sito. Utilizzare a proprio rischio e pericolo."
warning2 = " L'utilizzo del webscraper è piuttosto lento."
warning3 = " Questo è il tuo primo lancio :D Potrebbe essere necessario riavviare Alfred per utilizzare tutti i moduli"
warning4 = " Stai usando un Prerelease di Alfred!"

confirm1 = "Vuoi scaricare immagini/video? [Y/n] ⤷ "
confirm2 = "Eseguire di nuovo?: [Y/n] ⤷ "

prompt1 = "Entra di nuovo nel sito: ⤷ "
prompt2 = "Si prega di segnalare eventuali bug o errori al nostro repository o server Discord. "
prompt3 = "È possibile disabilitare l'aggiornamento nel file di configurazione"
prompt4 = "Unisciti al nostro Discord: https://discord.gg/xrdjxyuSQt "
prompt5 = "Ok! Ill chiedere più tardi...."

download1 = "Scaricare "
updates = "Gli aggiornamenti sono abilitati!"


idk1 = "Non sono sicuro di cosa volessi dire..."
idk2 = "Non sono sicuro di quello che hai in mente. Chiederò più tardi" 

scan1 = "Ricerca di siti con:"

status1 = "Funzionante...."
status2 = "Creazione/sovrascrittura del file di salvataggio."
status3 = "Reinstallazione in corso............"

save1 = "Risultati salvati in"

error1 = "Errore di autorizzazione"
error2 = "Tipo Errore"
error3 = "Non riesco a trovare il file di salvataggio!"
error4 = "La directory non esiste."
error5 = "Impossibile trovare i file necessari. Tentativo di reinstallare Alfred"

fileshare1 = "[*] Ascolto come "
# example bc imma forget
# import messages

# print(messages.title)  # Output: Hello, World!
# print(messages.text1)  # Output: This is a sample message.

# # Example of using placeholders in messages
# filename = "example.txt"
# print(messages.file_not_found.format(filename=filename))
import csv
def carica_da_file(file_path):
    """Carica le foto dal file, creando un nuovo anno ogni volta che compare per la prima volta"""
    # TODO
    album = {}
    try:
        with open(file_path, "r",newline='',encoding='utf-8') as file:
            f=csv.reader(file)
            next(f)
            for riga in f:
                if not riga:
                    continue
                codice = riga[0].strip()
                titolo = riga[1].strip()
                autore = riga[2].strip()
                mese = riga[3].strip()
                anno = riga[4].strip()
                if anno not in album:
                    album[anno]=[]
                elem={'codice':codice,'titolo':titolo,'autore':autore,'mese':mese}
                album[anno].append(elem)
    except FileNotFoundError:
        print(f'file {file_path} non trovato')
        return None

    return album


def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
    """Aggiunge una foto all'album, creando l'anno al volo se non è ancora presente"""
    # TODO
    if not (1<=int(mese)<=12):
        return None
    for anno1,foto in album.items():
        for f in foto:
            if f['codice']==codice:
                return None #codice già esiste
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"\n{codice},{titolo},{autore},{mese},{anno}")
    except FileNotFoundError:
        return None

    anno_str=str(anno)
    if anno_str not in album:
        album[anno_str]=[]
    nuova={
        'codice':codice,
        'titolo':titolo,
        'autore':autore,
        'mese':str(mese)
    }
    album[anno_str].append(nuova)
    return nuova


def cerca_foto(album, codice):
    """Cerca una foto nell'album dato il codice"""
    # TODO
    for anno1,foto in album.items():
        for f in foto:
            if codice==f['codice']:
                return f"{codice},{f['titolo']},{f['autore']},{f['mese']},{anno1}"

    return None

def elenco_foto_anno_per_titolo(album, anno):
    """Ordina i titoli delle foto di un dato anno in ordine alfabetico"""
    # TODO
    anno_str=str(anno)
    if anno_str not in album:
        return None
    titoli=[]
    for anno1,foto in album.items():
        if anno1==anno_str:
            for f in foto:
                titoli.append(f['titolo'])
    return sorted(titoli)





def main():
    album = []
    file_path = "album_fotografico.csv"

    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)
                if album is not None:
                    break

        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue

            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue

            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")

        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            risultato = cerca_foto(album, codice)
            if risultato:
                print(f"Foto trovata: {risultato}")
            else:
                print("Foto non trovata.")

        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_foto_anno_per_titolo(album, anno)
            if titoli is not None:
                print(f'\nFoto del {anno}:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print(f"Nessuna foto trovata per l'anno {anno}.")

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()


import os
import requests
import zipfile
from io import BytesIO

# URL del file ZIP
url = "https://www.kaggle.com/api/v1/datasets/download/diishasiing/revenue-for-cab-drivers/"

# Directory di destinazione per il CSV
save_dir = "data"

# Crea la directory se non esiste
os.makedirs(save_dir, exist_ok=True)

# Scarica il file ZIP in memoria
print(f"Scaricamento da: {url}")
response = requests.get(url)

if response.status_code == 200:
    # Apre lo ZIP in memoria
    with zipfile.ZipFile(BytesIO(response.content)) as z:
        # Estrai solo i file CSV
        csv_files = [f for f in z.namelist() if f.endswith(".csv")]
        if not csv_files:
            print("Nessun file CSV trovato nello ZIP.")
        else:
            for csv_file in csv_files:
                print(f"Estrazione di: {csv_file}")
                z.extract(csv_file, path=save_dir)
                print(f"File CSV salvato in: {os.path.join(save_dir, csv_file)}")
else:
    print(f"Errore nel download. Codice: {response.status_code}")

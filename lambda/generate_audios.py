from gtts import gTTS
import os

# Lista de frases en alemán
phrases = []
with open(os.getcwd() + "/data/phrases.txt", "r") as file:
    phrases = file.readlines()

# Crear carpeta de salida
output_dir = os.getcwd() + "/data/audios"
os.makedirs(output_dir, exist_ok=True)

# Generar audios
for i in range(len(phrases)):
    print(phrases[i].split("|")[0])
    filename = phrases[i].split("|")[0].replace(" ", "_").replace(".", "").replace("?", "").lower()
    tts = gTTS(text=phrases[i].split("|")[0], lang='de')
    tts.save(os.path.join(output_dir, f"{filename}.mp3"))
# aws s3 cp lambda/data/audios s3://spanish-to-english-words-ivandagomez/audios/ --recursive --acl public-read
#aws s3 cp lambda/data/audios s3://spanish-to-english-words-ivandagomez/audios/ --recursive
print("✅ Audios generados en la carpeta 'data/audios'")

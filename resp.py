from senha import API_KEY
import requests
import json
import time
from datetime import datetime


headers = {f"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo-0301"

body_question = {
    "model": id_modelo,
    "messages": [{"role": "user", "content": "fale um brasileiro famoso aleatorio e conte um pouco sobre ele em até 150 caracteres"}]
}


while True:
    now = datetime.now()
    if now.hour == 7 and now.minute == 0:
        body_question = json.dumps(body_question)
        requisicao = requests.post(link, headers=headers, data=body_question)
        resposta = requisicao.json()
        mensagem = resposta["choices"][0]["message"]["content"]
        time.sleep(24 * 60 * 60)
    else:
        time.sleep(60)


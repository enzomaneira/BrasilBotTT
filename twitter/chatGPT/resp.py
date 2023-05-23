from senha import API_KEY
import requests
import json


headers = {f"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo-0301"

body_question = {
    "model": id_modelo,
    "messages": [{"role": "user", "content": "fale um brasileiro famoso aleatorio e conte um pouco sobre ele"}]
}

body_question = json.dumps(body_question)

requisicao = requests.post(link, headers=headers, data=body_question)
print(requisicao)
print(requisicao.text)
import json
import requests
import uvicorn
from bs4 import BeautifulSoup
from fastapi import FastAPI
from edenkey import EDENAI_KEY

#Pour que le chatbot fonctionne : il faut saisir une key de l'API EdenAI
headers = {"Authorization": EDENAI_KEY}
url = "https://api.edenai.run/v2/text/chat"
provider = 'openai'


app = FastAPI()

#gestion des erreurs CORS
from fastapi.middleware.cors import CORSMiddleware
origins = ["http://localhost", "http://localhost:8001"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can restrict this to specific HTTP methods if needed
    allow_headers=["*"],  # You can restrict this to specific headers if needed
)

#Pour tester l'API
@app.get("/test/{prompt}", description="Test!")
def test():
    return "yo"

#Pour alimenter le chatbot avec les données du portfolio:
response = requests.get('http://localhost:8001/Portfolio.html')
soup = BeautifulSoup(response.text, 'html.parser')

#pour se connecter à l'API
@app.post("/chat/", description = 'output du chatbot')
async def chat(prompt):
    payload = {
        "providers": provider,
        "text": "",
        "chatbot_global_action": f"Act as an professional assistant with this :{soup}",
        "previous_history": [],
        "temperature": 0.8,
        "max_tokens": 200,
        "fallback_providers": ""
    }
    payload["text"] = prompt

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)[provider]

    return result['generated_text']

uvicorn.run(app)

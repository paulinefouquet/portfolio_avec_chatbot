import json
import requests


headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYzg2YmQ4MTktNmUwNS00OGUyLWI4YjItY2YwZjgyZWFiYmQ4IiwidHlwZSI6ImFwaV90b2tlbiJ9.Ls29O1PI0yDaiiP2aGM0GYziko79nUG8_d33BrBCrkI"}
url = "https://api.edenai.run/v2/text/chat"
provider = 'meta'

payload = {
    "providers": provider,
    #"model": "llama2-13b-chat-v1",
    "text": "",
    "chatbot_global_action": "Act as an professional assistant and answer in less than 50 words",
    "previous_history": [],
    "temperature": 0.8,
    "max_tokens": 50,
    "fallback_providers": ""
}

while True:
    prompt = input("Question:")
    if prompt in ["quit", "exit", "bye", "logout"]:
        break
    payload["text"] = prompt
    print("\n")

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)[provider]

    payload["previous_history"].append({"role": "user", "message" : prompt})
    payload["previous_history"].append({"role": "assistant", "message" : result['generated_text']})
    print(result['generated_text'])
    #print(result)
    print(payload["previous_history"])



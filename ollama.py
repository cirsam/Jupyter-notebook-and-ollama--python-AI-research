import requests
import json
def apiCallToOllamaServer(prompt:str,model:str):
        url= "http://localhost:11434/api/generate"
        print(url)
        response=requests.post(url,json={"model": model, "prompt": prompt, "stream": False})
        if response.status_code == 200:
            print(response.json()['response'])
        else:
            print("Error:", response.status_code)
            print("status_code", response.status_code)
            print("message", response.text)

apiCallToOllamaServer("What is the capital of France?","phi3:mini")
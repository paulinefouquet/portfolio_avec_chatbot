# Création de mon portfolio avec Chatbot intégré.

## Prérequis : pour faire fonctionner le chatbot

### Obtenir une Key de EdenAI

https://docs.edenai.co/reference/start-your-ai-journey-with-edenai

Dans répertoire du repo, créer un fichier edenkey.py qui contient la variable
EDENAI_KEY = "Bearer xxxxxxxxxxxxxx....xxxxxxxxxxxxxxxxxxx"

### Demarrer le portfolio sur un serveur specifique

Pour éviter les problemes de CORS : démarrer le portfolio depuis un port spécifique 8001
Pour cela se placer dans le dossier contenant l'index.html et lancer la commande:
```
python -m http.server 8001
```
Ensuite acceder au portfolio depuis le navigateur par http://localhost:8001/index.html

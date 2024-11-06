# Utiliser l'image officielle Python
FROM python:3.13.0-alpine3.20

# Créer un répertoire pour l'application
WORKDIR /app

# Copier le script sum.py dans le répertoire /app du conteneur
COPY sum.py /app

# Définir une commande par défaut pour maintenir le conteneur actif
CMD ["python", "/app/sum.py"]

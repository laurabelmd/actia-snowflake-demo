#!/bin/bash

echo "🔍 Vérification de l'environnement..."

# Vérifier Python
python --version

# Vérifier Streamlit
streamlit version

# Tuer les processus Streamlit existants (si bloqués)
echo "🧹 Nettoyage des processus Streamlit..."
pkill -f streamlit || true

# Attendre un peu
sleep 2

# Lancer l'application
echo "🚀 Lancement de l'application..."
streamlit run app.py --server.port 8501


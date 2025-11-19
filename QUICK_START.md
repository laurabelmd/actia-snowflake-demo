# 🚀 Quick Start Guide

## Installation Rapide (5 minutes)

### 1. Installer les dépendances

```bash
cd /Users/lbelmond/Desktop/EBC_27
pip install -r requirements.txt
```

### 2. Lancer la demo principale

```bash
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur à `http://localhost:8501`

### 3. Lancer le dashboard mobile (optionnel pour test local)

Dans un nouveau terminal:

```bash
cd /Users/lbelmond/Desktop/EBC_27
streamlit run mobile_app.py --server.port 8502
```

Le dashboard mobile sera accessible à `http://localhost:8502`

---

## 📱 Déploiement Production (Streamlit Cloud)

### Étape 1: Déployer l'app principale

1. Push le code sur GitHub
2. Aller sur https://share.streamlit.io/
3. Connecter votre repo
4. Sélectionner:
   - **Branch**: main
   - **Main file**: `app.py`
   - **Python**: 3.11
5. Déployer

Vous obtiendrez une URL comme: `https://actia-demo.streamlit.app`

### Étape 2: Déployer l'app mobile

1. Créer une nouvelle app sur Streamlit Cloud
2. Même repo, mais sélectionner:
   - **Main file**: `mobile_app.py`
3. Déployer

Vous obtiendrez une URL comme: `https://actia-mobile.streamlit.app`

### Étape 3: Lier le QR code

1. Copier l'URL de votre app mobile
2. Éditer `app.py` ligne ~234
3. Remplacer:
```python
qr_code_url = "https://api.qrserver.com/v1/create-qr-code/?size=400x400&data=https://YOUR-MOBILE-APP.streamlit.app"
```

Par:
```python
qr_code_url = "https://api.qrserver.com/v1/create-qr-code/?size=400x400&data=https://actia-mobile.streamlit.app"
```

4. Commit et push
5. Streamlit Cloud redéployera automatiquement

---

## ✅ Test de la Demo

### Checklist
- [ ] Page "Accueil" s'affiche avec les cartes métriques
- [ ] Page "Dashboard Mobile" montre le QR code
- [ ] Page "Traçabilité" : bouton "Tracer" fonctionne
- [ ] Page "IA Conversationnelle" : les 3 boutons affichent les réponses
- [ ] Page "Prédictions" : les 3 onglets s'ouvrent
- [ ] Page "Marketplace" : les 3 onglets montrent les données
- [ ] Page "Document AI" : l'upload de fichier fonctionne

### Test du mobile dashboard
- [ ] Scannez le QR code avec votre téléphone
- [ ] Le dashboard s'affiche correctement
- [ ] Les graphiques sont lisibles
- [ ] Le bouton "Actualiser" fonctionne

---

## 🎨 Personnalisation

### Changer le logo Actia

1. Remplacer le placeholder dans `app.py` ligne ~70:
```python
st.sidebar.image("https://via.placeholder.com/200x80/424242/8BC34A?text=ACTIA", ...)
```

Par:
```python
st.sidebar.image("path/to/actia_logo.png", ...)
```

### Ajouter de vraies données

Les sections avec données hardcodées:
- **Traçabilité** (ligne 300+): Modifier les DataFrames
- **LLM Responses** (ligne 400+): Modifier les réponses texte
- **Prédictions** (ligne 600+): Modifier les valeurs numpy/pandas
- **Marketplace** (ligne 800+): Modifier les prix et datasets

---

## 🐛 Troubleshooting

### Le QR code ne fonctionne pas
- Vérifiez que l'URL mobile est correcte
- Testez l'URL directement dans un navigateur mobile
- Utilisez un iPad de backup avec l'URL pré-chargée

### Erreur "Module not found"
```bash
pip install --upgrade streamlit pandas plotly numpy
```

### L'app est lente
- Normal en local si vous ouvrez tous les onglets
- Sur Streamlit Cloud, utilisez le cache
- Les graphiques Plotly peuvent être lourds

### Upload de fichier ne marche pas
- Vérifiez que le fichier fait <200MB (config dans config.toml)
- Types supportés: PDF, TXT, JPG, PNG, CSV

---

## 📞 Support

### Documentation
- Streamlit: https://docs.streamlit.io
- Plotly: https://plotly.com/python/
- Pandas: https://pandas.pydata.org/

### Commandes utiles

```bash
# Voir les logs en temps réel
streamlit run app.py --logger.level=debug

# Effacer le cache
streamlit cache clear

# Tester sans ouvrir le navigateur
streamlit run app.py --server.headless=true
```

---

## 📊 Structure du Projet

```
EBC_27/
├── app.py                    # Application principale
├── mobile_app.py            # Dashboard mobile
├── requirements.txt         # Dépendances Python
├── README.md               # Documentation complète
├── DEMO_SCRIPT.md          # Script de présentation
├── QUICK_START.md          # Ce fichier
├── sample_test_report.txt  # Exemple pour Document AI
├── .streamlit/
│   └── config.toml         # Config Streamlit (couleurs)
└── .gitignore              # Fichiers à ignorer
```

---

## 🎯 Prêt pour la Demo!

Une fois tout installé:
1. Ouvrez `DEMO_SCRIPT.md` pour le script détaillé
2. Lancez `streamlit run app.py`
3. Testez chaque section
4. Préparez votre téléphone pour le QR code
5. Go! 🚀


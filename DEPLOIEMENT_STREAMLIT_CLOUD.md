# 🚀 Déploiement sur Streamlit Cloud - Guide Complet

## 📋 Prérequis

✅ Compte Streamlit Cloud (vous l'avez)
✅ Compte GitHub
✅ Code prêt dans `/Users/lbelmond/Desktop/EBC_27`

---

## 🎯 Plan d'action

Nous allons déployer **2 applications**:
1. **App principale** (`app.py`) - Pour la projection
2. **Cortex Analyst** (`cortex_analyst_app.py`) - Pour les participants (QR code)

---

## 📦 Étape 1: Créer un fichier .gitignore

```bash
cd /Users/lbelmond/Desktop/EBC_27
```

Créer un fichier `.gitignore`:

```bash
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# Virtual environments
venv/
env/
ENV/

# Streamlit
.streamlit/secrets.toml

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Temp files
*.log
.cache/
EOF
```

---

## 🔧 Étape 2: Initialiser Git et pousser sur GitHub

### 2.1 Initialiser le repo

```bash
cd /Users/lbelmond/Desktop/EBC_27
git init
git add .
git commit -m "Initial commit - Actia Snowflake Demo"
```

### 2.2 Créer un repo sur GitHub

1. Aller sur https://github.com
2. Cliquer sur le **"+"** en haut à droite
3. Sélectionner **"New repository"**
4. Remplir:
   - **Repository name**: `actia-snowflake-demo`
   - **Description**: "Demo Actia avec Cortex Analyst et IA"
   - **Public** ou **Private** (Private recommandé)
   - **NE PAS** cocher "Add README"
5. Cliquer **"Create repository"**

### 2.3 Pousser le code

GitHub vous donnera des commandes. Utiliser:

```bash
git remote add origin https://github.com/VOTRE-USERNAME/actia-snowflake-demo.git
git branch -M main
git push -u origin main
```

**Remplacer** `VOTRE-USERNAME` par votre nom d'utilisateur GitHub.

---

## ☁️ Étape 3: Déployer sur Streamlit Cloud

### 3.1 Déployer l'application Cortex Analyst (IMPORTANT: À faire en PREMIER)

1. Aller sur https://share.streamlit.io/
2. Cliquer **"New app"**
3. Remplir:
   - **Repository**: `VOTRE-USERNAME/actia-snowflake-demo`
   - **Branch**: `main`
   - **Main file path**: `cortex_analyst_app.py` ⚠️ IMPORTANT
   - **App URL** (personnaliser): `actia-cortex-analyst`
4. Cliquer **"Deploy"**
5. ⏳ Attendre 2-3 minutes

**Vous obtiendrez une URL comme:**
```
https://actia-cortex-analyst.streamlit.app
```

**📝 NOTER CETTE URL!** Vous en aurez besoin à l'étape 4.

---

### 3.2 Déployer l'application principale

1. Toujours sur https://share.streamlit.io/
2. Cliquer **"New app"** à nouveau
3. Remplir:
   - **Repository**: `VOTRE-USERNAME/actia-snowflake-demo`
   - **Branch**: `main`
   - **Main file path**: `app.py` ⚠️ IMPORTANT
   - **App URL** (personnaliser): `actia-demo`
4. Cliquer **"Deploy"**
5. ⏳ Attendre 2-3 minutes

**Vous obtiendrez une URL comme:**
```
https://actia-demo.streamlit.app
```

---

## 🔗 Étape 4: Mettre à jour le QR code avec l'URL Cortex Analyst

### 4.1 Modifier app.py

Ouvrir `/Users/lbelmond/Desktop/EBC_27/app.py`

Aller à la **ligne 214** et remplacer:

```python
# AVANT (version locale):
cortex_url = "http://192.168.1.100:8502"  # Replace with your local IP

# APRÈS (version cloud):
cortex_url = "https://actia-cortex-analyst.streamlit.app"  # URL de l'étape 3.1
```

### 4.2 Commenter les instructions locales

```python
# For local testing, use this:
# cortex_url = "http://192.168.1.100:8502"  # Replace with your local IP

# For production (after Streamlit Cloud deployment), use this:
cortex_url = "https://actia-cortex-analyst.streamlit.app"  # ✅ Votre URL ici
```

### 4.3 Sauvegarder et pousser

```bash
cd /Users/lbelmond/Desktop/EBC_27
git add app.py
git commit -m "Update QR code with Streamlit Cloud URL"
git push
```

⏳ **L'app principale se mettra à jour automatiquement** (2-3 minutes)

---

## ✅ Étape 5: Vérifier que tout fonctionne

### 5.1 Tester l'app Cortex Analyst

Ouvrir: `https://actia-cortex-analyst.streamlit.app`

**Vérifier:**
- [ ] Logo Actia s'affiche
- [ ] Dashboard avec 4 métriques
- [ ] Graphiques de production/qualité
- [ ] Chatbox fonctionne
- [ ] Questions suggérées cliquables
- [ ] Réponses s'affichent

### 5.2 Tester l'app principale

Ouvrir: `https://actia-demo.streamlit.app`

**Vérifier:**
- [ ] Logo Actia dans la sidebar
- [ ] Toutes les pages accessibles
- [ ] Page "🤖 Cortex Analyst" affiche le QR code
- [ ] QR code scanne correctement

### 5.3 Tester le QR code

1. Ouvrir l'app principale sur votre ordi
2. Aller à la page "🤖 Cortex Analyst"
3. Scanner le QR code avec votre téléphone
4. ✅ Cortex Analyst devrait s'ouvrir!
5. Tester quelques questions dans le chatbox

---

## 🎬 URLs pour la démo

### Pour vous (présentateur):
**App principale à projeter:**
```
https://actia-demo.streamlit.app
```

### Pour les participants:
**Via QR code** → Scannent et accèdent à:
```
https://actia-cortex-analyst.streamlit.app
```

**Ou lien direct** (backup si QR ne marche pas):
```
https://actia-cortex-analyst.streamlit.app
```

---

## 🔧 Gestion des apps sur Streamlit Cloud

### Accéder au dashboard

1. Aller sur https://share.streamlit.io/
2. Vous verrez vos 2 apps:
   - `actia-demo` (app.py)
   - `actia-cortex-analyst` (cortex_analyst_app.py)

### Actions disponibles

Pour chaque app:
- **⚙️ Settings**: Modifier config
- **📊 Analytics**: Voir usage
- **🔄 Reboot**: Redémarrer l'app
- **⏸️ Hibernate**: Mettre en pause
- **🗑️ Delete**: Supprimer

### Mise à jour automatique

Chaque fois que vous faites un `git push`, les apps se mettent à jour automatiquement! 🎉

---

## 💡 Avantages de Streamlit Cloud

### Vs déploiement local:
✅ **Accessible partout**: Internet uniquement (pas besoin même WiFi)
✅ **Pas de config IP**: URL fixe et stable
✅ **Toujours en ligne**: Disponible 24/7
✅ **SSL gratuit**: HTTPS automatique
✅ **Mises à jour faciles**: Git push = déploiement

### Limites (plan gratuit):
- 1 GB RAM par app
- Ressources partagées
- L'app "hiberne" après inactivité (se réveille au 1er accès)

---

## 🔐 Sécurité et confidentialité

### Pour une démo publique:
⚠️ **Attention:** Vos apps seront accessibles à tous avec l'URL

**Recommandations:**
- Utiliser données fictives uniquement
- Pas de vraies credentials
- Pas de données sensibles
- Repo GitHub en **Private** si possible

### Ajouter une authentification (optionnel):

Créer `.streamlit/secrets.toml`:
```toml
[passwords]
demo = "actia2024"
```

Dans `app.py` et `cortex_analyst_app.py`, ajouter:
```python
import streamlit as st

# Simple password protection
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    password = st.text_input("Mot de passe:", type="password")
    if st.button("Connexion"):
        if password == st.secrets["passwords"]["demo"]:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Mot de passe incorrect")
    st.stop()

# Reste de votre code...
```

---

## 🐛 Troubleshooting

### Problème: App ne démarre pas
**Solution:**
1. Vérifier les logs sur Streamlit Cloud
2. Vérifier `requirements.txt` (toutes dépendances présentes)
3. Tester en local d'abord

### Problème: QR code ne fonctionne pas
**Vérifier:**
1. L'URL dans app.py ligne 214 est correcte
2. L'app Cortex Analyst est bien déployée
3. Le QR code s'est régénéré (après git push)

### Problème: App est lente
**Solutions:**
1. Attendre que l'app sorte d'hibernation (1er chargement)
2. Optimiser le code (cache avec `@st.cache_data`)
3. Réduire taille des données

### Problème: Logo ne s'affiche pas
**Vérifier:**
1. `actia_logo.svg` est bien dans le repo
2. Le fichier a été commit et push
3. Le chemin est correct (pas de sous-dossier)

---

## 📊 Monitoring

### Avant la démo:
1. Ouvrir les 2 apps 5-10 min avant (les "réveiller")
2. Tester le QR code
3. Vérifier qu'il n'y a pas de maintenance Streamlit

### Pendant la démo:
1. Garder les 2 URLs ouvertes en onglet
2. Avoir un plan B (screenshots) si problème
3. Avoir un lien court (bit.ly) en backup

---

## 🔄 Workflow de mise à jour

### Pour modifier le code:

```bash
# 1. Modifier vos fichiers localement
code app.py  # ou autre fichier

# 2. Tester en local
streamlit run app.py

# 3. Commit et push
git add .
git commit -m "Description des changements"
git push

# 4. Attendre 2-3 minutes
# Les apps se mettent à jour automatiquement!
```

---

## 📋 Checklist finale avant démo

### Déploiement
- [ ] Repo GitHub créé et code pushé
- [ ] App Cortex Analyst déployée
- [ ] App principale déployée
- [ ] URL Cortex Analyst notée
- [ ] QR code mis à jour dans app.py (ligne 214)
- [ ] Changements pushés sur GitHub

### Tests
- [ ] Les 2 apps chargent correctement
- [ ] Logo Actia visible partout
- [ ] QR code scanne et ouvre Cortex Analyst
- [ ] Chatbox répond aux questions
- [ ] Dashboard s'affiche correctement
- [ ] Toutes les pages de l'app principale fonctionnent

### Documentation
- [ ] URLs notées et partagées avec l'équipe
- [ ] Lien court créé (bit.ly) pour backup
- [ ] Script de démo adapté avec nouvelles URLs

---

## 🎯 Résumé des commandes

```bash
# Configuration initiale
cd /Users/lbelmond/Desktop/EBC_27
git init
git add .
git commit -m "Initial commit - Actia Demo"
git remote add origin https://github.com/VOTRE-USERNAME/actia-snowflake-demo.git
git push -u origin main

# Après modification du QR code
git add app.py
git commit -m "Update QR code URL"
git push

# Pour toute modification future
git add .
git commit -m "Description"
git push
```

---

## 🎉 C'est tout!

Une fois déployé:
- ✅ QR code fonctionne partout (pas besoin même WiFi)
- ✅ Apps toujours accessibles
- ✅ Mises à jour faciles (git push)
- ✅ URLs propres et professionnelles

**Bonne démo! 🚀**


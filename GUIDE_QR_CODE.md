# 📱 Guide QR Code pour Cortex Analyst

## 🎯 Objectif

Permettre aux participants de scanner un QR code depuis l'écran de projection et accéder à l'application **Cortex Analyst** sur leur téléphone/tablette pour:
- Voir le dashboard temps réel
- Poser des questions au chatbox IA
- Explorer les données interactivement

---

## 🚀 Configuration rapide (3 étapes)

### Étape 1: Obtenir votre adresse IP locale

```bash
# Sur Mac/Linux
ifconfig | grep "inet " | grep -v 127.0.0.1

# Sur Windows
ipconfig
```

**Exemple de résultat:** `192.168.1.42`

### Étape 2: Mettre à jour app.py

Ouvrez `app.py` et allez à la **ligne 214**:

```python
# Remplacer cette ligne:
cortex_url = "http://192.168.1.100:8502"

# Par votre IP:
cortex_url = "http://192.168.1.42:8502"  # Votre IP + port 8502
```

### Étape 3: Lancer les deux applications

```bash
# Terminal 1: App principale (pour la projection)
streamlit run app.py

# Terminal 2: Cortex Analyst (pour les participants)
streamlit run cortex_analyst_app.py --server.port 8502
```

---

## 📱 Flow de la démo

### 1. Page projetée (app.py)
```
┌─────────────────────────────────────┐
│  🤖 Actia Cortex Analyst            │
│                                     │
│  [QR Code géant]    [Preview app]  │
│                                     │
│  "Scannez pour accéder au          │
│   dashboard + chatbox IA"          │
└─────────────────────────────────────┘
```

### 2. Participants scannent

### 3. S'affiche sur leur téléphone
```
┌──────────────────┐
│ 🤖 Cortex        │
│ Analyst          │
├──────────────────┤
│ 📊 Production    │
│    1,247         │
├──────────────────┤
│ 💬 Chatbox       │
│ "Posez vos       │
│  questions..."   │
└──────────────────┘
```

---

## 🌐 Options de déploiement

### Option A: Démo locale (LAN)
✅ **Pour démo en interne, même WiFi**

**Avantages:**
- Rapide à configurer
- Pas besoin d'Internet
- Contrôle total

**Configuration:**
1. Tous connectés au même WiFi
2. App sur port 8502
3. QR code avec IP locale

**URL exemple:** `http://192.168.1.42:8502`

---

### Option B: Déploiement Streamlit Cloud
✅ **Pour démo avec accès Internet**

**Avantages:**
- Accessible de partout
- URL propre et stable
- Pas de config réseau

**Étapes:**

#### 1. Créer un repo GitHub
```bash
cd /Users/lbelmond/Desktop/EBC_27
git init
git add .
git commit -m "Actia Cortex Analyst Demo"
git remote add origin https://github.com/VOTRE-USERNAME/actia-demo
git push -u origin main
```

#### 2. Déployer sur Streamlit Cloud

**App 1: Principale (pour projection)**
- Aller sur https://streamlit.io/cloud
- New app
- Repo: votre repo GitHub
- Main file path: `app.py`
- Deploy

**App 2: Cortex Analyst (pour participants)**
- New app
- Même repo
- Main file path: `cortex_analyst_app.py`
- Deploy

#### 3. Récupérer l'URL

Vous obtiendrez une URL type:
```
https://actia-cortex-analyst.streamlit.app
```

#### 4. Mettre à jour app.py (ligne 214)

```python
# Commenter la version locale:
# cortex_url = "http://192.168.1.100:8502"

# Décommenter et utiliser l'URL Streamlit Cloud:
cortex_url = "https://actia-cortex-analyst.streamlit.app"
```

#### 5. Re-déployer

Git push → L'app se met à jour automatiquement

---

## 🔧 Troubleshooting

### Problème 1: QR code ne fonctionne pas
**Symptômes:** Scan réussi mais page ne charge pas

**Solutions:**
1. Vérifier que cortex_analyst_app tourne sur port 8502
2. Vérifier que l'IP dans app.py est correcte
3. Vérifier que tous sont sur le même WiFi
4. Désactiver pare-feu temporairement

**Test rapide:**
```bash
# Sur un autre appareil, ouvrir navigateur et taper:
http://VOTRE-IP:8502
```

---

### Problème 2: Logo ne s'affiche pas sur mobile
**Solution:** S'assurer que `actia_logo.svg` est dans le même dossier

---

### Problème 3: Chat ne répond pas
**Vérifier:**
1. Session state initialisé
2. Fonction `get_cortex_response` définie
3. Pas d'erreurs dans console terminal

---

## 📊 Test avant démo

### Checklist complète

#### Avant de commencer
- [ ] Les 2 apps compilent sans erreur
- [ ] Logo Actia s'affiche dans les 2 apps
- [ ] IP locale identifiée et mise à jour dans app.py
- [ ] Port 8502 disponible

#### Test technique
- [ ] App principale démarre sur port 8501
- [ ] Cortex Analyst démarre sur port 8502
- [ ] QR code s'affiche correctement
- [ ] Scanner le QR code depuis un téléphone
- [ ] Cortex Analyst charge sur mobile
- [ ] Dashboard s'affiche correctement
- [ ] Chat fonctionne (tester 2-3 questions)

#### Test utilisateur
- [ ] Navigation intuitive
- [ ] Temps de chargement acceptable (<3 sec)
- [ ] Lisible sur petit écran
- [ ] Boutons cliquables facilement

---

## 🎬 Script de démo (avec QR code)

### Minute 2-7: Cortex Analyst interactif

#### Présentateur:
> "Première chose: je veux que vous ayez la donnée dans vos mains. **Sortez vos téléphones.**"

*Afficher la page "🤖 Cortex Analyst" sur grand écran*

> "Vous voyez ce QR code? Scannez-le maintenant."

*Attendre 30 secondes que tout le monde scanne*

> "Une fois scanné, vous accédez à **Cortex Analyst** - notre IA conversationnelle. Vous avez:
> - Un dashboard temps réel de votre production
> - Un chatbox où vous pouvez poser n'importe quelle question en français
> - Des analyses instantanées"

*Montrer le preview à l'écran*

> "Essayez maintenant: posez une question. Par exemple:
> - 'Quel est le taux de qualité ce mois-ci?'
> - 'Quels composants ont des problèmes?'
> - 'Quelle est la tendance de production?'"

*Laisser 2-3 minutes explorer*

> "Vous voyez? Pas besoin d'être data analyst. Posez votre question, l'IA analyse et vous répond. C'est ça, la démocratisation de la donnée."

---

## 💡 Conseils pour la démo

### Technique
1. **Tester le QR code 30 min avant** avec 2-3 téléphones
2. **Avoir un plan B**: iPad de backup avec l'app déjà ouverte
3. **WiFi stable**: Vérifier la connexion avant
4. **Batterie**: Ordi chargé à 100%

### Présentation
1. **Montrer d'abord**: Scanner vous-même pour montrer
2. **Être patient**: Donner 30-60 sec pour que tous scannent
3. **Guider**: "Cliquez sur les boutons verts pour poser des questions"
4. **Circuler**: Voir si besoin d'aide

### Engagement
1. **Questions suggérées**: Donner 3-4 exemples concrets
2. **Encourager**: "N'hésitez pas, posez vos vraies questions"
3. **Réagir**: Si quelqu'un trouve un insight, le partager

---

## 📝 Fichiers concernés

| Fichier | Rôle | QR Code? |
|---------|------|----------|
| `app.py` | App principale (projection) | ✅ Génère le QR |
| `cortex_analyst_app.py` | App pour participants | ❌ Cible du QR |
| `actia_logo.svg` | Logo (les 2 apps) | - |

---

## 🎨 Personnalisation du QR code

### Changer la taille
```python
# Dans app.py, ligne 219
qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?size=500x500&data={cortex_url}"
#                                                                    ^^^^^^^ Ajuster ici
```

### Ajouter un logo au QR code
```python
# Service avancé (qr-code-generator.com)
qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?size=400x400&data={cortex_url}&logo=actia"
```

### QR code statique (backup)
Si l'API QR est down, avoir une image de backup:
```python
st.image("qr_code_backup.png", width=400)
```

---

## ✅ Checklist finale

### Jour J - 1h avant
- [ ] Les 2 apps tournent
- [ ] QR code testé avec 1 téléphone
- [ ] Chatbox répond correctement
- [ ] Dashboard s'affiche bien
- [ ] Écran de projection OK
- [ ] WiFi stable

### Jour J - Pendant la démo
- [ ] Afficher page QR code (minute 2)
- [ ] Laisser temps de scanner (30-60 sec)
- [ ] Guider l'exploration (2-3 min)
- [ ] Répondre aux questions techniques si besoin

---

## 📞 Support

**En cas de problème technique:**
1. Plan B: Montrer sur iPad/ordi de backup
2. Expliquer le concept même si QR ne marche pas
3. Partager le lien par email après

**Contact:**
- README.md pour documentation complète
- CORTEX_ANALYST_GUIDE.md pour guide utilisateur

---

**Guide créé pour la démo Actia - Novembre 2024**


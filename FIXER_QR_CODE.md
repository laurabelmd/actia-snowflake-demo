# 🔧 FIXER LE QR CODE

## 🎯 Problème Possible

Le QR code dans l'application principale (`app.py`) ne fonctionne pas car il pointe vers une **URL locale** qui n'est accessible que sur votre réseau.

---

## ✅ SOLUTION COMPLÈTE

### **Option 1 : Vous avez DÉJÀ déployé cortex_analyst_app.py**

Si votre app mobile est déjà sur Streamlit Cloud avec une URL comme :
`https://[votre-username]-cortex-analyst.streamlit.app`

**Action :** Mettre à jour l'URL dans `app.py` ligne 213-216 :

```python
# Commentez la ligne locale :
# cortex_url = "http://192.168.1.100:8502"

# Décommentez et mettez votre vraie URL :
cortex_url = "https://[VOTRE-URL-ICI].streamlit.app"
```

**Exemple :**
```python
cortex_url = "https://laurabelmd-actia-cortex.streamlit.app"
```

---

### **Option 2 : Vous n'avez PAS encore déployé cortex_analyst_app.py**

Vous devez déployer `cortex_analyst_app.py` sur Streamlit Cloud.

#### **Étape 1 : Vérifier que le fichier est sur GitHub**

```bash
cd /Users/lbelmond/Desktop/EBC_27
git add cortex_analyst_app.py
git commit -m "Add cortex analyst mobile app"
git push
```

#### **Étape 2 : Créer une nouvelle app sur Streamlit Cloud**

1. Allez sur https://share.streamlit.io/
2. Cliquez sur **"New app"**
3. **Remplissez :**
   - **Repository :** `laurabelmd/actia-snowflake-demo`
   - **Branch :** `main`
   - **Main file :** `cortex_analyst_app.py` ⚠️ (pas app.py !)
   - **App URL :** Choisissez un nom (ex: `actia-cortex`)
4. **Cliquez "Deploy"**
5. ⏱️ Attendez 3-5 minutes

#### **Étape 3 : Récupérer l'URL**

Une fois déployée, vous aurez une URL comme :
`https://[votre-username]-actia-cortex.streamlit.app`

**Copiez cette URL !**

#### **Étape 4 : Mettre à jour app.py**

Éditez `app.py` ligne 213-216 avec votre nouvelle URL.

---

### **Option 3 : Utiliser une URL temporaire pour tester localement**

Si vous voulez tester le QR code **avant** de déployer sur Streamlit Cloud :

#### **Étape 1 : Obtenir votre IP locale**

**Sur Mac :**
```bash
ipconfig getifaddr en0
```

**Exemple de résultat :** `192.168.1.45`

#### **Étape 2 : Lancer cortex_analyst_app.py localement**

```bash
cd /Users/lbelmond/Desktop/EBC_27
streamlit run cortex_analyst_app.py --server.port 8502
```

#### **Étape 3 : Mettre à jour l'URL dans app.py**

```python
cortex_url = "http://192.168.1.45:8502"  # Remplacez par votre IP
```

⚠️ **Limitation :** Ça ne marchera QUE sur votre réseau WiFi local

---

## 🔄 SCRIPT AUTOMATIQUE POUR METTRE À JOUR L'URL

Je peux créer un script pour vous si vous me donnez l'URL de votre app mobile :

**Dites-moi :**
- Quelle est l'URL de votre app mobile Cortex Analyst ?
- OU voulez-vous que je vous aide à la déployer d'abord ?

---

## 🧪 TESTER LE QR CODE

### **1. Vérifier que le QR code s'affiche**

1. Lancez `app.py`
2. Allez sur la page **"🤖 Cortex Analyst"**
3. Vous devriez voir :
   - Un grand carré noir et blanc (le QR code)
   - Taille : 400x400 pixels

**Si le QR code ne s'affiche PAS :**
- Problème de génération via `api.qrserver.com`
- Solution : Utiliser une bibliothèque Python locale (`qrcode`)

### **2. Tester le QR code avec votre téléphone**

1. Ouvrez l'**appareil photo** de votre téléphone
2. **Pointez** vers le QR code sur votre écran
3. Une **notification** devrait apparaître avec un lien
4. **Cliquez** sur le lien

**Résultat attendu :**
- ✅ Votre navigateur mobile s'ouvre
- ✅ L'app Cortex Analyst charge
- ✅ Vous voyez le dashboard + chatbot

**Si ça ne marche PAS :**
- Vérifiez l'URL dans `app.py` ligne 213
- Vérifiez que l'app mobile est bien déployée et accessible

---

## 🛠️ ALTERNATIVE : Générer le QR Code localement (plus fiable)

Au lieu d'utiliser `api.qrserver.com`, on peut générer le QR code directement avec Python :

### **1. Installer le module**

```bash
pip install qrcode[pil]
```

### **2. Modifier app.py**

Remplacer les lignes 218-219 par :

```python
import qrcode
import io
from PIL import Image

# Générer le QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(cortex_url)
qr.make(fit=True)

# Créer l'image
img = qr.make_image(fill_color="black", back_color="white")

# Convertir en bytes pour Streamlit
buf = io.BytesIO()
img.save(buf, format='PNG')
byte_im = buf.getvalue()

# Afficher
st.image(byte_im, width=400)
```

**Avantage :** Ne dépend pas d'une API externe, plus fiable

---

## 📋 CHECKLIST COMPLÈTE

- [ ] `cortex_analyst_app.py` existe dans le projet
- [ ] `cortex_analyst_app.py` est sur GitHub
- [ ] `cortex_analyst_app.py` est déployé sur Streamlit Cloud
- [ ] J'ai l'URL de l'app mobile (ex: https://xxx.streamlit.app)
- [ ] L'URL est mise à jour dans `app.py` ligne 213
- [ ] J'ai testé l'URL dans mon navigateur (elle fonctionne)
- [ ] Le QR code s'affiche dans `app.py`
- [ ] Le QR code scanne correctement avec mon téléphone
- [ ] L'app mobile s'ouvre quand je scanne le QR code

---

## 🆘 SI RIEN NE MARCHE

**Envoyez-moi :**
1. L'URL de votre app mobile (si elle existe)
2. Une capture d'écran de la page "🤖 Cortex Analyst" dans app.py
3. Le message d'erreur exact (si il y en a un)

**Et dites-moi :**
- Est-ce que l'app mobile (`cortex_analyst_app.py`) est déjà déployée sur Streamlit Cloud ?
- Quel est exactement le problème avec le QR code ? (ne s'affiche pas / ne scanne pas / ne mène nulle part)

---

## 🚀 PROCHAINES ÉTAPES

**Dites-moi ce que vous voulez :**

**Option A :** *"J'ai déjà déployé l'app mobile, voici l'URL : ..."*  
→ Je mets à jour le code immédiatement

**Option B :** *"Je n'ai pas encore déployé l'app mobile"*  
→ Je vous guide pour le faire (5 minutes)

**Option C :** *"Le QR code s'affiche mais ne fonctionne pas quand je le scanne"*  
→ Je change pour une génération locale du QR code

---

**Répondez et je vous aide à fixer ça en 2 minutes ! 🚀**


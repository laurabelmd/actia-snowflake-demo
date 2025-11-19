# 🎯 Configuration QR Code - Guide Rapide

## ✅ Ce qui a été fait

La page "Dashboard Mobile" a été **remplacée** par **"🤖 Cortex Analyst"** dans `app.py`.

Cette page affiche:
- Un **QR code géant** que les participants peuvent scanner
- Un **aperçu visuel** de l'application Cortex Analyst
- Les **fonctionnalités** disponibles (dashboard + chatbox)

---

## 🚀 Configuration en 3 étapes

### Étape 1: Trouver votre adresse IP locale

```bash
# Sur Mac/Linux, ouvrir Terminal:
ifconfig | grep "inet " | grep -v 127.0.0.1

# Sur Windows, ouvrir CMD:
ipconfig
```

**Exemple de résultat:**
```
inet 192.168.1.42
```

Notez votre IP: `192.168.1.42`

---

### Étape 2: Mettre à jour l'IP dans app.py

Ouvrir `/Users/lbelmond/Desktop/EBC_27/app.py`

Aller à la **ligne 214** et remplacer:

```python
# AVANT:
cortex_url = "http://192.168.1.100:8502"

# APRÈS (avec VOTRE IP):
cortex_url = "http://192.168.1.42:8502"
```

Sauvegarder le fichier.

---

### Étape 3: Lancer les 2 applications

**Terminal 1** (pour projection):
```bash
cd /Users/lbelmond/Desktop/EBC_27
streamlit run app.py
```

**Terminal 2** (pour participants):
```bash
cd /Users/lbelmond/Desktop/EBC_27
streamlit run cortex_analyst_app.py --server.port 8502
```

---

## 📱 Test rapide

### 1. Ouvrir les applications

- App principale: http://localhost:8501
- Cortex Analyst: http://localhost:8502

### 2. Naviguer vers la page QR code

Dans l'app principale, cliquer sur **"🤖 Cortex Analyst"** dans la sidebar

### 3. Scanner le QR code

Avec votre téléphone:
1. Ouvrir l'appareil photo
2. Pointer vers le QR code à l'écran
3. Cliquer sur le lien qui apparaît
4. ✅ Cortex Analyst devrait s'ouvrir!

### 4. Tester le chatbox

Sur votre téléphone, essayer:
- Cliquer sur les boutons de questions suggérées
- Taper une question dans l'input
- Vérifier que la réponse s'affiche

---

## 🎬 Flow de la démo

### Minute 2-7: Expérience Interactive

**Présentateur:**
> "Première chose: je veux que vous ayez la data dans vos mains. **Sortez vos téléphones.**"

*Naviguer vers la page "🤖 Cortex Analyst"*

> "Vous voyez ce QR code? **Scannez-le maintenant.**"

*Attendre 30-60 secondes*

> "Une fois scanné, vous avez accès à Cortex Analyst. Vous pouvez:
> - Voir le dashboard temps réel
> - Poser des questions au chatbox
> - Explorer vos données"

*Laisser 2-3 minutes pour qu'ils testent*

> "Essayez de poser une question. Par exemple: 'Quel est le taux de qualité ce mois-ci?'"

> "Vous voyez? L'IA analyse vos données et vous répond instantanément. **C'est ça, la démocratisation de la donnée.**"

---

## ⚙️ Options alternatives

### Option A: Démo locale (recommandé pour début)
✅ Configuration actuelle
- Tous sur le même WiFi
- IP locale dans QR code
- Rapide et fiable

### Option B: Déploiement cloud (pour prod)
Si vous voulez déployer en ligne:

1. **Déployer sur Streamlit Cloud** (voir GUIDE_QR_CODE.md)
2. **Récupérer l'URL** (ex: `https://actia-cortex.streamlit.app`)
3. **Mettre à jour app.py ligne 214:**
   ```python
   cortex_url = "https://actia-cortex.streamlit.app"
   ```

---

## 🔧 Troubleshooting

### Le QR code ne fonctionne pas
**Vérifier:**
1. Les 2 apps tournent (8501 et 8502)
2. L'IP dans app.py est correcte
3. Téléphone sur le même WiFi
4. Pas de pare-feu bloquant

**Test:**
Sur un navigateur mobile, taper directement: `http://VOTRE-IP:8502`

---

### Le chatbox ne répond pas
**Vérifier:**
1. Cortex Analyst tourne bien
2. Pas d'erreurs dans le terminal
3. Rafraîchir la page mobile

---

### Logo coupé sur mobile
**Déjà corrigé!** Le logo utilise `use_column_width=True`

---

## 📊 Checklist avant démo

### Préparation (1h avant)
- [ ] IP locale identifiée
- [ ] app.py mis à jour (ligne 214)
- [ ] Les 2 apps démarrent sans erreur
- [ ] Logo s'affiche correctement
- [ ] QR code testé avec 1 téléphone
- [ ] Chatbox répond correctement

### Pendant la démo
- [ ] Les 2 terminals ouverts et visibles
- [ ] Naviguer vers page "🤖 Cortex Analyst"
- [ ] QR code bien visible sur grand écran
- [ ] Laisser temps de scanner (30-60 sec)
- [ ] Guider: "Cliquez sur les questions suggérées"

---

## 💡 Conseils pro

### Pour le QR code
- **Taille**: Le QR est à 400x400px (bien visible)
- **Contraste**: Fond blanc, bon pour scanner
- **Position**: À gauche, impossible à louper

### Pour l'engagement
- **Montrer d'abord**: Scanner vous-même pour montrer
- **Questions exemple**: Écrire 3-4 questions au tableau
- **Circuler**: Voir si quelqu'un a besoin d'aide
- **Partager**: Si quelqu'un trouve un insight, le montrer

### Plan B
- iPad de backup avec l'app déjà chargée
- Lien court écrit au tableau (bit.ly)
- Continuer la démo même si QR ne marche pas

---

## 📁 Fichiers créés/modifiés

| Fichier | Statut | Description |
|---------|--------|-------------|
| `app.py` | ✅ Modifié | Page QR code créée (ligne 196-317) |
| `cortex_analyst_app.py` | ✅ Existant | App cible du QR code |
| `actia_logo.svg` | ✅ Existant | Logo officiel |
| `GUIDE_QR_CODE.md` | ✅ Créé | Guide détaillé |
| `CONFIGURATION_QR_CODE.md` | ✅ Créé | Ce fichier |

---

## 🎯 Résumé

### Ce qui fonctionne maintenant:
1. ✅ Page avec QR code dans app.py
2. ✅ QR code pointe vers Cortex Analyst (port 8502)
3. ✅ Preview visuel de l'app
4. ✅ Instructions claires pour participants

### Ce qu'il vous reste à faire:
1. 🔄 Trouver votre IP locale
2. 📝 Mettre à jour app.py ligne 214
3. 🧪 Tester avec un téléphone
4. 🎭 Répéter le script de démo

---

## 📞 Besoin d'aide?

**Voir aussi:**
- `GUIDE_QR_CODE.md` - Guide complet (configurations avancées)
- `CORTEX_ANALYST_GUIDE.md` - Guide utilisateur de l'app
- `TODO_RESTANT.md` - Liste complète des tâches

---

**Configuration prête pour la démo! 🚀**


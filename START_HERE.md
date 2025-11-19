# 🚀 START HERE - Actia x Snowflake Demo

## ✅ Ce qui a été créé

### 🎯 Applications Streamlit (Prêtes à déployer)
1. **app.py** (50KB) - Application principale de démo
   - 7 pages interactives avec couleurs Actia
   - Données hardcodées mais réalistes
   - Aucun backend nécessaire
   
2. **mobile_app.py** (8.6KB) - Dashboard mobile
   - Optimisé pour téléphones
   - Accessible via QR code
   - Temps réel simulé

### 📚 Documentation Complète
1. **README.md** - Documentation technique
2. **QUICK_START.md** - Guide démarrage rapide
3. **DEMO_SCRIPT.md** - Script minute-par-minute de présentation
4. **PROJECT_SUMMARY.md** - Résumé exécutif complet
5. **VISUAL_GUIDE.md** - Guide visuel de chaque page
6. **START_HERE.md** - Ce fichier

### 🛠️ Fichiers Support
- **requirements.txt** - Dépendances Python
- **sample_test_report.txt** - Exemple pour Document AI
- **.streamlit/config.toml** - Configuration couleurs Actia
- **.gitignore** - Exclusions Git

---

## ⚡ LANCEMENT RAPIDE (2 minutes)

### Option 1: Test Local Immédiat

```bash
# 1. Ouvrir un terminal
cd /Users/lbelmond/Desktop/EBC_27

# 2. Lancer l'app (les dépendances sont déjà installées)
streamlit run app.py
```

Votre navigateur s'ouvrira automatiquement à `http://localhost:8501`

### Option 2: Lancer aussi le mobile (optionnel)

Dans un NOUVEAU terminal:
```bash
cd /Users/lbelmond/Desktop/EBC_27
streamlit run mobile_app.py --server.port 8502
```

Dashboard mobile disponible à `http://localhost:8502`

---

## 🎬 STRUCTURE DE LA DEMO

### Flux Recommandé (20 minutes)
```
0-2 min   → 🏠 Accueil         (Établir l'urgence)
2-7 min   → 📱 Mobile + 🏭 Traçabilité  (QR code + demo)
7-12 min  → 📄 Document AI + 🤖 LLM     (IA en action)
12-15 min → 📊 Prédictions     (ML prédictif)
15-18 min → 🌐 Marketplace     (Revenus €1.2M-€2.4M)
18-20 min → Conclusion + 3 idées actionnables
```

**📖 Consultez DEMO_SCRIPT.md pour le script détaillé avec dialogues**

---

## 🎨 PAGES DE LA DEMO

### 1. 🏠 Accueil
- Contexte: Inflation (+24% Europe, +70% Tunisie)
- Concurrence: France 196 vs Chine 100
- 4 enjeux stratégiques Actia
- Promesse: IA protège marges + crée revenus

### 2. 📱 Dashboard Mobile
- **WOW EFFECT**: QR code à scanner
- Dashboard temps réel sur téléphone
- Production, qualité, alertes prix

### 3. 🏭 Traçabilité
- Besoin prioritaire DSI
- Traçabilité ascendante/descendante
- Timeline visuelle du parcours produit
- Composants + coûts + marges

### 4. 🤖 IA Conversationnelle (LLM)
- 3 questions prêtes à cliquer:
  1. Quels produits ont érosion de marge?
  2. Composants avec risque pénurie?
  3. Produits les plus profitables?
- Réponses hardcodées ultra-détaillées
- Démontre: Plus besoin d'experts Mongo!

### 5. 📊 Prédictions (ML)
- **Onglet 1**: Rentabilité produit (détecte sur-ingénierie)
- **Onglet 2**: Risque pénurie (heatmap composants)
- **Onglet 3**: Prévisions ventes (6 mois)

### 6. 🌐 Marketplace (GAME CHANGER)
- **Onglet 1**: Vendre vos données (€1.2M-€2.4M/an)
- **Onglet 2**: Acheter intelligence externe (démo import dataset)
- **Onglet 3**: ROI 7,013% sur 5 ans

### 7. 📄 Document AI
- Drag & drop `sample_test_report.txt`
- Structuration automatique
- 95% gain de temps
- SQL query généré

---

## 🎯 LES 3 IDÉES ACTIONNABLES

À présenter en conclusion:

### 1️⃣ Smart Traceability
- **Quoi**: Traçabilité end-to-end Toulouse + Tunis
- **Quand**: Q1 2026 (démarrage novembre)
- **Pour qui**: DSI (besoin prioritaire)

### 2️⃣ Profitability AI Agent
- **Quoi**: LLM qui répond "Ce produit est-il rentable?"
- **Quand**: POC Décembre 2024
- **Pour qui**: CEO (culture produit)

### 3️⃣ Marketplace Revenue Stream
- **Quoi**: Vendre données SDV trends
- **Quand**: Q2 2026
- **Pour qui**: Direction (nouveaux revenus)

---

## 📱 DÉPLOIEMENT PRODUCTION

### Streamlit Cloud (Gratuit, 5 minutes)

1. **Push sur GitHub**
   ```bash
   cd /Users/lbelmond/Desktop/EBC_27
   git init
   git add .
   git commit -m "Actia Snowflake Demo"
   git remote add origin https://github.com/VOTRE_COMPTE/actia-demo.git
   git push -u origin main
   ```

2. **Déployer sur Streamlit Cloud**
   - Aller sur https://share.streamlit.io/
   - "New app"
   - Connecter votre repo GitHub
   - Main file: `app.py`
   - Deploy!

3. **Déployer le mobile**
   - "New app" (2ème app)
   - Même repo
   - Main file: `mobile_app.py`
   - Deploy!

4. **Lier le QR code**
   - Copier l'URL de l'app mobile (ex: https://actia-mobile.streamlit.app)
   - Éditer `app.py` ligne 234
   - Remplacer `YOUR-MOBILE-APP` par votre URL
   - Commit + push

**⏱️ Temps total: 5-10 minutes**

---

## ✅ CHECKLIST PRE-DEMO

### Technique
- [ ] App principale lancée et testée
- [ ] Toutes les 7 pages fonctionnent
- [ ] QR code pointe vers le bon URL
- [ ] Testé QR code avec téléphone réel
- [ ] Fichier `sample_test_report.txt` prêt
- [ ] Connexion internet stable
- [ ] Backup: iPad avec URL mobile pré-chargé

### Présentation
- [ ] Lu DEMO_SCRIPT.md
- [ ] Mémorisé les 3 questions LLM
- [ ] Connu les 3 idées actionnables
- [ ] Timing 20 min répété
- [ ] Projecteur/TV testé

### Le Jour J
- [ ] Ouvrir `app.py` sur laptop
- [ ] Préparer téléphone pour montrer mobile
- [ ] Avoir `sample_test_report.txt` sous la main
- [ ] Timer visible
- [ ] Eau pour vous

---

## 🎨 PERSONNALISATION

### Ajouter le vrai logo Actia
1. Placer le fichier logo dans le dossier
2. Éditer `app.py` ligne 70:
   ```python
   st.sidebar.image("path/to/actia_logo.png")
   ```

### Changer les couleurs (si besoin)
Éditer `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#8BC34A"    # Vert Actia
textColor = "#424242"        # Gris Actia
```

### Ajouter de vraies données
Chercher les sections dans `app.py`:
- Ligne 300+: Données traçabilité
- Ligne 400+: Réponses LLM
- Ligne 600+: Données prédictions
- Ligne 800+: Données marketplace

---

## 🐛 TROUBLESHOOTING

### "Module not found"
```bash
pip install -r requirements.txt
```

### L'app ne se lance pas
```bash
# Vérifier l'installation Streamlit
streamlit --version

# Réinstaller si besoin
pip install --upgrade streamlit
```

### Le QR code ne marche pas
- Vérifier que l'app mobile est déployée
- Tester l'URL directement dans un navigateur
- Utiliser un iPad de backup

### Erreur upload fichier
- Vérifier que le fichier fait <200MB
- Types supportés: PDF, TXT, JPG, PNG, CSV

---

## 📖 DOCUMENTATION COMPLÈTE

### Pour Comprendre le Projet
1. **START_HERE.md** (ce fichier) - Vue d'ensemble
2. **PROJECT_SUMMARY.md** - Résumé exécutif détaillé
3. **README.md** - Documentation technique

### Pour Préparer la Demo
4. **DEMO_SCRIPT.md** - Script minute-par-minute
5. **VISUAL_GUIDE.md** - Aperçu visuel de chaque page
6. **QUICK_START.md** - Guide de démarrage rapide

**💡 Conseil: Commencez par lire DEMO_SCRIPT.md pour la présentation**

---

## 🎯 MESSAGES CLÉS

### Pour le CEO (Franck)
> "L'IA n'est pas optionnelle, c'est votre seule protection face à la Chine. Et vos données peuvent générer €1.2M-€2.4M/an via Marketplace."

### Pour le DSI
> "Traçabilité end-to-end pour novembre, consolidation Toulouse+Tunis, et fini les experts Mongo: le LLM répond en français."

### Pour le Comité
> "Schneider fait €3.2M/an, Stellantis €5.8M/an avec Marketplace. Actia peut faire pareil. Commençons en décembre."

---

## 🚀 PRÊT À DÉMARRER?

### Maintenant:
```bash
cd /Users/lbelmond/Desktop/EBC_27
streamlit run app.py
```

### Ensuite:
1. Explorer les 7 pages
2. Tester chaque fonctionnalité
3. Lire DEMO_SCRIPT.md
4. Répéter la présentation
5. Déployer sur Streamlit Cloud
6. **Convaincre Actia! 🎯**

---

## 📞 BESOIN D'AIDE?

### Commandes Utiles
```bash
# Lancer l'app principale
streamlit run app.py

# Lancer le mobile (port différent)
streamlit run mobile_app.py --server.port 8502

# Effacer le cache
streamlit cache clear

# Voir les logs
streamlit run app.py --logger.level=debug
```

### Resources
- Streamlit Docs: https://docs.streamlit.io
- Plotly: https://plotly.com/python/
- Snowflake Cortex: https://docs.snowflake.com/cortex

---

## ✨ FEATURES HIGHLIGHTS

### 🎨 Design
- ✅ Couleurs Actia (gris #424242 + vert #8BC34A)
- ✅ Graphiques Plotly interactifs
- ✅ Responsive (desktop + mobile)
- ✅ Animations fluides

### 🤖 IA
- ✅ LLM conversationnel (3 questions prêtes)
- ✅ ML prédictif (rentabilité, pénuries, ventes)
- ✅ Document AI (structuration automatique)

### 💰 Business
- ✅ ROI Marketplace: 7,013%
- ✅ Revenus potentiels: €1.2M-€2.4M/an
- ✅ 3 idées actionnables concrètes

### 📱 UX
- ✅ QR code pour mobile
- ✅ Drag & drop fichiers
- ✅ Boutons cliquables intuitifs
- ✅ Navigation sidebar claire

---

## 🎬 ACTION!

**Vous avez tout ce qu'il faut pour une demo exceptionnelle de 20 minutes.**

1. **Testez maintenant**: `streamlit run app.py`
2. **Lisez le script**: `DEMO_SCRIPT.md`
3. **Déployez**: Streamlit Cloud
4. **Convainquez Actia**: L'IA est MAINTENANT! 🚀

---

*Bonne chance avec votre démo! 🍀*

**Questions? Tout est documenté dans les fichiers .md du projet.**


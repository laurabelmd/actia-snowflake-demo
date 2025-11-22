# 🎯 PLAN D'ACTION FINAL - EBC ACTIA

## ✅ CE QUI A ÉTÉ FAIT (Analyse complète de la transcription Hugo)

### 📄 Documents créés :

1. **`PITCH_STRUCTURE_FINALE.md`** ⭐ DOCUMENT PRINCIPAL
   - Pitch complet structuré en 20 minutes
   - Framework Tell-Show-Tell pour chaque partie
   - Scripts détaillés avec roleplay (Valentin, Claire)
   - Timing précis pour chaque section
   - Vocabulaire clé du CEO (suringénierie, innovation profitable)
   - Messages de conclusion et perche à KPC

2. **`RESUME_FEEDBACKS_HUGO.md`**
   - Synthèse de tous les feedbacks de la réunion
   - Problèmes identifiés et solutions
   - Modifications par partie
   - Warnings et checklist

3. **`NOUVELLE_PARTIE2_CLAIRE.md`**
   - Spécification détaillée de l'histoire de Claire
   - Remplacement des 3 onglets séparés par UNE histoire cohérente
   - Flow complet : Contexte → Upload → Analyse → Actions → ROI

4. **`NOUVELLE_SECTION_CLAIRE_CODE.py`**
   - Code Python/Streamlit complet pour la section Claire
   - Prêt à intégrer dans `app.py`
   - Tous les éléments HTML/CSS inclus

---

## 🔑 POINTS CLÉS DES FEEDBACKS DE HUGO

### ⚠️ PROBLÈME PRINCIPAL
**"Tu es trop feature-oriented. Il faut être value-oriented."**

➡️ Ne PAS montrer des fonctionnalités  
➡️ Montrer la VALEUR BUSINESS (temps gagné, argent économisé, client conservé)

---

### 📊 STRUCTURE IMPOSÉE : TELL → SHOW → TELL

**À CHAQUE partie :**
1. **TELL (Intro)** : Annoncer le problème métier + ce qu'on va montrer
2. **SHOW (Démo)** : Montrer en live avec personnage/roleplay
3. **TELL (Conclusion)** : Résumer la valeur démontrée

---

### 🔄 MODIFICATIONS CRITIQUES

#### PARTIE 1 : L'ACTIA AUGMENTÉ ✅
- **Changement de nom** : "L'Actia Augmenté" (vs "Disponibilité de l'IA")
- **Ajout roleplay** : Introduire "Valentin" (employé usine)
- **Script 30 secondes** : "Valentin arrive, sort son téléphone, voit ses KPIs"
- **Garder** : QR code, interaction 5 min, traduction arabe

#### PARTIE 2 : TOUT DEVIENT MOTEUR POUR L'IA ⚠️ CHANGEMENT MAJEUR
**AVANT** : 3 onglets séparés (PDF, Image, Audio) = 3 mini-démos = 3 personnages = 12 min  
**APRÈS** : UNE histoire cohérente (Claire du service client) = 1 personnage = 6-7 min

**L'histoire de Claire :**
1. Client mécontent (PSA) : pièces défectueuses
2. Claire doit résoudre en 10 minutes
3. Upload simultané : PDF devis + Audio call + Photo défaut
4. Snowflake analyse et croise TOUTES les sources
5. Recommandation automatique + Email généré
6. ROI : 8 min vs 2 jours, client conservé (€2M/an)

**📁 Code prêt dans** : `NOUVELLE_SECTION_CLAIRE_CODE.py`

#### PARTIE 3 : ML & FORECASTING ✅ AJOUTS
**Problème Hugo** : "Trop statique, pas clair quel problème tu résous"

**Solutions :**
1. **Use case clair** : Forecasting production usine Toulouse
2. **Marketplace visuellement** : 3 graphes (SNP 500, Weather, Prix composants)
3. **Widgets interactifs** : Sliders pour simuler scénarios
   - Âge machine : 0-10 ans → Impact production
   - Stock composants : 30-50 → Impact rupture
   - Météo : Normal vs Canicule → Impact OEE
4. **Analyse prescriptive** : Actions recommandées automatiquement

---

## 📋 MODIFICATIONS À FAIRE DANS L'APP

### ÉTAPE 1 : Backup (✅ Déjà fait)
```bash
cd /Users/lbelmond/Desktop/EBC_27
cp app.py app_backup_avant_claire.py
```

### ÉTAPE 2 : Modifier la section "Tout est Données"

**Dans `app.py`, chercher la ligne :**
```python
elif page == "📄 Tout est Données":
```

**Remplacer tout le contenu de cette section par le code de :**
`NOUVELLE_SECTION_CLAIRE_CODE.py`

**⚠️ IMPORTANT :**
- Supprimer les 3 tabs actuels : `tabs = st.tabs([...])`
- Remplacer par la nouvelle structure avec l'histoire de Claire
- Tester que tous les uploads fonctionnent

### ÉTAPE 3 : Ajouter widgets à la Partie ML

**Dans la section ML (page "ML"), ajouter :**

```python
# Widgets de simulation
st.markdown("### 🎮 Simuler des Scénarios")

col_w1, col_w2, col_w3 = st.columns(3)

with col_w1:
    age_machine = st.slider("Âge machine (années)", 0, 10, 3)
    impact_age = 1 - (age_machine * 0.012)
    st.metric("Impact production", f"{impact_age*100:.1f}%", f"{(impact_age-1)*100:.1f}%")

with col_w2:
    stock_niveau = st.slider("Stock composants", 20, 60, 35)
    risque_rupture = max(0, (40 - stock_niveau) / 2)
    st.metric("Risque rupture", f"{risque_rupture:.1f}%", f"{-risque_rupture if stock_niveau > 35 else risque_rupture:.1f}%")

with col_w3:
    meteo = st.select_slider("Météo", options=["Normal", "Chaud", "Canicule"])
    oee_impact = {"Normal": 89, "Chaud": 82, "Canicule": 76}
    st.metric("OEE prévu", f"{oee_impact[meteo]}%", f"{oee_impact[meteo] - 89}%")
```

### ÉTAPE 4 : Ajouter graphes Marketplace

**Créer 3 graphes :**
1. **SNP 500 Automotive** (historique + prévisions)
2. **Weather Data Toulouse** (7 jours)
3. **Prix composants** (tendance inflation)

**Code exemple :**
```python
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Graphe SNP 500
dates_snp = [(datetime.now() - timedelta(days=30-i)).strftime('%Y-%m-%d') for i in range(40)]
values_snp = [3800 + random.randint(-100, 100) for _ in range(30)] + [3750, 3720, 3700, 3680, 3660, 3640, 3620, 3600, 3580, 3560]

fig_snp = go.Figure()
fig_snp.add_trace(go.Scatter(x=dates_snp[:30], y=values_snp[:30], name="Historique", line=dict(color=ACTIA_GREEN)))
fig_snp.add_trace(go.Scatter(x=dates_snp[29:], y=values_snp[29:], name="Prévision", line=dict(color='red', dash='dash')))
fig_snp.update_layout(title="📈 S&P 500 Automotive - Impact sur commandes futures", height=300)
st.plotly_chart(fig_snp, use_container_width=True)
```

---

## 📅 PLANNING RECOMMANDÉ

### Lundi 25/11 (AUJOURD'HUI)
- [ ] **Lire tous les documents** (PITCH_STRUCTURE_FINALE.md prioritaire)
- [ ] **Session avec Antoine** (feedbacks pitch + Actia)
- [ ] **Intégrer section Claire** dans app.py
- [ ] **Tester** que ça fonctionne localement

### Mardi 26/11 (MATIN)
- [ ] **Dry-run avec Hugo 1h** (chronométré !)
- [ ] Ajustements timing selon feedbacks
- [ ] Finir widgets Partie 3
- [ ] Préparer scripts roleplay (Valentin + Claire)

### Mercredi 27/11 (OFF - Répétition)
- [ ] Répétition solo du pitch complet
- [ ] Chronométrer : objectif 20-22 minutes
- [ ] Mémoriser transitions Tell-Show-Tell
- [ ] Tester QR code sur plusieurs téléphones
- [ ] Préparer backup (screenshots si réseau défaillant)

### Jeudi 28/11
- [ ] **🚀 EBC ACTIA - DEMO DAY !**

---

## 🎯 VOCABULAIRE CLÉ À UTILISER (CEO Fabien Trinité)

**À placer dans le pitch :**
- ✅ **"Suringénierie"** → "Éviter la suringénierie pour une innovation PROFITABLE"
- ✅ **"Innovation profitable"** → Ne PAS dire juste "innovation"
- ✅ **"Market relevance"** → Pertinence marché
- ✅ **"Robustesse ET agilité"** → Équilibre des deux
- ✅ **"Cycle de vie du produit"** → De la conception à la vente
- ✅ **"ROI immédiat"** → Vs investissement long terme

**Exemples de phrases :**
> "Chez Actia, vous ne voulez pas de suringénierie. Vous voulez une **innovation PROFITABLE** avec un **ROI immédiat**."

> "Chaque produit doit avoir une **market relevance** tout au long de son **cycle de vie**."

---

## ⏱️ TIMING FINAL OBJECTIF

| Section | Durée | Notes |
|---------|-------|-------|
| **Introduction** | 2 min | Accroche + annonce plan |
| **Partie 1 : Actia Augmenté** | 5-6 min | QR code + roleplay Valentin + interaction |
| **Partie 2 : Tout est moteur IA** | 6-7 min | Histoire Claire (PDF+Audio+Image) |
| **Partie 3 : ML & Forecasting** | 5-6 min | Widgets + Marketplace + Prescriptive |
| **Conclusion** | 1-2 min | Résumé + perche KPC |
| **TOTAL** | **19-23 min** | ✅ DANS LES TEMPS |

---

## 🎬 SCRIPTS ROLEPLAY

### Script Valentin (Partie 1 - 30 secondes)

> "Imaginez Valentin, responsable de ligne à l'usine de Toulouse.  
> Chaque matin, avant même d'enfiler sa blouse, il sort son téléphone.  
> Il scanne le QR code affiché dans l'atelier.  
> Et en 5 secondes, il voit :  
> - Sa production du jour : 1,247 composants  
> - Son taux de qualité : 98.4%  
> - Son OEE : 89.2%  
> 
> S'il a besoin de creuser, il pose une question au chatbot.  
> Pas besoin de créer un dashboard, pas besoin d'attendre 2 jours.  
> C'est ça, **l'Actia Augmenté de demain**."

### Script Claire (Partie 2 - Introduction 1 min)

> "Maintenant, parlons de Claire, du service client.  
> Lundi matin, 9h05, elle reçoit un appel de PSA Peugeot-Citroën.  
> Un client stratégique : 2 millions d'euros de chiffre d'affaires par an.  
> 
> Le problème : 50 modules TGX-2847 reçus ce matin, TOUS défectueux.  
> Production PSA arrêtée. Coût : 15 000 euros par jour.  
> Le client exige un geste commercial immédiat, sinon clause de pénalité.  
> 
> Claire a 10 minutes pour comprendre :  
> - Quel était le devis ? (PDF)  
> - Qu'a dit le client au téléphone ? (Audio)  
> - Y a-t-il vraiment un défaut ? (Photo)  
> - Quelle action prendre ?  
> 
> **Regardez comment Snowflake l'aide à résoudre ça en 8 minutes.**"

---

## ⚠️ WARNINGS DE HUGO (NE PAS OUBLIER !)

### 1. Timing serré
> "Tu as beaucoup de contenu pour 20 min. C'est dense."

**Action** : Se chronométrer, supprimer redondances

### 2. Cortex Analyst mobile
> "Dommage de pas avoir le vrai. Mais priorité : démos fonctionnelles + narrative."

**Action** : Si temps, fixer. Sinon, garder fake data (fonctionne à 100%)

### 3. Réseau Station F
> "Attention au réseau pendant la démo."

**Action** : Tester sur 4G/5G, préparer screenshots backup

### 4. Créer des histoires, pas montrer des features
> "Le PDF/Audio/Image, faut pas que ce soient des trucs décousus. UNE histoire."

**Action** : ✅ Fait avec Claire !

---

## 📞 NEXT STEPS AVEC L'ÉQUIPE

### Avec Hugo (Mardi matin)
- Dry-run chronométré
- Feedback sur transitions
- Synchronisation : phrases choc + perches

### Avec Antoine (Lundi)
- Feedbacks pitch général
- Insights Actia supplémentaires

### Avec Florian
- Atelier SQ Actia (dans 2.5 semaines)
- Problématique sécurité interne

### Avec KPC
- Alignment messaging Use Cases
- Partie Transformation + Data Office
- Perche de conclusion

---

## 🎯 OBJECTIF FINAL

**NE PAS VENDRE** Snowflake comme technologie  
**VENDRE** :
- ⏱️ Du temps gagné (95% sur résolution problèmes)
- 💰 Des coûts évités (€180K/an, clients conservés)
- 📈 Des marges préservées (anticipation vs réaction)
- 🚀 Une innovation PROFITABLE (market relevance)
- 🤝 Une adoption métier réussie (avec KPC)

---

## ✅ CHECKLIST FINALE AVANT EBC

### Technique
- [ ] App mobile charge rapidement (test 4G/5G)
- [ ] QR code testé (iPhone + Android)
- [ ] Section Claire intégrée et testée
- [ ] Widgets Partie 3 fonctionnels
- [ ] Graphes Marketplace affichés
- [ ] Vidéo usine Actia (8 sec) prête
- [ ] Backup screenshots si réseau défaillant

### Contenu
- [ ] Script Valentin mémorisé (30 sec)
- [ ] Script Claire mémorisé (1 min intro + flow)
- [ ] Transitions Tell-Show-Tell écrites
- [ ] Vocabulaire CEO intégré (suringénierie, etc.)
- [ ] Conclusion avec perche KPC

### Logistique
- [ ] QR codes imprimés (grand format pour scans)
- [ ] Laptop chargé + chargeur
- [ ] Connexion backup (hotspot téléphone)
- [ ] Eau / café pour vous !

---

## 🚀 VOUS AVEZ TOUS LES ÉLÉMENTS !

**Documents à lire dans l'ordre :**
1. **`PITCH_STRUCTURE_FINALE.md`** ⭐ (Le plus important !)
2. **`RESUME_FEEDBACKS_HUGO.md`** (Comprendre les changements)
3. **`NOUVELLE_PARTIE2_CLAIRE.md`** (Spécifications détaillées)
4. **`NOUVELLE_SECTION_CLAIRE_CODE.py`** (Code à intégrer)

**Vous êtes prête !** 🎉

La base technique est solide. Maintenant il faut transformer ça en **démo BUSINESS** avec des **histoires** (Valentin, Claire) qui montrent la **VALEUR**, pas les features.

**Bonne chance pour l'EBC ! 🚀**


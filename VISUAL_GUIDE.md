# 🎨 Guide Visuel - Actia x Snowflake Demo

Ce document décrit visuellement chaque page de la démo pour vous aider à naviguer et présenter efficacement.

---

## 🏠 Page 1: ACCUEIL

### Layout
```
┌─────────────────────────────────────────────────────────────┐
│             ❄️ Snowflake x Actia                           │
│     Transformation Digitale & IA pour la Compétitivité     │
└─────────────────────────────────────────────────────────────┘

┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ 🚨 L'URGENCE │  │ 🇨🇳 CONCURR. │  │ 💡 SOLUTION  │
│              │  │              │  │              │
│  +24%  +70% │  │  196 vs 100  │  │     IA       │
│  Europe Tun. │  │  France/Chine│  │  Protection  │
└──────────────┘  └──────────────┘  └──────────────┘

        🎯 Les 4 Enjeux Stratégiques
┌─────────────────────┐  ┌─────────────────────┐
│ 1️⃣ Expérience Client│  │ 2️⃣ Compétitivité    │
│ • Services MCO/MCS  │  │ • IA productivité   │
│ • Supply Chain      │  │ • Robustesse        │
└─────────────────────┘  └─────────────────────┘
┌─────────────────────┐  ┌─────────────────────┐
│ 3️⃣ Culture Produit  │  │ 4️⃣ Market Relevance │
│ • Fin sur-ingénierie│  │ • Valorisation data │
│ • Rentabilité       │  │ • Vitesse innovation│
└─────────────────────┘  └─────────────────────┘

╔═══════════════════════════════════════════════════╗
║ 🚀 Comment Snowflake + IA protège vos marges    ║
║    et crée de nouveaux flux de revenus           ║
╚═══════════════════════════════════════════════════╝
```

### Couleurs
- Cartes urgence: Gradient gris → vert foncé
- Enjeux 1 & 3: Bordure gauche verte
- Enjeux 2 & 4: Bordure gauche grise
- Banner final: Gradient vert clair → vert foncé

### Actions
- Aucune interaction
- Page de contexte et accroche

---

## 📱 Page 2: DASHBOARD MOBILE

### Layout
```
┌──────────────────────────────────────────────────┐
│      📱 Expérience Mobile Interactive            │
└──────────────────────────────────────────────────┘

COLONNE GAUCHE:               COLONNE DROITE:
┌─────────────────┐          ┌─────────────────┐
│ ✨ SCANNEZ QR   │          │ 👀 APERÇU       │
│                 │          │                 │
│  [QR CODE]      │          │  [MOCKUP PHONE] │
│  400x400        │          │                 │
│                 │          │  • Production   │
│                 │          │  • Alertes prix │
└─────────────────┘          │  • Qualité      │
┌─────────────────┐          └─────────────────┘
│ 📲 Accès à:     │
│ • Traçabilité   │
│ • Prix composants│
│ • Alertes qualité│
└─────────────────┘
```

### Éléments Clés
- **QR Code**: Généré dynamiquement via API qrserver.com
- **Mockup**: Cadre gris foncé simulant un téléphone
- **Inside mockup**: 
  - Header "Actia Live"
  - Carte verte: Production du jour
  - Carte grise: Alerte prix
  - Carte grise: Qualité

### Actions
- Participants scannent le QR code
- S'ouvre dans leur navigateur mobile
- Dashboard mobile app se lance

---

## 🏭 Page 3: TRAÇABILITÉ

### Layout
```
┌──────────────────────────────────────────────────┐
│      🏭 Traçabilité Intelligente                 │
│      Traçabilité ascendante et descendante       │
└──────────────────────────────────────────────────┘

[Produit ▼]  [Usine ▼]  [Date 📅]
  TGX-001     Toulouse   2024-11-17

         [🔍 TRACER LE PRODUIT]

┌─────────────────────────────────────────────────┐
│ ✅ Traçabilité complète trouvée                 │
└─────────────────────────────────────────────────┘

COLONNE GAUCHE (66%):        COLONNE DROITE (33%):
🛤️ Parcours du Produit       🔩 Composants Utilisés
┌─────────────────────┐      ┌──────────────────┐
│  Réception ●────────│      │ PCB-2847-A       │
│  Assemblage ●───────│      │ Resistor-R45     │
│  Test       ●───────│      │ Capacitor-C89    │
│  Intégration●───────│      │ IC-Chip-2024     │
│  Test Final ●───────│      │ Connector-X12    │
│  Expédition ●       │      └──────────────────┘
└─────────────────────┘      ┌──────────────────┐
                             │ 💰 Coût Total    │
Tableau détaillé:            │   €79.95         │
Date | Statut | Opérateur    │   Marge: 42%     │
                             └──────────────────┘
```

### Visuels
- **Timeline**: Plotly scatter + lines, cercles verts
- **Tableau parcours**: 6 lignes (étapes de production)
- **Tableau composants**: 5 lignes avec flags pays
- **Carte coût**: Fond gris clair, chiffres verts

### Actions
1. Sélectionner produit dans dropdown
2. Cliquer "Tracer le Produit"
3. Animation spinner 1.5 sec
4. Affichage timeline + données

---

## 🤖 Page 4: IA CONVERSATIONNELLE

### Layout
```
┌──────────────────────────────────────────────────┐
│      🤖 Assistant IA Snowflake Cortex            │
│      Interrogez vos données en langage naturel   │
└──────────────────────────────────────────────────┘

💡 Questions Suggérées:
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ 📉 Érosion   │ │ 📦 Pénurie   │ │ 💰 Profitable│
│   marge?     │ │   risque?    │ │   produits?  │
└──────────────┘ └──────────────┘ └──────────────┘

┌─────────────────────────────────────────────────┐
│ 👤 USER: Quels produits ont érosion de marge?  │
└─────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ ❄️ ASSISTANT:                                   │
│                                                 │
│ 📊 Analyse de l'érosion de marge - Q3 2024    │
│                                                 │
│ 🚨 Top 3 produits avec érosion critique:       │
│                                                 │
│ 1. TGX-ECU-2024                                │
│    Marge Q2: 45% → Q3: 28% (-17 points)       │
│    Cause: Augmentation prix semiconducteurs    │
│    Impact: -€240K de marge                     │
│                                                 │
│ 2. Actia Connect Pro                           │
│    Marge Q2: 38% → Q3: 22% (-16 points)       │
│    Cause: Sur-ingénierie (fonctions non utilis)│
│    Impact: -€180K                              │
│ ...                                             │
└─────────────────────────────────────────────────┘

💬 Historique de Conversation (4 derniers messages)
```

### Éléments Clés
- **3 boutons suggérés**: Cliquables, largeur égale
- **Chat interface**: Style ChatGPT
- **Messages user**: Fond par défaut
- **Messages assistant**: Avatar ❄️, réponses formatées Markdown
- **Input**: En bas, "Posez votre question..."

### Réponses Prêtes
1. **Érosion marge**: 3 produits avec causes + recommandations
2. **Pénurie**: Tableau 5 composants, analyse géopolitique, impact €1.2M
3. **Profitable**: Top 5 avec revenus cycle de vie, insight services connectés

### Actions
- Cliquer sur un bouton suggéré OU
- Taper une question personnalisée
- Animation "Analyse des données Snowflake..." 2 sec
- Réponse s'affiche avec formatage

---

## 📊 Page 5: PRÉDICTIONS

### 3 Onglets

#### Onglet 1: 🎯 Rentabilité Produit
```
COLONNE GAUCHE (66%):              COLONNE DROITE (33%):
Profit Net Prédit (5 ans)         ┌──────────────────┐
                                   │ ✅ Modèle ML Actif│
TGX Gateway     ████████ €6.4M    │ Précision: 94.3% │
SmartConnect    ██████ €4.7M      │ Données: 847 prod│
EcoLogic        ████ €3.2M        └──────────────────┘
DiagBox         ███ €2.8M         ┌──────────────────┐
PowerControl    ███ €2.4M         │🚨 Alerte         │
NewProduct X    ██ €1.2M          │ Sur-Ingénierie   │
NewProduct Y    █ €0.8M (ROUGE)   │                  │
                                   │ NewProduct Y     │
                                   │ Complexité: +++  │
                                   │ ROI: NÉGATIF     │
                                   │ Action: Annuler  │
                                   └──────────────────┘
```
- **Graphique**: Bar chart horizontal Plotly
- **Couleurs**: Vert (>€3M), Gris (€2-3M), Rouge (<€2M)

#### Onglet 2: ⚠️ Risque Pénurie
```
COLONNE GAUCHE (75%):              COLONNE DROITE (25%):
Carte de Chaleur - Risque (%)     ┌──────────────────┐
                                   │ 🔴 CRITIQUE      │
         Sem47 Sem48 Sem49 Sem50  │ IC-NXP-2847      │
IC-NXP    85%   90%   92%   95%   │ Risque: 95%      │
PCB       78%   82%   88%   90%   │ Délai: 2 semaines│
Capacitor 65%   70%   72%   75%   └──────────────────┘
Connector 60%   58%   62%   65%   ┌──────────────────┐
Sensor    45%   48%   50%   52%   │ 🟠 ÉLEVÉ         │
Display   30%   32%   28%   30%   │ PCB-Advanced     │
Battery   25%   22%   20%   18%   │ Risque: 90%      │
Cable     15%   14%   12%   10%   └──────────────────┘
                                   ┌──────────────────┐
                                   │ 🟢 OK            │
                                   │ 5 composants     │
                                   └──────────────────┘
```
- **Heatmap**: Vert (safe) → Jaune → Rouge (danger)
- **Chiffres**: Affichés dans chaque cellule

#### Onglet 3: 🔮 Prévision Ventes
```
         Prévision Ventes Quotidiennes (unités)

150 ┤                          ╱╱╱╱╱╱╱╱╱
    │                      ╱╱╱╱    ╱╱╱╱
    │                  ╱╱╱╱    ╱╱╱╱
120 │              ╱╱╱╱    ╱╱╱╱         [Zone verte
    │          ╱╱╱╱    ╱╱╱╱              de confiance]
    │      ╱╱╱╱────────────
 90 │  ────────           └── Prévision ML (vert pointillé)
    │ Historique (gris)
    └───────────────────────────────────────
    Nov   Dec   Jan   Feb   Mar   Avr

┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ 📈 Croissance│ │ 💰 Revenus   │ │ 🎯 Confiance │
│    +12.4%    │ │   €18.7M     │ │    91.2%     │
│  +2.1% vs Q4 │ │   +€2.1M     │ │   Élevée     │
└──────────────┘ └──────────────┘ └──────────────┘
```

---

## 🌐 Page 6: MARKETPLACE

### 3 Onglets

#### Onglet 1: 💰 Vendre vos Données
```
┌─────────────────────────────────────────────────┐
│ 🚀 Vos données ont de la valeur!                │
└─────────────────────────────────────────────────┘

COLONNE GAUCHE:                COLONNE DROITE:
┌─────────────────────┐       ┌─────────────────────┐
│📦 Dataset 1:        │       │📦 Dataset 3:        │
│ Automotive Benchmrks│       │ SDV Trends & Usage  │
│                     │       │                     │
│ Contenu:            │       │ Contenu:            │
│ • Temps production  │       │ • Télématique       │
│ • Taux défauts      │       │ • Patterns usage    │
│ • Coûts composants  │       │ • Performance soft. │
│                     │       │                     │
│ 🎯 OEMs, conseils   │       │ 🎯 OEMs, startups   │
│ 💰 €15K/an          │       │ 💰 €35K/an          │
│ 📊 25-40 clients    │       │ 📊 30-50 clients    │
└─────────────────────┘       │ 🔥 FORTE DEMANDE    │
┌─────────────────────┐       └─────────────────────┘
│📦 Dataset 2:        │       ┌─────────────────────┐
│ Supply Chain Intel. │       │ 💰 REVENU ANNUEL    │
│                     │       │  €1.2M - €2.4M      │
│ Contenu:            │       │                     │
│ • Évolution prix    │       │ Basé sur demande    │
│ • Fiabilité fournis.│       │ marché & benchmarks │
│                     │       └─────────────────────┘
│ 💰 €22K/an          │
└─────────────────────┘
```

#### Onglet 2: 🛒 Acheter Intelligence
```
┌─────────────────────────────────────────────────┐
│ 🌍 Enrichissez vos analyses avec données externes│
└─────────────────────────────────────────────────┘

┌──────────────────────────────────┐ ┌──────────┐
│ 🌐 Geopolitical Risk Intelligence│ │ €18K/an  │
│ Provider: McKinsey & Company     │ │          │
│ • Risques géopolitiques temps réel│ │ Économies│
│ • Impact supply chain            │ │ €500K/an │
│ ✅ Anticiper pénuries composants │ └──────────┘
└──────────────────────────────────┘

┌──────────────────────────────────┐ ┌──────────┐
│ 📊 Global Component Pricing      │ │ €25K/an  │
│ Provider: IHS Markit             │ │          │
│ • Prix composants worldwide      │ │ Économies│
│ ✅ Optimiser négociations        │ │ €780K/an │
└──────────────────────────────────┘ └──────────┘

        [▶️ IMPORTER 'GEOPOLITICAL RISK']

┌─────────────────────────────────────────────────┐
│ ⚠️ Alerte Géopolitique Détectée                 │
│ Composant: IC-NXP-2847                          │
│ 🌍 Origine: Taiwan (80% approvisionnement)      │
│ ⚠️ Risque Chine-Taiwan: Élevé (78/100)         │
│ 💡 Recommandation: Double-sourcing + Stock 4 mois│
│ 💰 Impact évité: €2.4M                          │
└─────────────────────────────────────────────────┘
```

#### Onglet 3: 📊 Revenus Potentiels
```
COLONNE GAUCHE (66%):              COLONNE DROITE (33%):
Projection Revenus (5 ans)        ┌──────────────────┐
                                   │   🎯 ROI Total   │
€2500K ┤              ████         │                  │
       │           ████            │     7,013%       │
€2000K ┤        ████               │                  │
       │     ████                  │   sur 5 ans      │
€1500K ┤  ████                     └──────────────────┘
       │████                       ┌──────────────────┐
€1000K ████                        │ 📈 Métriques Clés│
       │                           │                  │
  €500K                            │ Break-even: 2 mois│
       └────────────────           │ Marge nette: 94% │
        An1 An2 An3 An4 An5        │ Clients: 70-115  │
                                   └──────────────────┘
Calcul ROI:                        ┌──────────────────┐
┌──────────────────────────┐      │✅ Benchmark Sect.│
│ Revenus Vente   €7.47M ↗️│      │ Schneider: €3.2M │
│ Économies       €3.20M ↗️│      │ Bosch: €5.8M     │
│ Investissement -€0.15M ↘️│      │ Continental:€4.1M│
│ ROI Net        €10.52M 🎯│      │ Actia: €2.4M/an  │
└──────────────────────────┘      └──────────────────┘
```

---

## 📄 Page 7: DOCUMENT AI

### Layout
```
┌──────────────────────────────────────────────────┐
│      📄 Snowflake Document AI                    │
│      Structurez vos données non-structurées      │
└──────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────┐
│ 🎯 Cas d'usage Actia:                           │
│ • Testeurs → Structuration auto                 │
│ • Images composants → Extraction métadonnées    │
│ • Factures → Intégration comptable              │
└─────────────────────────────────────────────────┘

        📤 Glissez-Déposez vos Documents
┌─────────────────────────────────────────────────┐
│                                                 │
│       [DRAG & DROP ZONE]                        │
│   PDF, TXT, Images (JPG, PNG), CSV             │
│                                                 │
└─────────────────────────────────────────────────┘

APRÈS UPLOAD:

COLONNE GAUCHE (50%):           COLONNE DROITE (50%):
📄 Document Original            ✨ Données Structurées (AI)

ℹ️ Fichier: test_report.txt    [🚀 LANCER DOCUMENT AI]
   Taille: 986 bytes
                                 [Progress bar: ████████ 100%]
┌───────────────────────┐      
│ TEST REPORT           │       ✅ Document structuré!
│ COMPOSANT TGX-2847-A  │      
│                       │       ┌──────────────────────┐
│ Date: 2024-11-15      │       │ Type  | Valeur       │
│ Operateur: QC-12      │       ├──────────────────────┤
│ Usine: Toulouse       │       │ Date  | 2024-11-15   │
│                       │       │ Opér. | QC-12        │
│ Tension: 3.3V - PASS  │       │ Usine | Toulouse     │
│ Current: 450mA - PASS │       │ Tens. | 3.3V ✅ PASS │
│ ...                   │       │ Curr. | 450mA ✅     │
└───────────────────────┘       │ Qualité| 98.7% ✅    │
                                 │ Décis.| APPROUVÉ ✅  │
                                 │ Coût  | €45.20       │
                                 └──────────────────────┘

                                 ┌──────────┐ ┌──────────┐
                                 │⚡95% Gain│ │🎯 99.2%  │
                                 │  Temps   │ │ Précision│
                                 └──────────┘ └──────────┘

                                 💾 SQL Query:
                                 SELECT component_id,
                                        quality_score,
                                        test_date
                                 FROM actia.quality_tests
                                 WHERE quality_score > 95
```

### Éléments Clés
- **File uploader**: Zone drag & drop native Streamlit
- **Aperçu texte**: Text area disabled avec contenu brut
- **Bouton**: Vert Actia, pleine largeur
- **Progress bar**: Animation 0-100%
- **Tableau structuré**: DataFrame avec 16 lignes
- **Métriques**: 2 cartes (gain temps + précision)
- **SQL**: Code block avec syntax highlighting

### Actions
1. Uploader `sample_test_report.txt`
2. Cliquer "Lancer Document AI"
3. Progress bar anime 2 secondes
4. Affichage données structurées + métriques

---

## 📱 Mobile App (Accessible via QR Code)

### Layout
```
╔═══════════════════════════════════╗
║     📱 Actia Live                 ║
║  Dashboard Temps Réel             ║
╚═══════════════════════════════════╝

[🔄 Actualiser]

[Sélectionner Usine: Toulouse ▼]

┌─────────────────────────────────┐
│ 🏭 Production Aujourd'hui       │ (Vert)
│       1,247                     │
│  composants traités             │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ ✅ Taux Qualité                 │ (Gris)
│      98.7%                      │
│    conformité                   │
└─────────────────────────────────┘

💰 Alertes Prix Composants

┌─────────────────────────────────┐
│ 🚨 IC-NXP-2847            (Rouge)│
│     +15% cette semaine          │
│  Action requise                 │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ ⚠️ PCB-Advanced        (Orange) │
│     +12% cette semaine          │
│  À surveiller                   │
└─────────────────────────────────┘

📊 Tendance Production (7j)
[Graphique ligne verte]

🔧 Derniers Composants
[Tableau 5 lignes]

🎯 Qualité par Station
[Bar chart horizontal]

🔍 Traçabilité Rapide
[Input texte]

┌─────────────────────────────────┐
│ 🟢 Système actif | 15:42:30     │
└─────────────────────────────────┘
```

### Optimisations Mobile
- Police 18px minimum
- Boutons tactiles (48px min height)
- Pas de hover effects
- Scroll vertical naturel
- Graphs simplifiés (moins de points)

---

## 🎨 Palette Complète

### Couleurs Principales
```css
ACTIA_GREEN:       #8BC34A  ████████ (Vert feuille)
ACTIA_GREY:        #424242  ████████ (Gris foncé)
ACTIA_LIGHT_GREY:  #E0E0E0  ████████ (Gris clair)
ACTIA_DARK_GREEN:  #689F38  ████████ (Vert foncé)
```

### Couleurs Système
```css
Success:  #8BC34A  ████████ (Vert Actia)
Warning:  #FF9800  ████████ (Orange)
Error:    #F44336  ████████ (Rouge)
Info:     #424242  ████████ (Gris Actia)
```

### Gradients
```css
Gradient 1: linear-gradient(135deg, #424242 0%, #689F38 100%)
           (Gris → Vert foncé)

Gradient 2: linear-gradient(135deg, #8BC34A 0%, #689F38 100%)
           (Vert clair → Vert foncé)
```

---

## 🎯 Tips Navigation

### Ordre Recommandé
1. 🏠 Accueil (contexte)
2. 📱 Dashboard Mobile (QR code)
3. 🏭 Traçabilité (démonstration)
4. 📄 Document AI (drag & drop)
5. 🤖 IA Conversationnelle (3 questions)
6. 📊 Prédictions (3 onglets)
7. 🌐 Marketplace (focus revenus)
8. 🏠 Accueil (conclusion)

### Raccourcis Clavier
- `Ctrl/Cmd + R`: Recharger page
- `F11`: Plein écran (présentation)
- `Esc`: Sortir plein écran

### URLs Directes (une fois déployé)
```
https://actia-demo.streamlit.app/?page=home
https://actia-demo.streamlit.app/?page=mobile
https://actia-demo.streamlit.app/?page=traceability
(etc.)
```

---

## ✅ Checklist Visuelle

Avant la demo, vérifier:
- [ ] Toutes les cartes ont les bonnes couleurs
- [ ] Les graphiques s'affichent correctement
- [ ] Les boutons sont cliquables
- [ ] Le QR code est scannable
- [ ] Les onglets changent bien
- [ ] L'upload de fichier fonctionne
- [ ] Le texte est lisible sur projecteur
- [ ] Pas d'éléments tronqués

---

*Guide créé pour faciliter la présentation | Novembre 2024*


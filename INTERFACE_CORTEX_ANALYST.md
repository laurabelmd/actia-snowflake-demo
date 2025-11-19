# 🎨 Interface Cortex Analyst - Vue d'ensemble

## 📱 Aperçu de l'interface

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                          ┃
┃         🤖 Actia Cortex Analyst                         ┃
┃   Intelligence artificielle pour vos données            ┃
┃              de production                               ┃
┃                                                          ┃
┃  (Dégradé Gris #424242 → Vert #8BC34A)                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┌──────────────────────────────────────────────────────────┐
│ 🏭 Sélectionner l'usine: [Toulouse ▼]                   │
└──────────────────────────────────────────────────────────┘

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃           📊 Dashboard en Temps Réel                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┌──────────┬──────────┬──────────┬──────────┐
│   🏭     │   ✅     │   ⚡     │   🚨     │
│Production│ Qualité  │Efficacité│ Alertes  │
│          │          │          │          │
│  1,247   │  98.4%   │  89.2%   │    3     │
│composants│conformité│   OEE    │ actives  │
└──────────┴──────────┴──────────┴──────────┘
    (Dégradé Gris → Vert pour chaque carte)

┌─────────────────────────┬─────────────────────────┐
│ 📈 Production (7 jours) │ 🎯 Qualité par Station  │
│                         │                         │
│  1400 ┤    ╱•           │ Assemblage    ████ 99.2│
│       │   •             │ Test Élec.    ████ 98.7│
│  1300 ┤  •   •          │ Intégration   ███  97.8│
│       │ •     •         │ Test Final    ████ 99.5│
│  1200 ┤•       •        │                         │
│       └────────────     │  90%        100%        │
│       Lu Ma Me Je Ve    │                         │
└─────────────────────────┴─────────────────────────┘

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     💬 Interrogez vos données avec Cortex Analyst       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┌──────────────────────────────────────────────────────────┐
│ 💡 Posez vos questions en langage naturel - Cortex      │
│    Analyst analysera vos données et vous répondra.      │
└──────────────────────────────────────────────────────────┘

    Questions suggérées:
┌──────────────┬──────────────┬──────────────┐
│ [📊 Quel est │ [🔍 Quels   │ [📈 Quelle   │
│ le taux de   │ composants   │ est la       │
│ qualité...?] │ ont des...?] │ tendance...?]│
└──────────────┴──────────────┴──────────────┘

┌──────────────────────────────────────────────────────────┐
│                 💬 Zone de chat                          │
│                                                          │
│  👤 Vous: Quel est le taux de qualité ce mois?          │
│  ┌────────────────────────────────────────────┐         │
│  │ (Message utilisateur en vert #8BC34A)      │         │
│  └────────────────────────────────────────────┘         │
│                                                          │
│           🤖 Cortex Analyst:                            │
│  ┌────────────────────────────────────────────┐         │
│  │ 📊 Analyse de qualité pour Toulouse:       │         │
│  │                                             │         │
│  │ • Taux moyen: 98.4%                        │         │
│  │ • Évolution: +0.8% vs mois dernier         │         │
│  │ • Meilleure station: Test Final (99.5%)    │         │
│  │ • Station à surveiller: Intégration        │         │
│  │                                             │         │
│  │ Détails par composant:                     │         │
│  │ - TGX-2847: 99.1% (excellent)              │         │
│  │ - ECU-2024: 98.2% (normal)                 │         │
│  │ - PCB-1123: 97.5% (légère baisse)          │         │
│  │                                             │         │
│  │ 💡 Recommandation: Audit recommandé        │         │
│  └────────────────────────────────────────────┘         │
│  (Message assistant fond blanc, bordure gris)           │
│                                                          │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ Votre question:                                          │
│ [Ex: Quelle est la production totale cette semaine?   ] │
└──────────────────────────────────────────────────────────┘

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃               📋 Activité Récente                        ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

┌─────┬──────────────┬─────────────┬────────┬─────────┐
│Heure│  Composant   │   Station   │ Statut │ Qualité │
├─────┼──────────────┼─────────────┼────────┼─────────┤
│15:42│ TGX-2847-A   │ Test Final  │ ✅ OK  │  99%    │
│15:38│ ECU-2024-456 │ Intégration │ ✅ OK  │  98%    │
│15:35│ PCB-1123     │ Assemblage  │ ✅ OK  │  100%   │
│15:31│ IC-Chip-2024 │ Test Élec.  │ ✅ OK  │  97%    │
│15:28│ Sensor-T89   │ Assemblage  │ ✅ OK  │  99%    │
└─────┴──────────────┴─────────────┴────────┴─────────┘

┌──────────────────────────────────────────────────────────┐
│ 🟢 Système actif | Dernière mise à jour: 15:43:21       │
└──────────────────────────────────────────────────────────┘

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃          ❄️ Snowflake x Actia                           ┃
┃     Powered by Snowflake Cortex Analyst                 ┃
┃         (Fond gris #424242, texte blanc)                ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

---

## 🎨 Palette de couleurs

### Couleurs principales
```
┌─────────────────┬──────────┬─────────────────────┐
│ Nom             │ Hex      │ Usage               │
├─────────────────┼──────────┼─────────────────────┤
│ ACTIA_GREEN     │ #2EB873  │ Boutons, accents    │
│ ACTIA_GREY      │ #424242  │ Textes, header      │
│ ACTIA_LIGHT_GREY│ #E0E0E0  │ Fond info box       │
│ ACTIA_DARK_GREEN│ #1E8B57  │ Dégradés, hover     │
└─────────────────┴──────────┴─────────────────────┘
```

### Exemples visuels

#### Bouton principal
```
┌────────────────────────────────┐
│  📊 Quel est le taux de...?   │  ← Fond: #2EB873
│                                │     Texte: Blanc
└────────────────────────────────┘     Hover: #1E8B57
```

#### Message utilisateur (chat)
```
                    ┌──────────────────┐
                    │ Ma question ici  │  ← Fond: #2EB873
                    └──────────────────┘     Texte: Blanc
                                             Align: Droite
```

#### Message assistant (chat)
```
┌──────────────────┐
│ Réponse de l'IA  │  ← Fond: Blanc
└──────────────────┘     Bordure: #E0E0E0
                         Texte: #424242
                         Align: Gauche
```

#### Carte métrique
```
┌─────────────────────┐
│   Dégradé           │  ← Top: #424242
│   Gris → Vert       │     Bottom: #1E8B57
│                     │     Texte: Blanc
│      1,247          │     Shadow: 0 4px 6px
│   composants        │
└─────────────────────┘
```

---

## 📐 Dimensions et espacements

### Layout principal
- **Largeur**: 100% (responsive)
- **Padding général**: 10px
- **Margin entre sections**: 20-40px
- **Border radius**: 15px (cartes), 10px (boutons)

### Dashboard metrics
- **Colonnes**: 4 (égales)
- **Hauteur cartes**: Auto
- **Padding interne**: 20px
- **Gap entre colonnes**: 10px

### Graphiques
- **2 colonnes** (50/50)
- **Hauteur**: 250-300px
- **Margin bottom**: 20px

### Zone chat
- **Largeur messages**: Max 80%
- **Padding messages**: 15px
- **Margin messages**: 10px vertical
- **Border radius**: 15px

---

## 🎯 Éléments interactifs

### Boutons
```python
Défaut:
- Background: #8BC34A
- Color: white
- Padding: 10px 24px
- Border-radius: 10px
- Font-weight: bold

Hover:
- Background: #689F38
- Transition: 0.3s
```

### Input chat
```python
- Width: 100%
- Border-radius: 10px
- Padding: 10px
- Placeholder: Gris clair
- Focus: Bordure verte
```

### Selectbox usine
```python
- Width: 100%
- Options: ["Toulouse", "Tunis"]
- Style: Streamlit défaut
- Label: Visible avec emoji 🏭
```

---

## 📊 Graphiques Plotly

### Production (Line chart)
```python
Type: Scatter avec fill
Couleur ligne: #8BC34A
Largeur ligne: 3px
Markers: Taille 10, couleur #8BC34A
Fill: rgba(139, 195, 74, 0.2)
Background: Blanc
Grid: Gris clair (yaxis uniquement)
```

### Qualité par station (Bar chart)
```python
Type: Horizontal bar
Couleur bars: #8BC34A
Orientation: Horizontal
Text: Affiché (outside)
Background: Blanc
Range X: 90-100%
Grid: Gris clair (xaxis uniquement)
```

---

## 🔤 Typographie

### Titres
```
H1: 
- Taille: 32px
- Couleur: Blanc (dans header) ou #424242
- Font-weight: Bold

H2:
- Taille: 24px
- Couleur: #424242
- Font-weight: Bold
- Margin-top: 30-40px

H3:
- Taille: 18px
- Couleur: #8BC34A ou #424242
- Font-weight: Bold
```

### Corps de texte
```
Normal:
- Taille: 14-16px
- Couleur: #424242
- Line-height: 1.5

Labels métriques:
- Taille: 16px
- Couleur: Blanc (dans cartes)
- Opacity: 0.9

Valeurs métriques:
- Taille: 42px
- Couleur: Blanc (dans cartes)
- Font-weight: Bold
```

---

## 📱 Responsive Design

### Desktop (> 1200px)
- 4 colonnes pour métriques
- 2 colonnes pour graphiques
- Chat largeur max 80%

### Tablet (768-1200px)
- 2 colonnes pour métriques (2 lignes)
- 2 colonnes pour graphiques
- Chat largeur 85%

### Mobile (< 768px)
- 1 colonne pour métriques (4 lignes)
- 1 colonne pour graphiques (empilés)
- Chat largeur 95%

---

## 🎭 Animations

### Loader (lors du traitement)
```
🤖 Cortex Analyst analyse vos données...
(Spinner Streamlit en vert)
Durée: 1.5 secondes
```

### Transitions
- Hover boutons: 0.3s ease
- Apparition messages: Fade in
- Auto-scroll: Smooth

---

## 🖼️ Icônes utilisées

```
🤖 - Cortex Analyst / IA
🏭 - Usine / Production
✅ - Qualité / OK
⚡ - Efficacité / OEE
🚨 - Alertes
📊 - Métriques / Analyse
📈 - Graphique production
🎯 - Qualité par station
💬 - Chat / Conversation
🔍 - Recherche / Composants
🔮 - Prévisions
💰 - Coûts / Prix
📋 - Activité récente
🟢 - Système actif
❄️ - Snowflake
💡 - Conseil / Info
```

---

## 🎨 Cas d'usage des couleurs

### Vert (#8BC34A)
- ✅ Boutons d'action
- ✅ Messages utilisateur (chat)
- ✅ Accents graphiques
- ✅ Icônes importantes
- ✅ Dégradés (avec gris)

### Gris (#424242)
- ✅ Textes principaux
- ✅ Header background
- ✅ Footer background
- ✅ Dégradés (avec vert)
- ✅ Bordures subtiles

### Blanc
- ✅ Texte sur fond coloré
- ✅ Background cartes
- ✅ Background chat assistant
- ✅ Background page

### Gris clair (#E0E0E0)
- ✅ Info boxes
- ✅ Status bar
- ✅ Bordures messages
- ✅ Separateurs

---

## ✨ Points d'attention design

### Cohérence Actia
✅ Toutes les couleurs respectent la charte
✅ Logo/branding présent (header + footer)
✅ Style professionnel et moderne
✅ Pas de couleurs hors charte

### Accessibilité
✅ Contraste texte/fond suffisant
✅ Tailles de police lisibles
✅ Icônes pour clarté
✅ Messages d'erreur clairs

### Expérience utilisateur
✅ Navigation intuitive
✅ Feedback visuel (hover, loading)
✅ Messages clairs et structurés
✅ Responsive sur tous écrans

---

## 📸 Captures d'écran suggérées

Pour la documentation, capturer:

1. **Vue d'ensemble** - Interface complète
2. **Dashboard** - Métriques + graphiques
3. **Chat vide** - État initial avec suggestions
4. **Chat actif** - Exemple de conversation
5. **Mobile** - Vue responsive
6. **Hover states** - Boutons interactifs

---

**Interface créée pour Actia - Design System v1.0**
*Novembre 2024*


# 📋 Plan de Restructuration de la Démo

## ✅ Déjà fait

1. **Page d'accueil**
   - Message "Derrière la donnée, il y a des gens"
   - Agenda en 4 points
   - Footer "EBC 2025"

2. **Menu sidebar**
   - "🎯 Demo Navigation" → "📋 Agenda"
   - Nouvelles sections: IA Accessible, OEE & ML, Marketplace, Tout est Données

3. **Page IA Accessible**
   - Enlever mention IP locale ✅
   - Ajouter info sur catalogue LLM Snowflake
   - Mention traduction instantanée

## 🔄 À faire maintenant

### 1. Supprimer la page "IA Conversationnelle"
- Cette page n'existe plus dans le nouveau menu
- Code à retirer

### 2. Créer page "OEE & ML" (fusion Traçabilité + Prédictions)

**Dashboard inspiré du screenshot:**
```
┌────────────────────────────────────────────────┐
│ STATUS: Critical - Only 35% remaining prod     │
│ REASON: Production 51 units vs 144 needed...   │
├────────────────────────────────────────────────┤
│        [Graphique OEE multi-lignes]            │
├────────────────────────────────────────────────┤
│ Prompt: Why did OEE drop?                      │
│ Response: Analyse détaillée...                 │
└────────────────────────────────────────────────┘
```

**Contenu:**
- Dashboard OEE temps réel (comme screenshot)
- Graphique multi-lignes (qualité, performance, disponibilité)
- Status avec alerte critique
- Chatbox pour interroger les baisses
- Section ML forecasting
- Détection anomalies

### 3. Refaire page "Marketplace"

**Message clé:**
"Données enrichies → Meilleurs forecasts"

**Contenu:**
- Quelles données trouver (S&P 500, météo, géopolitique...)
- Pourquoi ça aide les forecasts
- Tuto simple pour vendre vos propres données
- ROI calculator

### 4. Créer page "Tout est Données" (remplace Document AI)

**Focus: Données non structurées**

**Sections:**
1. **PDF → Excel**
   - Drag & drop simulation
   - Conversion automatique
   
2. **Image → Texte**
   - Upload image
   - Extraction texte + analyse
   
3. **Détection anomalies visuelles**
   - Upload photo produit
   - IA détecte défauts

**Message:** "Énorme potentiel dans les données non structurées"

## 🎯 Priorités

**Immédiat:**
1. Terminer page OEE & ML (la plus complexe)
2. Adapter Marketplace (contenu + message)
3. Créer "Tout est Données"

**Après:**
- Tester le flow complet
- Ajuster si besoin
- Push final

## 📝 Notes importantes

- **Smartphone avec dashboard + chatbot**: À représenter sur page IA Accessible
- **Footer "EBC 2025"**: Déjà fait sur page d'accueil, à ajouter partout ?
- **Screenshot OEE fourni**: À utiliser comme inspiration visuelle
- **Simplifier**: Focus sur les concepts, pas trop de détails

---

**Status:** 30% terminé
**Prochaine étape:** Créer page OEE & ML complète


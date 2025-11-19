# 🤖 Guide Cortex Analyst - Interface Actia

## 📋 Vue d'ensemble

L'application **cortex_analyst_app.py** remplace l'ancien mobile_app.py et offre une interface complète combinant:
- 📊 Dashboard temps réel avec métriques clés
- 💬 Chatbox Cortex Analyst pour interroger vos données
- 🎨 Branding Actia (vert #8BC34A et gris #424242)

---

## 🚀 Lancement rapide

### En local
```bash
streamlit run cortex_analyst_app.py
```

### Sur un autre port (si app.py tourne déjà)
```bash
streamlit run cortex_analyst_app.py --server.port 8502
```

---

## 🎨 Fonctionnalités

### 1. Dashboard Temps Réel

**Métriques principales:**
- 🏭 **Production**: Nombre de composants traités aujourd'hui
- ✅ **Qualité**: Taux de conformité global
- ⚡ **Efficacité**: OEE (Overall Equipment Effectiveness)
- 🚨 **Alertes**: Nombre d'alertes actives

**Graphiques:**
- 📈 **Production sur 7 jours**: Tendance de production
- 🎯 **Qualité par station**: Performance par poste de travail

### 2. Cortex Analyst - Chat Intelligent

**Comment ça marche:**
1. Tapez votre question en langage naturel
2. Cortex Analyst analyse vos données
3. Vous recevez une réponse détaillée avec insights

**Questions suggérées:**
- "Quel est le taux de qualité moyen ce mois-ci?"
- "Quels composants ont des problèmes?"
- "Quelle est la tendance de production?"

**Types de questions supportées:**

| Catégorie | Mots-clés | Exemple |
|-----------|-----------|---------|
| 🎯 Qualité | qualité, taux, conformité, défaut | "Quel est le taux de qualité par station?" |
| 📊 Production | production, volume, quantité | "Quelle est la production cette semaine?" |
| 🔍 Composants | composant, traçabilité, pièce | "Quels composants ont des problèmes?" |
| 🔮 Prévisions | prévision, prévoir, futur | "Quelle est la production prévue demain?" |
| 💰 Coûts | coût, prix, euro, économie | "Quel est l'impact des hausses de prix?" |

### 3. Activité Récente

Tableau en temps réel des derniers composants traités avec:
- Heure de traitement
- ID composant
- Station de production
- Statut qualité
- Score de qualité

---

## 🎯 Cas d'usage

### Pour le Directeur d'Usine
- Visualiser la production en temps réel
- Identifier rapidement les problèmes
- Suivre les tendances qualité

### Pour le Responsable Qualité
- Analyser les taux de conformité par station
- Identifier les composants problématiques
- Comparer les performances inter-usines

### Pour le Supply Chain Manager
- Suivre les alertes sur les composants
- Analyser l'impact des hausses de prix
- Anticiper les pénuries

### Pour la Direction
- Vue d'ensemble en un coup d'œil
- Accès simplifié aux données (chat)
- Prise de décision data-driven

---

## 💡 Exemples de conversations

### Exemple 1: Analyse Qualité
```
Vous: "Quel est le taux de qualité moyen ce mois-ci?"

Cortex Analyst:
📊 Analyse de qualité pour Toulouse:

• Taux de qualité moyen ce mois: 98.4%
• Évolution: +0.8% vs mois dernier
• Meilleure station: Test Final (99.5%)
• Station à surveiller: Intégration (97.8%)

Détails par composant:
- TGX-2847: 99.1% (excellent)
- ECU-2024: 98.2% (normal)
- PCB-1123: 97.5% (légère baisse)

💡 Recommandation: Audit de la station d'intégration recommandé.
```

### Exemple 2: Problèmes Composants
```
Vous: "Quels composants ont des problèmes?"

Cortex Analyst:
🔍 Analyse des composants pour Toulouse:

Alertes actives:
1. 🔴 IC-NXP-2847: Prix +15% (critique)
   - Fournisseur: NXP Semiconductors
   - Stock actuel: 3 semaines
   
2. 🟡 PCB-Advanced: Qualité en baisse
   - Taux actuel: 96.8% (-1.4%)
   - 12 défauts détectés cette semaine
   
3. 🟡 Capacitor-MLX: Délai livraison augmenté
   - Délai normal: 2 semaines
   - Délai actuel: 4 semaines

✅ Les autres composants sont dans les normes.
```

### Exemple 3: Production Future
```
Vous: "Quelle est la production prévue pour la semaine prochaine?"

Cortex Analyst:
🔮 Prévisions pour Toulouse:

Prochaines 7 jours:
- Production attendue: 9,150 composants (+6% vs cette semaine)
- Taux qualité prévu: 98.6%
- Risque pénurie: Faible

Facteurs identifiés:
- ✅ Capacité production: Normal
- ⚠️ Stock IC-NXP-2847: Attention
- ✅ Équipes: Complet
- ✅ Équipements: Opérationnels

📊 Confiance de la prévision: 94%
```

---

## 🎨 Personnalisation

### Modifier les couleurs
Dans `cortex_analyst_app.py` lignes 10-14:
```python
ACTIA_GREEN = "#2EB873"       # Vert Actia
ACTIA_GREY = "#424242"        # Gris foncé
ACTIA_LIGHT_GREY = "#E0E0E0"  # Gris clair
ACTIA_DARK_GREEN = "#1E8B57"  # Vert foncé
```

### Ajouter des réponses personnalisées
Fonction `get_cortex_response()` ligne 280+:
- Ajouter de nouveaux mots-clés
- Personnaliser les réponses
- Intégrer vos vraies données

### Connecter à Snowflake
Pour connecter à un vrai compte Snowflake:
```python
import snowflake.connector

conn = snowflake.connector.connect(
    user='YOUR_USER',
    password='YOUR_PASSWORD',
    account='YOUR_ACCOUNT',
    warehouse='YOUR_WAREHOUSE',
    database='YOUR_DATABASE',
    schema='YOUR_SCHEMA'
)

# Remplacer les données hardcodées par des vraies requêtes
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM production WHERE date = CURRENT_DATE()")
production_today = cursor.fetchone()[0]
```

---

## 📱 Déploiement

### Streamlit Cloud

1. **Créer un nouveau déploiement**
   - Main file: `cortex_analyst_app.py`
   - Python version: 3.11+

2. **Configuration**
   - Public: Oui
   - Port: Défaut

3. **URL exemple**
   - `https://actia-cortex-analyst.streamlit.app`

### Docker (optionnel)

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY cortex_analyst_app.py .

EXPOSE 8501

CMD ["streamlit", "run", "cortex_analyst_app.py", "--server.port=8501"]
```

---

## 🔧 Maintenance

### Logs
Les conversations sont stockées dans `st.session_state.messages`

### Debugging
Activer les logs Streamlit:
```bash
streamlit run cortex_analyst_app.py --logger.level=debug
```

### Performance
- Données simulées: instantané
- Avec Snowflake: 1-3 secondes par requête
- Optimisations: cache Streamlit (`@st.cache_data`)

---

## ❓ FAQ

**Q: Les données sont-elles réelles?**
R: Non, tout est simulé pour la demo. Pour production, connecter à Snowflake.

**Q: Peut-on ajouter plus de questions?**
R: Oui, éditer la fonction `get_cortex_response()` pour ajouter vos propres réponses.

**Q: Comment intégrer le vrai Cortex Analyst?**
R: Utiliser l'API Snowflake Cortex pour remplacer les réponses hardcodées.

**Q: Est-ce mobile-friendly?**
R: Oui, l'interface est responsive et s'adapte aux écrans mobiles.

**Q: Peut-on changer la langue?**
R: Oui, modifier tous les textes dans le code (actuellement en français).

---

## 📞 Support

**Documentation:**
- [Streamlit Docs](https://docs.streamlit.io)
- [Snowflake Cortex](https://docs.snowflake.com/en/user-guide/snowflake-cortex)
- [Plotly Python](https://plotly.com/python/)

**Fichiers liés:**
- `app.py`: Application principale
- `requirements.txt`: Dépendances
- `README.md`: Documentation projet

---

## ✅ Checklist Déploiement

- [ ] Tester en local (`streamlit run cortex_analyst_app.py`)
- [ ] Vérifier les couleurs Actia
- [ ] Tester toutes les questions suggérées
- [ ] Vérifier le responsive mobile
- [ ] Déployer sur Streamlit Cloud
- [ ] Tester l'URL publique
- [ ] Partager avec les utilisateurs

---

**Créé pour Actia - Powered by Snowflake ❄️**


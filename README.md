# ❄️ Snowflake x Actia - Demo Interactive

Demo visuelle et interactive pour Actia showcasing Snowflake capabilities avec focus sur l'IA, la traçabilité, et la génération de revenus via Marketplace.

## 🎨 Caractéristiques

### Applications
- **app.py**: Application principale de démonstration (pour projection)
- **cortex_analyst_app.py**: Interface Cortex Analyst avec dashboard et chatbox IA

### Fonctionnalités
1. 🏠 **Accueil**: Présentation du contexte Actia et des 4 enjeux stratégiques
2. 🤖 **Cortex Analyst**: Interface IA conversationnelle avec dashboard temps réel
3. 🏭 **Traçabilité**: Suivi composants de bout en bout
4. 💬 **Chat Intelligent**: Interrogez vos données en langage naturel
5. 📊 **Prédictions**: ML pour rentabilité produits et risques pénurie
6. 🌐 **Marketplace**: Vente/achat de données, calcul ROI
7. 📄 **Document AI**: Drag & drop pour structurer données non-structurées

### Design
- Couleurs Actia officielles: Gris (#6e6b70) et Vert (#009653)
- Logo officiel Actia Group 2007 intégré
- Interface très visuelle avec graphiques Plotly
- Responsive et optimisé mobile

## 🚀 Déploiement sur Streamlit Cloud

### 1. Application Principale (Demo)

1. Créer un compte sur [Streamlit Cloud](https://streamlit.io/cloud)
2. Connecter votre repository GitHub
3. Déployer avec ces paramètres:
   - **Main file path**: `app.py`
   - **Python version**: 3.11
   - **Public URL**: Oui

### 2. Application Cortex Analyst

1. Déployer une seconde app avec:
   - **Main file path**: `cortex_analyst_app.py`
   - **Python version**: 3.11
   - **Public URL**: Oui

2. Une fois déployé, récupérer l'URL (ex: `https://actia-cortex.streamlit.app`)

3. **Fonctionnalités**:
   - Dashboard temps réel avec métriques clés
   - Chatbox pour interroger les données en langage naturel
   - Interface optimisée Actia branding

## 💻 Test en Local

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer l'app principale
streamlit run app.py

# Lancer l'app Cortex Analyst (dans un autre terminal)
streamlit run cortex_analyst_app.py --server.port 8502
```

## 🎯 Structure de la Demo (20 min)

### Minute 0-2: Accueil
- Présenter le contexte: inflation, concurrence chinoise
- Montrer les 4 enjeux

### Minute 2-7: Cortex Analyst en Action
- Présenter l'interface Cortex Analyst
- Dashboard temps réel avec métriques clés
- Demo du chatbox: interroger les données en langage naturel

### Minute 7-12: IA en Action
- **Document AI**: Drag & drop d'un fichier de test
- **LLM Conversationnel**: Poser les 3 questions suggérées
- Montrer la puissance de l'IA pour répondre

### Minute 12-15: Prédictions & ML
- Montrer la rentabilité produits (éviter sur-ingénierie)
- Carte de chaleur risques pénurie
- Prévisions ventes

### Minute 15-18: Marketplace
- Expliquer comment vendre leurs données (€2.4M/an potentiel)
- Démo import dataset géopolitique
- Calcul ROI: 7,013%

### Minute 18-20: Conclusion
- Recap des 3 idées actionnables
- Call to action: démarrage décembre
- Q&A

## 📝 Notes pour la Présentation

### Points Clés CEO
- ✅ Urgence IA pour compétitivité
- ✅ Data = nouveau revenu (marketplace)
- ✅ Questionner l'existant (peut-on remplacer l'ERP?)
- ✅ 1-3 idées concrètes actionnables

### Points Clés DSI
- ✅ Traçabilité ascendante/descendante
- ✅ Simplification accès data (LLM vs Mongo)
- ✅ Consolidation usines (Toulouse + Tunis)
- ✅ Données non-structurées (testeurs, images)

### Données "Fake" mais Réalistes
Toutes les données sont générées pour la demo mais basées sur:
- Vrais cas d'usage automotive
- Benchmarks secteur réels
- Best practices Snowflake

## 🎨 Customization

### Couleurs officielles Actia
Dans `app.py` et `cortex_analyst_app.py`:
```python
ACTIA_GREEN = "#009653"  # Vert Actia (du logo officiel)
ACTIA_GREY = "#6e6b70"   # Gris Actia (du logo officiel)
ACTIA_DARK_GREEN = "#007A43"
```

### Ajouter des données réelles
Les sections avec données hardcodées:
- Ligne 400+: Réponses LLM
- Ligne 600+: Données prédictions
- Ligne 800+: Données marketplace

## 🔒 Sécurité

⚠️ Cette demo utilise des données fictives. Pour production:
- Connecter à vrai Snowflake account
- Ajouter authentification
- Masquer données sensibles
- Utiliser secrets Streamlit pour credentials

## 📞 Support

Pour questions techniques:
- Documentation Streamlit: https://docs.streamlit.io
- Snowflake Cortex: https://docs.snowflake.com/en/user-guide/snowflake-cortex

## 📄 License

Demo créée pour Actia par EBC - 2024


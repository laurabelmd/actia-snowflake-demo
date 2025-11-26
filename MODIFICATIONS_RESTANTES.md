# Modifications Restantes à Appliquer

## ✅ DÉJÀ FAIT (dans la version actuelle)
- Emoji Albert agrandi (48px) sous le QR code
- Emoji Alban agrandi (48px) dans la page Donnée Captive
- Cadre gris autour de l'image IMG_1306.jpg
- Section "Pour conclure" avec vidéo YouTube
- Alerte cliquable dans cortex_analyst_app.py

## 📝 À FAIRE MANUELLEMENT (pour éviter erreurs d'indentation)

### 1. Supprimer section "Incident Client" et mettre 2 blocs côte à côte

**Remplacer** (lignes ~978-1033) :
```python
    # INTRO : Message clé
    st.markdown(f"""...80% des données...""")
    
    # SECTION 1: CONTEXTE DU PROBLÈME
    st.markdown(...Incident Client...)
    st.markdown(...Alerte 09:05...)
    st.markdown(...Déclaration client...)
    st.markdown(...Défi de Claire...)
    
    # SECTION 2: ANALYSE MULTI-SOURCE
    st.markdown(f"<h2>🔍 Analyse Multi-Source</h2>")
```

**Par** :
```python
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Mise en colonnes : Message clé + Titre Analyse
    col_intro, col_title = st.columns([1, 1])
    
    with col_intro:
        st.markdown(f"""
        <div style='background-color: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%;'>
            <h2 style='color: {ACTIA_GREY}; margin-top: 0;'>💡 80% des données d'entreprise sont non structurées</h2>
            <p style='font-size: 17px; color: {ACTIA_GREY}; line-height: 1.8;'>
                <strong>PDF</strong> de rapports et contrats • <strong>Photos</strong> de contrôle qualité • <strong>Audio</strong> des call centers
                <br><br>
                Aujourd'hui, <strong>tout cela devient exploitable</strong> sur une seule plateforme.
                <br>
                Laissez-moi vous montrer avec <strong>UNE histoire</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_title:
        st.markdown(f"""
        <div style='background-color: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%; display: flex; align-items: center; justify-content: center;'>
            <h2 style='color: {ACTIA_GREEN}; margin: 0; text-align: center;'>🔍 Analyse Multi-Source<br>Interface Unifiée</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
```

### 2. Changer le contenu du PDF pour un Bon de Commande

**Remplacer** le contenu dans `st.text_area` (ligne ~964) :
```
BON DE COMMANDE N° BC-2024-8745
===================================
ACTIA Automotive - Division Électronique
Date: 15 Novembre 2024
Date de livraison souhaitée: 10 Décembre 2024

FOURNISSEUR:
TechComponents International
45 Rue de l'Innovation
31400 Toulouse, France
TVA: FR12345678901

CLIENT:
ACTIA Automotive
5 Rue Jorge Semprun
31400 Toulouse, France
Contact: Alban Martinez - Responsable Achats
Tel: +33 5 61 76 50 00

-------------------------------------------
ARTICLES COMMANDÉS:

1. Carte ETX-845 (Calculateur Principal)
   Réf: ETX845-2024-A
   Quantité: 500 unités
   Prix unitaire: €125.00
   Montant: €62,500.00
   Délai: 3 semaines

2. Module CAN-Bus (Communication)
   Réf: CAN-BUS-PRO-24
   Quantité: 750 unités
   Prix unitaire: €45.50
   Montant: €34,125.00
   Délai: 2 semaines

3. Connecteur DB9 Industriel
   Réf: DB9-IND-2024
   Quantité: 1,200 unités
   Prix unitaire: €8.75
   Montant: €10,500.00
   Délai: 1 semaine

4. Capteur Température NTC
   Réf: NTC-TEMP-50K
   Quantité: 2,500 unités
   Prix unitaire: €3.20
   Montant: €8,000.00
   Délai: 2 semaines

-------------------------------------------
SOUS-TOTAL HT: €115,125.00
TVA (20%): €23,025.00
TOTAL TTC: €138,150.00

CONDITIONS:
- Paiement: 30 jours fin de mois
- Livraison: Franco de port
- Garantie: 24 mois
```

### 3. Changer le DataFrame Excel généré (ligne ~1017)

**Remplacer** :
```python
df_variance = pd.DataFrame({
    'Article': ['Carte ETX-845', 'Module CAN-Bus', 'Connecteur DB9', 'Capteur NTC'],
    'Référence': ['ETX845-2024-A', 'CAN-BUS-PRO-24', 'DB9-IND-2024', 'NTC-TEMP-50K'],
    'Quantité': [500, 750, 1200, 2500],
    'Prix Unit. (€)': [125.00, 45.50, 8.75, 3.20],
    'Montant HT (€)': [62500, 34125, 10500, 8000],
    'Délai': ['3 semaines', '2 semaines', '1 semaine', '2 semaines']
})
```

### 4. Changer les métriques Excel (ligne ~1046)

**Remplacer** :
```python
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric("Montant HT", "€115,125", "4 articles")
with col_m2:
    st.metric("Quantité Totale", "4,950", "unités")
with col_m3:
    st.metric("Temps Extraction", "2.3 sec", "vs 15 min manuel")
```

### 5. Changer la transcription audio (ligne ~1227)

**Remplacer le contenu** du `st.text_area` par :
```
[Appel Support Technique - 26 Nov 2024 - 09:15]

ALBAN (ACTIA - Support Niveau 1):
"Service Support Qualité Actia, bonjour. Alban à votre écoute."

M. DUBOIS (CLIENT - Responsable Qualité):
"Bonjour Alban, Monsieur Dubois. J'ai un souci majeur sur un lot 
de cartes ETX-845. Notre module logiciel n'arrive pas à se 
synchroniser avec la carte. On a des erreurs d'initialisation 
aléatoires. Le code série est le ETX845-SN-998533."

ALBAN:
"Je crée un ticket qualité prioritaire, référence TQ-2025-4590. 
Le problème est isolé à cette carte ou sur l'ensemble du lot?"

M. DUBOIS:
"C'est intermittent! J'en ai isolé cinq qui présentent le même 
comportement, mais je ne peux pas tester les 500 cartes! Mon 
usine est en attente. J'ai besoin qu'Actia utilise ses données!"

ALBAN:
"Pouvez-vous m'envoyer le log d'erreurs? Et vous avez raison, 
toutes nos données de traçabilité sont disponibles. À mon niveau, 
je ne peux pas croiser le numéro 998533 avec les variations de 
température de la machine de soudage. Votre dossier monte à 
l'équipe d'expertise Niveau 2. Un ingénieur vous rappellera dans 
les trente minutes pour lancer l'analyse approfondie."

M. DUBOIS:
"Trente minutes, c'est long, mais j'accepte. Donnez-moi non 
seulement le problème, mais aussi une solution préventive pour 
les prochains lots. Merci."
```

### 6. Modifier les insights audio (ligne ~1260)

**Changer** :
- Composant affecté: TGX-2847-A → Carte ETX-845
- Cause racine → Problème: Erreurs d'initialisation intermittentes
- Ajouter: Numéro de série: ETX845-SN-998533
- Ajouter: Client: M. Dubois
- Ajouter: Ticket: TQ-2025-4590
- Unités à retester: 200 → Cartes affectées: 5 sur 500

## 💡 CONSEIL

Ces modifications sont documentées mais PAS appliquées pour éviter de créer de nouvelles erreurs d'indentation.

L'application fonctionnera correctement avec la version actuelle (5a45388) qui inclut déjà les éléments visuels principaux.

Voulez-vous que je crée ces fichiers séparément ou préférez-vous les appliquer manuellement en copiant ce document?


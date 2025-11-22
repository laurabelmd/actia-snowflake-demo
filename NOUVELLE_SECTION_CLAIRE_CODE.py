# ===================================================================================
# CODE COMPLET POUR LA SECTION "TOUT EST DONNÉES" - HISTOIRE DE CLAIRE
# À intégrer dans app.py à la place des 3 tabs actuels
# ===================================================================================

# SECTION 2: Upload des fichiers (3 colonnes)
col_up1, col_up2, col_up3 = st.columns(3)

with col_up1:
    st.markdown(f"<h4 style='color: {ACTIA_GREY};'>📄 Devis & Contrat</h4>", unsafe_allow_html=True)
    uploaded_pdf = st.file_uploader("Upload Devis PDF", type=['pdf'], key='claire_pdf')
    
with col_up2:
    st.markdown(f"<h4 style='color: {ACTIA_GREY};'>🎤 Call Center</h4>", unsafe_allow_html=True)
    uploaded_audio = st.file_uploader("Upload Audio Call", type=['pdf', 'mp3', 'wav'], key='claire_audio')
    
with col_up3:
    st.markdown(f"<h4 style='color: {ACTIA_GREY};'>📷 Photo Défaut</h4>", unsafe_allow_html=True)
    uploaded_image = st.file_uploader("Upload Photo Carte", type=['jpg', 'png', 'jpeg'], key='claire_image')

st.markdown("<br>", unsafe_allow_html=True)

# ==================================================================================
# SI LES 3 FICHIERS SONT UPLOADÉS → MONTRER L'ANALYSE COMPLÈTE
# ==================================================================================

if uploaded_pdf and uploaded_audio and uploaded_image:
    
    # Bouton d'analyse
    if st.button("🤖 Lancer Analyse Snowflake (toutes sources)", use_container_width=True, type="primary"):
        
        # Progress bar
        with st.spinner("🔄 Analyse en cours... Snowflake combine PDF + Audio + Image"):
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.03)
                progress.progress(i + 1)
        
        st.success("✅ Analyse terminée en 8 secondes !")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # ============================================
        # SECTION 3: RÉSULTATS PAR SOURCE (4 colonnes)
        # ============================================
        
        st.markdown(f"<h3 style='color: {ACTIA_GREY};'>📊 Résultats par source de données</h3>", unsafe_allow_html=True)
        
        col_r1, col_r2, col_r3, col_r4 = st.columns(4)
        
        # Colonne 1: PDF Devis
        with col_r1:
            st.markdown(f"""
            <div style='background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); height: 100%;'>
                <h4 style='color: {ACTIA_GREEN}; margin-top: 0;'>📄 Devis Extrait</h4>
                <table style='width: 100%; font-size: 13px;'>
                    <tr><td><strong>Prix unitaire:</strong></td><td>127€</td></tr>
                    <tr><td><strong>Quantité:</strong></td><td>50 unités</td></tr>
                    <tr><td><strong>Total:</strong></td><td>€6,350</td></tr>
                    <tr><td><strong>Qualité:</strong></td><td>Niveau A</td></tr>
                    <tr><td><strong>Pénalité:</strong></td><td>-15% si défaut</td></tr>
                    <tr style='background-color: #ffebee;'><td><strong>Montant pénalité:</strong></td><td style='color: #c62828;'><strong>-€952</strong></td></tr>
                </table>
            </div>
            """, unsafe_allow_html=True)
        
        # Colonne 2: Audio Call
        with col_r2:
            st.markdown(f"""
            <div style='background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); height: 100%;'>
                <h4 style='color: {ACTIA_GREEN}; margin-top: 0;'>🎤 Analyse Audio</h4>
                <p style='font-size: 12px; color: {ACTIA_GREY}; line-height: 1.6;'>
                    <strong>Transcription (extrait):</strong><br>
                    <em>"...inacceptable...50 unités défectueuses...production arrêtée...geste commercial ou pénalité..."</em>
                </p>
                <table style='width: 100%; font-size: 13px; margin-top: 10px;'>
                    <tr style='background-color: #ffebee;'><td><strong>Sentiment:</strong></td><td>😡 -0.82 (Très négatif)</td></tr>
                    <tr><td><strong>Urgence:</strong></td><td>🔴 Haute</td></tr>
                    <tr><td><strong>Durée:</strong></td><td>4min 32s</td></tr>
                    <tr><td><strong>Demande:</strong></td><td>Remplacement + Geste</td></tr>
                </table>
            </div>
            """, unsafe_allow_html=True)
        
        # Colonne 3: Image Défaut
        with col_r3:
            st.markdown(f"""
            <div style='background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); height: 100%;'>
                <h4 style='color: {ACTIA_GREEN}; margin-top: 0;'>📷 Détection IA</h4>
            """, unsafe_allow_html=True)
            
            st.image(uploaded_image, use_container_width=True)
            
            st.markdown(f"""
                <table style='width: 100%; font-size: 13px; margin-top: 10px;'>
                    <tr style='background-color: #fff3cd;'><td><strong>Défaut:</strong></td><td>⚠️ Soudure froide</td></tr>
                    <tr><td><strong>Localisation:</strong></td><td>DB9 Pin 7</td></tr>
                    <tr><td><strong>Confiance:</strong></td><td>96.8%</td></tr>
                    <tr><td><strong>Sévérité:</strong></td><td>9/10</td></tr>
                </table>
            </div>
            """, unsafe_allow_html=True)
        
        # Colonne 4: Historique Client
        with col_r4:
            st.markdown(f"""
            <div style='background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); height: 100%;'>
                <h4 style='color: {ACTIA_GREEN}; margin-top: 0;'>📊 Historique</h4>
                <table style='width: 100%; font-size: 13px;'>
                    <tr style='background-color: #e8f5e9;'><td><strong>CA annuel:</strong></td><td style='color: {ACTIA_GREEN};'><strong>€2M</strong></td></tr>
                    <tr><td><strong>Croissance:</strong></td><td>+15% YoY</td></tr>
                    <tr><td><strong>Satisfaction:</strong></td><td>⭐ 92%</td></tr>
                    <tr><td><strong>Commandes:</strong></td><td>24/an</td></tr>
                    <tr><td><strong>Incidents:</strong></td><td>0 (1er problème)</td></tr>
                    <tr style='background-color: #fff3cd;'><td><strong>Statut:</strong></td><td>🎯 Stratégique</td></tr>
                </table>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # ===============================================
        # SECTION 4: SYNTHÈSE IA CROISÉE
        # ===============================================
        
        st.markdown(f"<h3 style='color: {ACTIA_GREY};'>🤖 Synthèse Snowflake - Toutes sources combinées</h3>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: {ACTIA_LIGHT_GREY}; padding: 25px; border-radius: 15px; border-left: 5px solid {ACTIA_GREEN};'>
            <h4 style='color: {ACTIA_DARK_GREEN}; margin-top: 0;'>✅ VÉRIFICATIONS</h4>
            <p style='color: {ACTIA_GREY}; font-size: 15px; line-height: 1.8;'>
                • <strong>Devis confirmé</strong> : Niveau A (0 défaut) requis → ✅ Client a raison<br>
                • <strong>Défaut confirmé</strong> par IA : Soudure froide critique → ✅ Non conforme<br>
                • <strong>Sentiment client</strong> : Très négatif + menace pénalité → ⚠️ Urgence haute<br>
                • <strong>Historique</strong> : Client stratégique, 1er incident → 🎯 À préserver absolument
            </p>
            
            <h4 style='color: {ACTIA_DARK_GREEN}; margin-top: 20px;'>💰 ANALYSE FINANCIÈRE</h4>
            <table style='width: 100%; color: {ACTIA_GREY}; font-size: 15px;'>
                <tr><td>Coût remplacement (50 unités):</td><td><strong>€6,350</strong></td></tr>
                <tr><td>Geste commercial suggéré (5%):</td><td><strong>+€318</strong></td></tr>
                <tr style='background-color: #ffebee;'><td>Pénalité si refus:</td><td style='color: #c62828;'><strong>-€952</strong></td></tr>
                <tr style='background-color: #e8f5e9;'><td>Risque perte client:</td><td style='color: {ACTIA_GREEN};'><strong>€2M/an</strong></td></tr>
                <tr style='background-color: #e8f5e9;'><td><strong>DÉCISION:</strong></td><td style='color: {ACTIA_GREEN};'><strong>✅ Accepter = ROI positif</strong></td></tr>
            </table>
            
            <h4 style='color: {ACTIA_DARK_GREEN}; margin-top: 20px;'>⏱️ URGENCE</h4>
            <p style='color: {ACTIA_GREY}; font-size: 15px; line-height: 1.8;'>
                • Production PSA arrêtée : Coût <strong>€15K/jour</strong> pour le client<br>
                • Délai remplacement : <strong>48h possible</strong> (stock Toulouse OK)<br>
                • <strong>Action immédiate requise</strong> pour préserver la relation
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # ===============================================
        # SECTION 5: ACTIONS AUTOMATIQUES DÉCLENCHÉES
        # ===============================================
        
        st.markdown(f"<h3 style='color: {ACTIA_GREY};'>✅ Actions Automatiques Déclenchées par Snowflake</h3>", unsafe_allow_html=True)
        
        col_a1, col_a2, col_a3 = st.columns(3)
        
        with col_a1:
            st.markdown(f"""
            <div style='background-color: #e8f5e9; padding: 15px; border-radius: 10px; border-left: 4px solid {ACTIA_GREEN};'>
                <h5 style='color: {ACTIA_DARK_GREEN}; margin: 0;'>🎫 Ticket Qualité</h5>
                <p style='color: {ACTIA_GREY}; margin: 5px 0 0 0; font-size: 14px;'>
                    ✅ Créé : #QA-2024-1142<br>
                    Assigné : Équipe Toulouse<br>
                    Priorité : Critique
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style='background-color: #e8f5e9; padding: 15px; border-radius: 10px; border-left: 4px solid {ACTIA_GREEN}; margin-top: 10px;'>
                <h5 style='color: {ACTIA_DARK_GREEN}; margin: 0;'>🚨 Alerte Production</h5>
                <p style='color: {ACTIA_GREY}; margin: 5px 0 0 0; font-size: 14px;'>
                    ✅ Envoyé à l'usine Toulouse<br>
                    Lot L2847-NOV24 bloqué<br>
                    Audit ligne #3 programmé
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_a2:
            st.markdown(f"""
            <div style='background-color: #e8f5e9; padding: 15px; border-radius: 10px; border-left: 4px solid {ACTIA_GREEN};'>
                <h5 style='color: {ACTIA_DARK_GREEN}; margin: 0;'>📦 Remplacement</h5>
                <p style='color: {ACTIA_GREY}; margin: 5px 0 0 0; font-size: 14px;'>
                    ✅ Stock réservé : 50 unités<br>
                    Livraison express : 27/11<br>
                    Destination : Site Sochaux PSA
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style='background-color: #e8f5e9; padding: 15px; border-radius: 10px; border-left: 4px solid {ACTIA_GREEN}; margin-top: 10px;'>
                <h5 style='color: {ACTIA_DARK_GREEN}; margin: 0;'>🔍 Audit Programmé</h5>
                <p style='color: {ACTIA_GREY}; margin: 5px 0 0 0; font-size: 14px;'>
                    ✅ Date : 26/11 à 14:00<br>
                    Ligne : #3 (TGX-2847)<br>
                    Rapport : Sous 72h
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col_a3:
            st.markdown(f"""
            <div style='background-color: #fff3cd; padding: 15px; border-radius: 10px; border-left: 4px solid #ffc107;'>
                <h5 style='color: #856404; margin: 0;'>📧 Email Client</h5>
                <p style='color: {ACTIA_GREY}; margin: 5px 0 0 0; font-size: 14px;'>
                    📝 Proposition auto-générée<br>
                    Statut : Prêt à envoyer<br>
                    👇 Voir ci-dessous
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style='background-color: #e3f2fd; padding: 15px; border-radius: 10px; border-left: 4px solid #1976d2; margin-top: 10px;'>
                <h5 style='color: #0d47a1; margin: 0;'>📊 Notifications</h5>
                <p style='color: {ACTIA_GREY}; margin: 5px 0 0 0; font-size: 14px;'>
                    ✅ CEO : Alerte client stratégique<br>
                    ✅ DSI : Incident qualité<br>
                    ✅ Finance : Impact marge
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Email auto-généré
        st.markdown(f"<h4 style='color: {ACTIA_GREY};'>📧 Email de Réponse (généré automatiquement par Snowflake)</h4>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); border: 1px solid #e0e0e0;'>
            <p style='color: {ACTIA_GREY}; font-size: 14px; line-height: 1.8;'>
                <strong>De :</strong> Claire Durand - Service Client Actia<br>
                <strong>À :</strong> Marc Leblanc - PSA Peugeot-Citroën<br>
                <strong>Objet :</strong> Réponse urgente - Incident Lot L2847-NOV24 TGX-2847<br>
                <hr style='border-color: #e0e0e0;'>
                <br>
                Monsieur Leblanc,
                <br><br>
                Suite à votre appel de ce matin concernant le lot L2847-NOV24, nous avons immédiatement analysé la situation avec nos systèmes IA.
                <br><br>
                <strong style='color: {ACTIA_DARK_GREEN};'>🔍 NOTRE ANALYSE :</strong><br>
                ✅ Défaut confirmé par notre IA Computer Vision : Soudure froide (Connecteur DB9, Pin 7)<br>
                ✅ Non-conformité reconnue : Niveau A (0 défaut) non respecté<br>
                ✅ Origine identifiée : Anomalie ligne production #3 (réglage machine corrigé)<br>
                <br>
                <strong style='color: {ACTIA_DARK_GREEN};'>🎯 NOTRE PROPOSITION :</strong><br>
                ✅ <strong>Remplacement GRATUIT</strong> des 50 unités sous 48h (mercredi 27/11 avant 10h)<br>
                ✅ <strong>Geste commercial</strong> : 5% de réduction sur votre prochaine commande<br>
                ✅ <strong>Audit qualité complet</strong> : Rapport détaillé sous 72h<br>
                ✅ <strong>Garantie renforcée</strong> : Contrôle à 100% sur prochains lots TGX-2847<br>
                <br>
                <strong>Livraison express :</strong> Mercredi 27/11 avant 10h à votre site de Sochaux (livraison prioritaire confirmée).
                <br><br>
                Nous vous présentons nos excuses pour ce désagrément et restons à votre entière disposition.
                <br><br>
                Cordialement,<br>
                <strong>Claire Durand</strong><br>
                Service Client - Actia Group<br>
                📞 +33 5 61 17 61 17 | 📧 claire.durand@actia.com
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            st.button("📧 Envoyer Email", use_container_width=True, type="primary")
        with col_btn2:
            st.button("✏️ Modifier", use_container_width=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # ===============================================
        # SECTION 6: MÉTRIQUES & ROI
        # ===============================================
        
        st.markdown(f"<h3 style='color: {ACTIA_GREY};'>📊 Impact & ROI de la Solution Snowflake</h3>", unsafe_allow_html=True)
        
        # Metrics en 4 colonnes
        col_m1, col_m2, col_m3, col_m4 = st.columns(4)
        
        with col_m1:
            st.metric(
                label="⏱️ Temps de résolution",
                value="8 minutes",
                delta="-95% vs manuel (2 jours)"
            )
        
        with col_m2:
            st.metric(
                label="💰 Coût solution",
                value="€6,668",
                delta="Remplacement + geste"
            )
        
        with col_m3:
            st.metric(
                label="💎 Client conservé",
                value="€2M/an",
                delta="+€1,994K ROI net"
            )
        
        with col_m4:
            st.metric(
                label="🤖 Sources analysées",
                value="4",
                delta="PDF + Audio + Image + BDD"
            )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Graphique ROI
        st.markdown(f"<h4 style='color: {ACTIA_GREY};'>💰 Analyse Coût-Bénéfice</h4>", unsafe_allow_html=True)
        
        fig_roi = go.Figure()
        
        fig_roi.add_trace(go.Bar(
            name='Coûts',
            x=['Solution Snowflake', 'Alternative manuelle'],
            y=[6668, 15000],
            marker_color='#f44336',
            text=['€6,668', '€15,000'],
            textposition='outside'
        ))
        
        fig_roi.add_trace(go.Bar(
            name='Temps (heures)',
            x=['Solution Snowflake', 'Alternative manuelle'],
            y=[0.13, 48],
            marker_color='#2196f3',
            text=['8 min', '2 jours'],
            textposition='outside',
            yaxis='y2'
        ))
        
        fig_roi.update_layout(
            title="Comparaison Solution IA vs Processus Manuel",
            barmode='group',
            yaxis=dict(title='Coût (€)'),
            yaxis2=dict(title='Temps (heures)', overlaying='y', side='right'),
            height=400
        )
        
        st.plotly_chart(fig_roi, use_container_width=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Bénéfices globaux
        st.markdown(f"""
        <div style='background-color: #e8f5e9; padding: 25px; border-radius: 15px; border-left: 5px solid {ACTIA_GREEN};'>
            <h4 style='color: {ACTIA_DARK_GREEN}; margin-top: 0;'>🎯 Bénéfices de l'approche unifiée Snowflake</h4>
            <div style='color: {ACTIA_GREY}; font-size: 16px; line-height: 2;'>
                ✅ <strong>Une seule interface</strong> pour toutes les sources (PDF, Audio, Image, BDD)<br>
                ✅ <strong>Analyse simultanée</strong> (pas séquentielle) → Gain de temps massif<br>
                ✅ <strong>Recommandations business</strong> (pas juste techniques) → Meilleure décision<br>
                ✅ <strong>Actions automatiques</strong> (tickets, alertes, emails) → 0 erreur humaine<br>
                ✅ <strong>ROI immédiat</strong> : Temps + Argent + Satisfaction client<br>
            </div>
        </div>
        """, unsafe_allow_html=True)

else:
    # Message si tous les fichiers ne sont pas uploadés
    st.info("👆 **Uploadez les 3 fichiers (PDF Devis + Audio Call + Photo Défaut) pour voir l'analyse complète de Claire**")
    
    st.markdown(f"""
    <div style='background-color: {ACTIA_LIGHT_GREY}; padding: 20px; border-radius: 10px; margin-top: 20px;'>
        <h4 style='color: {ACTIA_GREY};'>🎯 Ce que vous allez voir :</h4>
        <p style='color: {ACTIA_GREY}; font-size: 15px; line-height: 1.8;'>
            1. <strong>Extraction automatique</strong> du devis PDF (prix, quantités, clauses)<br>
            2. <strong>Transcription + Analyse sentiment</strong> de l'audio du call center<br>
            3. <strong>Détection IA de défauts</strong> sur la photo de carte électronique<br>
            4. <strong>Synthèse croisée</strong> de toutes les sources par Snowflake<br>
            5. <strong>Recommandations business</strong> + Actions automatiques<br>
            6. <strong>ROI immédiat</strong> : Résolution en 8 min vs 2 jours
        </p>
    </div>
    """, unsafe_allow_html=True)


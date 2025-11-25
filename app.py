import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import time
import random
import numpy as np

# Actia Colors (from official logo)
ACTIA_GREEN = "#009653"  # Actia green (official)
ACTIA_GREY = "#6e6b70"   # Actia grey (official)
ACTIA_LIGHT_GREY = "#E0E0E0"
ACTIA_DARK_GREEN = "#007A43"

# Page configuration
st.set_page_config(
    page_title="Snowflake x Actia Demo",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with Actia colors
st.markdown(f"""
    <style>
    .main {{
        background-color: #F5F5F5;
    }}
    .stButton>button {{
        background-color: {ACTIA_GREEN};
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
    }}
    .stButton>button:hover {{
        background-color: {ACTIA_DARK_GREEN};
    }}
    .metric-card {{
        background: linear-gradient(135deg, {ACTIA_GREY} 0%, {ACTIA_DARK_GREEN} 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}
    .success-box {{
        background-color: {ACTIA_GREEN};
        padding: 15px;
        border-radius: 10px;
        color: white;
        margin: 10px 0;
    }}
    .info-box {{
        background-color: {ACTIA_GREY};
        padding: 15px;
        border-radius: 10px;
        color: white;
        margin: 10px 0;
    }}
    h1, h2, h3 {{
        color: {ACTIA_GREY};
    }}
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {{
        font-size: 18px;
        font-weight: bold;
    }}
    .stTabs [data-baseweb="tab-list"] button:hover {{
        background-color: {ACTIA_LIGHT_GREY};
    }}
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {{
        background-color: {ACTIA_GREEN};
        color: white;
    }}
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.image("actia_logo.svg", use_column_width=True)
st.sidebar.markdown(f"<h2 style='color: {ACTIA_GREEN};'>📋 Agenda</h2>", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Sections",
    ["🚀 Vision", "🤖 Nea Actia", "📚 Donnée Captive", "📈 Anticipation & Marges", "📹 Pour conclure"],
    label_visibility="collapsed"
)

# Home Page
if page == "🚀 Vision":
    st.markdown(f"<h1 style='text-align: center; color: {ACTIA_GREY};'>❄️ Snowflake x Actia</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center; color: {ACTIA_GREEN};'>L'IA au Service des Gens et des Décisions</h3>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Intro humaniste
    st.markdown(f"""
    <div style='background-color: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h2 style='color: {ACTIA_GREY}; text-align: center;'>👥 Derrière la Donnée, il y a des Gens</h2>
        <p style='font-size: 18px; color: {ACTIA_GREY}; text-align: center; line-height: 1.8;'>
            Je suis allée sur vos sites, j'ai rencontré plein de gens. Pourquoi je commence avec ces banalités ? 
            <br><br>
            <strong>Parce que derrière la donnée, il y a des gens pour prendre des décisions.</strong>
            <br><br>
            Des gens qui voient leur environnement se bouleverser rapidement par l'émergence de l'IA.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Agenda de la demo
    st.markdown(f"<h2 style='color: {ACTIA_GREY}; text-align: center;'>📋 Agenda de la Démo</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {ACTIA_GREEN} 0%, {ACTIA_DARK_GREEN} 100%); 
                    padding: 25px; border-radius: 15px; margin: 10px 0; height: 280px;
                    display: flex; flex-direction: column; justify-content: center;'>
            <h3 style='color: white; margin: 0; text-align: center; font-size: 20px;'>1️⃣ La Donnée en libre accès :</h3>
            <h4 style='color: white; margin: 10px 0 0 0; text-align: center; font-size: 18px; font-weight: normal;'>Partout, Pour Tous.</h4>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {ACTIA_GREY} 0%, {ACTIA_DARK_GREEN} 100%); 
                    padding: 25px; border-radius: 15px; margin: 10px 0; height: 280px;
                    display: flex; flex-direction: column; justify-content: center;'>
            <h3 style='color: white; margin: 0; text-align: center; font-size: 20px;'>2️⃣ La Donnée Captive Libérée :</h3>
            <h4 style='color: white; margin: 10px 0 0 0; text-align: center; font-size: 18px; font-weight: normal;'>Transformer le Bruit en Action.</h4>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {ACTIA_GREEN} 0%, #1E8B57 100%); 
                    padding: 25px; border-radius: 15px; margin: 10px 0; height: 280px;
                    display: flex; flex-direction: column; justify-content: center;'>
            <h3 style='color: white; margin: 0; text-align: center; font-size: 20px;'>3️⃣ La Donnée Externe Stratégique :</h3>
            <h4 style='color: white; margin: 10px 0 0 0; text-align: center; font-size: 18px; font-weight: normal;'>Anticiper et Préserver les Marges.</h4>
        </div>
        """, unsafe_allow_html=True)

# IA Accessible Page
elif page == "🤖 Nea Actia":
    st.markdown(f"<h1 style='color: {ACTIA_GREY};'>🤖 Rendre l'IA Accessible</h1>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style='background-color: {ACTIA_LIGHT_GREY}; padding: 20px; border-radius: 10px; margin-bottom: 30px;'>
        <h3 style='color: {ACTIA_GREY}; margin: 0;'>📚 Snowflake: Le catalogue de LLM le plus fourni</h3>
        <p style='color: {ACTIA_GREY}; margin-top: 10px; font-size: 16px;'>
            Tous les LLM que vous entendez dans la presse (GPT, DeepSeek, Mistral, Claude...) 
            sont disponibles dans Snowflake en toute sécurité, <strong>sans que vos données soient réutilisées 
            pour de l'entraînement ou à des fins commerciales</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"""
        <div class='success-box'>
            <h2>✨ Scannez le QR Code</h2>
            <p style='font-size: 18px;'>Accédez à Cortex Analyst sur votre téléphone</p>
            <p style='font-size: 16px; margin-top: 10px;'>Dashboard temps réel + IA conversationnelle</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Generate QR code - Update this URL after deploying cortex_analyst_app.py
        st.markdown("<br>", unsafe_allow_html=True)
        
        # For local testing, use this:
        cortex_url = "https://actia-app-demo-aq7bhvmuvkeedyenaikjer.streamlit.app/"  # Replace with your local IP
        
        # For production (after Streamlit Cloud deployment), use this:
        # cortex_url = "https://actia-cortex-analyst.streamlit.app"
        
        qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?size=400x400&data={cortex_url}"
        st.image(qr_code_url, width=400)
        
        st.markdown(f"""
        <div class='info-box'>
            <h3>📲 Avec Cortex Analyst, vous pouvez:</h3>
            <ul style='font-size: 16px; line-height: 1.8;'>
                <li><strong>📊 Dashboard temps réel</strong><br>Production, qualité, efficacité, alertes</li>
                <li><strong>💬 Poser des questions en langage naturel</strong><br>"Quel est le taux de qualité ce mois-ci?"</li>
                <li><strong>🔍 Analyses instantanées</strong><br>Tendances, prévisions, recommandations</li>
                <li><strong>📈 Graphiques interactifs</strong><br>Production 7 jours, qualité par station</li>
                <li><strong>🌍 Traduction instantanée</strong><br>Dashboard disponible en plusieurs langues</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"<h3 style='color: {ACTIA_GREEN};'>👀 Aperçu Cortex Analyst</h3>", unsafe_allow_html=True)
        
        # Afficher l'image de l'interface Cortex Analyst
        st.image("IMG_1306.jpg", use_container_width=True)

# ML Page (fusion Traçabilité + Prédictions)
elif page == "📈 Anticipation & Marges":
    st.markdown(f"<h1 style='color: {ACTIA_GREY};'>🔮 L'IA qui Anticipe et qui Agit</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 18px; color: {ACTIA_GREEN};'>Du Forecasting à l'Analyse Prescriptive</p>", unsafe_allow_html=True)
    
    # INTRO : Use case clair
    st.markdown(f"""
    <div style='background-color: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin: 20px 0;'>
        <h2 style='color: {ACTIA_GREY}; margin-top: 0;'>🎯 Use Case : Forecasting Production Usine Toulouse</h2>
        <p style='font-size: 16px; color: {ACTIA_GREY}; line-height: 1.8;'>
            <strong>Le ML, ce n'est pas que des chatbots.</strong> C'est la capacité d'<strong>ANTICIPER</strong> et d'<strong>AGIR</strong>.
            <br><br>
            <strong>Objectif :</strong> Prévoir la production de demain et de la semaine prochaine pour l'usine de Toulouse,
            en tenant compte de <strong>facteurs externes</strong> (météo, marché, prix composants).
            <br><br>
            ✅ Forecast en quelques clics<br>
            ✅ Enrichissement avec la Marketplace<br>
            ✅ Simulations de scénarios interactives<br>
            ✅ Actions prescriptives automatiques
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ========================================
    # SECTION 1: MARKETPLACE - GRAPHES VISUELS
    # ========================================
    
    st.markdown(f"<h2 style='color: {ACTIA_GREY};'>📊 Étape 1 : Enrichir avec la Marketplace Snowflake</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: {ACTIA_GREY}; font-size: 16px;'>Accédez à des données externes de qualité en 1 clic (gratuites ou payantes)</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 3 graphes côte à côte
    col_mkt1, col_mkt2, col_mkt3 = st.columns(3)
    
    with col_mkt1:
        st.markdown(f"<h4 style='color: {ACTIA_GREEN}; text-align: center;'>📈 S&P 500 Automotive</h4>", unsafe_allow_html=True)
        
        # Données SNP 500
        dates_snp = pd.date_range(start='2024-10-01', end='2024-12-01', freq='D')
        values_snp = [3800 + i*2 + random.randint(-30, 30) for i in range(30)]
        # Prévision en baisse
        forecast_snp = [values_snp[-1] - i*3 for i in range(1, 32)]
        
        fig_snp = go.Figure()
        fig_snp.add_trace(go.Scatter(
            x=dates_snp[:30], 
            y=values_snp, 
            name="Historique", 
            line=dict(color=ACTIA_GREEN, width=2)
        ))
        fig_snp.add_trace(go.Scatter(
            x=pd.date_range(start='2024-11-30', end='2024-12-31', freq='D'),
            y=forecast_snp,
            name="Prévision",
            line=dict(color='red', dash='dash', width=2)
        ))
        
        fig_snp.update_layout(
            height=280,
            margin=dict(l=10, r=10, t=10, b=10),
            showlegend=False,
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True, gridcolor='#f0f0f0'),
            plot_bgcolor='white'
        )
        
        st.plotly_chart(fig_snp, use_container_width=True)
        
        st.markdown(f"""
        <div style='background-color: #ffebee; padding: 10px; border-radius: 5px; text-align: center;'>
            <p style='color: #c62828; margin: 0; font-size: 13px;'>
                <strong>-8% prévu</strong><br>
                → Baisse commandes PSA/Renault dans 3 mois
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_mkt2:
        st.markdown(f"<h4 style='color: {ACTIA_GREEN}; text-align: center;'>🌦️ Météo Toulouse</h4>", unsafe_allow_html=True)
        
        # Données météo
        dates_weather = pd.date_range(start='2024-11-25', end='2024-12-02', freq='D')
        temp_weather = [12, 14, 16, 22, 28, 37, 35, 33]  # Canicule prévue
        
        fig_weather = go.Figure()
        fig_weather.add_trace(go.Scatter(
            x=dates_weather,
            y=temp_weather,
            mode='lines+markers',
            line=dict(color='orange', width=3),
            marker=dict(size=8),
            fill='tozeroy',
            fillcolor='rgba(255, 165, 0, 0.2)'
        ))
        
        # Ligne d'alerte canicule
        fig_weather.add_hline(y=35, line_dash="dash", line_color="red", 
                               annotation_text="Seuil canicule", annotation_position="right")
        
        fig_weather.update_layout(
            height=280,
            margin=dict(l=10, r=10, t=10, b=10),
            xaxis=dict(showgrid=False),
            yaxis=dict(title="°C", showgrid=True, gridcolor='#f0f0f0'),
            plot_bgcolor='white'
        )
        
        st.plotly_chart(fig_weather, use_container_width=True)
        
        st.markdown(f"""
        <div style='background-color: #fff3cd; padding: 10px; border-radius: 5px; text-align: center;'>
            <p style='color: #856404; margin: 0; font-size: 13px;'>
                <strong>Canicule 26-28 Nov</strong><br>
                → Impact OEE usines non climatisées
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_mkt3:
        st.markdown(f"<h4 style='color: {ACTIA_GREEN}; text-align: center;'>💰 Prix Composants</h4>", unsafe_allow_html=True)
        
        # Prix composants (semi-conducteurs)
        dates_prix = pd.date_range(start='2024-06-01', end='2024-12-01', freq='M')
        prix_base = [100, 103, 107, 110, 113, 115, 118]
        
        fig_prix = go.Figure()
        fig_prix.add_trace(go.Bar(
            x=dates_prix,
            y=prix_base,
            marker=dict(color=['#2ca02c', '#2ca02c', '#ffc107', '#ffc107', '#ff9800', '#f44336', '#c62828']),
            text=[f"+{p-100}%" for p in prix_base],
            textposition='outside'
        ))
        
        fig_prix.update_layout(
            height=280,
            margin=dict(l=10, r=10, t=10, b=10),
            xaxis=dict(showgrid=False),
            yaxis=dict(title="Index (base 100)", showgrid=True, gridcolor='#f0f0f0'),
            plot_bgcolor='white'
        )
        
        st.plotly_chart(fig_prix, use_container_width=True)
        
        st.markdown(f"""
        <div style='background-color: #ffebee; padding: 10px; border-radius: 5px; text-align: center;'>
            <p style='color: #c62828; margin: 0; font-size: 13px;'>
                <strong>+18% depuis juin</strong><br>
                → Impact marges produits
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style='background-color: {ACTIA_LIGHT_GREY}; padding: 15px; border-radius: 10px; margin: 20px 0;'>
        <p style='color: {ACTIA_GREY}; margin: 0; font-size: 15px; text-align: center;'>
            💡 <strong>Ces données sont disponibles en 1 clic sur la Marketplace Snowflake</strong> 
            (gratuites ou payantes selon la source)
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ========================================
    # SECTION 2: FORECASTING INTERACTIF + WIDGETS
    # ========================================
    
    st.markdown(f"<h2 style='color: {ACTIA_GREY};'>🎮 Étape 2 : Forecasting Interactif avec Simulations</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: {ACTIA_GREY}; font-size: 16px;'>Testez différents scénarios en temps réel</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Forecast de base (sans modifications)
    st.markdown(f"""
    <div style='background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h3 style='color: {ACTIA_GREEN}; margin-top: 0;'>📊 Forecast de Production (baseline)</h3>
    """, unsafe_allow_html=True)
    
    col_base1, col_base2, col_base3 = st.columns(3)
    with col_base1:
        st.metric("Production prévue demain", "1,450 unités", "Confiance: 94%")
    with col_base2:
        st.metric("Production semaine prochaine", "9,200 unités", "Tendance stable")
    with col_base3:
        st.metric("OEE prévu moyen", "89%", "+2% vs semaine dernière")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # WIDGETS INTERACTIFS
    st.markdown(f"<h3 style='color: {ACTIA_GREEN};'>🎛️ Simulez des scénarios (modifiez les paramètres)</h3>", unsafe_allow_html=True)
    
    col_w1, col_w2, col_w3 = st.columns(3)
    
    with col_w1:
        st.markdown(f"<h4 style='color: {ACTIA_GREY}; text-align: center;'>⚙️ Âge des Machines</h4>", unsafe_allow_html=True)
        age_machine = st.slider(
            "Choisir la ligne de production",
            min_value=0,
            max_value=10,
            value=3,
            format="%d ans",
            key='age_machine',
            help="Ligne 1 (récente) vs Ligne 2 (10 ans)"
        )
        
        # Calcul impact
        impact_age = 1 - (age_machine * 0.012)  # -1.2% par année
        production_ajustee_age = int(1450 * impact_age)
        delta_age = production_ajustee_age - 1450
        
        st.metric(
            "Production ajustée",
            f"{production_ajustee_age} unités",
            delta=f"{delta_age:+d} unités ({(impact_age-1)*100:.1f}%)",
            delta_color="inverse" if delta_age < 0 else "normal"
        )
        
        if age_machine > 7:
            st.warning("⚠️ Machines anciennes → Impact significatif")
        elif age_machine < 3:
            st.success("✅ Machines récentes → Performance optimale")
    
    with col_w2:
        st.markdown(f"<h4 style='color: {ACTIA_GREY}; text-align: center;'>📦 Stock Composants</h4>", unsafe_allow_html=True)
        stock_niveau = st.slider(
            "Niveau de stock de sécurité",
            min_value=20,
            max_value=60,
            value=35,
            format="%d unités",
            key='stock_niveau',
            help="Impact sur le risque de rupture"
        )
        
        # Calcul risque rupture
        risque_rupture = max(0, (40 - stock_niveau) * 0.75)  # Risque augmente si stock < 40
        
        st.metric(
            "Risque de rupture",
            f"{risque_rupture:.1f}%",
            delta=f"{-risque_rupture if stock_niveau > 35 else risque_rupture:.1f}%",
            delta_color="inverse"
        )
        
        if risque_rupture > 10:
            st.error(f"🔴 Risque élevé → Augmenter stock")
        elif risque_rupture < 3:
            st.success("✅ Risque faible → Stock suffisant")
        else:
            st.warning("⚠️ Risque modéré")
    
    with col_w3:
        st.markdown(f"<h4 style='color: {ACTIA_GREY}; text-align: center;'>🌡️ Conditions Météo</h4>", unsafe_allow_html=True)
        meteo = st.select_slider(
            "Prévision température",
            options=["Normal (15-25°C)", "Chaud (26-34°C)", "Canicule (35-40°C)"],
            value="Normal (15-25°C)",
            key='meteo'
        )
        
        # Impact OEE selon météo
        oee_impact = {
            "Normal (15-25°C)": 89,
            "Chaud (26-34°C)": 82,
            "Canicule (35-40°C)": 76
        }
        
        oee_prevu = oee_impact[meteo]
        delta_oee = oee_prevu - 89
        
        st.metric(
            "OEE prévu",
            f"{oee_prevu}%",
            delta=f"{delta_oee:+d}%",
            delta_color="inverse" if delta_oee < 0 else "normal"
        )
        
        if "Canicule" in meteo:
            st.error("🔴 Canicule → Impact fort sur OEE")
        elif "Chaud" in meteo:
            st.warning("⚠️ Chaleur → Impact modéré")
        else:
            st.success("✅ Conditions normales")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Graphe forecast avec paramètres ajustés
    st.markdown(f"<h3 style='color: {ACTIA_GREY};'>📈 Forecast Ajusté selon Simulations</h3>", unsafe_allow_html=True)
    
    # Calculer production finale avec tous les paramètres
    production_finale = int(1450 * impact_age * (1 - risque_rupture/200) * (oee_prevu/89))
    
    dates_forecast = pd.date_range(start='2024-11-25', end='2024-12-02', freq='D')
    production_baseline = [1420, 1435, 1450, 1445, 1460, 1455, 1470, 1465]
    production_ajustee = [int(p * impact_age * (1 - risque_rupture/200) * (oee_prevu/89)) for p in production_baseline]
    
    fig_forecast = go.Figure()
    
    fig_forecast.add_trace(go.Scatter(
        x=dates_forecast,
        y=production_baseline,
        name="Baseline (conditions normales)",
        line=dict(color=ACTIA_GREEN, width=3),
        mode='lines+markers'
    ))
    
    fig_forecast.add_trace(go.Scatter(
        x=dates_forecast,
        y=production_ajustee,
        name="Avec paramètres simulés",
        line=dict(color='orange', width=3, dash='dash'),
        mode='lines+markers'
    ))
    
    fig_forecast.update_layout(
        height=400,
        xaxis_title="Date",
        yaxis_title="Production (unités/jour)",
        hovermode='x unified',
        plot_bgcolor='white',
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
    )
    
    st.plotly_chart(fig_forecast, use_container_width=True)
    
    # Résumé impact simulation
    delta_total = production_finale - 1450
    st.markdown(f"""
    <div style='background-color: {"#e8f5e9" if delta_total >= 0 else "#ffebee"}; padding: 20px; border-radius: 10px; border-left: 5px solid {"#2ca02c" if delta_total >= 0 else "#f44336"};'>
        <h4 style='color: {ACTIA_GREY}; margin-top: 0;'>📊 Impact Total de vos Simulations</h4>
        <p style='color: {ACTIA_GREY}; font-size: 16px; margin: 0;'>
            Production demain : <strong style='color: {"#2ca02c" if delta_total >= 0 else "#f44336"};'>{production_finale} unités</strong> 
            ({delta_total:+d} unités vs baseline)
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ========================================
    # SECTION 3: ANALYSE PRESCRIPTIVE
    # ========================================
    
    st.markdown(f"<h2 style='color: {ACTIA_GREY};'>🤖 Étape 3 : Analyse Prescriptive - Actions Recommandées</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: {ACTIA_GREY}; font-size: 16px;'>Du forecast à l'ACTION : que faire concrètement ?</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Générer recommandations basées sur les paramètres
    st.markdown(f"""
    <div style='background-color: {ACTIA_LIGHT_GREY}; padding: 25px; border-radius: 15px; border-left: 5px solid {ACTIA_GREEN};'>
        <h3 style='color: {ACTIA_DARK_GREEN}; margin-top: 0;'>🎯 Actions Prescriptives Automatiques</h3>
    """, unsafe_allow_html=True)
    
    col_act1, col_act2 = st.columns(2)
    
    with col_act1:
        st.markdown(f"<h4 style='color: {ACTIA_GREY};'>📅 Demain (Mardi 26/11)</h4>", unsafe_allow_html=True)
        
        actions_demain = []
        
        if "Canicule" in meteo or "Chaud" in meteo:
            actions_demain.append({
                'icon': '🌡️',
                'action': 'Activer ventilation supplémentaire dès 6h',
                'impact': 'Maintien OEE à 85% vs 76% sans action'
            })
            actions_demain.append({
                'icon': '💧',
                'action': 'Programmer pauses hydratation +2/jour',
                'impact': 'Prévention accidents du travail'
            })
            if "Canicule" in meteo:
                actions_demain.append({
                    'icon': '⚙️',
                    'action': 'Réduire cadence ligne 3 de 15%',
                    'impact': 'Éviter surchauffe machines'
                })
        
        if age_machine > 7:
            actions_demain.append({
                'icon': '🔧',
                'action': 'Maintenance préventive ligne 2',
                'impact': 'Éviter panne (coût évité: €25K)'
            })
        
        if risque_rupture > 10:
            actions_demain.append({
                'icon': '📦',
                'action': 'Commande urgente composants critiques',
                'impact': 'Éviter arrêt production (coût évité: €45K)'
            })
        
        if not actions_demain:
            actions_demain.append({
                'icon': '✅',
                'action': 'Conditions optimales',
                'impact': 'Aucune action urgente nécessaire'
            })
        
        for action in actions_demain:
            st.markdown(f"""
            <div style='background-color: white; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 3px solid {ACTIA_GREEN};'>
                <p style='color: {ACTIA_GREY}; margin: 0;'>
                    <strong>{action['icon']} {action['action']}</strong><br>
                    <span style='font-size: 14px;'>→ {action['impact']}</span>
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    with col_act2:
        st.markdown(f"<h4 style='color: {ACTIA_GREY};'>📅 Cette Semaine</h4>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: white; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 3px solid {ACTIA_GREEN};'>
            <p style='color: {ACTIA_GREY}; margin: 0;'>
                <strong>📊 Analyse données météo & marché</strong><br>
                <span style='font-size: 14px;'>→ Ajuster planning production</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if risque_rupture > 5:
            st.markdown(f"""
            <div style='background-color: white; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 3px solid {ACTIA_GREEN};'>
                <p style='color: {ACTIA_GREY}; margin: 0;'>
                    <strong>📦 Renégocier contrat fournisseur #2</strong><br>
                    <span style='font-size: 14px;'>→ Sécuriser approvisionnement</span>
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: white; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 3px solid {ACTIA_GREEN};'>
            <p style='color: {ACTIA_GREY}; margin: 0;'>
                <strong>🔍 Audit qualité ligne 3</strong><br>
                <span style='font-size: 14px;'>→ Prévenir défauts futurs</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"<h4 style='color: {ACTIA_GREY}; margin-top: 20px;'>📅 Dans 3 Mois</h4>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: #fff3cd; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 3px solid #ffc107;'>
            <p style='color: #856404; margin: 0;'>
                <strong>⚠️ Baisse commandes prévue (S&P 500 -8%)</strong><br>
                <span style='font-size: 14px;'>→ Réduire production de 12% en janvier</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: white; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 3px solid {ACTIA_GREEN};'>
            <p style='color: {ACTIA_GREY}; margin: 0;'>
                <strong>💰 Négocier prix composants MAINTENANT</strong><br>
                <span style='font-size: 14px;'>→ Avant nouvelle hausse prévue</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: white; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 3px solid {ACTIA_GREEN};'>
            <p style='color: {ACTIA_GREY}; margin: 0;'>
                <strong>🎓 Former équipes sur nouveau produit TGX-3000</strong><br>
                <span style='font-size: 14px;'>→ Anticipation baisse commandes TGX-2847</span>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ROI Final
    st.markdown(f"""
    <div style='background-color: #e8f5e9; padding: 25px; border-radius: 15px; border-left: 5px solid {ACTIA_GREEN};'>
        <h3 style='color: {ACTIA_DARK_GREEN}; margin-top: 0;'>💰 ROI de l'Analyse Prescriptive</h3>
        <div style='color: {ACTIA_GREY}; font-size: 16px; line-height: 2;'>
            ⏱️ <strong>80% de temps libéré</strong> pour les équipes data (crunching automatisé)<br>
            💰 <strong>€180K/an de coûts évités</strong> (arrêts production prévenus)<br>
            📈 <strong>Marges préservées</strong> grâce à l'anticipation vs réaction<br>
            🎯 <strong>Décisions basées sur la data</strong>, pas sur l'intuition<br>
            🚀 <strong>Innovation profitable</strong> avec market relevance
        </div>
    </div>
    """, unsafe_allow_html=True)

# Note: Pages IA Conversationnelle et Prédictions fusionnées dans OEE & ML

# Predictions Page
elif page == "📊 Prédictions":
    st.markdown(f"<h1 style='color: {ACTIA_GREY};'>📊 Machine Learning Prédictif</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 18px; color: {ACTIA_GREEN};'>Anticipez les risques et optimisez la rentabilité</p>", unsafe_allow_html=True)
    
    tabs = st.tabs(["🎯 Rentabilité Produit", "⚠️ Risque Pénurie", "🔮 Prévision Ventes"])
    
    # Tab 1: Product profitability
    with tabs[0]:
        st.markdown(f"<h3 style='color: {ACTIA_GREY};'>🎯 Prédiction Rentabilité sur Cycle de Vie</h3>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Fake ML prediction visualization
            products = ['TGX Gateway', 'SmartConnect', 'EcoLogic', 'DiagBox', 'PowerControl', 
                       'NewProduct X', 'NewProduct Y']
            predicted_profit = [6.4, 4.7, 3.2, 2.8, 2.4, 1.2, 0.8]
            colors = [ACTIA_GREEN if p > 3 else ACTIA_GREY if p > 2 else 'red' for p in predicted_profit]
            
            fig = go.Figure(go.Bar(
                x=predicted_profit,
                y=products,
                orientation='h',
                marker=dict(color=colors),
                text=[f'€{p}M' for p in predicted_profit],
                textposition='outside'
            ))
            
            fig.update_layout(
                title='Profit Net Prédit (5 ans)',
                xaxis_title='Millions €',
                height=400,
                plot_bgcolor='white'
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown(f"""
            <div class='success-box'>
                <h3>✅ Modèle ML Actif</h3>
                <p>Précision: 94.3%</p>
                <p>Données: 847 produits</p>
                <p>Entraînement: 2019-2024</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style='background-color: white; padding: 20px; border-radius: 10px; 
                        border: 2px solid red; margin-top: 20px;'>
                <h3 style='color: red;'>🚨 Alerte Sur-Ingénierie</h3>
                <p style='color: {ACTIA_GREY};'><strong>NewProduct Y</strong></p>
                <p style='color: {ACTIA_GREY};'>Complexité: Trop élevée</p>
                <p style='color: {ACTIA_GREY};'>Coût dev: €2.1M</p>
                <p style='color: {ACTIA_GREY};'>ROI prédit: <span style='color: red;'>Négatif</span></p>
                <p style='color: {ACTIA_GREY};'><strong>Action: Simplifier ou annuler</strong></p>
            </div>
            """, unsafe_allow_html=True)
    
    # Tab 2: Shortage risk
    with tabs[1]:
        st.markdown(f"<h3 style='color: {ACTIA_GREY};'>⚠️ Prédiction Risque de Pénurie</h3>", unsafe_allow_html=True)
        
        # Risk heatmap
        col1, col2 = st.columns([3, 1])
        
        with col1:
            components_risk = ['IC-NXP-2847', 'PCB-Advanced', 'Capacitor-MLX', 'Connector-USB', 
                              'Sensor-Temp', 'Display-LCD', 'Battery-Pack', 'Cable-Harness']
            weeks = ['Sem 47', 'Sem 48', 'Sem 49', 'Sem 50']
            
            # Generate fake risk scores
            risk_matrix = np.array([
                [85, 90, 92, 95],  # IC-NXP
                [78, 82, 88, 90],  # PCB
                [65, 70, 72, 75],  # Capacitor
                [60, 58, 62, 65],  # Connector
                [45, 48, 50, 52],  # Sensor
                [30, 32, 28, 30],  # Display
                [25, 22, 20, 18],  # Battery
                [15, 14, 12, 10],  # Cable
            ])
            
            fig = go.Figure(data=go.Heatmap(
                z=risk_matrix,
                x=weeks,
                y=components_risk,
                colorscale=[[0, ACTIA_GREEN], [0.5, 'yellow'], [1, 'red']],
                text=risk_matrix,
                texttemplate='%{text}%',
                textfont={"size": 12}
            ))
            
            fig.update_layout(
                title='Carte de Chaleur - Risque de Pénurie (%)',
                height=400,
                xaxis_title='Semaines',
                yaxis_title='Composants'
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown(f"""
            <div style='background-color: red; color: white; padding: 20px; 
                        border-radius: 10px; margin-bottom: 20px;'>
                <h3>🔴 CRITIQUE</h3>
                <p><strong>IC-NXP-2847</strong></p>
                <p>Risque: 95%</p>
                <p>Délai: 2 semaines</p>
                <p><strong>Action immédiate</strong></p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style='background-color: orange; color: white; padding: 20px; 
                        border-radius: 10px; margin-bottom: 20px;'>
                <h3>🟠 ÉLEVÉ</h3>
                <p><strong>PCB-Advanced</strong></p>
                <p>Risque: 90%</p>
                <p>Délai: 3 semaines</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style='background-color: {ACTIA_GREEN}; color: white; padding: 20px; 
                        border-radius: 10px;'>
                <h3>🟢 OK</h3>
                <p>5 composants</p>
                <p>Stock suffisant</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Tab 3: Sales forecast
    with tabs[2]:
        st.markdown(f"<h3 style='color: {ACTIA_GREY};'>🔮 Prévision des Ventes (6 mois)</h3>", unsafe_allow_html=True)
        
        # Generate forecast data
        dates = pd.date_range(start='2024-11-01', periods=180, freq='D')
        historical = np.random.normal(100, 15, 90)
        forecast = np.random.normal(110, 12, 90)
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=dates[:90],
            y=historical,
            mode='lines',
            name='Historique',
            line=dict(color=ACTIA_GREY, width=2)
        ))
        
        fig.add_trace(go.Scatter(
            x=dates[90:],
            y=forecast,
            mode='lines',
            name='Prévision ML',
            line=dict(color=ACTIA_GREEN, width=3, dash='dash')
        ))
        
        # Add confidence interval
        upper = forecast + 10
        lower = forecast - 10
        
        fig.add_trace(go.Scatter(
            x=dates[90:].tolist() + dates[90:][::-1].tolist(),
            y=upper.tolist() + lower[::-1].tolist(),
            fill='toself',
            fillcolor=f'rgba(139, 195, 74, 0.2)',
            line=dict(color='rgba(255,255,255,0)'),
            name='Intervalle de confiance',
            showlegend=True
        ))
        
        fig.update_layout(
            title='Prévision Ventes Quotidiennes (unités)',
            xaxis_title='Date',
            yaxis_title='Unités vendues',
            height=500,
            plot_bgcolor='white',
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("📈 Croissance Prévue", "+12.4%", "+2.1% vs Q4")
        with col2:
            st.metric("💰 Revenus Estimés", "€18.7M", "+€2.1M")
        with col3:
            st.metric("🎯 Confiance Modèle", "91.2%", "Élevée")

# Tout est Données Page
elif page == "📚 Donnée Captive":
    st.markdown(f"<h1 style='color: {ACTIA_GREY};'>📄 Tout devient moteur pour l'IA</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 18px; color: {ACTIA_GREEN};'>L'histoire de Claire - Service Client Actia</p>", unsafe_allow_html=True)
    
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
    
    # 3 tabs: PDF textuel, Photo, et Audio
    tabs = st.tabs(["📄 PDF → Excel (Analyse d'Écart)", "📷 Photo → Détection Défauts", "🎤 Audio → Insights"])
    
    # TAB 1: PDF → Excel (Analyse d'Écart et Coûts)
    with tabs[0]:
        st.markdown(f"<h2 style='color: {ACTIA_GREY};'>📄 Analyse d'Écart et Coûts (Variance Analysis)</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {ACTIA_GREY}; font-size: 16px;'>Convertissez automatiquement vos rapports PDF en données Excel exploitables</p>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        uploaded_pdf = st.file_uploader("📤 Glissez-déposez votre PDF ici", 
                                       type=['pdf'], key='pdf_variance')
        
        if uploaded_pdf:
            col_pdf1, col_pdf2 = st.columns([1, 1])
            
            with col_pdf1:
                st.markdown(f"<h4 style='color: {ACTIA_GREY};'>📄 Document PDF Brut</h4>", unsafe_allow_html=True)
                
                st.text_area("Contenu extrait du PDF:", """
RAPPORT D'ANALYSE D'ÉCART - Q4 2024
Actia Group - Division Automobile
Date: 20 Novembre 2024
-------------------------------------------

COMPOSANTS ÉLECTRONIQUES:

TGX-2847-A (ECU Principal)
- Coût Prévu: €45.20
- Coût Réel: €52.80
- Écart: +€7.60 (+16.8%)
- Volume: 1,247 unités
- Impact Total: +€9,477

PCB-Advanced (Carte mère)
- Coût Prévu: €28.50
- Coût Réel: €31.20
- Écart: +€2.70 (+9.5%)
- Volume: 2,134 unités
- Impact Total: +€5,762

Capacitor-MLX (Condensateur)
- Coût Prévu: €0.30
- Coût Réel: €0.42
- Écart: +€0.12 (+40%)
- Volume: 15,890 unités
- Impact Total: +€1,907

IC-NXP-Core (Puce NXP)
- Coût Prévu: €18.90
- Coût Réel: €17.50
- Écart: -€1.40 (-7.4%)
- Volume: 856 unités
- Impact Total: -€1,198

-------------------------------------------
SYNTHÈSE:
Total Écart: +€16,948
Taux Variance: +12.3%
Alerte: Dépassement budget composants
""", height=450, disabled=True)
            
            with col_pdf2:
                st.markdown(f"<h4 style='color: {ACTIA_GREEN};'>📊 Tableau Excel Généré</h4>", unsafe_allow_html=True)
                
                if st.button("🚀 Convertir en Excel", key='convert_pdf', use_container_width=True):
                    with st.spinner("🔄 Extraction et structuration en cours..."):
                        time.sleep(2)
                    
                    st.success("✅ Document converti avec succès!")
                    
                    # DataFrame structuré
                    df_variance = pd.DataFrame({
                        'Composant': ['TGX-2847-A', 'PCB-Advanced', 'Capacitor-MLX', 'IC-NXP-Core'],
                        'Coût Prévu (€)': [45.20, 28.50, 0.30, 18.90],
                        'Coût Réel (€)': [52.80, 31.20, 0.42, 17.50],
                        'Écart (€)': [7.60, 2.70, 0.12, -1.40],
                        'Écart (%)': ['+16.8%', '+9.5%', '+40.0%', '-7.4%'],
                        'Volume': [1247, 2134, 15890, 856],
                        'Impact Total (€)': [9477, 5762, 1907, -1198]
                    })
                    
                    # Colorer les écarts
                    st.dataframe(
                        df_variance.style.applymap(
                            lambda x: 'background-color: #ffebee' if isinstance(x, str) and '+' in x else 
                                     ('background-color: #e8f5e9' if isinstance(x, str) and '-' in x else ''),
                            subset=['Écart (%)']
                        ),
                        use_container_width=True,
                        hide_index=True
                    )
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    # Metrics
                    col_m1, col_m2, col_m3 = st.columns(3)
                    with col_m1:
                        st.metric("Écart Total", "+€16,948", "⚠️ +12.3%")
                    with col_m2:
                        st.metric("Composants Analysés", "4", "100%")
                    with col_m3:
                        st.metric("Temps Extraction", "2.3 sec", "vs 15 min manuel")
                    
                    st.download_button(
                        "⬇️ Télécharger Excel",
                        data="simulation",
                        file_name="analyse_ecart_Q4_2024.xlsx",
                        mime="application/vnd.ms-excel",
                        use_container_width=True
                    )
        else:
            st.info("👆 Uploadez un PDF pour voir la conversion automatique en Excel")
    
    # TAB 2: Photo → Détection Défauts
    with tabs[1]:
        st.markdown(f"<h2 style='color: {ACTIA_GREY};'>📷 Détection Automatique de Défauts Visuels</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {ACTIA_GREY}; font-size: 16px;'>IA pour identifier les défauts sur vos cartes électroniques</p>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        uploaded_photo = st.file_uploader("📤 Glissez-déposez une photo de carte électronique", 
                                        type=['jpg', 'png', 'jpeg', 'pdf'], key='photo_defect')
        
        if uploaded_photo:
            col_img1, col_img2 = st.columns([1, 1])
            
            with col_img1:
                st.markdown(f"<h4 style='color: {ACTIA_GREY};'>📷 Image Uploadée</h4>", unsafe_allow_html=True)
                
                # Si c'est une image, l'afficher. Si PDF, simuler
                if uploaded_photo.type.startswith('image'):
                    st.image(uploaded_photo, caption="Carte électronique à analyser", use_container_width=True)
                else:
                    # Pour PDF, afficher un placeholder
                    st.markdown(f"""
                    <div style='background-color: {ACTIA_LIGHT_GREY}; padding: 60px; text-align: center; border-radius: 10px;'>
                        <h3 style='color: {ACTIA_GREY};'>📄 PDF Chargé</h3>
                        <p style='color: {ACTIA_GREY};'>{uploaded_photo.name}</p>
                        <p style='color: {ACTIA_GREY};'>Taille: {uploaded_photo.size} bytes</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            with col_img2:
                st.markdown(f"<h4 style='color: {ACTIA_GREEN};'>🤖 Analyse IA</h4>", unsafe_allow_html=True)
                
                if st.button("🔍 Lancer Détection Défauts", key='detect_defects', use_container_width=True):
                    with st.spinner("🤖 Analyse IA en cours..."):
                        progress = st.progress(0)
                        for i in range(100):
                            time.sleep(0.02)
                            progress.progress(i + 1)
                    
                    st.warning("⚠️ **Défaut détecté sur la carte!**")
                    
                    # Simuler un cercle rouge sur une zone
                    st.markdown(f"""
                    <div style='background-color: #fff3cd; border-left: 5px solid #ffc107; 
                                padding: 20px; border-radius: 10px; margin: 15px 0;'>
                        <h4 style='color: #856404; margin: 0;'>🔍 Défaut Identifié</h4>
                        <br>
                        <ul style='color: #856404; margin: 10px 0; line-height: 1.8;'>
                            <li><strong>Type:</strong> Soudure froide (Cold Solder Joint)</li>
                            <li><strong>Localisation:</strong> Zone C4 (coin supérieur droit)</li>
                            <li><strong>Composant:</strong> Condensateur C47</li>
                            <li><strong>Sévérité:</strong> Critique (9/10)</li>
                            <li><strong>Confiance IA:</strong> 94.3%</li>
                            <li><strong>Action:</strong> ❌ Rejet - Reprise nécessaire</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Visualisation du défaut sur l'image réelle
                    st.markdown(f"<h5 style='color: {ACTIA_GREY};'>📍 Localisation Précise:</h5>", unsafe_allow_html=True)
                    
                    if uploaded_photo.type.startswith('image'):
                        from PIL import Image, ImageDraw
                        import io
                        
                        image = Image.open(uploaded_photo).convert('RGB')
                        draw = ImageDraw.Draw(image)
                        
                        img_width, img_height = image.size
                        defect_x = int(img_width * 0.60)
                        defect_y = int(img_height * 0.45)
                        radius = int(min(img_width, img_height) * 0.06)
                        
                        for i in range(2):
                            r = radius * (1 + i * 0.3)
                            draw.ellipse(
                                [defect_x - r, defect_y - r, defect_x + r, defect_y + r],
                                outline='red',
                                width=max(3, int(radius * 0.12))
                            )
                        
                        st.image(image, caption="Carte électronique avec défaut identifié par IA", use_container_width=True)
                        st.markdown(f"<p style='text-align: center; color: {ACTIA_GREY}; font-size: 14px; margin-top: 10px;'>🔴 Défaut détecté en Zone C4 (marqué par le cercle rouge)</p>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div style='background-color: {ACTIA_LIGHT_GREY}; padding: 20px; border-radius: 10px; text-align: center;'>
                            <div style='position: relative; display: inline-block;'>
                                <div style='width: 300px; height: 200px; background-color: #2d5016; 
                                            border-radius: 5px; position: relative;'>
                                    <div style='position: absolute; top: 30px; right: 40px; 
                                                width: 40px; height: 40px; 
                                                border: 3px solid red; border-radius: 50%;
                                                animation: pulse 1.5s infinite;'></div>
                                    <div style='position: absolute; top: 25px; right: 85px; 
                                                background-color: red; color: white; 
                                                padding: 5px 10px; border-radius: 5px; font-size: 12px;'>
                                        Zone C4 - Défaut détecté
                                    </div>
                                </div>
                            </div>
                            <p style='color: {ACTIA_GREY}; margin-top: 10px; font-size: 14px;'>
                                Représentation schématique de la carte avec défaut marqué en rouge
                            </p>
                        </div>
                        <style>
                        @keyframes pulse {{
                            0%, 100% {{ opacity: 1; }}
                            50% {{ opacity: 0.3; }}
                        }}
                        </style>
                        """, unsafe_allow_html=True)
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    # Stats
                    st.markdown(f"""
                    <div style='background-color: white; padding: 20px; border-radius: 10px; 
                                box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
                        <h4 style='color: {ACTIA_GREY}; margin-top: 0;'>📊 Statistiques Contrôle Qualité</h4>
                        <p><strong>Taux de détection automatique:</strong> <span style='color: {ACTIA_GREEN};'>99.2%</span></p>
                        <p><strong>Faux positifs:</strong> <span style='color: {ACTIA_GREY};'>0.8%</span></p>
                        <p><strong>Gain de temps:</strong> <span style='color: {ACTIA_GREEN};'>92%</span> vs inspection manuelle</p>
                        <p><strong>Coût évité:</strong> <span style='color: {ACTIA_GREEN};'>€180K/an</span> en défauts non détectés</p>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("👆 Uploadez une photo (JPG, PNG) ou un PDF de carte électronique pour analyse")
    
    # TAB 3: Audio → Insights
    with tabs[2]:
        st.markdown(f"<h2 style='color: {ACTIA_GREY};'>🎤 Audio → Insights (Transcription)</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: {ACTIA_GREY}; font-size: 16px;'>Analysez vos enregistrements vocaux et réunions</p>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        uploaded_audio_pdf = st.file_uploader("📤 Glissez-déposez votre PDF avec transcription audio", 
                                             type=['pdf'], key='audio_transcript')
        
        if uploaded_audio_pdf:
            col_aud1, col_aud2 = st.columns([1, 1])
            
            with col_aud1:
                st.markdown(f"<h4 style='color: {ACTIA_GREY};'>📄 Document PDF</h4>", unsafe_allow_html=True)
                
                st.markdown(f"""
                <div style='background-color: {ACTIA_LIGHT_GREY}; padding: 40px; text-align: center; border-radius: 10px;'>
                    <h3 style='color: {ACTIA_GREY};'>🎤 PDF Transcription</h3>
                    <p style='color: {ACTIA_GREY};'><strong>{uploaded_audio_pdf.name}</strong></p>
                    <p style='color: {ACTIA_GREY};'>Taille: {uploaded_audio_pdf.size / 1024:.1f} KB</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                st.text_area("📝 Transcription extraite du PDF:", """
[Réunion Qualité - 23 Nov 2024 - 10:45]

Ingénieur Qualité (Marie):
"Bonjour à tous. J'ai constaté une augmentation des défauts 
sur le composant TGX-2847-A depuis hier soir. On a eu 3 rejets 
sur les 50 dernières unités testées. Le problème semble venir 
des soudures sur le condensateur C47."

Responsable Production (Jean):
"J'ai vérifié les paramètres. La température de la station 
de soudage était à 315°C au lieu de 340°C. On a eu un problème 
de calibration ce matin."

Directeur Opérations (Paul):
"Il faut retester immédiatement les 200 unités produites 
depuis hier 18h. Marie, tu peux coordonner ça?"

Marie: "Oui, j'envoie l'alerte qualité maintenant."
""", height=320, disabled=True)
            
            with col_aud2:
                st.markdown(f"<h4 style='color: {ACTIA_GREEN};'>🤖 Analyse IA & Insights</h4>", unsafe_allow_html=True)
                
                if st.button("🚀 Extraire Insights", key='analyze_transcript', use_container_width=True):
                    with st.spinner("🔍 Analyse IA du contenu..."):
                        progress = st.progress(0)
                        for i in range(100):
                            time.sleep(0.02)
                            progress.progress(i + 1)
                    
                    st.success("✅ Insights extraits avec succès!")
                    
                    st.markdown(f"""
                    <div style='background-color: #fff3cd; border-left: 5px solid #ffc107; 
                                padding: 20px; border-radius: 10px; margin: 15px 0;'>
                        <h4 style='color: #856404; margin: 0;'>⚠️ Problème Qualité Critique Identifié</h4>
                        <br>
                        <ul style='color: #856404; margin: 10px 0; line-height: 1.8;'>
                            <li><strong>Composant affecté:</strong> TGX-2847-A, Condensateur C47</li>
                            <li><strong>Cause racine:</strong> Température incorrecte (315°C vs 340°C requis)</li>
                            <li><strong>Impact mesuré:</strong> 6% taux de rejet (3/50 unités)</li>
                            <li><strong>Période affectée:</strong> Hier 18h00 → Aujourd'hui 10h45</li>
                            <li><strong>Unités à retester:</strong> 200 unités</li>
                            <li><strong>Coût estimé:</strong> €3,200 si défauts non détectés</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(f"<h5 style='color: {ACTIA_GREY}; margin-top: 25px;'>📊 Actions Automatiques Déclenchées:</h5>", unsafe_allow_html=True)
                    
                    col_a1, col_a2 = st.columns(2)
                    with col_a1:
                        st.markdown(f"""
                        <div style='background-color: #e8f5e9; padding: 15px; border-radius: 10px; border-left: 4px solid {ACTIA_GREEN};'>
                            <strong style='color: {ACTIA_DARK_GREEN};'>✅ Ticket Qualité Créé</strong>
                            <p style='color: {ACTIA_GREY}; margin: 5px 0 0 0;'>#QA-2024-1142</p>
                        </div>
                        """, unsafe_allow_html=True)
                    with col_a2:
                        st.markdown(f"""
                        <div style='background-color: #e8f5e9; padding: 15px; border-radius: 10px; border-left: 4px solid {ACTIA_GREEN};'>
                            <strong style='color: {ACTIA_DARK_GREEN};'>✅ Alerte Envoyée</strong>
                            <p style='color: {ACTIA_GREY}; margin: 5px 0 0 0;'>Équipe qualité notifiée</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    # Métriques d'impact
                    col_m1, col_m2, col_m3 = st.columns(3)
                    with col_m1:
                        st.metric("Unités à Retester", "200", "⚠️")
                    with col_m2:
                        st.metric("Coût Risque", "€3,200", delta="Évité si action rapide", delta_color="inverse")
                    with col_m3:
                        st.metric("Temps Sauvé", "2h30", delta="vs saisie manuelle", delta_color="normal")
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    # Stats globales
                    st.markdown(f"""
                    <div style='background-color: white; padding: 20px; border-radius: 10px; 
                                box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
                        <h4 style='color: {ACTIA_GREY}; margin-top: 0;'>💡 Bénéfices Analyse Audio/Transcription</h4>
                        <p><strong>Temps de traitement:</strong> <span style='color: {ACTIA_GREEN};'>2 minutes</span> vs 2h30 manuel</p>
                        <p><strong>Précision extraction:</strong> <span style='color: {ACTIA_GREEN};'>98.7%</span></p>
                        <p><strong>Actions automatiques:</strong> <span style='color: {ACTIA_GREEN};'>Tickets + Alertes</span></p>
                        <p><strong>Réduction des délais:</strong> <span style='color: {ACTIA_GREEN};'>95%</span> plus rapide</p>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("👆 Uploadez un PDF contenant une transcription audio pour analyse")

# Pour conclure Page
elif page == "📹 Pour conclure":
    st.markdown(f"<h1 style='color: {ACTIA_GREY};'>📹 Pour Conclure</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 18px; color: {ACTIA_GREEN};'>L'innovation profitable commence ici</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Introduction
    st.markdown(f"""
    <div style='background-color: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin: 20px 0;'>
        <h2 style='color: {ACTIA_GREY}; margin-top: 0;'>🎯 Snowflake : Plus qu'une Plateforme, un Accélérateur de Transformation</h2>
        <p style='font-size: 17px; color: {ACTIA_GREY}; line-height: 1.8;'>
            Vous avez vu comment Snowflake transforme la donnée en actions concrètes :
            <br><br>
            ✅ <strong>IA accessible</strong> partout, pour tous<br>
            ✅ <strong>Données non structurées</strong> transformées en insights<br>
            ✅ <strong>Enrichissement externe</strong> pour anticiper et préserver les marges
            <br><br>
            Regardez cette vidéo pour comprendre l'impact de Snowflake sur votre compétitivité.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Section vidéo
    st.markdown(f"<h2 style='color: {ACTIA_GREY};'>🎬 Vidéo de Conclusion</h2>", unsafe_allow_html=True)
    
    # Vidéo YouTube
    video_url = "https://youtu.be/-82VSYiPZPg"
    st.video(video_url)
    
    # Message de conclusion
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, {ACTIA_GREEN} 0%, {ACTIA_DARK_GREEN} 100%); 
                padding: 30px; border-radius: 15px; text-align: center;'>
        <h2 style='color: white; margin: 0;'>🚀 Prêt à Transformer Vos Données en Avantage Concurrentiel ?</h2>
        <p style='color: white; margin-top: 15px; font-size: 18px;'>
            Contactez-nous pour découvrir comment Snowflake peut accélérer votre innovation.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div style='text-align: center; padding: 20px; background-color: {ACTIA_GREY}; 
            border-radius: 10px; color: white;'>
    <p style='margin: 0;'>❄️ <strong>Snowflake x Actia</strong> | Demo EBC 2025</p>
    <p style='margin: 5px 0 0 0; font-size: 14px;'>Votre plateforme data pour la compétitivité</p>
</div>
""", unsafe_allow_html=True)


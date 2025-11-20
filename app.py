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
    ["🏠 Accueil", "🤖 IA Accessible", "🏭 OEE & ML", "🌐 Marketplace", "📄 Tout est Données"],
    label_visibility="collapsed"
)

# Home Page
if page == "🏠 Accueil":
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
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {ACTIA_GREEN} 0%, {ACTIA_DARK_GREEN} 100%); 
                    padding: 25px; border-radius: 15px; margin: 10px 0; height: 200px;'>
            <h3 style='color: white; margin: 0;'>1️⃣ Rendre l'IA Accessible</h3>
            <p style='color: white; margin-top: 15px; font-size: 16px;'>
                • QR code<br>
                • Parler à l'IA en langage naturel<br>
                • Tous les LLM (GPT, DeepSeek...)<br>
                • Sécurité & confidentialité garanties
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {ACTIA_GREY} 0%, #8B8B8B 100%); 
                    padding: 25px; border-radius: 15px; margin: 10px 0; height: 200px;'>
            <h3 style='color: white; margin: 0;'>3️⃣ Vendre vos Données</h3>
            <p style='color: white; margin-top: 15px; font-size: 16px;'>
                • Enrichissement externe (S&P 500, météo)<br>
                • Meilleurs forecasts<br>
                • Marketplace pour monétiser<br>
                • Nouveaux flux de revenus
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {ACTIA_GREY} 0%, {ACTIA_DARK_GREEN} 100%); 
                    padding: 25px; border-radius: 15px; margin: 10px 0; height: 200px;'>
            <h3 style='color: white; margin: 0;'>2️⃣ L'IA c'est aussi le ML</h3>
            <p style='color: white; margin-top: 15px; font-size: 16px;'>
                • Dashboard OEE temps réel<br>
                • Prédictions & forecasting<br>
                • Détection d'anomalies<br>
                • Optimisation production
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {ACTIA_GREEN} 0%, #1E8B57 100%); 
                    padding: 25px; border-radius: 15px; margin: 10px 0; height: 200px;'>
            <h3 style='color: white; margin: 0;'>4️⃣ Tout est Données</h3>
            <p style='color: white; margin-top: 15px; font-size: 16px;'>
                • PDF → Excel automatique<br>
                • Image → Texte<br>
                • Détection d'anomalies visuelles<br>
                • Énorme potentiel non structuré
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Footer EBC 2025
    st.markdown(f"""
    <div style='text-align: center; padding: 20px; background-color: {ACTIA_GREY}; 
                border-radius: 10px; color: white; margin-top: 40px;'>
        <p style='margin: 0; font-size: 18px; font-weight: bold;'>EBC 2025</p>
        <p style='margin: 5px 0 0 0; font-size: 14px;'>❄️ Powered by Snowflake</p>
    </div>
    """, unsafe_allow_html=True)

# IA Accessible Page
elif page == "🤖 IA Accessible":
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
        cortex_url = "http://192.168.1.100:8502"  # Replace with your local IP
        
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
        
        # Preview of Cortex Analyst interface
        st.markdown(f"""
        <div style='background-color: {ACTIA_GREY}; padding: 40px 20px; border-radius: 30px; 
                    box-shadow: 0 10px 30px rgba(0,0,0,0.3);'>
            <div style='background-color: white; padding: 20px; border-radius: 20px; min-height: 600px;'>
                <div style='text-align: center; margin-bottom: 20px;'>
                    <h2 style='color: {ACTIA_GREY}; margin: 0;'>🤖 Actia Cortex Analyst</h2>
                    <p style='color: {ACTIA_GREY}; font-size: 14px;'>IA pour vos données de production</p>
                </div>
                
                <!-- Dashboard Metrics -->
                <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 20px 0;'>
                    <div style='background: linear-gradient(135deg, {ACTIA_GREY} 0%, {ACTIA_DARK_GREEN} 100%); 
                                color: white; padding: 15px; border-radius: 10px; text-align: center;'>
                        <div style='font-size: 12px;'>🏭 Production</div>
                        <div style='font-size: 24px; font-weight: bold;'>1,247</div>
                    </div>
                    <div style='background: linear-gradient(135deg, {ACTIA_GREY} 0%, {ACTIA_DARK_GREEN} 100%); 
                                color: white; padding: 15px; border-radius: 10px; text-align: center;'>
                        <div style='font-size: 12px;'>✅ Qualité</div>
                        <div style='font-size: 24px; font-weight: bold;'>98.4%</div>
                    </div>
                </div>
                
                <!-- Chart placeholder -->
                <div style='background-color: #f5f5f5; padding: 15px; border-radius: 10px; margin: 15px 0;'>
                    <div style='color: {ACTIA_GREY}; font-size: 14px; font-weight: bold; margin-bottom: 10px;'>
                        📈 Production (7 jours)
                    </div>
                    <div style='height: 100px; background: linear-gradient(to top, {ACTIA_GREEN}40 0%, {ACTIA_GREEN}20 100%); 
                                border-radius: 5px; position: relative;'>
                        <svg style='width: 100%; height: 100%;' viewBox='0 0 100 100' preserveAspectRatio='none'>
                            <polyline points='0,80 20,70 40,60 60,55 80,50 100,45' 
                                      style='fill: none; stroke: {ACTIA_GREEN}; stroke-width: 2;' />
                        </svg>
                    </div>
                </div>
                
                <!-- Chat section -->
                <div style='background-color: {ACTIA_LIGHT_GREY}; padding: 12px; border-radius: 10px; margin: 15px 0;'>
                    <div style='color: {ACTIA_GREY}; font-size: 13px; font-weight: bold; margin-bottom: 8px;'>
                        💬 Posez vos questions
                    </div>
                    <div style='display: flex; gap: 5px; flex-wrap: wrap;'>
                        <span style='background: {ACTIA_GREEN}; color: white; padding: 5px 10px; 
                                     border-radius: 15px; font-size: 11px;'>📊 Qualité?</span>
                        <span style='background: {ACTIA_GREEN}; color: white; padding: 5px 10px; 
                                     border-radius: 15px; font-size: 11px;'>🔍 Problèmes?</span>
                        <span style='background: {ACTIA_GREEN}; color: white; padding: 5px 10px; 
                                     border-radius: 15px; font-size: 11px;'>📈 Tendance?</span>
                    </div>
                </div>
                
                <!-- Chat example -->
                <div style='background-color: white; border: 2px solid {ACTIA_LIGHT_GREY}; 
                            padding: 10px; border-radius: 10px; margin: 10px 0;'>
                    <div style='color: {ACTIA_GREY}; font-size: 11px; font-weight: bold;'>🤖 Cortex Analyst</div>
                    <p style='color: {ACTIA_GREY}; font-size: 10px; margin: 5px 0; line-height: 1.4;'>
                        Taux qualité: 98.4%<br>
                        Évolution: +0.8% vs mois dernier<br>
                        Station à surveiller: Intégration
                    </p>
                </div>
                
                <div style='text-align: center; margin-top: 15px; padding-top: 15px; 
                            border-top: 1px solid {ACTIA_LIGHT_GREY};'>
                    <p style='color: {ACTIA_GREY}; font-size: 11px;'>❄️ Powered by Snowflake</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style='background-color: {ACTIA_GREEN}; color: white; padding: 20px; border-radius: 15px; text-align: center;'>
            <h3 style='margin: 0;'>🚀 Lancez Cortex Analyst</h3>
            <p style='margin: 10px 0 0 0;'>Scanner le QR code ou lancer localement sur le port 8502</p>
        </div>
        """, unsafe_allow_html=True)

# OEE & ML Page (fusion Traçabilité + Prédictions)
elif page == "🏭 OEE & ML":
    st.markdown(f"<h1 style='color: {ACTIA_GREY};'>📊 OEE Monitoring & Machine Learning</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 18px; color: {ACTIA_GREEN};'>L'IA c'est aussi le ML avec les forecasts</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Status Alert (inspired by screenshot)
    st.markdown(f"""
    <div style='background-color: #ffebee; border-left: 5px solid #f44336; 
                padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
        <h3 style='color: #d32f2f; margin: 0;'>🔴 STATUS: Critical - Only able to achieve 35% of remaining production needed</h3>
        <p style='color: {ACTIA_GREY}; margin-top: 10px; font-size: 16px;'>
            <strong>REASON:</strong> Current production trend shows ability to produce 51 units vs 144 needed units, 
            with OEE at 72% and Run Rate at 50%, indicating severe shortfall of 93 units by end of shift.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # OEE Metrics Chart (inspired by screenshot - multi-line graph)
    st.markdown(f"<h3 style='color: {ACTIA_GREY};'>📈 OEE Metrics - Live Monitoring</h3>", unsafe_allow_html=True)
    
    # Generate multi-line OEE data (simulating different stations like screenshot)
    dates = pd.date_range(start='2024-05-22 15:00', end='2024-05-23 01:00', freq='H')
    
    # Create data for multiple production lines (like screenshot)
    fig_oee = go.Figure()
    
    lines = [
        {'name': 'DTP-RL-01 - Material Intake', 'color': '#1f77b4'},
        {'name': 'DTP-RL-02 - Storage', 'color': '#ff7f0e'},
        {'name': 'DTP-RL-03 - Distribution', 'color': '#2ca02c'},
        {'name': 'DTP-RL-04 - Assembly Line 1', 'color': '#d62728'},
        {'name': 'DTP-RL-05 - Assembly Line 2', 'color': '#9467bd'},
        {'name': 'DTP-RL-06 - Quality Check', 'color': '#8c564b'},
        {'name': 'DTP-RL-07 - Packaging', 'color': '#e377c2'}
    ]
    
    for line in lines:
        # Generate varying OEE values (70-100% with some drops)
        oee_values = []
        for i in range(len(dates)):
            base = random.uniform(80, 95)
            # Add occasional drops
            if random.random() < 0.1:
                base = random.uniform(60, 75)
            oee_values.append(base)
        
        fig_oee.add_trace(go.Scatter(
            x=dates,
            y=oee_values,
            name=line['name'],
            mode='lines+markers',
            line=dict(width=2, color=line['color']),
            marker=dict(size=6)
        ))
    
    fig_oee.update_layout(
        height=500,
        xaxis_title="Time",
        yaxis_title="OEE (%)",
        yaxis=dict(range=[50, 105]),
        hovermode='x unified',
        plot_bgcolor='white',
        legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5)
    )
    
    st.plotly_chart(fig_oee, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Chatbot section (like screenshot with "Why did OEE drop?")
    col_chat, col_info = st.columns([3, 2])
    
    with col_chat:
        st.markdown(f"""
        <div style='background-color: white; padding: 20px; border-radius: 15px; 
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
            <h3 style='color: {ACTIA_GREEN}; margin-top: 0;'>💬 Ask the AI</h3>
            <div style='background-color: {ACTIA_LIGHT_GREY}; padding: 15px; border-radius: 10px; margin: 10px 0;'>
                <strong style='color: {ACTIA_GREY};'>Prompt:</strong>
                <p style='color: {ACTIA_GREY}; margin: 5px 0;'>Why did OEE drop?</p>
            </div>
            <div style='background-color: white; border: 2px solid {ACTIA_LIGHT_GREY}; 
                        padding: 15px; border-radius: 10px;'>
                <strong style='color: {ACTIA_GREEN};'>Response:</strong>
                <p style='color: {ACTIA_GREY}; margin-top: 10px; line-height: 1.6;'>
                    To analyze why OEE dropped, I'll look for significant decreases in the OEE values 
                    and examine the contributing factors (Quality, Performance, and Availability).
                    <br><br>
                    Looking at the data, there are several notable drops in OEE. One significant drop 
                    occurs at <strong>2024-05-23 01:00:00.000</strong> where OEE falls to 0.7109. 
                    This drop was caused by:
                    <br><br>
                    1. A relatively good <strong>Quality score (0.9552)</strong><br>
                    2. A decent <strong>Performance score (0.9255)</strong><br>
                    3. A low <strong>Availability score (0.8042)</strong>
                    <br><br>
                    The main factor causing this OEE drop was the <span style='color: #d32f2f;'><strong>low Availability score</strong></span>, 
                    indicating that the equipment was not running as much as it should have been during this period. 
                    This could be due to:
                    <br>
                    • Unplanned downtime<br>
                    • Equipment failures<br>
                    • Setup and adjustment time<br>
                    • Idle time<br>
                    • Material shortages
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_info:
        st.markdown(f"<h3 style='color: {ACTIA_GREEN};'>🎯 ML Predictions</h3>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: white; padding: 15px; border-radius: 10px; 
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 15px;'>
            <h4 style='color: {ACTIA_GREY}; margin: 0;'>Forecast Next 4 Hours</h4>
            <h2 style='color: {ACTIA_GREEN}; margin: 10px 0;'>78% OEE</h2>
            <p style='color: {ACTIA_GREY}; margin: 0;'>Confidence: 92%</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: #fff3cd; border-left: 5px solid #ffc107; 
                    padding: 15px; border-radius: 10px; margin-bottom: 15px;'>
            <h4 style='color: #856404; margin: 0;'>⚠️ Risk Alert</h4>
            <p style='color: #856404; margin: 10px 0 0 0;'>
                Station RL-03 predicted to drop below 75% within 2 hours
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: white; padding: 15px; border-radius: 10px; 
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
            <h4 style='color: {ACTIA_GREY}; margin: 0;'>🔍 Root Causes Detected</h4>
            <ul style='color: {ACTIA_GREY}; margin: 10px 0;'>
                <li>Availability: -12%</li>
                <li>Changeover time: +18%</li>
                <li>Material delay: 3 incidents</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Note: Pages IA Conversationnelle et Prédictions fusionnées dans OEE & ML

# Marketplace Page (refaite)
elif page == "🌐 Marketplace":
    st.markdown(f"<h1 style='color: {ACTIA_GREY};'>🤖 Assistant IA Snowflake Cortex</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 18px; color: {ACTIA_GREEN};'>Interrogez vos données en langage naturel</p>", unsafe_allow_html=True)
    
    # Pre-defined questions
    st.markdown(f"<h3 style='color: {ACTIA_GREY};'>💡 Questions Suggérées</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        q1 = st.button("📉 Quels produits ont une érosion de marge?", use_container_width=True)
    with col2:
        q2 = st.button("📦 Composants avec risque de pénurie?", use_container_width=True)
    with col3:
        q3 = st.button("💰 Produits les plus profitables?", use_container_width=True)
    
    # Chat interface
    st.markdown("<br>", unsafe_allow_html=True)
    
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Handle button clicks
    if q1:
        question = "Quels produits ont eu une érosion de marge au Q3 et pourquoi?"
    elif q2:
        question = "Liste les composants avec une augmentation de prix >30% des fournisseurs chinois"
    elif q3:
        question = "Quels sont les 5 produits les plus profitables sur leur cycle de vie?"
    else:
        question = None
    
    # Custom question input
    user_input = st.chat_input("Posez votre question...")
    
    if user_input:
        question = user_input
    
    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        
        # Display chat
        with st.chat_message("user"):
            st.markdown(question)
        
        with st.chat_message("assistant", avatar="❄️"):
            with st.spinner("🔍 Analyse des données Snowflake..."):
                time.sleep(2)
            
            # Hardcoded responses based on question type
            if "érosion" in question.lower() or "marge" in question.lower():
                response = f"""
                📊 **Analyse de l'érosion de marge - Q3 2024**
                
                J'ai analysé 247 produits dans Snowflake. Voici les résultats :
                
                **🚨 Top 3 produits avec érosion critique:**
                
                1. **TGX-ECU-2024** 
                   - Marge Q2: 45% → Q3: 28% (-17 points)
                   - Cause: Augmentation prix composants semiconducteurs (+35%)
                   - Impact: -€240K de marge
                
                2. **Actia Connect Pro**
                   - Marge Q2: 38% → Q3: 22% (-16 points)
                   - Cause: Sur-ingénierie (fonctionnalités non utilisées)
                   - Impact: -€180K de marge
                
                3. **SmartLogger V3**
                   - Marge Q2: 42% → Q3: 31% (-11 points)
                   - Cause: Concurrence chinoise (guerre des prix)
                   - Impact: -€125K de marge
                
                **💡 Recommandations:**
                - Renégocier contrats fournisseurs semiconducteurs
                - Simplifier Actia Connect Pro (retirer 3 modules non utilisés)
                - Repositionner SmartLogger sur services connectés
                """
            
            elif "pénurie" in question.lower() or "risque" in question.lower() or "composant" in question.lower():
                response = f"""
                ⚠️ **Analyse des risques de pénurie**
                
                **🔴 ALERTES CRITIQUES (5 composants):**
                
                | Composant | Prix | Fournisseur | Risque | Action |
                |-----------|------|-------------|--------|---------|
                | **IC-NXP-2847** | +38% | 🇨🇳 Chine | ⚠️ Élevé | Stock stratégique |
                | **PCB-Advanced** | +32% | 🇨🇳 Chine | ⚠️ Élevé | Double source |
                | **Capacitor-MLX** | +31% | 🇹🇼 Taiwan | 🟡 Moyen | Surveillance |
                | **Connector-USB-C** | +29% | 🇨🇳 Chine | 🟡 Moyen | Alternative EU |
                | **Sensor-Temp-Pro** | +27% | 🇰🇷 Corée | 🟢 Faible | Monitoring |
                
                **🌍 Analyse géopolitique:**
                - Tensions commerciales USA-Chine impactent 40% de votre supply chain
                - Recommandation: Diversification vers Europe (Infineon, STMicro)
                
                **💰 Impact financier estimé:**
                - Surcoût annuel: €1.2M si non géré
                - Économie potentielle avec stratégie alternative: €780K
                """
            
            elif "profitable" in question.lower():
                response = f"""
                💰 **Top 5 Produits les Plus Profitables (Cycle de Vie)**
                
                Analyse sur 5 ans de données Snowflake:
                
                **🏆 Classement:**
                
                1. **Actia TGX Gateway** 
                   - Marge moyenne: 52%
                   - Revenus cycle: €12.4M
                   - Profit net: €6.4M
                   - 🌟 Services récurrents: +€2.1M
                
                2. **SmartConnect Fleet**
                   - Marge moyenne: 48%
                   - Revenus cycle: €9.8M
                   - Profit net: €4.7M
                   - 🌟 SaaS: +€1.8M/an
                
                3. **EcoLogic Telematics**
                   - Marge moyenne: 45%
                   - Revenus cycle: €7.2M
                   - Profit net: €3.2M
                   - 🌟 Marketplace data: +€400K
                
                4. **DiagBox Pro**
                   - Marge moyenne: 43%
                   - Revenus cycle: €6.5M
                   - Profit net: €2.8M
                
                5. **Actia PowerControl**
                   - Marge moyenne: 41%
                   - Revenus cycle: €5.9M
                   - Profit net: €2.4M
                
                **📈 Insight clé:**
                Les produits avec services connectés génèrent 3x plus de revenus sur leur cycle de vie!
                """
            else:
                response = f"""
                🤖 **Analyse en cours...**
                
                J'ai accès à toutes vos données Snowflake:
                - 📊 Ventes & Commerce (5 ans historique)
                - 🏭 Production & Usines (Toulouse, Tunis)
                - 💰 Finance & Marges
                - 📦 Supply Chain & Fournisseurs
                - 🔧 Qualité & Traçabilité
                
                Posez-moi une question spécifique sur:
                - Rentabilité produits
                - Performance usines
                - Prévisions ventes
                - Risques supply chain
                - Analyse concurrence
                """
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Display conversation history
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: {ACTIA_GREEN};'>💬 Historique de Conversation</h3>", unsafe_allow_html=True)
    
    for msg in st.session_state.messages[-4:]:  # Show last 4 messages
        with st.chat_message(msg["role"], avatar="❄️" if msg["role"] == "assistant" else None):
            st.markdown(msg["content"])

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

# Marketplace Page
elif page == "🌐 Marketplace":
    st.markdown(f"<h1 style='color: {ACTIA_GREY};'>🌐 Snowflake Marketplace</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 18px; color: {ACTIA_GREEN};'>Nouveaux flux de revenus + Intelligence externe</p>", unsafe_allow_html=True)
    
    tabs = st.tabs(["💰 Vendre vos Données", "🛒 Acheter de l'Intelligence", "📊 Revenus Potentiels"])
    
    # Tab 1: Sell data
    with tabs[0]:
        st.markdown(f"<h2 style='color: {ACTIA_GREY};'>💰 Monétisez Vos Données</h2>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class='success-box'>
            <h3>🚀 Vos données ont de la valeur!</h3>
            <p style='font-size: 18px;'>Le secteur automobile cherche des données de production, qualité et tendances marché</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div style='background-color: white; padding: 25px; border-radius: 15px; 
                        border-left: 5px solid {ACTIA_GREEN}; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
                <h3 style='color: {ACTIA_GREY};'>📦 Dataset 1: Automotive Benchmarks</h3>
                <p><strong>Contenu:</strong></p>
                <ul>
                    <li>Temps de production moyens (anonymisés)</li>
                    <li>Taux de défauts par catégorie</li>
                    <li>Coûts composants agrégés</li>
                    <li>Tendances qualité 2020-2024</li>
                </ul>
                <p><strong>🎯 Clients potentiels:</strong> OEMs, cabinets conseil, investisseurs</p>
                <p><strong>💰 Prix suggéré:</strong> <span style='color: {ACTIA_GREEN}; font-size: 24px;'>€15K/an</span></p>
                <p><strong>📊 Demande estimée:</strong> 25-40 clients</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style='background-color: white; padding: 25px; border-radius: 15px; 
                        border-left: 5px solid {ACTIA_GREEN}; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
                <h3 style='color: {ACTIA_GREY};'>📦 Dataset 2: Supply Chain Intelligence</h3>
                <p><strong>Contenu:</strong></p>
                <ul>
                    <li>Évolution prix composants (historique 5 ans)</li>
                    <li>Fiabilité fournisseurs (scoring)</li>
                    <li>Délais de livraison moyens</li>
                    <li>Incidents supply chain</li>
                </ul>
                <p><strong>🎯 Clients potentiels:</strong> Manufacturiers, analystes financiers</p>
                <p><strong>💰 Prix suggéré:</strong> <span style='color: {ACTIA_GREEN}; font-size: 24px;'>€22K/an</span></p>
                <p><strong>📊 Demande estimée:</strong> 15-25 clients</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div style='background-color: white; padding: 25px; border-radius: 15px; 
                        border-left: 5px solid {ACTIA_DARK_GREEN}; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
                <h3 style='color: {ACTIA_GREY};'>📦 Dataset 3: SDV Trends & Usage</h3>
                <p><strong>Contenu:</strong></p>
                <ul>
                    <li>Données télématiques agrégées</li>
                    <li>Patterns d'utilisation véhicules</li>
                    <li>Performance software embarqué</li>
                    <li>Tendances features utilisées</li>
                </ul>
                <p><strong>🎯 Clients potentiels:</strong> OEMs, startups SDV, plateformes MaaS</p>
                <p><strong>💰 Prix suggéré:</strong> <span style='color: {ACTIA_GREEN}; font-size: 24px;'>€35K/an</span></p>
                <p><strong>📊 Demande estimée:</strong> 30-50 clients</p>
                <p><strong>🔥 FORTE DEMANDE</strong></p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, {ACTIA_GREEN} 0%, {ACTIA_DARK_GREEN} 100%); 
                        padding: 30px; border-radius: 15px; color: white; text-align: center;'>
                <h2>💰 Revenu Annuel Potentiel</h2>
                <h1 style='font-size: 48px; color: white;'>€1.2M - €2.4M</h1>
                <p style='font-size: 18px;'>Basé sur demande marché et benchmarks secteur</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Tab 2: Buy intelligence
    with tabs[1]:
        st.markdown(f"<h2 style='color: {ACTIA_GREY};'>🛒 Achetez de l'Intelligence Externe</h2>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class='info-box'>
            <h3>🌍 Enrichissez vos analyses avec des données externes</h3>
            <p style='font-size: 16px;'>Combinaison de vos données + données marketplace = Insights puissants</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Showcase marketplace datasets
        datasets = [
            {
                'name': '🌐 Geopolitical Risk Intelligence',
                'provider': 'McKinsey & Company',
                'desc': 'Risques géopolitiques temps réel, impact supply chain, prévisions tensions commerciales',
                'use_case': '✅ Anticiper pénuries composants',
                'price': '€18K/an',
                'impact': 'Économies: €500K/an'
            },
            {
                'name': '📊 Global Component Pricing',
                'provider': 'IHS Markit',
                'desc': 'Prix composants électroniques worldwide, historique + prévisions, indice inflation',
                'use_case': '✅ Optimiser négociations fournisseurs',
                'price': '€25K/an',
                'impact': 'Économies: €780K/an'
            },
            {
                'name': '🚛 Logistics & Weather Data',
                'provider': 'Weather.com + DHL',
                'desc': 'Données météo + disruptions logistiques, prévisions délais transport',
                'use_case': '✅ Optimiser planning production',
                'price': '€12K/an',
                'impact': 'Gain efficacité: +8%'
            },
            {
                'name': '🔋 EV Market Trends',
                'provider': 'BloombergNEF',
                'desc': 'Tendances marché véhicules électriques, adoption technologies, forecasts 2030',
                'use_case': '✅ Orienter R&D produits',
                'price': '€30K/an',
                'impact': 'ROI Innovation: +45%'
            }
        ]
        
        for dataset in datasets:
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"""
                <div style='background-color: white; padding: 20px; border-radius: 10px; 
                            margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                    <h3 style='color: {ACTIA_GREEN};'>{dataset['name']}</h3>
                    <p style='color: {ACTIA_GREY};'><strong>Fournisseur:</strong> {dataset['provider']}</p>
                    <p style='color: {ACTIA_GREY};'>{dataset['desc']}</p>
                    <p style='color: {ACTIA_GREY};'><strong>Cas d'usage Actia:</strong> {dataset['use_case']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div style='background-color: {ACTIA_LIGHT_GREY}; padding: 20px; 
                            border-radius: 10px; text-align: center; height: 100%;'>
                    <p style='color: {ACTIA_GREY};'><strong>Prix</strong></p>
                    <h3 style='color: {ACTIA_GREEN};'>{dataset['price']}</h3>
                    <p style='color: {ACTIA_GREY}; font-size: 14px;'>{dataset['impact']}</p>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Demo: Import dataset
        st.markdown(f"<h3 style='color: {ACTIA_GREEN};'>🎬 Démo: Import Dataset Marketplace</h3>", unsafe_allow_html=True)
        
        if st.button("▶️ Importer 'Geopolitical Risk Intelligence'", use_container_width=True):
            with st.spinner("Connexion au Snowflake Marketplace..."):
                time.sleep(1)
            st.success("✅ Dataset importé avec succès!")
            
            with st.spinner("Analyse des risques supply chain..."):
                time.sleep(1.5)
            
            st.markdown(f"""
            <div class='success-box'>
                <h3>⚠️ Alerte Géopolitique Détectée</h3>
                <p><strong>Composant: IC-NXP-2847</strong></p>
                <p>🌍 Origine: Taiwan (80% de votre approvisionnement)</p>
                <p>⚠️ Risque tensions Chine-Taiwan: Élevé (score 78/100)</p>
                <p>📅 Horizon: 3-6 mois</p>
                <p><strong>💡 Recommandation:</strong> Double-sourcing Europe (Infineon Germany) + Stock stratégique 4 mois</p>
                <p><strong>💰 Impact évité:</strong> €2.4M de pertes production</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Tab 3: Revenue projections
    with tabs[2]:
        st.markdown(f"<h2 style='color: {ACTIA_GREY};'>📊 Projection de Revenus Marketplace</h2>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Revenue projection chart
            years = ['Année 1', 'Année 2', 'Année 3', 'Année 4', 'Année 5']
            revenue = [400, 920, 1650, 2100, 2400]
            
            fig = go.Figure()
            
            fig.add_trace(go.Bar(
                x=years,
                y=revenue,
                marker=dict(
                    color=revenue,
                    colorscale=[[0, ACTIA_GREY], [1, ACTIA_GREEN]],
                    showscale=False
                ),
                text=[f'€{r}K' for r in revenue],
                textposition='outside'
            ))
            
            fig.update_layout(
                title='Projection Revenus Marketplace (5 ans)',
                yaxis_title='Milliers €',
                height=400,
                plot_bgcolor='white'
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # ROI calculation
            st.markdown(f"<h3 style='color: {ACTIA_GREEN};'>💡 Calcul ROI</h3>", unsafe_allow_html=True)
            
            roi_data = {
                'Élément': ['Revenus Vente Données (5 ans)', 'Économies Achats Intelligents (5 ans)', 
                           'Investissement Marketplace', 'ROI Net (5 ans)'],
                'Montant': ['€7.47M', '€3.20M', '-€150K', '€10.52M'],
                'Impact': ['📈', '💰', '💳', '🎯']
            }
            df_roi = pd.DataFrame(roi_data)
            st.dataframe(df_roi, use_container_width=True, hide_index=True)
        
        with col2:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, {ACTIA_DARK_GREEN} 0%, {ACTIA_GREEN} 100%); 
                        padding: 30px; border-radius: 15px; color: white; text-align: center;'>
                <h3 style='color: white;'>🎯 ROI Total</h3>
                <h1 style='font-size: 56px; color: white;'>7,013%</h1>
                <p style='font-size: 18px;'>sur 5 ans</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style='background-color: white; padding: 20px; border-radius: 10px; 
                        box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
                <h4 style='color: {ACTIA_GREY};'>📈 Métriques Clés</h4>
                <p style='color: {ACTIA_GREY};'><strong>Break-even:</strong> 2 mois</p>
                <p style='color: {ACTIA_GREY};'><strong>Marge nette:</strong> 94%</p>
                <p style='color: {ACTIA_GREY};'><strong>Clients potentiels:</strong> 70-115</p>
                <p style='color: {ACTIA_GREY};'><strong>Coût opérationnel:</strong> Minimal (automatisé)</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style='background-color: {ACTIA_GREEN}; padding: 20px; border-radius: 10px; color: white;'>
                <h4>✅ Benchmark Secteur</h4>
                <p><strong>Schneider Electric:</strong> €3.2M/an</p>
                <p><strong>Bosch:</strong> €5.8M/an</p>
                <p><strong>Continental:</strong> €4.1M/an</p>
                <p style='margin-top: 15px;'><strong>Votre potentiel: €2.4M/an dès année 5</strong></p>
            </div>
            """, unsafe_allow_html=True)

# Document AI Page
elif page == "📄 Document AI":
    st.markdown(f"<h1 style='color: {ACTIA_GREY};'>📄 Snowflake Document AI</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 18px; color: {ACTIA_GREEN};'>Structurez vos données non-structurées automatiquement</p>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='info-box'>
        <h3>🎯 Cas d'usage Actia</h3>
        <p>• Testeurs générant des fichiers texte → Structuration automatique</p>
        <p>• Images de composants → Extraction métadonnées</p>
        <p>• Factures fournisseurs → Intégration comptable</p>
        <p>• Rapports qualité PDF → Base de données analytique</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # File uploader
    st.markdown(f"<h3 style='color: {ACTIA_GREEN};'>📤 Glissez-Déposez vos Documents</h3>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Formats supportés: PDF, TXT, Images (JPG, PNG), CSV",
        type=['pdf', 'txt', 'jpg', 'png', 'csv'],
        help="Le Document AI va extraire et structurer automatiquement les données"
    )
    
    if uploaded_file is not None:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown(f"<h4 style='color: {ACTIA_GREY};'>📄 Document Original</h4>", unsafe_allow_html=True)
            
            # Display file info
            st.info(f"**Fichier:** {uploaded_file.name}\n\n**Taille:** {uploaded_file.size} bytes")
            
            # Simulate file content
            if uploaded_file.name.endswith('.txt'):
                st.text_area("Aperçu (non structuré):", 
"""TEST REPORT - COMPOSANT TGX-2847-A
Date: 2024-11-15
Operateur: QC-12
Usine: Toulouse

Tension: 3.3V - PASS
Current: 450mA - PASS
Temperature: -40C to 85C - PASS
Vibration Test: 20G - PASS
EMI Compliance: EN55022 - PASS

Defects Found: None
Quality Score: 98.7%
Recommendation: APPROVED FOR PRODUCTION

Components tested: 247
Batch: 2024-11-B-0847
Supplier: OMRON Japan
Cost: €45.20/unit
""", height=300, disabled=True)
        
        with col2:
            st.markdown(f"<h4 style='color: {ACTIA_GREEN};'>✨ Données Structurées (AI)</h4>", unsafe_allow_html=True)
            
            if st.button("🚀 Lancer Document AI", use_container_width=True):
                with st.spinner("🤖 IA Snowflake en cours d'analyse..."):
                    progress_bar = st.progress(0)
                    for i in range(100):
                        time.sleep(0.02)
                        progress_bar.progress(i + 1)
                
                st.success("✅ Document structuré avec succès!")
                
                # Display structured data
                structured_data = {
                    'Type': ['Rapport Test', 'Date', 'Opérateur', 'Usine', 'Composant',
                            'Tension', 'Courant', 'Température', 'Test Vibration', 
                            'Conformité EMI', 'Score Qualité', 'Décision', 
                            'Quantité Testée', 'Batch', 'Fournisseur', 'Coût Unitaire'],
                    'Valeur': ['Qualité Composant', '2024-11-15', 'QC-12', 'Toulouse', 'TGX-2847-A',
                              '3.3V', '450mA', '-40°C à 85°C', '20G', 'EN55022',
                              '98.7%', '✅ APPROUVÉ', '247', '2024-11-B-0847', 
                              'OMRON Japan', '€45.20'],
                    'Statut': ['📄', '📅', '👤', '🏭', '🔧',
                              '✅ PASS', '✅ PASS', '✅ PASS', '✅ PASS', '✅ PASS',
                              '✅', '✅', '📊', '📦', '🏢', '💰']
                }
                
                df_structured = pd.DataFrame(structured_data)
                st.dataframe(df_structured, use_container_width=True, hide_index=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                col_a, col_b = st.columns(2)
                
                with col_a:
                    st.markdown(f"""
                    <div style='background-color: {ACTIA_GREEN}; padding: 20px; 
                                border-radius: 10px; color: white;'>
                        <h4>⚡ Gain de Temps</h4>
                        <h2 style='color: white;'>95%</h2>
                        <p>5 min → 15 secondes</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col_b:
                    st.markdown(f"""
                    <div style='background-color: {ACTIA_GREY}; padding: 20px; 
                                border-radius: 10px; color: white;'>
                        <h4>🎯 Précision IA</h4>
                        <h2 style='color: white;'>99.2%</h2>
                        <p>Extraction données</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # SQL query to access data
                st.markdown(f"<h4 style='color: {ACTIA_GREEN};'>💾 Données Prêtes pour Snowflake</h4>", unsafe_allow_html=True)
                
                st.code("""
-- Les données sont maintenant queryables dans Snowflake
SELECT 
    component_id,
    quality_score,
    test_date,
    operator,
    factory,
    cost_per_unit,
    supplier
FROM actia.quality_tests
WHERE quality_score > 95 
    AND test_date >= DATEADD(month, -1, CURRENT_DATE())
ORDER BY test_date DESC;

-- Résultat: 1,247 tests trouvés
                """, language="sql")
                
                # Impact metrics
                st.markdown(f"<h4 style='color: {ACTIA_GREEN};'>📊 Impact sur Actia</h4>", unsafe_allow_html=True)
                
                impact_data = {
                    'Métrique': ['Documents traités/jour', 'Temps économisé/mois', 
                                'Erreurs de saisie', 'Coût FTE économisé/an'],
                    'Avant': ['~50 (manuel)', '120 heures', '~15%', '-'],
                    'Avec Document AI': ['~800 (automatique)', '480 heures', '<1%', '€85K'],
                    'Amélioration': ['16x', '4x', '94%', '💰']
                }
                
                df_impact = pd.DataFrame(impact_data)
                st.dataframe(df_impact, use_container_width=True, hide_index=True)
    
    else:
        # Show examples while waiting for upload
        st.markdown(f"<h3 style='color: {ACTIA_GREY};'>💡 Exemples de Documents Supportés</h3>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div style='background-color: white; padding: 20px; border-radius: 10px; 
                        text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <h1 style='color: {ACTIA_GREEN};'>📄</h1>
                <h4 style='color: {ACTIA_GREY};'>Rapports Test</h4>
                <p style='color: {ACTIA_GREY};'>TXT, PDF</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div style='background-color: white; padding: 20px; border-radius: 10px; 
                        text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <h1 style='color: {ACTIA_GREEN};'>🖼️</h1>
                <h4 style='color: {ACTIA_GREY};'>Images Composants</h4>
                <p style='color: {ACTIA_GREY};'>JPG, PNG</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div style='background-color: white; padding: 20px; border-radius: 10px; 
                        text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
                <h1 style='color: {ACTIA_GREEN};'>🧾</h1>
                <h4 style='color: {ACTIA_GREY};'>Factures</h4>
                <p style='color: {ACTIA_GREY};'>PDF, CSV</p>
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div style='text-align: center; padding: 20px; background-color: {ACTIA_GREY}; 
            border-radius: 10px; color: white;'>
    <p style='margin: 0;'>❄️ <strong>Snowflake x Actia</strong> | Demo EBC 2024</p>
    <p style='margin: 5px 0 0 0; font-size: 14px;'>Votre plateforme data pour la compétitivité</p>
</div>
""", unsafe_allow_html=True)


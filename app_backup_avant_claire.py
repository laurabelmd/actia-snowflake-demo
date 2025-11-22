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
    ["🏠 Accueil", "🤖 IA Accessible", "📄 Tout est Données", "🏭 ML"],
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

# ML Page (fusion Traçabilité + Prédictions)
elif page == "🏭 ML":
    st.markdown(f"<h1 style='color: {ACTIA_GREY};'>📊 Machine Learning & OEE Monitoring</h1>", unsafe_allow_html=True)
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
elif page == "📄 Tout est Données":
    st.markdown(f"<h1 style='color: {ACTIA_GREY};'>📄 Tout est Données</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 18px; color: {ACTIA_GREEN};'>Énorme potentiel dans les données non structurées</p>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style='background-color: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h2 style='color: {ACTIA_GREY}; margin-top: 0;'>💡 80% des données d'entreprise sont non structurées</h2>
        <p style='font-size: 17px; color: {ACTIA_GREY}; line-height: 1.8;'>
            Les données non structurées (PDF, images, vidéos, audio...) représentent un <strong>potentiel énorme</strong>:
            <br><br>
            ✅ <strong>PDF → Excel</strong> → Automatiser l'extraction de données<br>
            ✅ <strong>Image → Détection défauts</strong> → Contrôle qualité visuel automatique<br>
            ✅ <strong>Analyse en temps réel</strong> → Snowflake Document AI
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
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
                    
                    # Visualisation du défaut
                    st.markdown(f"<h5 style='color: {ACTIA_GREY};'>📍 Localisation Précise:</h5>", unsafe_allow_html=True)
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

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
<div style='text-align: center; padding: 20px; background-color: {ACTIA_GREY}; 
            border-radius: 10px; color: white;'>
    <p style='margin: 0;'>❄️ <strong>Snowflake x Actia</strong> | Demo EBC 2025</p>
    <p style='margin: 5px 0 0 0; font-size: 14px;'>Votre plateforme data pour la compétitivité</p>
</div>
""", unsafe_allow_html=True)


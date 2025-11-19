import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import time
import random

# Actia Colors (from official logo)
ACTIA_GREEN = "#009653"  # Actia green (official)
ACTIA_GREY = "#6e6b70"   # Actia grey (official)
ACTIA_LIGHT_GREY = "#E0E0E0"
ACTIA_DARK_GREEN = "#007A43"

# Function to generate responses (simulated Cortex Analyst)
def get_cortex_response(question, factory):
    question_lower = question.lower()
    
    # Quality related
    if any(word in question_lower for word in ['qualité', 'taux', 'conformité', 'défaut']):
        return f"""📊 **Analyse de qualité pour {factory}:**

• **Taux de qualité moyen ce mois:** 98.4%
• **Évolution:** +0.8% vs mois dernier
• **Meilleure station:** Test Final (99.5%)
• **Station à surveiller:** Intégration (97.8%)

**Détails par composant:**
- TGX-2847: 99.1% (excellent)
- ECU-2024: 98.2% (normal)
- PCB-1123: 97.5% (légère baisse)

💡 Recommandation: Audit de la station d'intégration recommandé."""
    
    # Production related
    elif any(word in question_lower for word in ['production', 'produire', 'produit', 'volume', 'quantité']):
        return f"""📈 **Analyse de production pour {factory}:**

• **Production aujourd'hui:** 1,247 composants
• **Production cette semaine:** 8,654 composants
• **Production ce mois:** 26,384 composants
• **Objectif mensuel:** 30,000 (88% atteint)

**Tendance:**
- Pic le mercredi: 1,320 unités/jour
- Creux le lundi: 1,180 unités/jour
- Croissance: +5.2% vs mois dernier

⚡ Les équipes sont sur la bonne voie pour atteindre l'objectif."""
    
    # Components/traceability
    elif any(word in question_lower for word in ['composant', 'traça', 'pièce', 'problème', 'défectueux']):
        return f"""🔍 **Analyse des composants pour {factory}:**

**Alertes actives:**
1. 🔴 **IC-NXP-2847**: Prix +15% (critique)
   - Fournisseur: NXP Semiconductors
   - Stock actuel: 3 semaines
   
2. 🟡 **PCB-Advanced**: Qualité en baisse
   - Taux actuel: 96.8% (-1.4%)
   - 12 défauts détectés cette semaine
   
3. 🟡 **Capacitor-MLX**: Délai livraison augmenté
   - Délai normal: 2 semaines
   - Délai actuel: 4 semaines

✅ Les autres composants sont dans les normes."""
    
    # Predictions/forecasting
    elif any(word in question_lower for word in ['prévision', 'prévoir', 'futur', 'demain', 'semaine prochaine']):
        return f"""🔮 **Prévisions pour {factory}:**

**Prochaines 7 jours:**
- Production attendue: 9,150 composants (+6% vs cette semaine)
- Taux qualité prévu: 98.6%
- Risque pénurie: Faible

**Facteurs identifiés:**
- ✅ Capacité production: Normal
- ⚠️ Stock IC-NXP-2847: Attention
- ✅ Équipes: Complet
- ✅ Équipements: Opérationnels

📊 Confiance de la prévision: 94%"""
    
    # Costs/pricing
    elif any(word in question_lower for word in ['coût', 'prix', 'euro', 'économie', 'budget']):
        return f"""💰 **Analyse des coûts pour {factory}:**

**Ce mois:**
- Coût matières premières: €487,340
- Évolution: +12% vs mois dernier
- Principaux contributeurs:
  - IC-NXP-2847: +€42,000 (+15%)
  - PCB-Advanced: +€28,000 (+12%)
  - Autres: +€18,000 (+8%)

**Impact sur marge:**
- Marge actuelle: 28.4%
- Marge objectif: 30%
- Écart: -1.6 points

💡 Actions suggérées: Négocier volumes avec NXP, chercher fournisseurs alternatifs."""
    
    # General/default
    else:
        return f"""🤖 **Résumé général pour {factory}:**

**État actuel:**
• Production: ✅ Normal (1,247 composants aujourd'hui)
• Qualité: ✅ Bonne (98.4%)
• Efficacité (OEE): ✅ Bonne (89.2%)
• Alertes: ⚠️ 3 actives

**Points d'attention:**
1. Prix composant IC-NXP-2847 en hausse
2. Qualité PCB-Advanced en légère baisse
3. Délais livraison Capacitor-MLX rallongés

**Questions que vous pouvez me poser:**
- Détails sur la production (volume, tendances)
- Analyse qualité par station/composant
- Traçabilité et problèmes composants
- Prévisions et planification
- Analyse des coûts et marges

Comment puis-je vous aider plus précisément?"""

# Page configuration
st.set_page_config(
    page_title="Actia Cortex Analyst",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with Actia branding
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
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 10px 0;
    }}
    .chat-message {{
        padding: 15px;
        border-radius: 15px;
        margin: 10px 0;
        max-width: 80%;
    }}
    .user-message {{
        background-color: {ACTIA_GREEN};
        color: white;
        margin-left: auto;
        text-align: right;
    }}
    .assistant-message {{
        background-color: white;
        color: {ACTIA_GREY};
        border: 2px solid {ACTIA_LIGHT_GREY};
    }}
    .dashboard-metric {{
        background: linear-gradient(135deg, {ACTIA_GREY} 0%, {ACTIA_DARK_GREEN} 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}
    .metric-value {{
        font-size: 42px;
        font-weight: bold;
        margin: 10px 0;
    }}
    .metric-label {{
        font-size: 16px;
        opacity: 0.9;
    }}
    h1, h2, h3 {{
        color: {ACTIA_GREY};
    }}
    .stTextInput>div>div>input {{
        border-radius: 10px;
    }}
    /* Chat container styling */
    .chat-container {{
        background: white;
        border-radius: 15px;
        padding: 20px;
        height: 500px;
        overflow-y: auto;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}
    </style>
""", unsafe_allow_html=True)

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Header with Actia branding
col_logo, col_title = st.columns([2, 3])
with col_logo:
    st.image("actia_logo.svg", use_column_width=True)
with col_title:
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, {ACTIA_GREY} 0%, {ACTIA_DARK_GREEN} 100%); 
                padding: 25px; border-radius: 15px; text-align: center;'>
        <h1 style='color: white; margin: 0; font-size: 28px;'>🤖 Cortex Analyst</h1>
        <p style='color: white; margin: 8px 0 0 0; font-size: 16px;'>Intelligence artificielle pour vos données de production</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Factory selector
factory = st.selectbox("🏭 Sélectionner l'usine", ["Toulouse", "Tunis"], label_visibility="visible")

# Dashboard Section
st.markdown(f"<h2 style='color: {ACTIA_GREY}; margin-top: 30px;'>📊 Dashboard en Temps Réel</h2>", unsafe_allow_html=True)

# Key Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    production_today = random.randint(1200, 1300)
    st.markdown(f"""
    <div class='dashboard-metric'>
        <div class='metric-label'>🏭 Production</div>
        <div class='metric-value'>{production_today:,}</div>
        <div class='metric-label'>composants</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    quality_rate = round(random.uniform(97.5, 99.5), 1)
    st.markdown(f"""
    <div class='dashboard-metric'>
        <div class='metric-label'>✅ Qualité</div>
        <div class='metric-value'>{quality_rate}%</div>
        <div class='metric-label'>conformité</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    efficiency = round(random.uniform(85, 95), 1)
    st.markdown(f"""
    <div class='dashboard-metric'>
        <div class='metric-label'>⚡ Efficacité</div>
        <div class='metric-value'>{efficiency}%</div>
        <div class='metric-label'>OEE</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    alerts = random.randint(2, 5)
    st.markdown(f"""
    <div class='dashboard-metric'>
        <div class='metric-label'>🚨 Alertes</div>
        <div class='metric-value'>{alerts}</div>
        <div class='metric-label'>actives</div>
    </div>
    """, unsafe_allow_html=True)

# Production Chart
st.markdown("<br>", unsafe_allow_html=True)
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.markdown(f"<h3 style='color: {ACTIA_GREY};'>📈 Production (7 jours)</h3>", unsafe_allow_html=True)
    dates = [(datetime.now() - timedelta(days=i)).strftime("%d/%m") for i in range(6, -1, -1)]
    production = [random.randint(1100, 1350) for _ in range(7)]
    
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(
        x=dates,
        y=production,
        mode='lines+markers',
        line=dict(color=ACTIA_GREEN, width=3),
        marker=dict(size=10, color=ACTIA_GREEN),
        fill='tozeroy',
        fillcolor=f'rgba(139, 195, 74, 0.2)'
    ))
    fig1.update_layout(
        height=250,
        margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor='white',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='lightgray'),
        showlegend=False
    )
    st.plotly_chart(fig1, use_container_width=True)

with col_chart2:
    st.markdown(f"<h3 style='color: {ACTIA_GREY};'>🎯 Qualité par Station</h3>", unsafe_allow_html=True)
    stations = ['Assemblage', 'Test Élec.', 'Intégration', 'Test Final']
    quality_by_station = [99.2, 98.7, 97.8, 99.5]
    
    fig2 = go.Figure(go.Bar(
        x=quality_by_station,
        y=stations,
        orientation='h',
        marker=dict(color=ACTIA_GREEN),
        text=[f'{q}%' for q in quality_by_station],
        textposition='outside'
    ))
    fig2.update_layout(
        height=250,
        margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor='white',
        xaxis=dict(range=[90, 100], showgrid=True, gridcolor='lightgray'),
        yaxis=dict(showgrid=False),
        showlegend=False
    )
    st.plotly_chart(fig2, use_container_width=True)

# Cortex Analyst Chat Section
st.markdown(f"<h2 style='color: {ACTIA_GREY}; margin-top: 40px;'>💬 Interrogez vos données avec Cortex Analyst</h2>", unsafe_allow_html=True)

st.markdown(f"""
<div style='background-color: {ACTIA_LIGHT_GREY}; padding: 15px; border-radius: 10px; margin-bottom: 20px;'>
    <p style='color: {ACTIA_GREY}; margin: 0;'>
        💡 <strong>Posez vos questions en langage naturel</strong> - Cortex Analyst analysera vos données de production et vous répondra.
    </p>
</div>
""", unsafe_allow_html=True)

# Predefined questions
st.markdown(f"<p style='color: {ACTIA_GREY};'><strong>Questions suggérées:</strong></p>", unsafe_allow_html=True)
col_q1, col_q2, col_q3 = st.columns(3)

with col_q1:
    if st.button("📊 Quel est le taux de qualité moyen ce mois-ci?"):
        st.session_state.messages.append({
            "role": "user",
            "content": "Quel est le taux de qualité moyen ce mois-ci?"
        })

with col_q2:
    if st.button("🔍 Quels composants ont des problèmes?"):
        st.session_state.messages.append({
            "role": "user",
            "content": "Quels composants ont des problèmes?"
        })

with col_q3:
    if st.button("📈 Quelle est la tendance de production?"):
        st.session_state.messages.append({
            "role": "user",
            "content": "Quelle est la tendance de production?"
        })

# Chat display area
chat_container = st.container()

with chat_container:
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    
    if len(st.session_state.messages) == 0:
        st.markdown(f"""
        <div style='text-align: center; padding: 50px; color: {ACTIA_GREY};'>
            <h3>👋 Bienvenue!</h3>
            <p>Posez-moi des questions sur vos données de production, qualité, ou traçabilité.</p>
        </div>
        """, unsafe_allow_html=True)
    
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class='chat-message user-message'>
                <strong>Vous:</strong><br>{message["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='chat-message assistant-message'>
                <strong>🤖 Cortex Analyst:</strong><br>{message["content"]}
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Chat input
user_question = st.text_input(
    "Votre question:",
    placeholder="Ex: Quelle est la production totale cette semaine?",
    key="user_input",
    label_visibility="collapsed"
)

if user_question:
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })
    
    # Simulate processing
    with st.spinner("🤖 Cortex Analyst analyse vos données..."):
        time.sleep(1.5)
    
    # Generate contextual response based on keywords
    response = get_cortex_response(user_question, factory)
    
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
    
    st.rerun()

# Recent Activity
st.markdown(f"<h2 style='color: {ACTIA_GREY}; margin-top: 40px;'>📋 Activité Récente</h2>", unsafe_allow_html=True)

recent_data = {
    'Heure': ['15:42', '15:38', '15:35', '15:31', '15:28'],
    'Composant': ['TGX-2847-A', 'ECU-2024-456', 'PCB-1123', 'IC-Chip-2024', 'Sensor-T89'],
    'Station': ['Test Final', 'Intégration', 'Assemblage', 'Test Élec.', 'Assemblage'],
    'Statut': ['✅ OK', '✅ OK', '✅ OK', '✅ OK', '✅ OK'],
    'Qualité': ['99%', '98%', '100%', '97%', '99%']
}

df_recent = pd.DataFrame(recent_data)
st.dataframe(df_recent, use_container_width=True, hide_index=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
current_time = datetime.now().strftime("%H:%M:%S")
st.markdown(f"""
<div style='background-color: {ACTIA_LIGHT_GREY}; padding: 15px; border-radius: 10px; text-align: center; margin: 20px 0;'>
    <p style='color: {ACTIA_GREY}; margin: 0;'>🟢 Système actif | Dernière mise à jour: {current_time}</p>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div style='text-align: center; padding: 20px; background-color: {ACTIA_GREY}; 
            border-radius: 10px; color: white;'>
    <p style='margin: 0; font-size: 16px;'>❄️ <strong>Snowflake x Actia</strong></p>
    <p style='margin: 5px 0 0 0; font-size: 14px;'>Powered by Snowflake Cortex Analyst</p>
</div>
""", unsafe_allow_html=True)


"""
GRADIEN INTERACTIVE VISUALIZER - Premium Professional Version
Media Pembelajaran Matematika SMP
Materi: Menentukan Gradien Garis Lurus

Author: Yustika Berlian Cindy Aprillia
Untuk: SMP Negeri 2 Lawang, Kelas VIII-H
"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
from fractions import Fraction
import base64
from io import BytesIO

# ═══════════════════════════════════════════════════════════
#  PAGE CONFIG
# ═══════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Gradien Visualizer — Media Pembelajaran Matematika",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════
#  PREMIUM PROFESSIONAL CSS
# ═══════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap');

/* ══════════════════════════════════════════════
   GLOBAL - Clean & Professional
   ══════════════════════════════════════════════ */
html, body, [class*="css"], .stApp, p, div, span, label, h1, h2, h3 {
    font-family: 'Inter', -apple-system, system-ui, sans-serif !important;
}

#MainMenu, footer, header { visibility: hidden; }

.stApp { 
    background: #F8FAFC;
}

/* ══════════════════════════════════════════════
   HEADER - Minimal & Elegant
   ══════════════════════════════════════════════ */
.app-header {
    background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
    padding: 28px 48px;
    margin: -1rem -1rem 0 -1rem;
    border-bottom: 3px solid #3B82F6;
}
.app-title { 
    color: white;
    font-family: 'Poppins', sans-serif !important;
    font-size: 1.75rem; 
    font-weight: 600; 
    margin: 0;
    letter-spacing: -0.3px;
}
.app-sub { 
    color: #CBD5E1; 
    font-size: 0.95rem; 
    margin: 6px 0 0 0;
    font-weight: 400;
}

/* ══════════════════════════════════════════════
   NAVIGATION TABS - Clean Professional
   ══════════════════════════════════════════════ */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background-color: white;
    padding: 8px;
    border-radius: 12px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.stTabs [data-baseweb="tab"] {
    height: 48px;
    border-radius: 8px;
    padding: 0 24px;
    background-color: transparent;
    border: none;
    color: #64748B;
    font-weight: 500;
}

.stTabs [aria-selected="true"] {
    background-color: #3B82F6 !important;
    color: white !important;
}

/* ══════════════════════════════════════════════
   BUTTONS - Professional & Subtle
   ══════════════════════════════════════════════ */
.stButton > button {
    font-family: 'Inter', sans-serif !important;
    font-weight: 500;
    font-size: 0.95rem;
    padding: 12px 24px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    width: 100%;
    transition: all 0.2s ease;
    color: white !important;
    background: #3B82F6 !important;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}
.stButton > button:hover { 
    background: #2563EB !important;
    box-shadow: 0 4px 6px rgba(59, 130, 246, 0.2);
}

/* Pop-up close button - WIDER */
.stButton button[kind="secondary"],
button:contains("Tutup") {
    min-width: 220px !important;
    background: #F1F5F9 !important;
    color: #475569 !important;
    border: 1px solid #E2E8F0 !important;
}
.stButton button[kind="secondary"]:hover {
    background: #E2E8F0 !important;
}

/* ══════════════════════════════════════════════
   INPUTS - Clean & Minimal
   ══════════════════════════════════════════════ */
.stTextInput > div > div > input {
    font-family: 'Inter', sans-serif !important;
    font-size: 1rem;
    font-weight: 500;
    text-align: center;
    border-radius: 8px;
    border: 1.5px solid #E2E8F0;
    padding: 10px 16px;
    background: white;
    transition: all 0.2s ease;
    color: #1E293B;
}
.stTextInput > div > div > input:focus {
    border-color: #3B82F6;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
    outline: none;
}
.stTextInput > label {
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    color: #475569 !important;
    margin-bottom: 6px !important;
}

/* ══════════════════════════════════════════════
   CARDS - Minimal Elegant
   ══════════════════════════════════════════════ */
.panel-card {
    background: white;
    border-radius: 12px;
    padding: 28px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    border: 1px solid #F1F5F9;
}

.titik-label {
    display: inline-block;
    padding: 6px 16px;
    border-radius: 6px;
    font-weight: 600;
    font-size: 0.875rem;
    color: white;
    margin-bottom: 10px;
}

/* ══════════════════════════════════════════════
   RESULT BOX - Clean Display
   ══════════════════════════════════════════════ */
.result-box {
    background: #F8FAFC;
    border-radius: 10px;
    padding: 24px 20px;
    text-align: center;
    margin-top: 16px;
    border: 1px solid #E2E8F0;
}
.result-label { 
    color: #64748B; 
    font-size: 0.75rem; 
    font-weight: 600; 
    letter-spacing: 1px; 
    text-transform: uppercase; 
}
.result-value { 
    font-size: 2.25rem; 
    font-weight: 700; 
    margin: 8px 0;
    color: #1E293B;
}
.result-desc { 
    color: #64748B; 
    font-size: 0.95rem;
    font-weight: 400;
}

/* ══════════════════════════════════════════════
   MODAL/DIALOG - Professional Pop-up
   ══════════════════════════════════════════════ */
[data-testid="stModal"] {
    background: rgba(15, 23, 42, 0.75) !important;
}

[data-testid="stModal"] > div {
    max-width: 900px !important;
    background: white;
    border-radius: 16px;
    padding: 0;
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
}

/* ══════════════════════════════════════════════
   STEP CARDS - Elegant Minimal
   ══════════════════════════════════════════════ */
.step-wrap {
    background: white;
    border-radius: 10px;
    margin-bottom: 14px;
    overflow: hidden;
    border: 1px solid #E2E8F0;
}
.step-header {
    display: flex;
    align-items: center;
    padding: 14px 20px;
    gap: 12px;
    background: #F8FAFC;
    border-bottom: 1px solid #E2E8F0;
}
.step-badge {
    padding: 4px 12px;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 600;
    color: white;
    white-space: nowrap;
}
.step-title { 
    font-weight: 600; 
    font-size: 0.95rem; 
    color: #1E293B;
}
.step-body { 
    padding: 16px 20px;
    line-height: 1.7;
    color: #334155;
}
.formula-box {
    background: #F8FAFC;
    border: 1.5px solid #E2E8F0;
    border-radius: 8px;
    padding: 12px 20px;
    font-family: 'Monaco', 'Courier New', monospace;
    font-size: 1rem;
    font-weight: 500;
    margin: 10px 0;
    display: inline-block;
    color: #1E293B;
}
.keterangan { 
    color: #64748B; 
    font-style: italic; 
    font-size: 0.875rem; 
    margin: 6px 0 2px 20px;
    font-weight: 400;
}
.bullet-line { 
    margin: 6px 0 6px 6px;
    font-weight: 400;
    color: #475569;
}

/* ══════════════════════════════════════════════
   CONCLUSION - Subtle Success
   ══════════════════════════════════════════════ */
.conclusion-box {
    background: #F0FDF4;
    border: 1.5px solid #BBF7D0;
    border-radius: 10px;
    padding: 20px 24px;
    margin-top: 16px;
}
.conc-label { 
    color: #15803D; 
    font-weight: 600; 
    font-size: 0.8rem; 
    letter-spacing: 0.5px;
    text-transform: uppercase;
}
.conc-summary { 
    font-size: 1.25rem; 
    font-weight: 600; 
    color: #166534; 
    margin: 10px 0 6px 0;
}
.conc-desc { 
    color: #15803D;
    font-weight: 400;
    font-size: 0.95rem;
}

/* ══════════════════════════════════════════════
   SCORE - Minimal Clean
   ══════════════════════════════════════════════ */
.score-box {
    background: #1E293B;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    color: white;
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 16px;
}

/* ══════════════════════════════════════════════
   DRILL QUESTION
   ══════════════════════════════════════════════ */
.drill-q-card {
    background: #F8FAFC;
    border-radius: 10px;
    padding: 20px 24px;
    margin-bottom: 16px;
    line-height: 1.7;
    border: 1px solid #E2E8F0;
}
.drill-q-num { 
    color: #3B82F6; 
    font-weight: 600; 
    font-size: 0.8rem; 
    letter-spacing: 0.5px; 
    margin-bottom: 8px;
    text-transform: uppercase;
}

/* ══════════════════════════════════════════════
   FEEDBACK - Subtle & Clean
   ══════════════════════════════════════════════ */
.fb-correct {
    background: #F0FDF4;
    border: 1.5px solid #BBF7D0;
    border-radius: 8px;
    padding: 16px 20px;
    color: #15803D;
    font-weight: 500;
    text-align: center;
    font-size: 1rem;
}
.fb-wrong {
    background: #FEF2F2;
    border: 1.5px solid #FECACA;
    border-radius: 8px;
    padding: 16px 20px;
    color: #991B1B;
    font-weight: 500;
    text-align: center;
    font-size: 1rem;
}
.fb-hint {
    background: #FFFBEB;
    border: 1.5px solid #FDE68A;
    border-radius: 8px;
    padding: 16px 20px;
    color: #92400E;
    font-weight: 400;
    line-height: 1.7;
}

/* ══════════════════════════════════════════════
   REVIEW SECTION - Professional
   ══════════════════════════════════════════════ */
.review-banner {
    background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
    border-radius: 12px;
    padding: 24px 32px;
    margin-bottom: 28px;
    color: white;
    font-size: 1.5rem;
    font-weight: 600;
    border-left: 4px solid #3B82F6;
}
.sec-card { 
    background: white;
    border-radius: 12px; 
    padding: 28px 32px; 
    margin-bottom: 24px; 
    line-height: 1.7;
    border: 1px solid #E2E8F0;
}
.sec-card-green  { 
    border-left: 3px solid #10B981;
}
.sec-card-orange { 
    border-left: 3px solid #F59E0B;
}
.sec-card-purple { 
    border-left: 3px solid #8B5CF6;
}

.sec-num-title {
    display: flex; 
    align-items: center; 
    gap: 14px;
    margin-bottom: 18px; 
    padding-bottom: 14px;
    border-bottom: 1px solid #E2E8F0;
}
.sec-num { 
    font-size: 1.5rem;
    font-weight: 600;
    color: #1E293B;
}
.sec-title { 
    font-size: 1.15rem; 
    font-weight: 600;
    color: #1E293B;
}
.sec-subtitle { 
    font-weight: 600; 
    font-size: 0.95rem; 
    color: #1E293B; 
    margin: 16px 0 8px 0; 
    letter-spacing: 0.3px;
}
.sec-divider { 
    border: none; 
    border-top: 1px solid #E2E8F0; 
    margin: 18px 0;
}
.contoh-label { 
    font-weight: 600; 
    font-size: 1rem; 
    margin: 16px 0 8px 0;
    color: #334155;
}
.kesimpulan-box { 
    background: #F8FAFC;
    border-radius: 8px; 
    padding: 12px 18px; 
    margin-top: 12px; 
    font-size: 0.95rem;
    font-weight: 400;
    border-left: 3px solid #3B82F6;
    color: #475569;
}
.info-banner { 
    background: #1E293B;
    color: white; 
    border-radius: 10px; 
    padding: 20px 28px; 
    font-weight: 400; 
    margin-top: 12px; 
    line-height: 1.7;
}

/* ══════════════════════════════════════════════
   GRAPH IN MODAL - Professional Display
   ══════════════════════════════════════════════ */
.graph-in-modal {
    background: white;
    border-radius: 10px;
    padding: 20px;
    margin: 16px 0;
    border: 1px solid #E2E8F0;
}
.graph-title-modal {
    font-size: 1rem;
    font-weight: 600;
    color: #1E293B;
    margin-bottom: 12px;
}

/* ══════════════════════════════════════════════
   TYPOGRAPHY - Clean & Readable
   ══════════════════════════════════════════════ */
h1, h2, h3 { 
    color: #1E293B !important;
    font-weight: 600 !important;
}
p { 
    color: #475569 !important; 
    line-height: 1.7 !important;
}
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
#  HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════
def fraction_str(numerator, denominator):
    if denominator == 0:
        return "tak terdefinisi"
    f = Fraction(int(round(numerator)), int(round(denominator)))
    return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"

def format_num(v):
    return str(int(v)) if v == int(v) else f"{v:.1f}"

def fig_to_base64(fig):
    """Convert matplotlib figure to base64 for embedding"""
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=120, bbox_inches='tight', facecolor='white')
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode()
    buf.close()
    return img_str


# ═══════════════════════════════════════════════════════════
#  HEADER
# ═══════════════════════════════════════════════════════════
st.markdown("""
<div class="app-header">
    <div class="app-title">Gradien Visualizer</div>
    <div class="app-sub">Media Pembelajaran Interaktif — Matematika SMP Kelas VIII</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
#  SESSION STATE INIT
# ═══════════════════════════════════════════════════════════
if 'drill_score' not in st.session_state:
    st.session_state.drill_score = 0
if 'drill_total' not in st.session_state:
    st.session_state.drill_total = 0
if 'drill_x1' not in st.session_state:
    st.session_state.drill_x1 = None
if 'current_graph' not in st.session_state:
    st.session_state.current_graph = None


# ═══════════════════════════════════════════════════════════
#  TABS
# ═══════════════════════════════════════════════════════════
tab1, tab2, tab3 = st.tabs(["Mode Visualizer", "Mode Drill Practice", "Review Materi"])


# ═══════════════════════════════════════════════════════════
#  TAB 1: VISUALIZER
# ═══════════════════════════════════════════════════════════
with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_left, col_right = st.columns([1, 1], gap="large")
    
    with col_left:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True)
        st.markdown("### Input Koordinat")
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Titik 1
        st.markdown('<span class="titik-label" style="background:#EC4899">Titik 1</span>', unsafe_allow_html=True)
        col1a, col1b = st.columns(2)
        with col1a:
            x1 = st.text_input("x₁", key="x1", label_visibility="visible")
        with col1b:
            y1 = st.text_input("y₁", key="y1", label_visibility="visible")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Titik 2
        st.markdown('<span class="titik-label" style="background:#06B6D4">Titik 2</span>', unsafe_allow_html=True)
        col2a, col2b = st.columns(2)
        with col2a:
            x2 = st.text_input("x₂", key="x2", label_visibility="visible")
        with col2b:
            y2 = st.text_input("y₂", key="y2", label_visibility="visible")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("Hitung Gradien", use_container_width=True):
            try:
                x1_val = float(x1)
                y1_val = float(y1)
                x2_val = float(x2)
                y2_val = float(y2)
                
                # Calculate gradient
                if x2_val - x1_val == 0:
                    m_value = None
                    m_display = "tak terdefinisi"
                    desc = "Garis Vertikal"
                    color = "#64748B"
                else:
                    m_value = (y2_val - y1_val) / (x2_val - x1_val)
                    m_display = fraction_str(y2_val - y1_val, x2_val - x1_val)
                    
                    if m_value > 0:
                        desc = "Garis Naik (Positif)"
                        color = "#10B981"
                    elif m_value < 0:
                        desc = "Garis Turun (Negatif)"
                        color = "#EF4444"
                    else:
                        desc = "Garis Horizontal"
                        color = "#3B82F6"
                
                # Display result
                st.markdown(f"""
                <div class="result-box">
                    <div class="result-label">Gradien (m)</div>
                    <div class="result-value" style="color:{color}">{m_display}</div>
                    <div class="result-desc">{desc}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Store for modal
                st.session_state.last_calc = {
                    'x1': x1_val, 'y1': y1_val, 
                    'x2': x2_val, 'y2': y2_val,
                    'm': m_value, 'm_display': m_display
                }
                
            except ValueError:
                st.error("Mohon masukkan angka yang valid")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col_right:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True)
        st.markdown("### Visualisasi Grafik")
        
        if 'last_calc' in st.session_state:
            calc = st.session_state.last_calc
            fig, ax = plt.subplots(figsize=(7, 6), facecolor='white')
            
            # Setup axes
            ax.axhline(y=0, color='#94A3B8', linewidth=1.2)
            ax.axvline(x=0, color='#94A3B8', linewidth=1.2)
            ax.grid(True, alpha=0.2, linestyle='-', linewidth=0.5, color='#CBD5E1')
            
            # Determine color
            if calc['m'] is None:
                line_color = '#64748B'
            elif calc['m'] > 0:
                line_color = '#10B981'
            elif calc['m'] < 0:
                line_color = '#EF4444'
            else:
                line_color = '#3B82F6'
            
            # Plot line
            ax.plot([calc['x1'], calc['x2']], [calc['y1'], calc['y2']], 
                   color=line_color, linewidth=3, marker='o', markersize=10,
                   markeredgecolor='white', markeredgewidth=2)
            
            # Annotate
            ax.annotate(f"({format_num(calc['x1'])}, {format_num(calc['y1'])})", 
                       xy=(calc['x1'], calc['y1']), xytext=(calc['x1']+0.5, calc['y1']+0.5),
                       fontsize=10, fontweight='bold', color='#1E293B',
                       bbox=dict(boxstyle='round,pad=0.4', facecolor='white', 
                                edgecolor=line_color, linewidth=1.5))
            ax.annotate(f"({format_num(calc['x2'])}, {format_num(calc['y2'])})", 
                       xy=(calc['x2'], calc['y2']), xytext=(calc['x2']+0.5, calc['y2']+0.5),
                       fontsize=10, fontweight='bold', color='#1E293B',
                       bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                                edgecolor=line_color, linewidth=1.5))
            
            # Set limits
            x_range = max(abs(calc['x1']), abs(calc['x2']), 5) + 2
            y_range = max(abs(calc['y1']), abs(calc['y2']), 5) + 2
            ax.set_xlim(-x_range, x_range)
            ax.set_ylim(-y_range, y_range)
            
            ax.set_xlabel('x', fontsize=11, fontweight='600', color='#475569')
            ax.set_ylabel('y', fontsize=11, fontweight='600', color='#475569')
            ax.set_facecolor('#F8FAFC')
            
            # Store figure for modal
            st.session_state.current_graph = fig
            
            st.pyplot(fig)
            plt.close()
        else:
            st.info("Masukkan koordinat dan klik 'Hitung Gradien' untuk melihat grafik")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Button to show steps in MODAL
    if 'last_calc' in st.session_state:
        if st.button("Tampilkan Langkah Penyelesaian", use_container_width=True, type="secondary"):
            show_steps_modal()


# ═══════════════════════════════════════════════════════════
#  MODAL FOR STEPS
# ═══════════════════════════════════════════════════════════
@st.dialog("Langkah-Langkah Penyelesaian", width="large")
def show_steps_modal():
    if 'last_calc' not in st.session_state:
        st.warning("Belum ada perhitungan")
        return
    
    calc = st.session_state.last_calc
    x1, y1, x2, y2 = calc['x1'], calc['y1'], calc['x2'], calc['y2']
    
    # Show graph in modal too!
    if st.session_state.current_graph:
        st.markdown('<div class="graph-in-modal">', unsafe_allow_html=True)
        st.markdown('<div class="graph-title-modal">Visualisasi Grafik</div>', unsafe_allow_html=True)
        st.pyplot(st.session_state.current_graph)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Generate steps
    steps_html = build_steps_html(x1, y1, x2, y2)
    st.markdown(steps_html, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Conclusion
    conclusion_html = build_conclusion_html(x1, y1, x2, y2)
    st.markdown(conclusion_html, unsafe_allow_html=True)


def build_steps_html(x1, y1, x2, y2):
    """Build step-by-step solution HTML"""
    x1_s = format_num(x1)
    y1_s = format_num(y1)
    x2_s = format_num(x2)
    y2_s = format_num(y2)
    
    steps = []
    
    if x1 == 0 and y1 == 0:
        # Through origin
        steps.append({
            'num': 1,
            'title': 'Identifikasi Koordinat',
            'content': f'Titik pertama: O(0, 0)<br>Titik kedua: ({x2_s}, {y2_s})',
            'color': '#0EA5E9'
        })
        steps.append({
            'num': 2,
            'title': 'Pilih Rumus',
            'content': f'Karena garis melalui titik pusat O(0,0):<br><div class="formula-box">m = y/x</div>',
            'color': '#8B5CF6'
        })
        steps.append({
            'num': 3,
            'title': 'Substitusi Nilai',
            'content': f'<div class="formula-box">m = {y2_s}/{x2_s}</div>',
            'color': '#F59E0B'
        })
        
        if x2 != 0:
            m = y2 / x2
            m_display = fraction_str(y2, x2)
            steps.append({
                'num': 4,
                'title': 'Hasil Perhitungan',
                'content': f'<div class="formula-box">m = {m_display}</div>',
                'color': '#10B981'
            })
    else:
        # General case
        steps.append({
            'num': 1,
            'title': 'Identifikasi Koordinat',
            'content': f'Titik 1: ({x1_s}, {y1_s}) → x₁ = {x1_s}, y₁ = {y1_s}<br>Titik 2: ({x2_s}, {y2_s}) → x₂ = {x2_s}, y₂ = {y2_s}',
            'color': '#0EA5E9'
        })
        steps.append({
            'num': 2,
            'title': 'Pilih Rumus',
            'content': 'Gunakan rumus gradien untuk dua titik:<br><div class="formula-box">m = (y₂ - y₁) / (x₂ - x₁)</div>',
            'color': '#8B5CF6'
        })
        steps.append({
            'num': 3,
            'title': 'Substitusi Nilai',
            'content': f'<div class="formula-box">m = ({y2_s} - {y1_s}) / ({x2_s} - {x1_s})</div>',
            'color': '#F59E0B'
        })
        
        dy = y2 - y1
        dx = x2 - x1
        dy_s = format_num(dy)
        dx_s = format_num(dx)
        
        steps.append({
            'num': 4,
            'title': 'Hitung Pembilang dan Penyebut',
            'content': f'<div class="formula-box">m = {dy_s} / {dx_s}</div>',
            'color': '#EC4899'
        })
        
        if dx != 0:
            m = dy / dx
            m_display = fraction_str(dy, dx)
            steps.append({
                'num': 5,
                'title': 'Hasil Perhitungan',
                'content': f'<div class="formula-box">m = {m_display}</div>',
                'color': '#10B981'
            })
    
    # Build HTML
    html = ""
    for step in steps:
        html += f"""
        <div class="step-wrap">
            <div class="step-header">
                <span class="step-badge" style="background:{step['color']}">Langkah {step['num']}</span>
                <span class="step-title">{step['title']}</span>
            </div>
            <div class="step-body">{step['content']}</div>
        </div>
        """
    
    return html


def build_conclusion_html(x1, y1, x2, y2):
    """Build conclusion HTML"""
    if x2 - x1 == 0:
        return """
        <div class="conclusion-box">
            <div class="conc-label">KESIMPULAN</div>
            <div class="conc-summary">Gradien tidak terdefinisi</div>
            <div class="conc-desc">Garis vertikal (sejajar sumbu y)</div>
        </div>
        """
    
    m = (y2 - y1) / (x2 - x1)
    m_display = fraction_str(y2 - y1, x2 - x1)
    
    if m > 0:
        desc = "Garis naik dari kiri ke kanan (gradien positif)"
    elif m < 0:
        desc = "Garis turun dari kiri ke kanan (gradien negatif)"
    else:
        desc = "Garis horizontal (sejajar sumbu x)"
    
    return f"""
    <div class="conclusion-box">
        <div class="conc-label">KESIMPULAN</div>
        <div class="conc-summary">Gradien = {m_display}</div>
        <div class="conc-desc">{desc}</div>
    </div>
    """


# ═══════════════════════════════════════════════════════════
#  TAB 2: DRILL PRACTICE
# ═══════════════════════════════════════════════════════════
with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown(f'<div class="score-box">Skor: {st.session_state.drill_score}/{st.session_state.drill_total}</div>', unsafe_allow_html=True)
    
    col_graph, col_input = st.columns([1, 1], gap="large")
    
    with col_graph:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True)
        st.markdown("### Grafik Soal")
        
        if st.session_state.drill_x1 is not None:
            fig, ax = plt.subplots(figsize=(6, 5), facecolor='white')
            
            ax.axhline(y=0, color='#94A3B8', linewidth=1.2)
            ax.axvline(x=0, color='#94A3B8', linewidth=1.2)
            ax.grid(True, alpha=0.2, linestyle='-', linewidth=0.5, color='#CBD5E1')
            
            x1_d = st.session_state.drill_x1
            y1_d = st.session_state.drill_y1
            x2_d = st.session_state.drill_x2
            y2_d = st.session_state.drill_y2
            
            m_drill = (y2_d - y1_d) / (x2_d - x1_d)
            
            if m_drill > 0:
                color = '#10B981'
            elif m_drill < 0:
                color = '#EF4444'
            else:
                color = '#3B82F6'
            
            ax.plot([x1_d, x2_d], [y1_d, y2_d], 
                   color=color, linewidth=4, marker='o', markersize=12,
                   markeredgecolor='white', markeredgewidth=2)
            
            x_range = max(abs(x1_d), abs(x2_d), 5) + 2
            y_range = max(abs(y1_d), abs(y2_d), 5) + 2
            ax.set_xlim(-x_range, x_range)
            ax.set_ylim(-y_range, y_range)
            
            ax.set_xlabel('x', fontsize=11, fontweight='600', color='#475569')
            ax.set_ylabel('y', fontsize=11, fontweight='600', color='#475569')
            ax.set_facecolor('#F8FAFC')
            
            st.pyplot(fig)
            plt.close()
        else:
            st.info("Klik 'Generate Soal Baru' untuk memulai")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col_input:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True)
        
        if st.session_state.drill_x1 is not None:
            st.markdown(f'<div class="drill-q-card"><div class="drill-q-num">SOAL {st.session_state.drill_total + 1}</div>Perhatikan grafik di samping. Tentukan gradien garis tersebut!</div>', unsafe_allow_html=True)
        
        user_answer = st.text_input("Jawaban Anda (m)", key="drill_input")
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("Generate Soal Baru", use_container_width=True):
                # Generate new question
                if random.random() < 0.3:
                    x1_new, y1_new = 0, 0
                    x2_new = random.randint(-8, 8)
                    while x2_new == 0:
                        x2_new = random.randint(-8, 8)
                    y2_new = random.randint(-8, 8)
                else:
                    x1_new = random.randint(-8, 8)
                    y1_new = random.randint(-8, 8)
                    x2_new = random.randint(-8, 8)
                    while x2_new == x1_new:
                        x2_new = random.randint(-8, 8)
                    y2_new = random.randint(-8, 8)
                
                st.session_state.drill_x1 = x1_new
                st.session_state.drill_y1 = y1_new
                st.session_state.drill_x2 = x2_new
                st.session_state.drill_y2 = y2_new
                st.rerun()
        
        with col_btn2:
            if st.button("Cek Jawaban", use_container_width=True, type="primary"):
                if st.session_state.drill_x1 is None:
                    st.warning("Generate soal terlebih dahulu")
                else:
                    try:
                        user_val = float(user_answer)
                        correct_m = (st.session_state.drill_y2 - st.session_state.drill_y1) / (st.session_state.drill_x2 - st.session_state.drill_x1)
                        correct_display = fraction_str(st.session_state.drill_y2 - st.session_state.drill_y1, st.session_state.drill_x2 - st.session_state.drill_x1)
                        
                        st.session_state.drill_total += 1
                        
                        if abs(user_val - correct_m) < 0.01:
                            st.session_state.drill_score += 1
                            st.markdown(f'<div class="fb-correct">Benar! Gradien = {correct_display}</div>', unsafe_allow_html=True)
                        else:
                            st.markdown(f'<div class="fb-wrong">Belum tepat. Jawaban yang benar: m = {correct_display}</div>', unsafe_allow_html=True)
                        
                        st.rerun()
                    except ValueError:
                        st.error("Mohon masukkan angka yang valid")
        
        if st.button("Tampilkan Koordinat (Hint)", use_container_width=True):
            if st.session_state.drill_x1 is not None:
                st.markdown(f'<div class="fb-hint">Titik 1: ({format_num(st.session_state.drill_x1)}, {format_num(st.session_state.drill_y1)})<br>Titik 2: ({format_num(st.session_state.drill_x2)}, {format_num(st.session_state.drill_y2)})</div>', unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
#  TAB 3: REVIEW MATERI
# ═══════════════════════════════════════════════════════════
with tab3:
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown('<div class="review-banner">Review Materi — Gradien Garis Lurus</div>', unsafe_allow_html=True)
    
    # Section 1
    st.markdown("""
    <div class="sec-card sec-card-green">
        <div class="sec-num-title">
            <span class="sec-num">1</span>
            <span class="sec-title">GRADIEN MELALUI TITIK PUSAT</span>
        </div>
        
        <div class="sec-subtitle">Rumus</div>
        <div class="formula-box">m = y/x</div>
        <div class="keterangan">dengan syarat x ≠ 0</div>
        
        <div class="sec-subtitle">Catatan Penting</div>
        <div class="bullet-line">• Jika x = 0 (garis vertikal) maka gradien tidak terdefinisi</div>
        <div class="bullet-line">• Jika y = 0 (garis horizontal) maka gradien m = 0</div>
        
        <hr class="sec-divider">
        
        <div class="contoh-label">Contoh 1: Gradien Positif</div>
        <p>Tentukan gradien persamaan garis lurus yang melalui titik pusat koordinat dan titik (4,8)!</p>
        <p><strong>Penyelesaian:</strong></p>
        <p>Persamaan garis lurus melalui titik (0,0) dan (4,8), sehingga gradiennya adalah:</p>
        <div class="formula-box">m = y/x = 8/4 = 2</div>
        <div class="kesimpulan-box">Kesimpulan: Didapatkan gradien positif (m = 2), artinya garis naik dari kiri ke kanan.</div>
        
        <hr class="sec-divider">
        
        <div class="contoh-label">Contoh 2: Gradien Negatif</div>
        <p>Tentukan gradien persamaan garis lurus yang melalui titik pusat koordinat dan titik (6,-3)!</p>
        <p><strong>Penyelesaian:</strong></p>
        <p>Persamaan garis lurus melalui titik (0,0) dan (6,-3), sehingga gradiennya adalah:</p>
        <div class="formula-box">m = y/x = -3/6 = -1/2</div>
        <div class="kesimpulan-box">Kesimpulan: Didapatkan gradien negatif (m = -1/2), artinya garis turun dari kiri ke kanan.</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Section 2
    st.markdown("""
    <div class="sec-card sec-card-orange">
        <div class="sec-num-title">
            <span class="sec-num">2</span>
            <span class="sec-title">GRADIEN MELALUI DUA TITIK</span>
        </div>
        
        <div class="sec-subtitle">Rumus</div>
        <div class="formula-box">m = (y₂ - y₁) / (x₂ - x₁)</div>
        <div class="keterangan">dengan syarat x₁ ≠ x₂</div>
        
        <div class="sec-subtitle">Catatan Penting</div>
        <div class="bullet-line">• Jika x₁ = x₂ (garis vertikal) maka gradien tidak terdefinisi</div>
        
        <hr class="sec-divider">
        
        <div class="contoh-label">Contoh 1: Gradien Tidak Terdefinisi</div>
        <p>Tentukan gradien garis yang melalui P(3,1) dan Q(3,5)!</p>
        <p><strong>Penyelesaian:</strong></p>
        <p>Titik P(3,1) → x₁ = 3 dan y₁ = 1<br>Titik Q(3,5) → x₂ = 3 dan y₂ = 5</p>
        <p>Gradien garis PQ sebagai berikut:</p>
        <div class="formula-box">m = (5 - 1) / (3 - 3) = 4/0</div>
        <div class="kesimpulan-box">Kesimpulan: Diperoleh x₁ dan x₂ = 0. Karena penyebut = 0, maka gradien tidak terdefinisi dan berupa garis vertikal.</div>
        
        <hr class="sec-divider">
        
        <div class="contoh-label">Contoh 2: Gradien Negatif</div>
        <p>Tentukan gradien garis yang melalui P(1,4) dan Q(5,2)!</p>
        <p><strong>Penyelesaian:</strong></p>
        <p>Titik P(1,4) → x₁ = 1 dan y₁ = 4<br>Titik Q(5,2) → x₂ = 5 dan y₂ = 2</p>
        <p>Gradien garis PQ sebagai berikut:</p>
        <div class="formula-box">m = (2 - 4) / (5 - 1) = -2/4 = -1/2</div>
        <div class="kesimpulan-box">Kesimpulan: Jadi, gradien garis PQ adalah -1/2. Didapatkan gradien negatif, artinya garis turun dari kiri ke kanan.</div>
        
        <hr class="sec-divider">
        
        <div class="contoh-label">Contoh 3: Gradien Nol</div>
        <p>Tentukan gradien garis yang melalui P(2,3) dan Q(7,3)!</p>
        <p><strong>Penyelesaian:</strong></p>
        <p>Titik P(2,3) → x₁ = 2 dan y₁ = 3<br>Titik Q(7,3) → x₂ = 7 dan y₂ = 3</p>
        <p>Gradien garis PQ sebagai berikut:</p>
        <div class="formula-box">m = (3 - 3) / (7 - 2) = 0/5 = 0</div>
        <div class="kesimpulan-box">Kesimpulan: Jado, gradien garis PQ adalah 0. Didapatkan gradien 0 dan berupa garis horizontal.</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Section 3
    st.markdown("""
    <div class="sec-card sec-card-purple">
        <div class="sec-num-title">
            <span class="sec-num">3</span>
            <span class="sec-title">INTERPRETASI GRADIEN</span>
        </div>
        
        <div class="sec-subtitle">Berdasarkan Nilai m</div>
        <div class="bullet-line"><strong>m > 0</strong> → Garis naik dari kiri ke kanan (gradien positif)<br><span class="keterangan">Contoh: m = 2, m = 1/2, m = 5</span></div>
        
        <div class="bullet-line"><strong>m < 0</strong> → Garis turun dari kiri ke kanan (gradien negatif)<br><span class="keterangan">Contoh: m = -2, m = -1/2, m = -5</span></div>
        
        <div class="bullet-line"><strong>m = 0</strong> → Garis horizontal (sejajar sumbu x)<br><span class="keterangan">Contoh: garis y = 3, y = -2</span></div>
        
        <div class="bullet-line"><strong>m tidak terdefinisi</strong> → Garis vertikal (sejajar sumbu y)<br><span class="keterangan">Contoh: garis x = 2, x = -5</span></div>
        
        <hr class="sec-divider">
        
        <div class="sec-subtitle">Tips Penting</div>
        <div class="bullet-line">1. Semakin besar nilai |m|, semakin curam garisnya</div>
        <div class="bullet-line">2. Dua garis sejajar memiliki gradien yang sama</div>
        <div class="bullet-line">3. Dua garis tegak lurus: m₁ × m₂ = -1</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="info-banner">Gunakan Mode Visualizer untuk melihat grafik dan perhitungan langkah demi langkah. Gunakan Mode Drill Practice untuk berlatih mengerjakan soal.</div>', unsafe_allow_html=True)

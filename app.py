"""
GRADIEN INTERACTIVE VISUALIZER - Fixed Premium Version
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

# ═══════════════════════════════════════════════════════════
#  PAGE CONFIG
# ═══════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Gradien Visualizer",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════
#  CSS - PREMIUM PROFESSIONAL
# ═══════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"], .stApp, p, div, span, label, h1, h2, h3 {
    font-family: 'Inter', sans-serif !important;
}

#MainMenu, footer, header { visibility: hidden; }

.stApp { background: #F8FAFC; }

/* Header */
.app-header {
    background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
    padding: 28px 48px;
    margin: -1rem -1rem 0 -1rem;
    border-bottom: 3px solid #3B82F6;
}
.app-title { 
    color: white;
    font-size: 1.75rem; 
    font-weight: 600; 
    margin: 0;
}
.app-sub { 
    color: #CBD5E1; 
    font-size: 0.95rem; 
    margin: 6px 0 0 0;
}

/* Buttons */
.stButton > button {
    font-weight: 500;
    font-size: 0.95rem;
    padding: 12px 24px;
    border-radius: 8px;
    border: none;
    transition: all 0.2s ease;
    color: white !important;
    background: #3B82F6 !important;
}
.stButton > button:hover { 
    background: #2563EB !important;
}

/* Inputs */
.stTextInput > div > div > input {
    font-size: 1rem;
    font-weight: 500;
    text-align: center;
    border-radius: 8px;
    border: 1.5px solid #E2E8F0;
    padding: 10px 16px;
    color: #1E293B;
}
.stTextInput > div > div > input:focus {
    border-color: #3B82F6;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

/* Cards */
.panel-card {
    background: white;
    border-radius: 12px;
    padding: 28px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    border: 1px solid #F1F5F9;
}

/* Result */
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

/* Modal Dialog */
[data-testid="stModal"] {
    background: rgba(15, 23, 42, 0.75) !important;
}

/* Steps */
.step-wrap {
    background: white;
    border-radius: 10px;
    margin-bottom: 14px;
    border: 1px solid #E2E8F0;
}
.step-header {
    padding: 14px 20px;
    background: #F8FAFC;
    border-bottom: 1px solid #E2E8F0;
}
.step-body { 
    padding: 16px 20px;
    color: #334155;
}
.formula-box {
    background: #F8FAFC;
    border: 1.5px solid #E2E8F0;
    border-radius: 8px;
    padding: 12px 20px;
    font-family: 'Monaco', monospace;
    font-size: 1rem;
    margin: 10px 0;
    display: inline-block;
}

/* Conclusion */
.conclusion-box {
    background: #F0FDF4;
    border: 1.5px solid #BBF7D0;
    border-radius: 10px;
    padding: 20px 24px;
    margin-top: 16px;
}
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
#  HELPER FUNCTIONS - DEFINE FIRST!
# ═══════════════════════════════════════════════════════════
def fraction_str(numerator, denominator):
    if denominator == 0:
        return "tak terdefinisi"
    f = Fraction(int(round(numerator)), int(round(denominator)))
    return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"

def format_num(v):
    return str(int(v)) if v == int(v) else f"{v:.1f}"


# ═══════════════════════════════════════════════════════════
#  MODAL FUNCTIONS - DEFINE BEFORE USE!
# ═══════════════════════════════════════════════════════════
@st.dialog("Langkah-Langkah Penyelesaian", width="large")
def show_steps_modal():
    """Pop-up untuk menampilkan langkah penyelesaian + grafik"""
    
    if 'last_calc' not in st.session_state:
        st.warning("Belum ada perhitungan. Silakan hitung gradien terlebih dahulu.")
        return
    
    calc = st.session_state.last_calc
    x1, y1, x2, y2 = calc['x1'], calc['y1'], calc['x2'], calc['y2']
    
    # ═══ GRAFIK DI MODAL ═══
    st.markdown("### Visualisasi Grafik")
    
    fig, ax = plt.subplots(figsize=(8, 6), facecolor='white')
    
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
    
    # Plot
    ax.plot([x1, x2], [y1, y2], 
           color=line_color, linewidth=3, marker='o', markersize=10,
           markeredgecolor='white', markeredgewidth=2)
    
    # Annotate
    ax.annotate(f"({format_num(x1)}, {format_num(y1)})", 
               xy=(x1, y1), xytext=(x1+0.5, y1+0.5),
               fontsize=10, fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.4', facecolor='white', 
                        edgecolor=line_color, linewidth=1.5))
    ax.annotate(f"({format_num(x2)}, {format_num(y2)})", 
               xy=(x2, y2), xytext=(x2+0.5, y2+0.5),
               fontsize=10, fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                        edgecolor=line_color, linewidth=1.5))
    
    x_range = max(abs(x1), abs(x2), 5) + 2
    y_range = max(abs(y1), abs(y2), 5) + 2
    ax.set_xlim(-x_range, x_range)
    ax.set_ylim(-y_range, y_range)
    
    ax.set_xlabel('x', fontsize=11, fontweight='600')
    ax.set_ylabel('y', fontsize=11, fontweight='600')
    ax.set_facecolor('#F8FAFC')
    
    st.pyplot(fig)
    plt.close()
    
    st.markdown("---")
    
    # ═══ LANGKAH-LANGKAH ═══
    st.markdown("### Langkah-Langkah Penyelesaian")
    
    x1_s = format_num(x1)
    y1_s = format_num(y1)
    x2_s = format_num(x2)
    y2_s = format_num(y2)
    
    if x1 == 0 and y1 == 0:
        # Through origin
        st.markdown(f"""
        <div class="step-wrap">
            <div class="step-header"><b>Langkah 1: Identifikasi Koordinat</b></div>
            <div class="step-body">
                Titik pertama: O(0, 0)<br>
                Titik kedua: ({x2_s}, {y2_s})
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="step-wrap">
            <div class="step-header"><b>Langkah 2: Pilih Rumus</b></div>
            <div class="step-body">
                Karena garis melalui titik pusat O(0,0):<br>
                <div class="formula-box">m = y/x</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="step-wrap">
            <div class="step-header"><b>Langkah 3: Substitusi Nilai</b></div>
            <div class="step-body">
                <div class="formula-box">m = {y2_s}/{x2_s}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if x2 != 0:
            m = y2 / x2
            m_display = fraction_str(y2, x2)
            st.markdown(f"""
            <div class="step-wrap">
                <div class="step-header"><b>Langkah 4: Hasil Perhitungan</b></div>
                <div class="step-body">
                    <div class="formula-box">m = {m_display}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        # General case
        st.markdown(f"""
        <div class="step-wrap">
            <div class="step-header"><b>Langkah 1: Identifikasi Koordinat</b></div>
            <div class="step-body">
                Titik 1: ({x1_s}, {y1_s}) → x₁ = {x1_s}, y₁ = {y1_s}<br>
                Titik 2: ({x2_s}, {y2_s}) → x₂ = {x2_s}, y₂ = {y2_s}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="step-wrap">
            <div class="step-header"><b>Langkah 2: Pilih Rumus</b></div>
            <div class="step-body">
                Gunakan rumus gradien untuk dua titik:<br>
                <div class="formula-box">m = (y₂ - y₁) / (x₂ - x₁)</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="step-wrap">
            <div class="step-header"><b>Langkah 3: Substitusi Nilai</b></div>
            <div class="step-body">
                <div class="formula-box">m = ({y2_s} - {y1_s}) / ({x2_s} - {x1_s})</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        dy = y2 - y1
        dx = x2 - x1
        dy_s = format_num(dy)
        dx_s = format_num(dx)
        
        st.markdown(f"""
        <div class="step-wrap">
            <div class="step-header"><b>Langkah 4: Hitung</b></div>
            <div class="step-body">
                <div class="formula-box">m = {dy_s} / {dx_s}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if dx != 0:
            m = dy / dx
            m_display = fraction_str(dy, dx)
            st.markdown(f"""
            <div class="step-wrap">
                <div class="step-header"><b>Langkah 5: Hasil</b></div>
                <div class="step-body">
                    <div class="formula-box">m = {m_display}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # ═══ KESIMPULAN ═══
    if x2 - x1 == 0:
        st.markdown("""
        <div class="conclusion-box">
            <b>KESIMPULAN</b><br>
            <div style="font-size:1.25rem; font-weight:600; margin:10px 0;">
                Gradien tidak terdefinisi
            </div>
            Garis vertikal (sejajar sumbu y)
        </div>
        """, unsafe_allow_html=True)
    else:
        m = (y2 - y1) / (x2 - x1)
        m_display = fraction_str(y2 - y1, x2 - x1)
        
        if m > 0:
            desc = "Garis naik dari kiri ke kanan (gradien positif)"
        elif m < 0:
            desc = "Garis turun dari kiri ke kanan (gradien negatif)"
        else:
            desc = "Garis horizontal (sejajar sumbu x)"
        
        st.markdown(f"""
        <div class="conclusion-box">
            <b>KESIMPULAN</b><br>
            <div style="font-size:1.25rem; font-weight:600; margin:10px 0;">
                Gradien = {m_display}
            </div>
            {desc}
        </div>
        """, unsafe_allow_html=True)


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
#  SESSION STATE
# ═══════════════════════════════════════════════════════════
if 'drill_score' not in st.session_state:
    st.session_state.drill_score = 0
if 'drill_total' not in st.session_state:
    st.session_state.drill_total = 0
if 'drill_x1' not in st.session_state:
    st.session_state.drill_x1 = None


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
        
        # Titik 1
        st.markdown('<div style="color:#EC4899; font-weight:600; margin:10px 0;">Titik 1</div>', unsafe_allow_html=True)
        col1a, col1b = st.columns(2)
        with col1a:
            x1 = st.text_input("x₁", key="x1")
        with col1b:
            y1 = st.text_input("y₁", key="y1")
        
        # Titik 2
        st.markdown('<div style="color:#06B6D4; font-weight:600; margin:10px 0;">Titik 2</div>', unsafe_allow_html=True)
        col2a, col2b = st.columns(2)
        with col2a:
            x2 = st.text_input("x₂", key="x2")
        with col2b:
            y2 = st.text_input("y₂", key="y2")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Buttons
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            if st.button("Hitung Gradien", use_container_width=True):
                try:
                    x1_val = float(x1)
                    y1_val = float(y1)
                    x2_val = float(x2)
                    y2_val = float(y2)
                    
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
                    
                    st.markdown(f"""
                    <div class="result-box">
                        <div class="result-label">Gradien (m)</div>
                        <div class="result-value" style="color:{color}">{m_display}</div>
                        <div style="color:#64748B; font-size:0.95rem;">{desc}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.session_state.last_calc = {
                        'x1': x1_val, 'y1': y1_val, 
                        'x2': x2_val, 'y2': y2_val,
                        'm': m_value, 'm_display': m_display
                    }
                    
                except ValueError:
                    st.error("Mohon masukkan angka yang valid")
        
        with col_btn2:
            # TOMBOL RESET
            if st.button("Reset", use_container_width=True):
                # Clear session state
                if 'last_calc' in st.session_state:
                    del st.session_state.last_calc
                st.rerun()
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col_right:
        st.markdown('<div class="panel-card">', unsafe_allow_html=True)
        st.markdown("### Visualisasi Grafik")
        
        if 'last_calc' in st.session_state:
            calc = st.session_state.last_calc
            fig, ax = plt.subplots(figsize=(7, 6), facecolor='white')
            
            ax.axhline(y=0, color='#94A3B8', linewidth=1.2)
            ax.axvline(x=0, color='#94A3B8', linewidth=1.2)
            ax.grid(True, alpha=0.2, linestyle='-', linewidth=0.5, color='#CBD5E1')
            
            if calc['m'] is None:
                line_color = '#64748B'
            elif calc['m'] > 0:
                line_color = '#10B981'
            elif calc['m'] < 0:
                line_color = '#EF4444'
            else:
                line_color = '#3B82F6'
            
            ax.plot([calc['x1'], calc['x2']], [calc['y1'], calc['y2']], 
                   color=line_color, linewidth=3, marker='o', markersize=10,
                   markeredgecolor='white', markeredgewidth=2)
            
            ax.annotate(f"({format_num(calc['x1'])}, {format_num(calc['y1'])})", 
                       xy=(calc['x1'], calc['y1']), xytext=(calc['x1']+0.5, calc['y1']+0.5),
                       fontsize=10, fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.4', facecolor='white', 
                                edgecolor=line_color, linewidth=1.5))
            ax.annotate(f"({format_num(calc['x2'])}, {format_num(calc['y2'])})", 
                       xy=(calc['x2'], calc['y2']), xytext=(calc['x2']+0.5, calc['y2']+0.5),
                       fontsize=10, fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                                edgecolor=line_color, linewidth=1.5))
            
            x_range = max(abs(calc['x1']), abs(calc['x2']), 5) + 2
            y_range = max(abs(calc['y1']), abs(calc['y2']), 5) + 2
            ax.set_xlim(-x_range, x_range)
            ax.set_ylim(-y_range, y_range)
            
            ax.set_xlabel('x', fontsize=11, fontweight='600')
            ax.set_ylabel('y', fontsize=11, fontweight='600')
            ax.set_facecolor('#F8FAFC')
            
            st.pyplot(fig)
            plt.close()
        else:
            st.info("Masukkan koordinat dan klik 'Hitung Gradien'")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Button POP-UP
    if 'last_calc' in st.session_state:
        if st.button("Tampilkan Langkah Penyelesaian", use_container_width=True, type="primary"):
            show_steps_modal()


# ═══════════════════════════════════════════════════════════
#  TAB 2: DRILL (Simplified for now)
# ═══════════════════════════════════════════════════════════
with tab2:
    st.info("Mode Drill Practice - Coming soon!")


# ═══════════════════════════════════════════════════════════
#  TAB 3: REVIEW (Simplified for now)
# ═══════════════════════════════════════════════════════════
with tab3:
    st.info("Review Materi - Coming soon!")

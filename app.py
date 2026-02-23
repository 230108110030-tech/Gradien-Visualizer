"""
GRADIEN INTERACTIVE VISUALIZER - Streamlit Version
Media Pembelajaran Matematika SMP
Materi: Menentukan Gradien Garis Lurus

Author: Yustika Berlian Cindy Aprillia
Untuk: SMP Negeri 2 Lawang, Kelas VIII-H
"""

import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import numpy as np
import random
from fractions import Fraction

st.set_page_config(
    page_title="Gradien Visualizer — Media Pembelajaran Matematika",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════════
#  PREMIUM CSS
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

*, html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    box-sizing: border-box;
}
code, .formula-box, .formula-inline {
    font-family: 'JetBrains Mono', monospace !important;
}

#MainMenu, footer, header { visibility: hidden; }
.stApp { background: #F8F9FC; }

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #F1F5F9; }
::-webkit-scrollbar-thumb { background: #CBD5E1; border-radius: 3px; }

/* ── HEADER ── */
.app-header {
    background: linear-gradient(135deg, #1E1B4B 0%, #312E81 40%, #4338CA 100%);
    padding: 32px 48px 28px;
    margin: -1rem -1rem 0 -1rem;
    position: relative;
    overflow: hidden;
}
.app-header::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(99,102,241,0.3) 0%, transparent 70%);
    border-radius: 50%;
}
.app-header::after {
    content: '';
    position: absolute;
    bottom: -40px; left: 30%;
    width: 300px; height: 120px;
    background: radial-gradient(ellipse, rgba(167,139,250,0.15) 0%, transparent 70%);
}
.header-badge {
    display: inline-block;
    background: rgba(255,255,255,0.12);
    color: #C7D2FE;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.15);
    margin-bottom: 10px;
}
.app-title {
    color: #FFFFFF;
    font-size: 2.1rem;
    font-weight: 800;
    margin: 0;
    letter-spacing: -0.5px;
    line-height: 1.2;
}
.app-sub {
    color: #A5B4FC;
    font-size: 0.9rem;
    font-weight: 500;
    margin: 6px 0 0 0;
}
.accent-bar {
    height: 3px;
    background: linear-gradient(90deg, #818CF8, #6366F1, #4F46E5);
    margin: 0 -1rem 0 -1rem;
    opacity: 0.6;
}

/* ── NAV BUTTONS ── */
.stButton > button {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 600;
    font-size: 0.88rem;
    padding: 9px 16px;
    border-radius: 10px;
    border: 1.5px solid transparent;
    cursor: pointer;
    width: 100%;
    transition: all 0.2s ease;
    background: #E2E8F0 !important;
    color: #475569 !important;
    letter-spacing: 0.2px;
}
.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.12) !important;
    background: #CBD5E1 !important;
}
.stButton > button:active { transform: translateY(0); }

/* ── INPUTS ── */
.stTextInput > div > div > input {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 1rem;
    font-weight: 600;
    text-align: center;
    border-radius: 10px;
    border: 1.5px solid #E2E8F0;
    padding: 9px 14px;
    background: #FAFBFF;
    transition: all 0.2s;
    color: #1E293B;
}
.stTextInput > div > div > input:focus {
    border-color: #6366F1;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.12);
    background: white;
}
.stTextInput > label {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    color: #64748B !important;
    letter-spacing: 0.3px;
    text-transform: uppercase;
}

/* ── CARDS ── */
.surface-card {
    background: white;
    border-radius: 16px;
    padding: 28px;
    border: 1px solid #E8ECF4;
    box-shadow: 0 1px 4px rgba(0,0,0,0.04), 0 4px 16px rgba(0,0,0,0.04);
}

/* ── TITIK BADGE ── */
.titik-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 7px 16px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 0.88rem;
    color: white;
    margin-bottom: 12px;
    letter-spacing: 0.3px;
}

/* ── RESULT BOX ── */
.result-card {
    background: linear-gradient(135deg, #F0F4FF 0%, #EEF2FF 100%);
    border: 1px solid #C7D2FE;
    border-radius: 14px;
    padding: 22px 18px;
    text-align: center;
    margin-top: 16px;
}
.result-eyebrow {
    color: #6366F1;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 6px;
}
.result-value {
    font-size: 2.2rem;
    font-weight: 800;
    margin: 4px 0 6px 0;
    line-height: 1.1;
    font-family: 'JetBrains Mono', monospace !important;
}
.result-desc { color: #64748B; font-size: 0.88rem; font-weight: 500; }

/* ── MODAL OVERLAY ── */
.modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(15, 23, 42, 0.55);
    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
    z-index: 9998;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    padding: 40px 16px;
    overflow-y: auto;
}
.modal-box {
    background: white;
    border-radius: 20px;
    padding: 32px 36px;
    width: 100%;
    max-width: 720px;
    box-shadow: 0 24px 80px rgba(0,0,0,0.18);
    position: relative;
    animation: slideUp 0.25s ease;
}
@keyframes slideUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}
.modal-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 1px solid #F1F5F9;
}
.modal-title {
    font-size: 1.15rem;
    font-weight: 800;
    color: #1E293B;
    letter-spacing: -0.2px;
}
.modal-soal {
    background: #F8FAFF;
    border: 1px solid #E0E7FF;
    border-radius: 10px;
    padding: 14px 18px;
    font-size: 0.95rem;
    color: #334155;
    font-weight: 500;
    margin-bottom: 20px;
    line-height: 1.6;
}
.modal-soal-label {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #6366F1;
    text-transform: uppercase;
    margin-bottom: 5px;
}

/* ── STEP CARDS ── */
.step-item {
    background: #FAFBFF;
    border: 1px solid #E8ECF4;
    border-radius: 12px;
    margin-bottom: 10px;
    overflow: hidden;
}
.step-head {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 16px;
    background: white;
    border-bottom: 1px solid #F1F5F9;
}
.step-num {
    padding: 3px 12px;
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 700;
    color: white;
    letter-spacing: 0.5px;
    white-space: nowrap;
}
.step-name { font-weight: 700; font-size: 0.95rem; color: #1E293B; }
.step-content { padding: 12px 16px 14px; }
.formula-box {
    display: block;
    background: #EEF2FF;
    color: #4338CA;
    border-radius: 8px;
    padding: 9px 16px;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 1rem;
    font-weight: 600;
    margin: 6px 0;
    border: 1px solid #C7D2FE;
    white-space: nowrap;
    overflow-x: auto;
}
.step-note { color: #94A3B8; font-style: italic; font-size: 0.83rem; margin: 4px 0 2px 4px; }
.step-text { color: #475569; font-size: 0.92rem; margin: 5px 0; line-height: 1.6; }
.step-bullet { color: #475569; font-size: 0.92rem; margin: 5px 0 5px 8px; line-height: 1.6; }

/* ── CONCLUSION ── */
.conc-box {
    background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%);
    border: 1px solid #6EE7B7;
    border-radius: 14px;
    padding: 18px 22px;
    margin-top: 14px;
}
.conc-eyebrow { color: #059669; font-size: 0.7rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 4px; }
.conc-value { font-size: 1.3rem; font-weight: 800; color: #064E3B; margin: 4px 0; font-family: 'JetBrains Mono', monospace !important; }
.conc-detail { color: #065F46; font-size: 0.88rem; font-weight: 500; }

/* ── MODAL CLOSE BTN ── */
.modal-close-row { display: flex; justify-content: center; margin-top: 24px; }
.modal-close-btn {
    background: #1E293B;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 48px;
    font-size: 0.92rem;
    font-weight: 700;
    cursor: pointer;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    transition: all 0.2s;
    letter-spacing: 0.3px;
}
.modal-close-btn:hover { background: #334155; transform: translateY(-1px); }

/* ── SCORE BOX ── */
.score-card {
    background: linear-gradient(135deg, #4338CA 0%, #6366F1 100%);
    border-radius: 14px;
    padding: 18px;
    text-align: center;
    color: white;
    margin-bottom: 16px;
    box-shadow: 0 4px 16px rgba(99,102,241,0.3);
}
.score-eyebrow { font-size: 0.7rem; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; opacity: 0.75; }
.score-value { font-size: 2rem; font-weight: 800; margin: 2px 0; line-height: 1; }

/* ── DRILL QUESTION ── */
.q-card {
    background: #FAFBFF;
    border: 1px solid #E0E7FF;
    border-radius: 14px;
    padding: 18px 20px;
    margin-bottom: 16px;
    line-height: 1.7;
}
.q-eyebrow { color: #6366F1; font-weight: 700; font-size: 0.72rem; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 6px; }
.q-text { color: #1E293B; font-size: 0.95rem; font-weight: 500; }
.q-hint { color: #94A3B8; font-size: 0.82rem; margin-top: 4px; }

/* ── FEEDBACK ── */
.fb-ok  { background: #ECFDF5; border: 1.5px solid #6EE7B7; border-radius: 12px; padding: 14px 18px; color: #065F46; font-weight: 700; text-align: center; font-size: 0.97rem; }
.fb-err { background: #FFF1F2; border: 1.5px solid #FDA4AF; border-radius: 12px; padding: 14px 18px; color: #9F1239; font-weight: 700; text-align: center; font-size: 0.97rem; }
.fb-tip { background: #FFFBEB; border: 1.5px solid #FDE68A; border-radius: 12px; padding: 14px 18px; color: #78350F; font-weight: 500; line-height: 1.8; }

/* ── REVIEW ── */
.review-hero {
    background: linear-gradient(135deg, #78350F 0%, #B45309 50%, #D97706 100%);
    border-radius: 16px;
    padding: 24px 32px;
    margin-bottom: 28px;
    color: white;
    box-shadow: 0 4px 20px rgba(180,83,9,0.25);
}
.review-hero-eyebrow { font-size: 0.72rem; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; opacity: 0.75; margin-bottom: 4px; }
.review-hero-title { font-size: 1.5rem; font-weight: 800; line-height: 1.2; }

.sec-banner {
    border-radius: 12px;
    padding: 16px 22px;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 14px;
}
.sec-banner-green  { background: linear-gradient(135deg, #166534, #16A34A); }
.sec-banner-orange { background: linear-gradient(135deg, #7C2D12, #EA580C); }
.sec-banner-purple { background: linear-gradient(135deg, #4C1D95, #9333EA); }
.sec-banner-num { font-size: 0.72rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: rgba(255,255,255,0.65); margin-bottom: 2px; }
.sec-banner-title { font-size: 1.05rem; font-weight: 800; color: white; }

.formula-box-green  { background: #DCFCE7; color: #166534; border: 1px solid #86EFAC; }
.formula-box-orange { background: #FEF3C7; color: #92400E; border: 1px solid #FCD34D; }
.formula-box-purple { background: #EDE9FE; color: #4C1D95; border: 1px solid #C4B5FD; }

.conc-inline {
    border-radius: 10px;
    padding: 10px 16px;
    font-size: 0.9rem;
    font-weight: 600;
    margin-top: 10px;
    background: rgba(255,255,255,0.6);
    border: 1px solid rgba(0,0,0,0.06);
}
.sec-divider { border: none; border-top: 1px solid #F1F5F9; margin: 20px 0; }
.contoh-head { font-weight: 700; font-size: 0.95rem; margin: 16px 0 6px 0; }
.info-strip {
    background: linear-gradient(135deg, #312E81, #4338CA);
    border-radius: 14px;
    padding: 18px 24px;
    color: white;
    font-weight: 500;
    font-size: 0.9rem;
    margin-top: 10px;
    line-height: 1.8;
    box-shadow: 0 4px 16px rgba(67,56,202,0.25);
}

/* ── SECTION LABEL ── */
.section-eyebrow {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #94A3B8;
    margin-bottom: 6px;
}

/* ── DIVIDER LINE ── */
.divider-line {
    height: 1px;
    background: linear-gradient(90deg, transparent, #E2E8F0, transparent);
    margin: 6px 0 20px 0;
}

/* ── ACTIVE NAV indicator ── */
.nav-active-vis .stButton > button { background: #4338CA !important; color: white !important; border-color: #4338CA !important; }
.nav-active-drill .stButton > button { background: #DB2777 !important; color: white !important; border-color: #DB2777 !important; }
.nav-active-review .stButton > button { background: #D97706 !important; color: white !important; border-color: #D97706 !important; }

/* ── GRAPH LABEL ── */
.graph-eyebrow { font-size: 0.72rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: #94A3B8; margin-bottom: 8px; }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  HELPERS
# ═══════════════════════════════════════════════════════════════
def fraction_str(numerator, denominator):
    if denominator == 0:
        return "tak terdefinisi"
    f = Fraction(int(round(numerator)), int(round(denominator)))
    return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"

def format_num(v):
    return str(int(v)) if v == int(v) else f"{v:.1f}"

def parse_coord(s):
    try:
        return float(s.strip().replace(",", "."))
    except Exception:
        return None

def build_steps(x1, y1, x2, y2):
    x1s, y1s = format_num(x1), format_num(y1)
    x2s, y2s = format_num(x2), format_num(y2)
    dx, dy   = x2 - x1, y2 - y1
    dxs, dys = format_num(dx), format_num(dy)
    steps    = []

    if x1 == 0 and y1 == 0:
        lines = [("bullet", f"Titik pertama : O(0, 0)  — Titik pusat / origin"),
                 ("bullet", f"Titik kedua   : ({x2s}, {y2s})")]
    else:
        lines = [("bullet", f"Titik pertama : ({x1s}, {y1s})  —  x\u2081 = {x1s},  y\u2081 = {y1s}"),
                 ("bullet", f"Titik kedua   : ({x2s}, {y2s})  —  x\u2082 = {x2s},  y\u2082 = {y2s}")]
    steps.append({"title": "Identifikasi Koordinat Titik", "lines": lines})

    if x1 == 0 and y1 == 0:
        lines = [("text",    "Karena garis melewati titik pusat O(0,0), digunakan rumus khusus:"),
                 ("formula", "m  =  y / x"),
                 ("note",    "di mana x dan y adalah koordinat titik kedua (selain O)")]
    else:
        lines = [("text",    "Gunakan rumus gradien dua titik:"),
                 ("formula", "m  =  (y\u2082 \u2212 y\u2081) / (x\u2082 \u2212 x\u2081)"),
                 ("note",    "Rumus ini berlaku selama x\u2082 \u2260 x\u2081")]
    steps.append({"title": "Rumus yang Digunakan", "lines": lines})

    if dx == 0:
        steps.append({"title": "Substitusi Nilai", "lines": [
            ("text",    "Masukkan nilai koordinat ke dalam rumus:"),
            ("formula", f"m  =  ({y2s} \u2212 {y1s}) / ({x2s} \u2212 {x1s})"),
            ("formula", f"m  =  {dys} / {dxs}"),
        ]})
        steps.append({"title": "Analisis Hasil", "lines": [
            ("text", f"Diperoleh x\u2082 \u2212 x\u2081 = {dxs}"),
            ("text", "Karena penyebut = 0, gradien TIDAK TERDEFINISI. Ini adalah garis vertikal."),
        ]})
        return steps

    if x1 == 0 and y1 == 0:
        lines = [("text",    "Masukkan koordinat titik kedua ke dalam rumus:"),
                 ("formula", f"m  =  {y2s} / {x2s}")]
    else:
        lines = [("text",    "Masukkan nilai koordinat ke dalam rumus:"),
                 ("formula", f"m  =  ({y2s} \u2212 {y1s}) / ({x2s} \u2212 {x1s})"),
                 ("formula", f"m  =  {dys} / {dxs}")]
    steps.append({"title": "Substitusi Nilai", "lines": lines})

    frac  = Fraction(int(round(dy)), int(round(dx)))
    m_str = fraction_str(dy, dx)
    if frac.denominator == 1:
        lines = [("text",    "Bagi pembilang dengan penyebut:"),
                 ("formula", f"m  =  {dys} \u00f7 {dxs}  =  {m_str}"),
                 ("note",    "Hasil berupa bilangan bulat.")]
    else:
        lines = [("text",    "Sederhanakan pecahan:"),
                 ("formula", f"m  =  {dys}/{dxs}  =  {m_str}"),
                 ("note",    f"Pecahan {dys}/{dxs} disederhanakan menjadi {m_str}.")]
    steps.append({"title": "Sederhanakan / Hitung Hasil", "lines": lines})
    return steps

def build_conclusion(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    if dx == 0:
        return {"summary": "Gradien tidak terdefinisi (garis vertikal)",
                "desc": "Garis vertikal tidak memiliki nilai gradien karena penyebutnya = 0.",
                "color": "#94A3B8"}
    m_str = fraction_str(dy, dx)
    m_val = dy / dx
    if m_val > 0:
        return {"summary": f"m  =  {m_str}", "desc": "Garis NAIK dari kiri ke kanan — gradien POSITIF", "color": "#059669"}
    elif m_val < 0:
        return {"summary": f"m  =  {m_str}", "desc": "Garis TURUN dari kiri ke kanan — gradien NEGATIF", "color": "#DC2626"}
    else:
        return {"summary": f"m  =  {m_str}", "desc": "Garis HORIZONTAL — gradien bernilai NOL", "color": "#4338CA"}

def build_steps_html(x1, y1, x2, y2):
    """Build complete HTML string for steps — safe to inject into modal overlay."""
    x1s, y1s = format_num(x1), format_num(y1)
    x2s, y2s = format_num(x2), format_num(y2)

    if x1 == 0 and y1 == 0:
        soal = f"Tentukan gradien garis yang melalui titik O(0, 0) dan ({x2s}, {y2s})"
    else:
        soal = f"Tentukan gradien garis yang melalui titik ({x1s}, {y1s}) dan ({x2s}, {y2s})"

    step_colors = ["#0369A1", "#059669", "#D97706", "#7C3AED", "#DB2777"]
    steps = build_steps(x1, y1, x2, y2)

    html = f"""
    <div style="font-size:0.72rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;
                color:#6366F1;margin-bottom:6px;">Soal</div>
    <div style="background:#F8FAFF;border:1px solid #E0E7FF;border-radius:10px;
                padding:14px 18px;font-size:0.95rem;color:#334155;font-weight:500;
                margin-bottom:20px;line-height:1.6;">{soal}</div>
    """

    for i, step in enumerate(steps):
        c = step_colors[i % len(step_colors)]
        content_html = ""
        for ltype, text in step["lines"]:
            if ltype == "text":
                content_html += f'<p style="color:#475569;font-size:0.92rem;margin:6px 0;line-height:1.6;">{text}</p>'
            elif ltype == "bullet":
                content_html += f'<p style="color:#475569;font-size:0.92rem;margin:5px 0 5px 8px;line-height:1.6;">— {text}</p>'
            elif ltype == "formula":
                content_html += f'''<div style="display:block;background:#EEF2FF;color:#4338CA;
                    border:1px solid #C7D2FE;border-radius:8px;padding:9px 16px;
                    font-family:monospace;font-size:1rem;font-weight:600;
                    margin:5px 0;white-space:nowrap;overflow-x:auto;">{text}</div>'''
            elif ltype == "note":
                content_html += f'<p style="color:#94A3B8;font-style:italic;font-size:0.83rem;margin:3px 0;">{text}</p>'

        html += f"""
        <div style="background:#FAFBFF;border:1px solid #E8ECF4;border-radius:12px;
                    margin-bottom:10px;overflow:hidden;">
            <div style="display:flex;align-items:center;gap:12px;padding:11px 16px;
                        background:white;border-bottom:1px solid #F1F5F9;">
                <span style="padding:3px 12px;border-radius:20px;font-size:0.72rem;
                             font-weight:700;color:white;background:{c};letter-spacing:0.5px;
                             white-space:nowrap;">LANGKAH {i+1}</span>
                <span style="font-weight:700;font-size:0.95rem;color:#1E293B;">{step['title']}</span>
            </div>
            <div style="padding:12px 16px 14px;">{content_html}</div>
        </div>
        """

    conc = build_conclusion(x1, y1, x2, y2)
    html += f"""
    <div style="background:linear-gradient(135deg,#ECFDF5,#D1FAE5);border:1px solid #6EE7B7;
                border-radius:14px;padding:18px 22px;margin-top:14px;">
        <div style="color:#059669;font-size:0.7rem;font-weight:700;letter-spacing:1.5px;
                    text-transform:uppercase;margin-bottom:4px;">Kesimpulan</div>
        <div style="font-size:1.2rem;font-weight:800;color:#064E3B;margin:4px 0;
                    font-family:monospace;">{conc['summary']}</div>
        <div style="color:#065F46;font-size:0.88rem;font-weight:500;">{conc['desc']}</div>
    </div>
    """
    return html

def make_graph(x1, y1, x2, y2, color, title):
    import matplotlib.ticker as ticker
    fig, ax = plt.subplots(figsize=(7, 6))
    fig.patch.set_facecolor("#FAFBFF")
    ax.set_facecolor("#F8F9FC")

    xr = max(abs(x1), abs(x2), 5) + 3
    yr = max(abs(y1), abs(y2), 5) + 3
    # Round up to nice integer boundary
    xr = int(xr) + 1
    yr = int(yr) + 1
    ax.set_xlim(-xr, xr)
    ax.set_ylim(-yr, yr)

    ax.axhline(0, color="#CBD5E1", linewidth=1.0)
    ax.axvline(0, color="#CBD5E1", linewidth=1.0)
    ax.grid(True, linestyle="--", linewidth=0.5, color="#E2E8F0", alpha=0.9)

    # Integer-only ticks — step 1 or 2 depending on range
    step = 2 if xr > 8 else 1
    ax.xaxis.set_major_locator(ticker.MultipleLocator(step))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(step))
    ax.xaxis.set_minor_locator(ticker.NullLocator())
    ax.yaxis.set_minor_locator(ticker.NullLocator())

    ax.plot([x1, x2], [y1, y2], color=color, linewidth=3, marker="o",
            markersize=10, markeredgecolor="white", markeredgewidth=2.5, zorder=5)

    bbox_style = dict(boxstyle="round,pad=0.4", facecolor="white",
                      edgecolor=color, linewidth=1.5, alpha=0.97)

    # Smart label placement: push each label into opposite quadrant from the other point
    # relative to the midpoint, and avoid the axes lines
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    off_x = xr * 0.22
    off_y = yr * 0.22

    def get_offset(px, py, other_x, other_y):
        # Direction away from the other point
        dx = px - other_x
        dy = py - other_y
        dist = max((dx**2 + dy**2)**0.5, 0.001)
        nx = dx / dist * off_x
        ny = dy / dist * off_y

        tx, ty = px + nx, py + ny

        # Push away from axes if too close (avoid being on the line)
        if abs(tx) < xr * 0.15:
            tx += xr * 0.20 * (1 if nx >= 0 else -1)
        if abs(ty) < yr * 0.12:
            ty += yr * 0.18 * (1 if ny >= 0 else -1)

        # Clamp inside plot
        margin_x = xr * 0.18
        margin_y = yr * 0.18
        tx = max(-xr + margin_x, min(xr - margin_x, tx))
        ty = max(-yr + margin_y, min(yr - margin_y, ty))
        return tx, ty

    tx1, ty1 = get_offset(x1, y1, x2, y2)
    tx2, ty2 = get_offset(x2, y2, x1, y1)

    # No arrow lines — just place label box directly (no arrowprops)
    ax.annotate(f"({format_num(x1)}, {format_num(y1)})", xy=(x1, y1),
                xytext=(tx1, ty1), fontsize=10, fontweight="bold",
                bbox=bbox_style, color=color, zorder=7,
                arrowprops=None)
    ax.annotate(f"({format_num(x2)}, {format_num(y2)})", xy=(x2, y2),
                xytext=(tx2, ty2), fontsize=10, fontweight="bold",
                bbox=bbox_style, color=color, zorder=7,
                arrowprops=None)

    ax.set_xlabel("x", fontsize=12, fontweight="bold", color="#6366F1")
    ax.set_ylabel("y", fontsize=12, fontweight="bold", color="#6366F1")
    ax.set_title(title, fontsize=13, fontweight="bold", color="#1E293B", pad=12)
    ax.spines[['top','right','left','bottom']].set_color('#E2E8F0')
    fig.tight_layout()
    return fig

def make_empty_graph(title="Sistem Koordinat Kartesius"):
    import matplotlib.ticker as ticker
    fig, ax = plt.subplots(figsize=(7, 6))
    fig.patch.set_facecolor("#FAFBFF")
    ax.set_facecolor("#F8F9FC")
    ax.axhline(0, color="#CBD5E1", linewidth=1.0)
    ax.axvline(0, color="#CBD5E1", linewidth=1.0)
    ax.grid(True, linestyle="--", linewidth=0.5, color="#E2E8F0", alpha=0.9)
    ax.set_xlim(-10, 10); ax.set_ylim(-10, 10)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
    ax.xaxis.set_minor_locator(ticker.NullLocator())
    ax.yaxis.set_minor_locator(ticker.NullLocator())
    ax.set_xlabel("x", fontsize=12, fontweight="bold", color="#6366F1")
    ax.set_ylabel("y", fontsize=12, fontweight="bold", color="#6366F1")
    tc = "#1E293B" if "Koordinat" in title else "#94A3B8"
    ax.set_title(title, fontsize=13, fontweight="bold", color=tc, pad=12)
    ax.spines[['top','right','left','bottom']].set_color('#E2E8F0')
    fig.tight_layout()
    return fig


# ═══════════════════════════════════════════════════════════════
#  DIALOG (TRUE POPUP) — Langkah Penyelesaian
# ═══════════════════════════════════════════════════════════════
@st.dialog("Langkah Penyelesaian", width="large")
def show_langkah_dialog():
    r = st.session_state.calc_result
    if not r or "error" in r:
        st.warning("Belum ada hasil perhitungan.")
        return

    x1, y1, x2, y2 = r["x1"], r["y1"], r["x2"], r["y2"]
    x1s, y1s = format_num(x1), format_num(y1)
    x2s, y2s = format_num(x2), format_num(y2)

    # Soal
    if x1 == 0 and y1 == 0:
        soal = f"Tentukan gradien garis yang melalui titik O(0, 0) dan ({x2s}, {y2s})"
    else:
        soal = f"Tentukan gradien garis yang melalui titik ({x1s}, {y1s}) dan ({x2s}, {y2s})"

    st.markdown(f"""
    <div style="font-size:0.7rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;
                color:#6366F1;margin-bottom:5px;">SOAL</div>
    <div style="background:#F8FAFF;border:1px solid #E0E7FF;border-radius:10px;
                padding:13px 17px;font-size:0.95rem;color:#334155;font-weight:500;
                margin-bottom:18px;line-height:1.6;">{soal}</div>
    """, unsafe_allow_html=True)

    # Langkah-langkah
    step_colors = ["#0369A1", "#059669", "#D97706", "#7C3AED", "#DB2777"]
    steps = build_steps(x1, y1, x2, y2)

    for i, step in enumerate(steps):
        c = step_colors[i % len(step_colors)]
        # Build content html for this step
        content = ""
        for ltype, text in step["lines"]:
            if ltype == "text":
                content += f'<p style="color:#475569;font-size:0.92rem;margin:6px 0;line-height:1.6;">{text}</p>'
            elif ltype == "bullet":
                content += f'<p style="color:#475569;font-size:0.92rem;margin:5px 0 5px 8px;line-height:1.6;">— {text}</p>'
            elif ltype == "formula":
                content += f'<div style="display:block;background:#EEF2FF;color:#4338CA;border:1px solid #C7D2FE;border-radius:8px;padding:9px 16px;font-family:monospace;font-size:1rem;font-weight:600;margin:5px 0;white-space:nowrap;overflow-x:auto;">{text}</div>'
            elif ltype == "note":
                content += f'<p style="color:#94A3B8;font-style:italic;font-size:0.83rem;margin:3px 0;">{text}</p>'

        st.markdown(f"""
        <div style="background:#FAFBFF;border:1px solid #E8ECF4;border-radius:12px;
                    margin-bottom:10px;overflow:hidden;">
            <div style="display:flex;align-items:center;gap:12px;padding:11px 16px;
                        background:white;border-bottom:1px solid #F1F5F9;">
                <span style="padding:3px 12px;border-radius:20px;font-size:0.72rem;
                             font-weight:700;color:white;background:{c};
                             letter-spacing:0.5px;white-space:nowrap;">LANGKAH {i+1}</span>
                <span style="font-weight:700;font-size:0.95rem;color:#1E293B;">{step['title']}</span>
            </div>
            <div style="padding:12px 16px 14px;">{content}</div>
        </div>
        """, unsafe_allow_html=True)

    # Kesimpulan
    conc = build_conclusion(x1, y1, x2, y2)
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#ECFDF5,#D1FAE5);border:1px solid #6EE7B7;
                border-radius:14px;padding:18px 22px;margin-top:6px;">
        <div style="color:#059669;font-size:0.7rem;font-weight:700;letter-spacing:1.5px;
                    text-transform:uppercase;margin-bottom:4px;">Kesimpulan</div>
        <div style="font-size:1.2rem;font-weight:800;color:#064E3B;margin:4px 0;
                    font-family:monospace;">{conc['summary']}</div>
        <div style="color:#065F46;font-size:0.88rem;font-weight:500;">{conc['desc']}</div>
    </div>
    <div style="height:12px"></div>
    """, unsafe_allow_html=True)

    # Grafik di dalam dialog
    dx = x2 - x1
    if dx != 0:
        m_val = (y2 - y1) / dx
        gcolor = "#059669" if m_val > 0 else ("#DC2626" if m_val < 0 else "#4338CA")
    else:
        gcolor = "#94A3B8"
    st.markdown('<div style="font-size:0.72rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#6366F1;margin-bottom:6px;">VISUALISASI GRAFIK</div>', unsafe_allow_html=True)
    fig_modal = make_graph(x1, y1, x2, y2, gcolor, "Visualisasi Garis Lurus")
    st.pyplot(fig_modal, use_container_width=True)
    plt.close(fig_modal)

    # Tombol tutup (menutup dialog secara native)
    if st.button("✕  Tutup", use_container_width=True, key="dialog_tutup"):
        st.session_state.show_modal = False
        st.rerun()

    st.markdown("""
    <style>
    div[data-testid="stDialog"] button[kind="secondary"] {
        background: #1E293B !important;
        color: white !important;
        font-weight: 700 !important;
        border-radius: 10px !important;
        font-size: 0.92rem !important;
        margin-top: 4px;
    }
    div[data-testid="stDialog"] [data-testid="stBaseButton-headerNoPadding"] {
        color: #94A3B8 !important;
    }
    </style>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  SESSION STATE
# ═══════════════════════════════════════════════════════════════
for k, v in {
    "mode": "visualizer", "calc_result": None, "show_modal": False,
    "drill_score": 0, "drill_total": 0, "drill_coords": None,
    "drill_feedback": None, "drill_answered": False,
    "reset_key": 0
}.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ═══════════════════════════════════════════════════════════════
#  HEADER
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="app-header">
    <div class="header-badge">Media Pembelajaran Matematika</div>
    <div class="app-title">Gradien Visualizer</div>
    <div class="app-sub">Visualisasi Interaktif &nbsp;&middot;&nbsp; SMP Kelas VIII</div>
</div>
<div class="accent-bar"></div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  NAVIGATION
# ═══════════════════════════════════════════════════════════════
n1, n2, n3, _ = st.columns([1.2, 1.4, 1.2, 4])
with n1:
    if st.button("Mode Visualizer", use_container_width=True, key="nav_vis"):
        st.session_state.mode = "visualizer"
        st.session_state.show_modal = False
        st.rerun()
with n2:
    if st.button("Mode Drill Practice", use_container_width=True, key="nav_drill"):
        st.session_state.mode = "drill"; st.rerun()
with n3:
    if st.button("Review Materi", use_container_width=True, key="nav_review"):
        st.session_state.mode = "review"; st.rerun()

# Active button highlight
_mode_color = {"visualizer": "#4338CA", "drill": "#DB2777", "review": "#D97706"}[st.session_state.mode]
_mode_idx   = {"visualizer": 1, "drill": 2, "review": 3}[st.session_state.mode]
st.markdown(f"""
<style>
div[data-testid="stHorizontalBlock"] > div:nth-child({_mode_idx}) .stButton > button {{
    background: {_mode_color} !important;
    color: white !important;
    box-shadow: 0 4px 14px {_mode_color}55 !important;
}}
</style>""", unsafe_allow_html=True)

st.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  MODE: VISUALIZER
# ═══════════════════════════════════════════════════════════════
if st.session_state.mode == "visualizer":

    left_col, right_col = st.columns([1, 1.65], gap="large")

    with left_col:
        # Input panel
        st.markdown('<div class="section-eyebrow">Input Koordinat</div>', unsafe_allow_html=True)

        # Titik 1
        st.markdown('<span class="titik-badge" style="background:linear-gradient(135deg,#DC2626,#EF4444);">Titik 1</span>',
                    unsafe_allow_html=True)
        a1, b1 = st.columns(2)
        with a1: x1_str = st.text_input("x₁", value="", placeholder="Ketik angka...", key=f"vi_x1_{st.session_state.reset_key}")
        with b1: y1_str = st.text_input("y₁", value="", placeholder="Ketik angka...", key=f"vi_y1_{st.session_state.reset_key}")

        st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

        # Titik 2
        st.markdown('<span class="titik-badge" style="background:linear-gradient(135deg,#4338CA,#6366F1);">Titik 2</span>',
                    unsafe_allow_html=True)
        a2, b2 = st.columns(2)
        with a2: x2_str = st.text_input("x₂", value="", placeholder="Ketik angka...", key=f"vi_x2_{st.session_state.reset_key}")
        with b2: y2_str = st.text_input("y₂", value="", placeholder="Ketik angka...", key=f"vi_y2_{st.session_state.reset_key}")

        st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

        # Action buttons
        b_hitung  = st.button("Hitung Gradien",                  use_container_width=True, key="vi_hitung")
        b_langkah = st.button("Tampilkan Langkah Penyelesaian",  use_container_width=True, key="vi_langkah")
        b_reset   = st.button("Reset",                           use_container_width=True, key="vi_reset")

        # Button colors
        st.markdown("""
        <style>
        /* Hitung = indigo */
        div[data-testid="stVerticalBlock"] > div:has(> div[data-testid="element-container"]:nth-of-type(1)) {}
        </style>""", unsafe_allow_html=True)

        if b_reset:
            st.session_state.calc_result = None
            st.session_state.show_modal  = False
            st.session_state.reset_key  += 1
            st.rerun()

        def do_calc():
            x1 = parse_coord(x1_str); y1 = parse_coord(y1_str)
            x2 = parse_coord(x2_str); y2 = parse_coord(y2_str)
            if None in (x1, y1, x2, y2):
                st.session_state.calc_result = {"error": "Mohon masukkan angka yang valid di semua kolom."}
                return
            dx, dy = x2 - x1, y2 - y1
            if dx == 0:
                st.session_state.calc_result = {
                    "x1":x1,"y1":y1,"x2":x2,"y2":y2,
                    "m_str":"tak terdefinisi","desc":"Garis vertikal  (x\u2081 = x\u2082)","color":"#94A3B8"}
            else:
                m_str = fraction_str(dy, dx)
                m_val = dy / dx
                if   m_val > 0: color, desc = "#059669", "Garis naik — gradien positif"
                elif m_val < 0: color, desc = "#DC2626", "Garis turun — gradien negatif"
                else:           color, desc = "#4338CA", "Garis horizontal — gradien nol"
                st.session_state.calc_result = {
                    "x1":x1,"y1":y1,"x2":x2,"y2":y2,"m_str":m_str,"desc":desc,"color":color}

        if b_hitung:
            do_calc(); st.rerun()

        if b_langkah:
            do_calc()
            if st.session_state.calc_result and "error" not in st.session_state.calc_result:
                st.session_state.show_modal = True
            st.rerun()

        # Result card
        r = st.session_state.calc_result
        st.markdown('<div id="hasil-anchor"></div>', unsafe_allow_html=True)
        if r and "error" in r:
            st.error(r["error"])
        elif r:
            st.markdown(f"""
            <div class="result-card">
                <div class="result-eyebrow">Hasil Gradien</div>
                <div class="result-value" style="color:{r['color']};">m = {r['m_str']}</div>
                <div class="result-desc">{r['desc']}</div>
            </div>""", unsafe_allow_html=True)
            # Auto-scroll to result on mobile
            st.markdown("""
            <script>
            (function() {
                var el = document.getElementById('hasil-anchor');
                if (el) { el.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
            })();
            </script>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-card">
                <div class="result-eyebrow">Hasil</div>
                <div style="color:#CBD5E1;font-size:1rem;margin:10px 0;font-weight:600;">
                    Masukkan koordinat dan klik<br>Hitung Gradien
                </div>
            </div>""", unsafe_allow_html=True)

    with right_col:
        st.markdown('<div class="graph-eyebrow">Visualisasi Grafik</div>', unsafe_allow_html=True)
        r = st.session_state.calc_result
        if r and "error" not in r:
            fig = make_graph(r["x1"],r["y1"],r["x2"],r["y2"],r["color"],"Visualisasi Garis Lurus")
        else:
            fig = make_empty_graph()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

    # ── TRUE POPUP dengan @st.dialog ─────────────────────
    if st.session_state.show_modal and st.session_state.calc_result \
            and "error" not in st.session_state.calc_result:
        show_langkah_dialog()


# ═══════════════════════════════════════════════════════════════
#  MODE: DRILL PRACTICE
# ═══════════════════════════════════════════════════════════════
elif st.session_state.mode == "drill":

    graph_col, ctrl_col = st.columns([1.7, 1], gap="large")

    with ctrl_col:
        # Score
        st.markdown(f"""
        <div class="score-card">
            <div class="score-eyebrow">Skor Latihan</div>
            <div class="score-value">{st.session_state.drill_score} / {st.session_state.drill_total}</div>
        </div>""", unsafe_allow_html=True)

        # Question
        if st.session_state.drill_coords:
            qnum = st.session_state.drill_total + (0 if st.session_state.drill_answered else 1)
            st.markdown(f"""
            <div class="q-card">
                <div class="q-eyebrow">Soal #{qnum}</div>
                <div class="q-text">Perhatikan grafik di sebelah kiri.<br>
                <strong>Berapa nilai gradien garis tersebut?</strong></div>
                <div class="q-hint">Tulis angka atau pecahan, contoh: -1/2</div>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="q-card" style="text-align:center;color:#94A3B8;">
                Klik <strong>Soal Baru</strong> untuk memulai latihan
            </div>""", unsafe_allow_html=True)

        ans_input = st.text_input("Jawaban (m) =", placeholder="misalkan: 3  atau  -1/2",
                                   key="drill_ans", disabled=st.session_state.drill_answered)

        db1, db2 = st.columns(2)
        with db1: new_q = st.button("Soal Baru",   use_container_width=True, key="d_newq")
        with db2: cek   = st.button("Cek Jawaban", use_container_width=True, key="d_cek",
                                     disabled=(st.session_state.drill_answered or not st.session_state.drill_coords))
        hint_btn = st.button("Tampilkan Koordinat", use_container_width=True, key="d_hint")

        if new_q:
            if random.random() < 0.3:
                gx1, gy1 = 0, 0
                gx2 = random.choice([i for i in range(-8, 9) if i != 0])
                gy2 = random.randint(-8, 8)
            else:
                gx1 = random.randint(-7, 7); gy1 = random.randint(-7, 7)
                gx2 = random.choice([i for i in range(-7, 8) if i != gx1])
                gy2 = random.randint(-7, 7)
            st.session_state.drill_coords   = (gx1, gy1, gx2, gy2)
            st.session_state.drill_feedback = None
            st.session_state.drill_answered = False
            st.rerun()

        if cek and st.session_state.drill_coords and not st.session_state.drill_answered:
            raw = ans_input.strip(); user_m = None
            try:
                if "/" in raw:
                    n, d = raw.split("/"); user_m = float(n) / float(d)
                elif raw:
                    user_m = float(raw)
            except Exception:
                pass
            if user_m is None:
                st.session_state.drill_feedback = {"type":"error","text":"Masukkan angka atau pecahan, contoh: -1/2"}
            else:
                gx1,gy1,gx2,gy2 = st.session_state.drill_coords
                correct     = Fraction(int(round(gy2-gy1)), int(round(gx2-gx1)))
                correct_str = fraction_str(gy2-gy1, gx2-gx1)
                st.session_state.drill_total += 1
                if abs(user_m - float(correct)) < 0.0001:
                    st.session_state.drill_score += 1
                    st.session_state.drill_feedback = {"type":"correct","text":f"Benar!  —  m = {correct_str}"}
                else:
                    st.session_state.drill_feedback = {"type":"wrong","text":f"Belum tepat. Jawaban yang benar: m = {correct_str}"}
                st.session_state.drill_answered = True
            st.rerun()

        if hint_btn and st.session_state.drill_coords:
            gx1,gy1,gx2,gy2 = st.session_state.drill_coords
            st.session_state.drill_feedback = {"type":"hint",
                "text":(f"Petunjuk Koordinat\n\n"
                        f"Titik 1 : ({format_num(gx1)}, {format_num(gy1)})\n"
                        f"Titik 2 : ({format_num(gx2)}, {format_num(gy2)})")}
            st.rerun()

        fb = st.session_state.drill_feedback
        if fb:
            txt = fb["text"].replace("\n","<br>")
            if   fb["type"] == "correct": st.markdown(f'<div class="fb-ok">{txt}</div>',  unsafe_allow_html=True)
            elif fb["type"] == "wrong":   st.markdown(f'<div class="fb-err">{txt}</div>', unsafe_allow_html=True)
            elif fb["type"] == "hint":    st.markdown(f'<div class="fb-tip">{txt}</div>', unsafe_allow_html=True)
            elif fb["type"] == "error":   st.warning(fb["text"])

    with graph_col:
        st.markdown('<div class="graph-eyebrow">Grafik Soal</div>', unsafe_allow_html=True)
        if st.session_state.drill_coords:
            gx1,gy1,gx2,gy2 = st.session_state.drill_coords
            m_val  = (gy2-gy1)/(gx2-gx1)
            gcolor = "#059669" if m_val > 0 else ("#DC2626" if m_val < 0 else "#4338CA")
            fig = make_graph(gx1,gy1,gx2,gy2,gcolor,"Tentukan Gradien Garis Ini")
        else:
            fig = make_empty_graph("Klik Soal Baru untuk mulai")
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)


# ═══════════════════════════════════════════════════════════════
#  MODE: REVIEW MATERI
# ═══════════════════════════════════════════════════════════════
elif st.session_state.mode == "review":

    st.markdown("""
    <div class="review-hero">
        <div class="review-hero-eyebrow">Materi Pembelajaran</div>
        <div class="review-hero-title">Gradien Garis Lurus</div>
    </div>
    """, unsafe_allow_html=True)

    # ── SECTION 1 ───────────────────────────────────────
    st.markdown("""
    <div class="sec-banner sec-banner-green">
        <div>
            <div class="sec-banner-num">Bagian 1</div>
            <div class="sec-banner-title">Gradien Melalui Titik Pusat</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**Gradien Garis Melalui Titik Pusat (0,0) dan Titik (x,y)**")
    st.markdown("**Rumus:**")
    st.markdown('<div class="formula-box formula-box-green">m &nbsp;=&nbsp; y / x &nbsp;&nbsp;&nbsp;&nbsp;(dengan syarat x &ne; 0)</div>', unsafe_allow_html=True)
    st.markdown("**Catatan Penting:**")
    st.markdown("- Jika **x = 0** (garis vertikal) → gradien **TIDAK TERDEFINISI**\n- Jika **y = 0** (garis horizontal) → gradien **m = 0**")
    st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)

    st.markdown('<p class="contoh-head" style="color:#166534;">Contoh 1 — Gradien Positif</p>', unsafe_allow_html=True)
    st.markdown("**Soal:** Tentukan gradien persamaan garis lurus yang melalui titik pusat koordinat dan titik (4, 8)!")
    st.markdown("**Penyelesaian:**  \nPersamaan garis lurus melalui titik (0,0) dan (4,8), sehingga gradiennya adalah:")
    st.markdown('<div class="formula-box formula-box-green">m &nbsp;=&nbsp; y/x &nbsp;=&nbsp; 8/4 &nbsp;=&nbsp; 2</div>', unsafe_allow_html=True)
    st.markdown('<div class="conc-inline" style="color:#166534;">Kesimpulan: Gradien positif (m = 2) — garis <strong>NAIK</strong> dari kiri ke kanan.</div>', unsafe_allow_html=True)
    st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)

    st.markdown('<p class="contoh-head" style="color:#166534;">Contoh 2 — Gradien Negatif</p>', unsafe_allow_html=True)
    st.markdown("**Soal:** Tentukan gradien persamaan garis lurus yang melalui titik pusat koordinat dan titik (6, −3)!")
    st.markdown("**Penyelesaian:**  \nPersamaan garis lurus melalui titik (0,0) dan (6,−3), sehingga gradiennya adalah:")
    st.markdown('<div class="formula-box formula-box-green">m &nbsp;=&nbsp; y/x &nbsp;=&nbsp; &minus;3/6 &nbsp;=&nbsp; &minus;1/2</div>', unsafe_allow_html=True)
    st.markdown('<div class="conc-inline" style="color:#166534;">Kesimpulan: Gradien negatif (m = &minus;1/2) — garis <strong>TURUN</strong> dari kiri ke kanan.</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)

    # ── SECTION 2 ───────────────────────────────────────
    st.markdown("""
    <div class="sec-banner sec-banner-orange">
        <div>
            <div class="sec-banner-num">Bagian 2</div>
            <div class="sec-banner-title">Gradien Melalui Dua Titik</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**Gradien Garis Melalui Dua Titik (x₁, y₁) dan (x₂, y₂)**")
    st.markdown("**Rumus:**")
    st.markdown("""
    <div class="formula-box formula-box-orange" style="font-size:1.05rem;line-height:2;">
        m &nbsp;=&nbsp;
        <span style="display:inline-block;text-align:center;vertical-align:middle;">
            <span style="display:block;border-bottom:2px solid #92400E;padding-bottom:3px;">
                y<sub>2</sub> &minus; y<sub>1</sub>
            </span>
            <span style="display:block;padding-top:3px;">
                x<sub>2</sub> &minus; x<sub>1</sub>
            </span>
        </span>
        &nbsp;&nbsp;&nbsp;(dengan syarat x<sub>1</sub> &ne; x<sub>2</sub>)
    </div>
    """, unsafe_allow_html=True)
    st.markdown("**Catatan Penting:**")
    st.markdown("- Jika **x₁ = x₂** (garis vertikal) → gradien **TIDAK TERDEFINISI**")
    st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)

    st.markdown('<p class="contoh-head" style="color:#92400E;">Contoh 1 — Gradien Tidak Terdefinisi</p>', unsafe_allow_html=True)
    st.markdown("**Soal:** Tentukan gradien garis yang melalui P(3,1) dan Q(3,5)!")
    st.markdown("**Penyelesaian:**  \nTitik P(3,1) → x₁ = 3 dan y₁ = 1  \nTitik Q(3,5) → x₂ = 3 dan y₂ = 5  \nGradien garis PQ sebagai berikut:")
    st.markdown('<div class="formula-box formula-box-orange">m &nbsp;=&nbsp; (5 &minus; 1)/(3 &minus; 3) &nbsp;=&nbsp; 4/0</div>', unsafe_allow_html=True)
    st.markdown('<div class="conc-inline" style="color:#92400E;">Kesimpulan: Penyebut = 0, sehingga gradien <strong>TIDAK TERDEFINISI</strong> — berupa garis vertikal.</div>', unsafe_allow_html=True)
    st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)

    st.markdown('<p class="contoh-head" style="color:#92400E;">Contoh 2 — Gradien Negatif</p>', unsafe_allow_html=True)
    st.markdown("**Soal:** Tentukan gradien garis yang melalui P(1,4) dan Q(5,2)!")
    st.markdown("**Penyelesaian:**  \nTitik P(1,4) → x₁ = 1 dan y₁ = 4  \nTitik Q(5,2) → x₂ = 5 dan y₂ = 2  \nGradien garis PQ sebagai berikut:")
    st.markdown('<div class="formula-box formula-box-orange">m &nbsp;=&nbsp; (2 &minus; 4)/(5 &minus; 1) &nbsp;=&nbsp; &minus;2/4 &nbsp;=&nbsp; &minus;1/2</div>', unsafe_allow_html=True)
    st.markdown('<div class="conc-inline" style="color:#92400E;">Kesimpulan: Gradien garis PQ adalah &minus;1/2 — garis <strong>TURUN</strong> dari kiri ke kanan.</div>', unsafe_allow_html=True)
    st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)

    st.markdown('<p class="contoh-head" style="color:#92400E;">Contoh 3 — Gradien Nol</p>', unsafe_allow_html=True)
    st.markdown("**Soal:** Tentukan gradien garis yang melalui P(2,3) dan Q(7,3)!")
    st.markdown("**Penyelesaian:**  \nTitik P(2,3) → x₁ = 2 dan y₁ = 3  \nTitik Q(7,3) → x₂ = 7 dan y₂ = 3  \nGradien garis PQ sebagai berikut:")
    st.markdown('<div class="formula-box formula-box-orange">m &nbsp;=&nbsp; (3 &minus; 3)/(7 &minus; 2) &nbsp;=&nbsp; 0/5 &nbsp;=&nbsp; 0</div>', unsafe_allow_html=True)
    st.markdown('<div class="conc-inline" style="color:#92400E;">Kesimpulan: Gradien garis PQ adalah 0 — berupa <strong>GARIS HORIZONTAL</strong>.</div>', unsafe_allow_html=True)

    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)

    # ── SECTION 3 ───────────────────────────────────────
    st.markdown("""
    <div class="sec-banner sec-banner-purple">
        <div>
            <div class="sec-banner-num">Bagian 3</div>
            <div class="sec-banner-title">Interpretasi &amp; Tips</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**Interpretasi Nilai Gradien (m):**")
    st.markdown("""
| Nilai m | Jenis Garis | Keterangan |
|---------|-------------|------------|
| m > 0 | Naik (↗) | Gradien positif |
| m < 0 | Turun (↘) | Gradien negatif |
| m = 0 | Horizontal (→) | Sejajar sumbu x |
| m tak terdefinisi | Vertikal (↕) | Sejajar sumbu y |
""")
    st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)
    st.markdown("**Tips Penting:**")
    st.markdown("""
1. Semakin besar nilai **|m|**, semakin **curam** garisnya
2. Dua garis **sejajar** memiliki gradien yang **sama**
3. Dua garis **tegak lurus**: m₁ × m₂ = −1
4. Garis **horizontal** → gradien selalu = 0
5. Garis **vertikal** → gradien tidak terdefinisi
""")

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="info-strip">
        Gunakan <strong>Mode Visualizer</strong> untuk melihat grafik dan langkah penyelesaian secara lengkap.<br>
        Gunakan <strong>Mode Drill Practice</strong> untuk berlatih mengerjakan soal secara mandiri.
    </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
#  FOOTER
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div style="text-align:center;margin-top:48px;padding:20px;color:#CBD5E1;font-size:0.82rem;border-top:1px solid #F1F5F9;">
    Gradien Visualizer &nbsp;&middot;&nbsp; Media Pembelajaran Matematika SMP Kelas VIII<br>
    Dibuat oleh <strong style="color:#94A3B8;">Yustika Berlian Cindy Aprillia</strong>
</div>
""", unsafe_allow_html=True)

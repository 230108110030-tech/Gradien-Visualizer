"""
GRADIEN INTERACTIVE VISUALIZER - Streamlit Version
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

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Gradien Visualizer — Media Pembelajaran Matematika",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  MODERN CSS - Professional & Eye-Catching
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap');

/* ══════════════════════════════════════════════
   GLOBAL - Modern Foundation
   ══════════════════════════════════════════════ */
html, body, [class*="css"], .stApp, p, div, span, label, h1, h2, h3 {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

#MainMenu, footer, header { visibility: hidden; }

.stApp { 
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    background-attachment: fixed;
}

/* ══════════════════════════════════════════════
   HEADER - Glassmorphism Effect
   ══════════════════════════════════════════════ */
.app-header {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    padding: 32px 48px;
    margin: -1rem -1rem 0 -1rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}
.app-title { 
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 2.5rem; 
    font-weight: 900; 
    margin: 0;
    letter-spacing: -0.5px;
}
.app-sub { 
    color: #6B7280; 
    font-size: 1.05rem; 
    margin: 8px 0 0 0;
    font-weight: 500;
}
.accent-stripe {
    height: 4px;
    background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
    margin: 0 -1rem 24px -1rem;
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
}

/* ══════════════════════════════════════════════
   BUTTONS - Modern with 3D Effect
   ══════════════════════════════════════════════ */
.stButton > button {
    font-family: 'Inter', sans-serif !important;
    font-weight: 600;
    font-size: 1rem;
    padding: 14px 28px;
    border-radius: 12px;
    border: none;
    cursor: pointer;
    width: 100%;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    color: white !important;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    letter-spacing: 0.3px;
}
.stButton > button:hover { 
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5);
}
.stButton > button:active {
    transform: translateY(0px);
}

/* Tombol "Tutup" - LEBIH LEBAR sesuai request! */
button[kind="secondary"], 
.stButton button:contains("Tutup"),
div[data-testid="column"] > div > div > div > button {
    min-width: 240px !important;
    padding: 16px 60px !important;
    font-size: 1.05rem !important;
}

/* ══════════════════════════════════════════════
   INPUTS - Clean & Modern
   ══════════════════════════════════════════════ */
.stTextInput > div > div > input {
    font-family: 'Inter', sans-serif !important;
    font-size: 1.1rem;
    font-weight: 600;
    text-align: center;
    border-radius: 12px;
    border: 2px solid #E5E7EB;
    padding: 12px 16px;
    background: white;
    transition: all 0.3s ease;
}
.stTextInput > div > div > input:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
    outline: none;
}
.stTextInput > label {
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    color: #374151 !important;
    margin-bottom: 8px !important;
}

/* ══════════════════════════════════════════════
   CARDS - Glassmorphism Premium
   ══════════════════════════════════════════════ */
.panel-card {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: 20px;
    padding: 32px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.3);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.panel-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
}

.titik-label {
    display: inline-block;
    padding: 8px 24px;
    border-radius: 12px;
    font-weight: 700;
    font-size: 1rem;
    color: white;
    margin-bottom: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* ══════════════════════════════════════════════
   RESULT BOX - Gradient Style
   ══════════════════════════════════════════════ */
.result-box {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    border-radius: 16px;
    padding: 28px 20px;
    text-align: center;
    margin-top: 20px;
    border: 1px solid rgba(255, 255, 255, 0.5);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
}
.result-label { 
    color: #6B7280; 
    font-size: 0.8rem; 
    font-weight: 700; 
    letter-spacing: 2px; 
    text-transform: uppercase; 
}
.result-value { 
    font-size: 2.5rem; 
    font-weight: 900; 
    margin: 10px 0 6px 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.result-desc { 
    color: #6B7280; 
    font-size: 1rem;
    font-weight: 500;
}

/* ══════════════════════════════════════════════
   STEP CARDS - Premium Design
   ══════════════════════════════════════════════ */
.step-wrap {
    background: white;
    border-radius: 16px;
    margin-bottom: 16px;
    overflow: hidden;
    box-shadow: 0 2px 16px rgba(0, 0, 0, 0.08);
    border: 1px solid #F3F4F6;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.step-wrap:hover {
    transform: translateX(4px);
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.12);
}
.step-header {
    display: flex;
    align-items: center;
    padding: 16px 24px;
    gap: 14px;
    background: linear-gradient(135deg, #f9fafb 0%, #f3f4f6 100%);
}
.step-badge {
    padding: 6px 16px;
    border-radius: 24px;
    font-size: 0.8rem;
    font-weight: 700;
    color: white;
    white-space: nowrap;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}
.step-title { 
    font-weight: 700; 
    font-size: 1.05rem; 
    color: #111827;
    letter-spacing: -0.2px;
}
.step-body { 
    padding: 8px 24px 20px 24px;
    line-height: 1.8;
}
.formula-box {
    background: #F9FAFB;
    border: 2px solid #E5E7EB;
    border-radius: 12px;
    padding: 14px 24px;
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    font-size: 1.1rem;
    font-weight: 600;
    margin: 12px 0;
    display: inline-block;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}
.keterangan { 
    color: #6B7280; 
    font-style: italic; 
    font-size: 0.9rem; 
    margin: 6px 0 2px 24px;
    font-weight: 500;
}
.bullet-line { 
    margin: 8px 0 8px 6px;
    font-weight: 500;
}

/* ══════════════════════════════════════════════
   CONCLUSION - Eye-Catching
   ══════════════════════════════════════════════ */
.conclusion-box {
    background: linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%);
    border: 2px solid #10b981;
    border-radius: 16px;
    padding: 24px 32px;
    margin-top: 20px;
    box-shadow: 0 4px 20px rgba(16, 185, 129, 0.2);
}
.conc-label { 
    color: #065f46; 
    font-weight: 700; 
    font-size: 0.85rem; 
    letter-spacing: 1.5px;
    text-transform: uppercase;
}
.conc-summary { 
    font-size: 1.4rem; 
    font-weight: 900; 
    color: #065f46; 
    margin: 12px 0 8px 0;
    letter-spacing: -0.3px;
}
.conc-desc { 
    color: #047857;
    font-weight: 600;
    font-size: 1.05rem;
}

/* ══════════════════════════════════════════════
   SCORE - Bold Display
   ══════════════════════════════════════════════ */
.score-box {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 16px;
    padding: 24px;
    text-align: center;
    color: white;
    font-size: 1.8rem;
    font-weight: 900;
    margin-bottom: 20px;
    box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);
    letter-spacing: 1px;
}

/* ══════════════════════════════════════════════
   DRILL QUESTION CARD
   ══════════════════════════════════════════════ */
.drill-q-card {
    background: white;
    border-radius: 16px;
    padding: 24px 28px;
    margin-bottom: 20px;
    line-height: 1.8;
    box-shadow: 0 2px 16px rgba(0, 0, 0, 0.08);
    border: 1px solid #F3F4F6;
}
.drill-q-num { 
    color: #667eea; 
    font-weight: 700; 
    font-size: 0.85rem; 
    letter-spacing: 1.5px; 
    margin-bottom: 8px;
    text-transform: uppercase;
}

/* ══════════════════════════════════════════════
   FEEDBACK - Modern Alerts
   ══════════════════════════════════════════════ */
.fb-correct {
    background: linear-gradient(135deg, #d4fc79 0%, #96e6a1 100%);
    border: 2px solid #10b981;
    border-radius: 14px;
    padding: 18px 24px;
    color: #065f46;
    font-weight: 700;
    text-align: center;
    font-size: 1.1rem;
    box-shadow: 0 4px 16px rgba(16, 185, 129, 0.2);
}
.fb-wrong {
    background: linear-gradient(135deg, #ffdde1 0%, #ee9ca7 100%);
    border: 2px solid #ef4444;
    border-radius: 14px;
    padding: 18px 24px;
    color: #991b1b;
    font-weight: 700;
    text-align: center;
    font-size: 1.1rem;
    box-shadow: 0 4px 16px rgba(239, 68, 68, 0.2);
}
.fb-hint {
    background: linear-gradient(135deg, #fff6e5 0%, #ffe4b5 100%);
    border: 2px solid #f59e0b;
    border-radius: 14px;
    padding: 18px 24px;
    color: #92400e;
    font-weight: 600;
    line-height: 1.9;
    box-shadow: 0 4px 16px rgba(245, 158, 11, 0.2);
}

/* ══════════════════════════════════════════════
   REVIEW SECTION - Premium Cards
   ══════════════════════════════════════════════ */
.review-banner {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    border-radius: 20px;
    padding: 28px 40px;
    margin-bottom: 32px;
    color: white;
    font-size: 1.8rem;
    font-weight: 900;
    box-shadow: 0 8px 32px rgba(245, 87, 108, 0.3);
    letter-spacing: -0.5px;
}
.sec-card { 
    background: white;
    border-radius: 20px; 
    padding: 32px 36px; 
    margin-bottom: 28px; 
    line-height: 1.9;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
    border: 1px solid #F3F4F6;
}
.sec-card-green  { 
    border-left: 6px solid #10b981;
    background: linear-gradient(135deg, #ffffff 0%, #f0fdf4 100%);
}
.sec-card-orange { 
    border-left: 6px solid #f59e0b;
    background: linear-gradient(135deg, #ffffff 0%, #fffbeb 100%);
}
.sec-card-purple { 
    border-left: 6px solid #8b5cf6;
    background: linear-gradient(135deg, #ffffff 0%, #faf5ff 100%);
}

.sec-num-title {
    display: flex; 
    align-items: center; 
    gap: 16px;
    margin-bottom: 20px; 
    padding-bottom: 16px;
    border-bottom: 2px solid rgba(0,0,0,0.06);
}
.sec-num { 
    font-size: 1.8rem;
    font-weight: 900;
}
.sec-title { 
    font-size: 1.25rem; 
    font-weight: 800;
    letter-spacing: -0.3px;
}
.sec-subtitle { 
    font-weight: 700; 
    font-size: 1rem; 
    color: #111827; 
    margin: 18px 0 10px 0; 
    text-transform: uppercase; 
    letter-spacing: 0.8px;
}
.sec-divider { 
    border: none; 
    border-top: 2px solid rgba(0,0,0,0.08); 
    margin: 20px 0;
}
.contoh-label { 
    font-weight: 700; 
    font-size: 1.05rem; 
    margin: 18px 0 8px 0;
    color: #374151;
}
.kesimpulan-box { 
    background: rgba(102, 126, 234, 0.08);
    border-radius: 12px; 
    padding: 14px 20px; 
    margin-top: 12px; 
    font-size: 1rem;
    font-weight: 600;
    border-left: 4px solid #667eea;
}
.info-banner { 
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white; 
    border-radius: 16px; 
    padding: 24px 32px; 
    font-weight: 600; 
    margin-top: 12px; 
    line-height: 1.9;
    box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);
}

/* ══════════════════════════════════════════════
   ANIMATIONS - Smooth & Professional
   ══════════════════════════════════════════════ */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes slideIn {
    from { opacity: 0; transform: translateX(-20px); }
    to { opacity: 1; transform: translateX(0); }
}

.panel-card, .step-wrap, .sec-card {
    animation: fadeIn 0.4s ease-out;
}

.step-wrap:nth-child(odd) {
    animation: slideIn 0.5s ease-out;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────
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
    dx, dy = x2 - x1, y2 - y1
    dxs, dys = format_num(dx), format_num(dy)
    steps = []

    # Langkah 1
    if x1 == 0 and y1 == 0:
        lines = [("bullet", f"Titik pertama : O(0, 0)  ← Titik pusat / origin"),
                 ("bullet", f"Titik kedua   : ({x2s}, {y2s})")]
    else:
        lines = [("bullet", f"Titik pertama : ({x1s}, {y1s})  →  x₁ = {x1s},  y₁ = {y1s}"),
                 ("bullet", f"Titik kedua   : ({x2s}, {y2s})  →  x₂ = {x2s},  y₂ = {y2s}")]
    steps.append({"title": "Identifikasi Koordinat Titik", "lines": lines})

    # Langkah 2
    if x1 == 0 and y1 == 0:
        lines = [("text",      "Karena garis melewati titik pusat O(0,0), digunakan rumus khusus:"),
                 ("formula",   "m  =  y / x"),
                 ("keterangan","di mana x dan y adalah koordinat titik kedua (selain O)")]
    else:
        lines = [("text",      "Gunakan rumus gradien dua titik:"),
                 ("formula",   "m  =  (y₂ − y₁) / (x₂ − x₁)"),
                 ("keterangan","Rumus ini berlaku untuk semua pasang titik selama x₂ ≠ x₁")]
    steps.append({"title": "Rumus yang Digunakan", "lines": lines})

    # Langkah 3 — vertical case
    if dx == 0:
        steps.append({"title": "Substitusi Nilai", "lines": [
            ("text",    "Masukkan nilai koordinat ke dalam rumus:"),
            ("formula", f"m  =  ({y2s} − {y1s}) / ({x2s} − {x1s})"),
            ("formula", f"m  =  {dys} / {dxs}"),
        ]})
        steps.append({"title": "Cek Penyebut (x₂ − x₁)", "lines": [
            ("text", f"Diperoleh x₂ − x₁ = {dxs}"),
            ("text", "⚠️ Karena penyebut = 0, gradien TIDAK TERDEFINISI. Ini adalah garis vertikal."),
        ]})
        return steps

    if x1 == 0 and y1 == 0:
        lines = [("text",    "Masukkan koordinat titik kedua ke dalam rumus:"),
                 ("formula", f"m  =  {y2s} / {x2s}")]
    else:
        lines = [("text",    "Masukkan nilai koordinat ke dalam rumus:"),
                 ("formula", f"m  =  ({y2s} − {y1s}) / ({x2s} − {x1s})"),
                 ("formula", f"m  =  {dys} / {dxs}")]
    steps.append({"title": "Substitusi Nilai", "lines": lines})

    # Langkah 4
    frac  = Fraction(int(round(dy)), int(round(dx)))
    m_str = fraction_str(dy, dx)
    if frac.denominator == 1:
        lines = [("text",       "Bagi pembilang dan penyebut:"),
                 ("formula",    f"m  =  {dys} ÷ {dxs}  =  {m_str}"),
                 ("keterangan", "Hasil sudah berupa bilangan bulat.")]
    else:
        lines = [("text",       "Sederhanakan pecahan dengan membagi dengan FPB-nya:"),
                 ("formula",    f"m  =  {dys}/{dxs}  =  {m_str}"),
                 ("keterangan", f"Pecahan {dys}/{dxs} disederhanakan menjadi {m_str}.")]
    steps.append({"title": "Sederhanakan / Hitung Hasil", "lines": lines})
    return steps

def build_conclusion(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    if dx == 0:
        return {"summary": "Gradien tidak terdefinisi  (garis vertikal)",
                "desc":    "Garis vertikal tidak memiliki nilai gradien karena penyebutnya = 0.",
                "color":   "#64748B"}
    m_str = fraction_str(dy, dx)
    m_val = dy / dx
    if m_val > 0:
        return {"summary": f"Gradien garis  =  m  =  {m_str}",
                "desc":    "📈  Garis NAIK dari kiri ke kanan  →  gradien bernilai POSITIF", "color": "#06D6A0"}
    elif m_val < 0:
        return {"summary": f"Gradien garis  =  m  =  {m_str}",
                "desc":    "📉  Garis TURUN dari kiri ke kanan  →  gradien bernilai NEGATIF", "color": "#EF233C"}
    else:
        return {"summary": f"Gradien garis  =  m  =  {m_str}",
                "desc":    "➡️  Garis HORIZONTAL  →  gradien bernilai NOL", "color": "#4361EE"}

def render_steps(x1, y1, x2, y2):
    x1s, y1s = format_num(x1), format_num(y1)
    x2s, y2s = format_num(x2), format_num(y2)
    if x1 == 0 and y1 == 0:
        soal = f"Tentukan gradien garis yang melalui titik O(0, 0) dan ({x2s}, {y2s})"
    else:
        soal = f"Tentukan gradien garis yang melalui titik ({x1s}, {y1s}) dan ({x2s}, {y2s})"
    st.info(f"📌 **SOAL**\n\n{soal}")

    colors = ["#0284C7","#16A34A","#EA580C","#9333EA","#E91E63"]
    for i, step in enumerate(build_steps(x1, y1, x2, y2)):
        c = colors[i % len(colors)]
        st.markdown(
            f'<div class="step-wrap">'
            f'<div class="step-header" style="border-left:5px solid {c};">'
            f'<span class="step-badge" style="background:{c};">Langkah {i+1}</span>'
            f'<span class="step-title">{step["title"]}</span>'
            f'</div><div class="step-body">',
            unsafe_allow_html=True)
        for ltype, text in step["lines"]:
            if ltype   == "text":
                st.markdown(f"<p style='margin:6px 0;color:#1E293B;'>{text}</p>", unsafe_allow_html=True)
            elif ltype == "bullet":
                st.markdown(f"<p class='bullet-line'>• {text}</p>", unsafe_allow_html=True)
            elif ltype == "formula":
                st.markdown(f'<div class="formula-box" style="background:#EEF2FF;color:#3A0CA3;">{text}</div>', unsafe_allow_html=True)
            elif ltype == "keterangan":
                st.markdown(f"<p class='keterangan'>{text}</p>", unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)

    conc = build_conclusion(x1, y1, x2, y2)
    st.markdown(
        f'<div class="conclusion-box">'
        f'<div class="conc-label">✅  KESIMPULAN</div>'
        f'<div class="conc-summary">{conc["summary"]}</div>'
        f'<div class="conc-desc">{conc["desc"]}</div>'
        f'</div>', unsafe_allow_html=True)

def make_graph(x1, y1, x2, y2, color, title):
    fig, ax = plt.subplots(figsize=(7, 6))
    fig.patch.set_facecolor("#FAFBFF")
    ax.set_facecolor("#F0F4FF")
    xr = max(abs(x1), abs(x2), 5) + 3
    yr = max(abs(y1), abs(y2), 5) + 3
    ax.set_xlim(-xr, xr); ax.set_ylim(-yr, yr)
    ax.axhline(0, color="#94A3B8", linewidth=1.2)
    ax.axvline(0, color="#94A3B8", linewidth=1.2)
    ax.grid(True, linestyle="--", linewidth=0.6, color="#CBD5E1", alpha=0.8)
    ax.plot([x1,x2],[y1,y2], color=color, linewidth=3.5, marker="o", markersize=11,
            markeredgecolor="white", markeredgewidth=2, zorder=4)
    off  = max(xr, yr) * 0.07
    bbox = dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor=color, linewidth=1.5, alpha=0.9)
    ax.annotate(f"({format_num(x1)}, {format_num(y1)})", xy=(x1,y1),
                xytext=(x1+off, y1+off), fontsize=11, fontweight="bold", bbox=bbox, color=color)
    ax.annotate(f"({format_num(x2)}, {format_num(y2)})", xy=(x2,y2),
                xytext=(x2+off, y2+off), fontsize=11, fontweight="bold", bbox=bbox, color=color)
    ax.set_xlabel("x", fontsize=13, fontweight="bold", color="#4361EE")
    ax.set_ylabel("y", fontsize=13, fontweight="bold", color="#4361EE")
    ax.set_title(title, fontsize=15, fontweight="bold", color="#3A0CA3", pad=14)
    fig.tight_layout()
    return fig

def make_empty_graph(title="Sistem Koordinat Kartesius"):
    fig, ax = plt.subplots(figsize=(7, 6))
    fig.patch.set_facecolor("#FAFBFF")
    ax.set_facecolor("#F0F4FF")
    ax.axhline(0, color="#94A3B8", linewidth=1.2)
    ax.axvline(0, color="#94A3B8", linewidth=1.2)
    ax.grid(True, linestyle="--", linewidth=0.6, color="#CBD5E1", alpha=0.8)
    ax.set_xlim(-10, 10); ax.set_ylim(-10, 10)
    ax.set_xlabel("x", fontsize=13, fontweight="bold", color="#4361EE")
    ax.set_ylabel("y", fontsize=13, fontweight="bold", color="#4361EE")
    tc = "#3A0CA3" if "Koordinat" in title else "#64748B"
    ax.set_title(title, fontsize=14, fontweight="bold", color=tc, pad=14)
    fig.tight_layout()
    return fig


# ─────────────────────────────────────────────
#  SESSION STATE
# ─────────────────────────────────────────────
for k, v in {"mode":"visualizer","calc_result":None,"show_steps":False,
             "drill_score":0,"drill_total":0,"drill_coords":None,
             "drill_feedback":None,"drill_answered":False}.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ─────────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <div class="app-title">📐 Gradien Visualizer</div>
    <div class="app-sub">Media Pembelajaran Interaktif &nbsp;·&nbsp; SMP Kelas VIII</div>
</div>
<div class="accent-stripe"></div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  NAV
# ─────────────────────────────────────────────
nc1, nc2, nc3, _ = st.columns([1.3, 1.5, 1.2, 4])
with nc1:
    if st.button("📊  Mode Visualizer", use_container_width=True, key="nav_vis"):
        st.session_state.mode = "visualizer"; st.session_state.show_steps = False; st.rerun()
with nc2:
    if st.button("🎯  Mode Drill Practice", use_container_width=True, key="nav_drill"):
        st.session_state.mode = "drill"; st.rerun()
with nc3:
    if st.button("📚  Review Materi", use_container_width=True, key="nav_review"):
        st.session_state.mode = "review"; st.rerun()

# Active button color
_ac = {"visualizer":"#4361EE","drill":"#F72585","review":"#FFB703"}[st.session_state.mode]
_ai = {"visualizer":1,"drill":2,"review":3}[st.session_state.mode]
st.markdown(f"""
<style>
div[data-testid="stHorizontalBlock"] > div:nth-child({_ai}) .stButton > button
    {{ background-color: {_ac} !important; }}
div[data-testid="stHorizontalBlock"] > div:not(:nth-child({_ai})):not(:nth-child(4)) .stButton > button
    {{ background-color: #475569 !important; }}
</style>""", unsafe_allow_html=True)

st.markdown("<hr style='margin:6px 0 20px 0;border-color:#E2E8F0;'>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
#  VISUALIZER
# ═══════════════════════════════════════════════════════
if st.session_state.mode == "visualizer":

    left_col, right_col = st.columns([1.05, 1.6], gap="large")

    with left_col:
        st.markdown("### 🗂️ Input Koordinat")
        st.caption("Masukkan koordinat dua titik untuk menentukan gradien.")
        st.markdown("---")

        # Titik 1
        st.markdown('<span class="titik-label" style="background:#EF233C;">🔴  Titik 1</span>',
                    unsafe_allow_html=True)
        a1, b1 = st.columns(2)
        with a1: x1_str = st.text_input("x₁  =", value="", placeholder="contoh: 2", key="vi_x1")
        with b1: y1_str = st.text_input("y₁  =", value="", placeholder="contoh: 6", key="vi_y1")
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

        # Titik 2
        st.markdown('<span class="titik-label" style="background:#4361EE;">🔵  Titik 2</span>',
                    unsafe_allow_html=True)
        a2, b2 = st.columns(2)
        with a2: x2_str = st.text_input("x₂  =", value="", placeholder="contoh: 1", key="vi_x2")
        with b2: y2_str = st.text_input("y₂  =", value="", placeholder="contoh: 3", key="vi_y2")
        st.markdown("---")

        # Buttons
        btn_hitung  = st.button("✅  Hitung Gradien",            use_container_width=True, key="vi_hitung")
        btn_langkah = st.button("📋  Tampilkan Langkah-Langkah", use_container_width=True, key="vi_langkah")
        btn_reset   = st.button("🔄  Reset",                     use_container_width=True, key="vi_reset")

        # Style vis buttons
        st.markdown("""
        <style>
        [data-testid="stVerticalBlock"] [data-testid="element-container"]:has(button[kind="secondary"]) button {
            background-color: #94A3B8 !important;
        }
        </style>""", unsafe_allow_html=True)

        if btn_reset:
            st.session_state.calc_result = None
            st.session_state.show_steps  = False
            st.rerun()

        def do_calc():
            x1 = parse_coord(x1_str); y1 = parse_coord(y1_str)
            x2 = parse_coord(x2_str); y2 = parse_coord(y2_str)
            if None in (x1, y1, x2, y2):
                st.session_state.calc_result = {"error": "⚠️ Mohon masukkan angka yang valid di semua kolom."}
                return
            dx, dy = x2 - x1, y2 - y1
            if dx == 0:
                st.session_state.calc_result = {
                    "x1":x1,"y1":y1,"x2":x2,"y2":y2,
                    "m_str":"tak terdefinisi","desc":"Garis vertikal  (x₁ = x₂)","color":"#94A3B8"}
            else:
                m_str = fraction_str(dy, dx)
                m_val = dy / dx
                if   m_val > 0: color, desc = "#06D6A0", "📈 Garis naik · gradien positif"
                elif m_val < 0: color, desc = "#EF233C", "📉 Garis turun · gradien negatif"
                else:           color, desc = "#4361EE", "➡️ Garis horizontal · gradien nol"
                st.session_state.calc_result = {
                    "x1":x1,"y1":y1,"x2":x2,"y2":y2,"m_str":m_str,"desc":desc,"color":color}

        if btn_hitung:
            do_calc(); st.session_state.show_steps = False; st.rerun()
        if btn_langkah:
            do_calc()
            if st.session_state.calc_result and "error" not in st.session_state.calc_result:
                st.session_state.show_steps = True
            st.rerun()

        # Result
        r = st.session_state.calc_result
        if r and "error" in r:
            st.error(r["error"])
        elif r:
            st.markdown(f"""
            <div class="result-box">
                <div class="result-label">Hasil Gradien</div>
                <div class="result-value" style="color:{r['color']};">m &nbsp;=&nbsp; {r['m_str']}</div>
                <div class="result-desc">{r['desc']}</div>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-box">
                <div class="result-label">Hasil</div>
                <div style="color:#94A3B8;font-size:1rem;margin:10px 0;">
                    Masukkan koordinat<br>lalu klik Hitung Gradien</div>
            </div>""", unsafe_allow_html=True)

    with right_col:
        st.markdown("**Visualisasi Grafik**")
        r = st.session_state.calc_result
        if r and "error" not in r:
            fig = make_graph(r["x1"],r["y1"],r["x2"],r["y2"],r["color"],"Visualisasi Garis Lurus")
        else:
            fig = make_empty_graph()
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

    # Steps below
    if st.session_state.show_steps and st.session_state.calc_result \
            and "error" not in st.session_state.calc_result:
        st.markdown("---")
        st.markdown("## 📋 Langkah-Langkah Perhitungan")
        r = st.session_state.calc_result
        render_steps(r["x1"],r["y1"],r["x2"],r["y2"])
        st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)
        if st.button("✖  Tutup", key="close_steps"):
            st.session_state.show_steps = False; st.rerun()


# ═══════════════════════════════════════════════════════
#  DRILL PRACTICE
# ═══════════════════════════════════════════════════════
elif st.session_state.mode == "drill":

    graph_col, ctrl_col = st.columns([1.7, 1], gap="large")

    with ctrl_col:
        # Score
        st.markdown(
            f'<div class="score-box">🏆 Skor &nbsp; {st.session_state.drill_score} / {st.session_state.drill_total}</div>',
            unsafe_allow_html=True)

        # Question
        if st.session_state.drill_coords:
            qnum = st.session_state.drill_total + (0 if st.session_state.drill_answered else 1)
            st.markdown(f"""
            <div class="drill-q-card">
                <div class="drill-q-num">SOAL #{qnum}</div>
                Perhatikan grafik di sebelah kiri.<br>
                <strong>Berapa nilai gradien garis tersebut?</strong><br>
                <span style="color:#64748B;font-size:0.88rem;">(Tulis angka atau pecahan, mis: -1/2)</span>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="drill-q-card" style="text-align:center;color:#64748B;">
                Klik <strong>Soal Baru</strong> untuk memulai latihan! 🎯
            </div>""", unsafe_allow_html=True)

        # Input
        ans_input = st.text_input(
            "Gradien  ( m )  =",
            placeholder="contoh: 3  atau  -1/2",
            key="drill_ans",
            disabled=st.session_state.drill_answered)

        # Buttons
        db1, db2 = st.columns(2)
        with db1: new_q = st.button("🎲  Soal Baru",  use_container_width=True, key="d_newq")
        with db2: cek   = st.button("✔  Cek Jawaban", use_container_width=True, key="d_cek",
                                     disabled=(st.session_state.drill_answered or not st.session_state.drill_coords))
        hint_btn = st.button("💡  Tampilkan Koordinat", use_container_width=True, key="d_hint")

        # New question logic
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

        # Check answer logic
        if cek and st.session_state.drill_coords and not st.session_state.drill_answered:
            raw    = ans_input.strip()
            user_m = None
            try:
                if "/" in raw:
                    n, d = raw.split("/"); user_m = float(n) / float(d)
                elif raw:
                    user_m = float(raw)
            except Exception:
                pass

            if user_m is None:
                st.session_state.drill_feedback = {"type":"error",
                    "text":"⚠️ Masukkan angka atau pecahan seperti -1/2"}
            else:
                gx1,gy1,gx2,gy2 = st.session_state.drill_coords
                correct     = Fraction(int(round(gy2-gy1)), int(round(gx2-gx1)))
                correct_str = fraction_str(gy2-gy1, gx2-gx1)
                st.session_state.drill_total += 1
                if abs(user_m - float(correct)) < 0.0001:
                    st.session_state.drill_score += 1
                    st.session_state.drill_feedback = {"type":"correct",
                        "text":f"✅  Benar!\n\nm  =  {correct_str}"}
                else:
                    st.session_state.drill_feedback = {"type":"wrong",
                        "text":f"❌  Belum tepat.\n\nJawaban yang benar:\nm  =  {correct_str}"}
                st.session_state.drill_answered = True
            st.rerun()

        # Hint logic
        if hint_btn and st.session_state.drill_coords:
            gx1,gy1,gx2,gy2 = st.session_state.drill_coords
            st.session_state.drill_feedback = {"type":"hint",
                "text":(f"💡  Petunjuk:\n\n"
                        f"Titik 1 : ({format_num(gx1)}, {format_num(gy1)})\n"
                        f"Titik 2 : ({format_num(gx2)}, {format_num(gy2)})")}
            st.rerun()

        # Feedback display
        fb = st.session_state.drill_feedback
        if fb:
            txt = fb["text"].replace("\n", "<br>")
            if   fb["type"] == "correct": st.markdown(f'<div class="fb-correct">{txt}</div>', unsafe_allow_html=True)
            elif fb["type"] == "wrong":   st.markdown(f'<div class="fb-wrong">{txt}</div>',   unsafe_allow_html=True)
            elif fb["type"] == "hint":    st.markdown(f'<div class="fb-hint">{txt}</div>',    unsafe_allow_html=True)
            elif fb["type"] == "error":   st.warning(fb["text"])

    with graph_col:
        st.markdown("**Grafik Soal**")
        if st.session_state.drill_coords:
            gx1,gy1,gx2,gy2 = st.session_state.drill_coords
            m_val  = (gy2-gy1)/(gx2-gx1)
            gcolor = "#06D6A0" if m_val > 0 else ("#EF233C" if m_val < 0 else "#4361EE")
            fig = make_graph(gx1,gy1,gx2,gy2,gcolor,"Tentukan Gradien Garis Ini!")
        else:
            fig = make_empty_graph("Klik 'Soal Baru' untuk mulai!")
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)


# ═══════════════════════════════════════════════════════
#  REVIEW MATERI  ← pakai st.markdown native, BUKAN unsafe HTML untuk konten
# ═══════════════════════════════════════════════════════
elif st.session_state.mode == "review":

    st.markdown('<div class="review-banner">📚  REVIEW MATERI — GRADIEN GARIS LURUS</div>',
                unsafe_allow_html=True)

    # ── SECTION 1 ── kotak hanya berisi judul ──────────
    st.markdown("""
    <div class="sec-card sec-card-green" style="padding:18px 24px;">
        <div style="display:flex;align-items:center;gap:14px;">
            <span style="font-size:1.6rem;">1️⃣</span>
            <span style="font-size:1.2rem;font-weight:900;color:#16A34A;">
                GRADIEN MELALUI TITIK PUSAT
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**Gradien Garis Melalui Titik Pusat (0,0) dan Titik (x,y)**")
    st.markdown("**📐 Rumus:**")
    st.markdown('<div class="formula-box" style="background:#C8F7DC;color:#065F46;">m &nbsp;=&nbsp; y / x &nbsp;&nbsp;&nbsp;&nbsp;(dengan syarat x ≠ 0)</div>',
                unsafe_allow_html=True)
    st.markdown("**⚠️ Catatan Penting:**")
    st.markdown("- Jika **x = 0** (garis vertikal) → gradien **TIDAK TERDEFINISI**\n- Jika **y = 0** (garis horizontal) → gradien **m = 0**")
    st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)

    st.markdown('<p class="contoh-label" style="color:#16A34A;">📝 CONTOH 1 — Gradien Positif</p>', unsafe_allow_html=True)
    st.markdown("**Soal:** Tentukan gradien persamaan garis lurus yang melalui titik pusat koordinat dan titik (4, 8)!")
    st.markdown("**Penyelesaian:**  \nPersamaan garis lurus melalui titik (0,0) dan (4,8), sehingga gradiennya adalah:")
    st.markdown('<div class="formula-box" style="background:#C8F7DC;color:#065F46;">m &nbsp;=&nbsp; y/x &nbsp;=&nbsp; 8/4 &nbsp;=&nbsp; 2</div>', unsafe_allow_html=True)
    st.markdown('<div class="kesimpulan-box">✅ <strong>Kesimpulan:</strong> Didapatkan gradien positif (m = 2), artinya garis <strong>NAIK</strong> dari kiri ke kanan.</div>', unsafe_allow_html=True)
    st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)

    st.markdown('<p class="contoh-label" style="color:#16A34A;">📝 CONTOH 2 — Gradien Negatif</p>', unsafe_allow_html=True)
    st.markdown("**Soal:** Tentukan gradien persamaan garis lurus yang melalui titik pusat koordinat dan titik (6, −3)!")
    st.markdown("**Penyelesaian:**  \nPersamaan garis lurus melalui titik (0,0) dan (6,−3), sehingga gradiennya adalah:")
    st.markdown('<div class="formula-box" style="background:#C8F7DC;color:#065F46;">m &nbsp;=&nbsp; y/x &nbsp;=&nbsp; −3/6 &nbsp;=&nbsp; −1/2</div>', unsafe_allow_html=True)
    st.markdown('<div class="kesimpulan-box">✅ <strong>Kesimpulan:</strong> Didapatkan gradien negatif (m = −1/2), artinya garis <strong>TURUN</strong> dari kiri ke kanan, seperti jalan menurun.</div>', unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom:22px'></div>", unsafe_allow_html=True)

    # ── SECTION 2 ── kotak hanya berisi judul ──────────
    st.markdown("""
    <div class="sec-card sec-card-orange" style="padding:18px 24px;">
        <div style="display:flex;align-items:center;gap:14px;">
            <span style="font-size:1.6rem;">2️⃣</span>
            <span style="font-size:1.2rem;font-weight:900;color:#EA580C;">
                GRADIEN MELALUI DUA TITIK
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**Gradien Garis Melalui Dua Titik (x₁,y₁) dan (x₂,y₂)**")
    st.markdown("**📐 Rumus:**")
    st.markdown('<div class="formula-box" style="background:#FDDCB5;color:#7C2D12;">m &nbsp;=&nbsp; (y₂ − y₁) / (x₂ − x₁) &nbsp;&nbsp;&nbsp;&nbsp;(dengan syarat x₁ ≠ x₂)</div>', unsafe_allow_html=True)
    st.markdown("**⚠️ Catatan Penting:**")
    st.markdown("- Jika **x₁ = x₂** (garis vertikal) → gradien **TIDAK TERDEFINISI**")
    st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)

    st.markdown('<p class="contoh-label" style="color:#EA580C;">📝 CONTOH 1 — Gradien Tidak Terdefinisi</p>', unsafe_allow_html=True)
    st.markdown("**Soal:** Tentukan gradien garis yang melalui P(3,1) dan Q(3,5)!")
    st.markdown("**Penyelesaian:**  \nTitik P(3,1) → x₁ = 3 dan y₁ = 1  \nTitik Q(3,5) → x₂ = 3 dan y₂ = 5  \nGradien garis PQ sebagai berikut:")
    st.markdown('<div class="formula-box" style="background:#FDDCB5;color:#7C2D12;">m &nbsp;=&nbsp; (5 − 1)/(3 − 3) &nbsp;=&nbsp; 4/0</div>', unsafe_allow_html=True)
    st.markdown('<div class="kesimpulan-box">✅ <strong>Kesimpulan:</strong> Karena penyebut = 0, maka gradien <strong>TIDAK TERDEFINISI</strong> dan berupa <strong>GARIS VERTIKAL</strong>.</div>', unsafe_allow_html=True)
    st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)

    st.markdown('<p class="contoh-label" style="color:#EA580C;">📝 CONTOH 2 — Gradien Negatif</p>', unsafe_allow_html=True)
    st.markdown("**Soal:** Tentukan gradien garis yang melalui P(1,4) dan Q(5,2)!")
    st.markdown("**Penyelesaian:**  \nTitik P(1,4) → x₁ = 1 dan y₁ = 4  \nTitik Q(5,2) → x₂ = 5 dan y₂ = 2  \nGradien garis PQ sebagai berikut:")
    st.markdown('<div class="formula-box" style="background:#FDDCB5;color:#7C2D12;">m &nbsp;=&nbsp; (2 − 4)/(5 − 1) &nbsp;=&nbsp; −2/4 &nbsp;=&nbsp; −1/2</div>', unsafe_allow_html=True)
    st.markdown('<div class="kesimpulan-box">✅ <strong>Kesimpulan:</strong> Gradien garis PQ adalah −1/2. Garis <strong>TURUN</strong> dari kiri ke kanan.</div>', unsafe_allow_html=True)
    st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)

    st.markdown('<p class="contoh-label" style="color:#EA580C;">📝 CONTOH 3 — Gradien Nol</p>', unsafe_allow_html=True)
    st.markdown("**Soal:** Tentukan gradien garis yang melalui P(2,3) dan Q(7,3)!")
    st.markdown("**Penyelesaian:**  \nTitik P(2,3) → x₁ = 2 dan y₁ = 3  \nTitik Q(7,3) → x₂ = 7 dan y₂ = 3  \nGradien garis PQ sebagai berikut:")
    st.markdown('<div class="formula-box" style="background:#FDDCB5;color:#7C2D12;">m &nbsp;=&nbsp; (3 − 3)/(7 − 2) &nbsp;=&nbsp; 0/5 &nbsp;=&nbsp; 0</div>', unsafe_allow_html=True)
    st.markdown('<div class="kesimpulan-box">✅ <strong>Kesimpulan:</strong> Gradien garis PQ adalah 0. Berupa <strong>GARIS HORIZONTAL</strong>.</div>', unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom:22px'></div>", unsafe_allow_html=True)

    # ── SECTION 3 ── kotak hanya berisi judul ──────────
    st.markdown("""
    <div class="sec-card sec-card-purple" style="padding:18px 24px;">
        <div style="display:flex;align-items:center;gap:14px;">
            <span style="font-size:1.6rem;">3️⃣</span>
            <span style="font-size:1.2rem;font-weight:900;color:#9333EA;">
                INTERPRETASI &amp; TIPS
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**📊 Interpretasi Nilai Gradien (m):**")
    st.markdown("""
| Nilai m | Jenis Garis | Keterangan |
|---------|-------------|------------|
| m > 0 | ↗ Naik | Gradien positif |
| m < 0 | ↘ Turun | Gradien negatif |
| m = 0 | → Horizontal | Sejajar sumbu x |
| m tak terdefinisi | ↕ Vertikal | Sejajar sumbu y |
""")
    st.markdown('<hr class="sec-divider">', unsafe_allow_html=True)
    st.markdown("**💡 Tips Penting:**")
    st.markdown("""
1. Semakin besar nilai **|m|**, semakin **CURAM** garisnya
2. Dua garis **sejajar** memiliki gradien yang **SAMA**
3. Dua garis **tegak lurus**: m₁ × m₂ = −1
4. Garis **horizontal** → gradien selalu = 0
5. Garis **vertikal** → gradien tidak terdefinisi
""")

    # Info banner
    st.markdown("""
    <div class="info-banner">
        💡 Gunakan <strong>Mode Visualizer</strong> untuk melihat grafik dan perhitungan langkah demi langkah!<br>
        🎯 Gunakan <strong>Mode Drill Practice</strong> untuk berlatih mengerjakan soal!
    </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;margin-top:40px;padding:20px;color:#94A3B8;font-size:0.85rem;">
    📐 Gradien Visualizer &nbsp;·&nbsp; Media Pembelajaran Matematika SMP Kelas VIII<br>
    Dibuat oleh <strong>Yustika Berlian Cindy Aprillia</strong>
</div>
""", unsafe_allow_html=True)

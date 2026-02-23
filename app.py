
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Kalkulator Gradien", layout="centered")

st.title("Kalkulator Gradien Garis")
st.caption("Masukkan dua titik untuk menentukan gradien dan visualisasi grafik garis")

# ---------- Helper: Auto Scroll ----------
def scroll_to_result():
    st.markdown(
        '''
        <script>
        const resultSection = document.getElementById("hasil");
        if (resultSection) {
            resultSection.scrollIntoView({behavior: "smooth"});
        }
        </script>
        ''',
        unsafe_allow_html=True
    )

# ---------- Input Section ----------
st.subheader("Input Titik")

x1 = st.number_input("X₁", key="x1", value=0)
y1 = st.number_input("Y₁", key="y1", value=0)
x2 = st.number_input("X₂", key="x2", value=0)
y2 = st.number_input("Y₂", key="y2", value=0)

st.caption("⬇️ Scroll ke bawah untuk melihat hasil dan visualisasi grafik")

# ---------- Plot Function ----------
def plot_garis(x1, y1, x2, y2):
    fig, ax = plt.subplots()
    ax.plot([x1, x2], [y1, y2], marker='o')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    return fig

# ---------- Button Actions ----------
col1, col2 = st.columns(2)

with col1:
    hitung = st.button("Hitung Gradien")

with col2:
    reset = st.button("Reset")

if reset:
    for key in ["x1", "y1", "x2", "y2"]:
        st.session_state[key] = 0
    st.session_state["hasil"] = None
    st.session_state["fig"] = None
    st.experimental_rerun()

if hitung:
    if x2 - x1 == 0:
        st.error("Gradien tidak terdefinisi karena pembagi nol.")
    else:
        m = (y2 - y1) / (x2 - x1)
        fig = plot_garis(x1, y1, x2, y2)

        st.session_state["hasil"] = m
        st.session_state["fig"] = fig

        scroll_to_result()

# ---------- Result Section ----------
st.markdown('<div id="hasil"></div>', unsafe_allow_html=True)
st.subheader("Hasil")

if "hasil" in st.session_state and st.session_state["hasil"] is not None:
    st.success(f"Gradien garis adalah: **{st.session_state['hasil']}**")

    st.markdown(
        r'''
        <div style="overflow-x:auto; white-space: nowrap;">
        $$ m = \frac{y_2 - y_1}{x_2 - x_1} \quad (x_2 \neq x_1) $$
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.pyplot(st.session_state["fig"])

    with st.expander("Langkah Penyelesaian"):
        st.write("1. Menentukan selisih koordinat y dan x")
        st.write("2. Membagi selisih y dengan selisih x")
        st.latex(r"m = \frac{y_2 - y_1}{x_2 - x_1}")
        st.pyplot(st.session_state["fig"])
else:
    st.info("Silakan masukkan data dan klik **Hitung Gradien**.")


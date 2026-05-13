import streamlit as st
import random
import time

# Sayfa ayarları
st.set_page_config(
    page_title="Çarpım Tablosu Alıştırması",
    page_icon="✖️",
    layout="centered"
)

# CSS stil
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Nunito', sans-serif;
    }

    .main {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        min-height: 100vh;
    }

    .soru-kutusu {
        background: rgba(255,255,255,0.05);
        border: 2px solid rgba(255,255,255,0.15);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        backdrop-filter: blur(10px);
        margin: 20px 0;
    }

    .soru-text {
        font-size: 3rem;
        font-weight: 900;
        color: #e2e8f0;
        letter-spacing: 2px;
    }

    .dogru {
        background: linear-gradient(135deg, #22c55e, #16a34a);
        color: white;
        padding: 15px 30px;
        border-radius: 15px;
        font-size: 1.5rem;
        font-weight: 800;
        text-align: center;
        animation: pulse 0.5s ease;
    }

    .yanlis {
        background: linear-gradient(135deg, #ef4444, #dc2626);
        color: white;
        padding: 15px 30px;
        border-radius: 15px;
        font-size: 1.5rem;
        font-weight: 800;
        text-align: center;
    }

    .puan-kutusu {
        background: linear-gradient(135deg, #7c3aed, #6d28d9);
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        color: white;
        font-size: 1.2rem;
        font-weight: 700;
    }

    .baslik {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 900;
        background: linear-gradient(90deg, #60a5fa, #a78bfa, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 10px;
    }

    .alt-baslik {
        text-align: center;
        color: #94a3b8;
        font-size: 1rem;
        margin-bottom: 30px;
    }

    stButton > button {
        border-radius: 12px !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
    }
</style>
""", unsafe_allow_html=True)

# Session state başlat
if "soru" not in st.session_state:
    st.session_state.soru = None
if "dogru_cevap" not in st.session_state:
    st.session_state.dogru_cevap = None
if "puan" not in st.session_state:
    st.session_state.puan = 0
if "toplam" not in st.session_state:
    st.session_state.toplam = 0
if "geri_bildirim" not in st.session_state:
    st.session_state.geri_bildirim = None
if "cevaplandi" not in st.session_state:
    st.session_state.cevaplandi = False
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "max_streak" not in st.session_state:
    st.session_state.max_streak = 0


def yeni_soru(aralik):
    a = random.randint(aralik[0], aralik[1])
    b = random.randint(aralik[0], aralik[1])
    st.session_state.soru = (a, b)
    st.session_state.dogru_cevap = a * b
    st.session_state.geri_bildirim = None
    st.session_state.cevaplandi = False


def cevabi_kontrol(cevap):
    st.session_state.toplam += 1
    st.session_state.cevaplandi = True
    if cevap == st.session_state.dogru_cevap:
        st.session_state.puan += 1
        st.session_state.streak += 1
        if st.session_state.streak > st.session_state.max_streak:
            st.session_state.max_streak = st.session_state.streak
        st.session_state.geri_bildirim = "dogru"
    else:
        st.session_state.streak = 0
        st.session_state.geri_bildirim = "yanlis"


# ── Başlık ──
st.markdown('<div class="baslik">✖️ Çarpım Tablosu</div>', unsafe_allow_html=True)
st.markdown('<div class="alt-baslik">Çarpım tablonu pratik yap ve puanını artır!</div>', unsafe_allow_html=True)

# ── Ayarlar ──
with st.expander("⚙️ Ayarlar", expanded=False):
    aralik = st.select_slider(
        "Sayı aralığı seç:",
        options=list(range(1, 13)),
        value=(1, 10),
        help="Soruların hangi sayılar arasından geleceğini belirler."
    )

# ── İstatistikler ──
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div class="puan-kutusu">
        🏆 Puan<br>
        <span style="font-size:2rem">{st.session_state.puan}/{st.session_state.toplam}</span>
    </div>""", unsafe_allow_html=True)

with col2:
    oran = int((st.session_state.puan / st.session_state.toplam * 100) if st.session_state.toplam > 0 else 0)
    renk = "#22c55e" if oran >= 70 else "#f59e0b" if oran >= 40 else "#ef4444"
    st.markdown(f"""
    <div class="puan-kutusu" style="background: linear-gradient(135deg, {renk}aa, {renk});">
        🎯 Başarı<br>
        <span style="font-size:2rem">%{oran}</span>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="puan-kutusu" style="background: linear-gradient(135deg, #f59e0b, #d97706);">
        🔥 Seri<br>
        <span style="font-size:2rem">{st.session_state.streak} / en fazla {st.session_state.max_streak}</span>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Soru üret ──
if st.session_state.soru is None:
    yeni_soru(aralik)

a, b = st.session_state.soru

# ── Soru Kutusu ──
st.markdown(f"""
<div class="soru-kutusu">
    <div class="soru-text">{a} × {b} = ?</div>
</div>
""", unsafe_allow_html=True)

# ── Cevap girişi ──
if not st.session_state.cevaplandi:
    with st.form("cevap_formu", clear_on_submit=True):
        cevap_input = st.number_input(
            "Cevabını gir:",
            min_value=0,
            max_value=10000,
            step=1,
            label_visibility="collapsed"
        )
        gonder = st.form_submit_button("✅ Kontrol Et", use_container_width=True)

    if gonder:
        cevabi_kontrol(int(cevap_input))
        st.rerun()

# ── Geri Bildirim ──
if st.session_state.geri_bildirim == "dogru":
    st.markdown(f'<div class="dogru">🎉 Harika! {a} × {b} = {st.session_state.dogru_cevap} — Doğru!</div>', unsafe_allow_html=True)
    if st.session_state.streak >= 3:
        st.markdown(f"<center style='color:#f59e0b; font-size:1.3rem; font-weight:800;'>🔥 {st.session_state.streak} doğru seri!</center>", unsafe_allow_html=True)

elif st.session_state.geri_bildirim == "yanlis":
    st.markdown(f'<div class="yanlis">❌ Yanlış! Doğru cevap: {a} × {b} = {st.session_state.dogru_cevap}</div>', unsafe_allow_html=True)

# ── Sonraki Soru ──
if st.session_state.cevaplandi:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("➡️ Sonraki Soru", use_container_width=True):
        yeni_soru(aralik)
        st.rerun()

# ── Sıfırla ──
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔄 Sıfırla", use_container_width=False):
    st.session_state.puan = 0
    st.session_state.toplam = 0
    st.session_state.streak = 0
    st.session_state.max_streak = 0
    yeni_soru(aralik)
    st.rerun()

# ── Çarpım Tablosu Referansı ──
with st.expander("📊 Çarpım Tablosu Referansı"):
    import pandas as pd
    data = {str(i): [i * j for j in range(1, 13)] for i in range(1, 13)}
    df = pd.DataFrame(data, index=range(1, 13))
    df.index.name = "×"
    st.dataframe(df, use_container_width=True)

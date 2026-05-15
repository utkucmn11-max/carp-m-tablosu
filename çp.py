import streamlit as st
import random

st.set_page_config(
    page_title="Çarpım Tablosu Oyunu",
    page_icon="🎯",
    layout="centered"
)

# Session state oluştur
if "score" not in st.session_state:
    st.session_state.score = 0

if "num1" not in st.session_state:
    st.session_state.num1 = random.randint(1, 10)

if "num2" not in st.session_state:
    st.session_state.num2 = random.randint(1, 10)

# Başlık
st.title("🎯 Çarpım Tablosu Öğreniyorum")
st.write("Doğru cevabı yaz ve puan kazan!")

# Soru
st.subheader(
    f"{st.session_state.num1} × {st.session_state.num2} = ?"
)

# Kullanıcı cevabı
answer = st.number_input(
    "Cevabın:",
    step=1,
    format="%d"
)

# Buton
if st.button("Kontrol Et"):

    correct_answer = (
        st.session_state.num1 *
        st.session_state.num2
    )

    if answer == correct_answer:
        st.success("✅ Doğru cevap!")
        st.session_state.score += 1
    else:
        st.error(
            f"❌ Yanlış! Doğru cevap: {correct_answer}"
        )

    # Yeni soru oluştur
    st.session_state.num1 = random.randint(1, 10)
    st.session_state.num2 = random.randint(1, 10)

# Puan
st.markdown("---")
st.subheader(f"🏆 Puan: {st.session_state.score}")

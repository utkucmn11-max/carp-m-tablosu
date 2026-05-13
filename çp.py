import streamlit as st
import time

# Sayfa Ayarları
st.set_page_config(page_title="Hızlı Çarpım Tablosu Öğretici", page_icon="🔢")

st.title("🔢 Çarpım Tablosu Kahramanı Ol!")
st.subheader("Hiç bilmeyenler için en hızlı öğrenme platformu ✨")

# Öğrenme Aşamaları
tab1, tab2, tab3 = st.tabs(["💡 Mantığını Anla", "🏋️ Alıştırma Yap", "🏆 Kendini Sına"])

with tab1:
    st.header("1. Adım: Toplamanın Kısa Yolu")
    st.write("""
    Çarpma aslında sadece **hızlı toplamadır**. 
    Örneğin; $3 \\times 4$ demek, 3 tane 4'ü yan yana koyup toplamak demektir:  
    **4 + 4 + 4 = 12** 🍎🍎🍎🍎 + 🍎🍎🍎🍎 + 🍎🍎🍎🍎
    """)
    
    sayi = st.slider("Hangi sayıyı öğrenmek istersin?", 1, 10, 5)
    st.info(f"Şu an {sayi}'ler basamağına bakıyorsun. Her adımda üzerine {sayi} ekleyerek ilerle!")
    
    for i in range(1, 11):
        st.write(f"👉 {i} tane {sayi} = **{i * sayi}**")

with tab2:
    st.header("2. Adım: Görsel Alıştırma")
    st.write("Sayıların ritmini hisset! 🎵")
    
    col1, col2 = st.columns(2)
    with col1:
        soru_sayi = st.number_input("Bir sayı seç:", 1, 10, 2)
    with col2:
        hedef = st.selectbox("Kaçla çarpalım?", list(range(1, 11)))
    
    if st.button("Sonucu Gör"):
        st.success(f"Cevap: {soru_sayi * hedef} ✅")
        st.balloons()

with tab3:
    st.header("3. Adım: Hız Testi")
    st.write("Bakalım ne kadar hızlısın? ⚡")
    
    if 'score' not in st.session_state:
        st.session_state.score = 0

    import random
    s1 = random.randint(2, 9)
    s2 = random.randint(2, 9)
    
    st.write(f"### Soru: {s1} x {s2} kaçtır?")
    cevap = st.number_input("Cevabını buraya yaz:", min_value=0)
    
    if st.button("Kontrol Et"):
        if cevap == s1 * s2:
            st.session_state.score += 1
            st.balloons()
            st.success(f"Harika! Puanın: {st.session_state.score} ⭐")
        else:
            st.error(f"Üzgünüm, doğru cevap {s1 * s2} olmalıydı. Tekrar dene! 💪")

st.sidebar.markdown("---")
st.sidebar.write("### 💡 Küçük İpuçları")
st.sidebar.info("- 5'lerle çarparken sonuç hep 0 veya 5 ile biter. 🖐️")
st.sidebar.info("- 9'larla çarparken sonuçların rakamları toplamı hep 9'dur! 🧠")
st.sidebar.info("- 0 ile neyi çarparsan çarp, sonuç koca bir 0 olur! 🌪️")
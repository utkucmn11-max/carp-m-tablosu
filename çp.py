import streamlit as st
import random

# Sayfa Ayarları
st.set_page_config(page_title="Hızlı Çarpım Tablosu", page_icon="🔢")

# Hafıza Kontrolü (Sorunun değişmemesi için)
if 's1' not in st.session_state:
    st.session_state.s1 = random.randint(2, 9)
if 's2' not in st.session_state:
    st.session_state.s2 = random.randint(2, 9)
if 'score' not in st.session_state:
    st.session_state.score = 0

st.title("🔢 Çarpım Tablosu Kahramanı")

tab1, tab2, tab3 = st.tabs(["💡 Mantığını Anla", "🏋️ Alıştırma Yap", "🏆 Kendini Sına"])

with tab1:
    st.header("1. Adım: Toplamanın Kısayolu")
    st.write("Çarpma işlemi aslında aynı sayıyı defalarca toplamanın hızlı yoludur.")
    
    sayi = st.slider("Hangi sayıyı öğrenmek istersin?", 1, 10, 5)
    for i in range(1, 11):
        st.write(f"{i} tane {sayi} yanyana gelirse: **{i * sayi}** eder. 🍎")

with tab2:
    st.header("2. Adım: Görsel Deneme")
    c1, c2 = st.columns(2)
    with c1:
        n1 = st.number_input("Sayı 1:", 1, 10, 3)
    with c2:
        n2 = st.number_input("Sayı 2:", 1, 10, 4)
    
    if st.button("Sonucu Hesapla"):
        st.info(f"{n1} x {n2} = {n1*n2}")

with tab3:
    st.header("3. Adım: Hız Testi ⚡")
    st.write(f"### Soru: {st.session_state.s1} x {st.session_state.s2} kaçtır?")
    
    user_answer = st.number_input("Cevabınız:", min_value=0, key="answer_input")
    
    if st.button("Kontrol Et"):
        if user_answer == st.session_state.s1 * st.session_state.s2:
            st.success("Tebrikler! Doğru cevap. 🎉")
            st.session_state.score += 1
            # Yeni soru oluştur
            st.session_state.s1 = random.randint(2, 9)
            st.session_state.s2 = random.randint(2, 9)
            st.rerun() # Sayfayı yenileyerek yeni soruyu getir
        else:
            st.error(f"Hatalı! Tekrar düşünmelisin. 💪")

st.sidebar.metric("Toplam Puanın", st.session_state.score)

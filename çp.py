import streamlit as st
import random

# Sayfa Ayarları
st.set_page_config(page_title="Hızlı Çarpım Tablosu", page_icon="🔢")

# Hafıza Kontrolü: Soruların değişmemesi için session_state kullanıyoruz
if 's1' not in st.session_state:
    st.session_state.s1 = random.randint(2, 9)
if 's2' not in st.session_state:
    st.session_state.s2 = random.randint(2, 9)
if 'puan' not in st.session_state:
    st.session_state.puan = 0

st.title("🔢 Çarpım Tablosunu Şimşek Gibi Öğren!")
st.write(f"### Mevcut Puanın: {st.session_state.puan} ⭐")

# Form Yapısı: Butona basana kadar içeriği dondurur
with st.form(key='soru_formu'):
    st.subheader(f"Soru: {st.session_state.s1} x {st.session_state.s2} kaçtır?")
    
    cevap = st.number_input("Cevabını buraya yaz ve Enter'a bas:", min_value=0, step=1, value=0)
    
    submit_button = st.form_submit_button(label='Kontrol Et ✅')

# Kontrol Mekanizması
if submit_button:
    dogru_sonuc = st.session_state.s1 * st.session_state.s2
    
    if cevap == dogru_sonuc:
        st.success(f"Harikasın! {st.session_state.s1} x {st.session_state.s2} = {dogru_sonuc} doğru! 🎉")
        st.session_state.puan += 1
        # Yeni soru hazırla
        st.session_state.s1 = random.randint(2, 9)
        st.session_state.s2 = random.randint(2, 9)
        st.info("Yeni soruya geçmek için sayfayı yukarıdan aşağı kaydır veya bir sonraki cevaba hazırlan! 🚀")
        st.balloons()
    else:
        st.error(f"Maalesef yanlış! ❌")
        st.warning(f"Doğru cevap: **{st.session_state.s1} x {st.session_state.s2} = {dogru_sonuc}** olmalıydı. 💡")
        st.info("Vazgeçme, tekrar dene! 💪")

# Tabloyu görmek isteyenler için küçük bir rehber
with st.expander("💡 Çarpım Tablosu Rehberini Aç"):
    st.write("Öğrendiğin sayının katlarını buradan kontrol edebilirsin:")
    cols = st.columns(5)
    for i in range(1, 11):
        with cols[(i-1)%5]:
            st.write(f"**{i}'ler**")
            for j in range(1, 11):
                st.text(f"{i} x {j} = {i*j}")

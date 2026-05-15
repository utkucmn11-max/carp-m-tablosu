import streamlit as st
import random
import time

# Sayfa Ayarları
st.set_page_config(page_title="Çarpım Ustası", page_icon="🧠", layout="centered")

# Başlık ve Karşılama
st.title("✨ Çarpım Ustası'na Hoş Geldin! ✨")
st.markdown("---")

# Yan Menü (Sidebar) Seçenekleri
option = st.sidebar.selectbox(
    'Ne yapmak istersin?',
    ('Öğrenme Paneli 📖', 'Kendini Test Et! 🎯')
)

if option == 'Öğrenme Paneli 📖':
    st.header("Sayıları Keşfet 🔢")
    sayi = st.slider("Hangi sayıyı öğrenmek istersin?", 1, 10, 5)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(f"{sayi}'ler Tablosu")
        for i in range(1, 11):
            st.write(f"**{sayi} x {i} = {sayi * i}**")
            
    with col2:
        # Görsel bir grafik ekleyerek görsel hafızayı destekleyebiliriz
        st.subheader("İlerleme Grafiği")
        grafik_verisi = [sayi * i for i in range(1, 11)]
        st.line_chart(grafik_verisi)

elif option == 'Kendini Test Et! 🎯':
    st.header("Hız ve Zeka Testi 🚀")
    
    # Session state ile skor tutma
    if 'skor' not in st.session_state:
        st.session_state.skor = 0
    if 'soru_a' not in st.session_state:
        st.session_state.soru_a = random.randint(1, 10)
        st.session_state.soru_b = random.randint(1, 10)

    st.write(f"### Soru: **{st.session_state.soru_a} x {st.session_state.soru_b} = ?**")
    
    cevap = st.number_input("Cevabını buraya yaz:", min_value=0, step=1, value=None, placeholder="...")
    
    if st.button("Kontrol Et ✅"):
        dogru_cevap = st.session_state.soru_a * st.session_state.soru_b
        if cevap == dogru_cevap:
            st.success("Harika! Doğru cevap. 🎉")
            st.session_state.skor += 1
            # Yeni soru üret
            st.session_state.soru_a = random.randint(1, 10)
            st.session_state.soru_b = random.randint(1, 10)
            time.sleep(1) # Kısa bir bekleme
            st.rerun()
        else:
            st.error(f"Maalesef yanlış. Doğru cevap {dogru_cevap} olmalıydı. 🤔")
            st.session_state.skor = 0 # Yanlışta skoru sıfırla (opsiyonel)

    st.metric(label="Mevcut Skorun 🏆", value=st.session_state.skor)
    
    if st.button("Skoru Sıfırla 🔄"):
        st.session_state.skor = 0
        st.rerun()

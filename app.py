import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Pendeteksi Bakat & Jurusan", page_icon="🎓", layout="centered")

st.title("🎓 Tes Bakat & Rekomendasi Jurusan")
st.write("Jawab pertanyaan berikut untuk mengetahui jurusan yang paling cocok dengan dirimu!")

st.divider()

# 2. Form Pertanyaan
with st.form("quiz_form"):
    st.subheader("📋 Pertanyaan Minat & Kebiasaan")
    
    q1 = st.radio(
        "1. Kegiatan mana yang paling kamu sukai di waktu luang?",
        ["Mencoba aplikasi/game baru atau mengotak-atik barang elektronik",
         "Membuat karya seni, menulis cerita, atau desain visual",
         "Mengatur keuangan, jualan online, atau buat strategi event",
         "Membaca berita, diskusi sosial, atau bantu teman curhat"]
    )
    
    q2 = st.radio(
        "2. Mata pelajaran apa yang paling kamu nikmati?",
        ["Matematika / Fisika / Informatika",
         "Seni Budaya / Bahasa",
         "Ekonomi / Akuntansi",
         "Sosiologi / Sejarah / PPKn"]
    )
    
    q3 = st.radio(
        "3. Bagaimana cara belajarmu yang paling efektif?",
        ["Praktek langsung dan memecahkan masalah logika",
         "Visual dengan gambar, warna, atau kebebasan berekspresi",
         "Diskusi kelompok, simulasi proyek, atau analisis studi kasus",
         "Membaca, mendengarkan cerita, dan memahami konsep manusia"]
    )
    
    # Tombol submit form
    submitted = st.form_submit_button("🎯 Lihat Hasil Rekomendasi")

# 3. Logika Perhitungan Skor & Output
if submitted:
    # Inisialisasi Skor
    scores = {
        "Teknik & IT": 0,
        "Seni & Desain": 0,
        "Bisnis & Ekonomi": 0,
        "Sosial & Hukum": 0
    }
    
    # Hitung Skor Q1
    if "aplikasi" in q1: scores["Teknik & IT"] += 3
    elif "seni" in q1: scores["Seni & Desain"] += 3
    elif "keuangan" in q1: scores["Bisnis & Ekonomi"] += 3
    elif "berita" in q1: scores["Sosial & Hukum"] += 3
        
    # Hitung Skor Q2
    if "Matematika" in q2: scores["Teknik & IT"] += 3
    elif "Seni" in q2: scores["Seni & Desain"] += 3
    elif "Ekonomi" in q2: scores["Bisnis & Ekonomi"] += 3
    elif "Sosiologi" in q2: scores["Sosial & Hukum"] += 3
        
    # Hitung Skor Q3
    if "Praktek" in q3: scores["Teknik & IT"] += 2
    elif "Visual" in q3: scores["Seni & Desain"] += 2
    elif "Diskusi" in q3: scores["Bisnis & Ekonomi"] += 2
    elif "Membaca" in q3: scores["Sosial & Hukum"] += 2

    # Konversi ke DataFrame
    df = pd.DataFrame(list(scores.items()), columns=['Jurusan', 'Skor'])
    df['Persentase'] = (df['Skor'] / df['Skor'].sum()) * 100
    
    # Cari rekomendasi tertinggi
    top_jurusan = df.sort_values(by='Skor', ascending=False).iloc[0]['Jurusan']
    
    st.divider()
    st.success(f"🎉 Jurusan yang Paling Cocok Untukmu: **{top_jurusan}**")
    
    # Tampilkan Grafik
    st.subheader("📊 Grafik Persentase Kecocokan")
    fig = px.pie(df, values='Persentase', names='Jurusan', hole=0.4,
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig, use_container_width=True)
    
    # Detail Prospek Karir
    st.subheader("🚀 Prospek Karir Utama")
    prospek = {
        "Teknik & IT": "Software Engineer, Data Analyst, Network Administrator, Systems Analyst.",
        "Seni & Desain": "UI/UX Designer, Graphic Designer, Animator, Content Creator.",
        "Bisnis & Ekonomi": "Entrepreneur, Marketing Strategist, Financial Analyst, HR Manager.",
        "Sosial & Hukum": "Diplomat, Konsultan Hukum, Journalist, Public Relations Specilist."
    }
    st.info(prospek[top_jurusan])
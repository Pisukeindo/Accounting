import streamlit as st
import requests


def penjualan_harian():

    def format_rupiah(angka):
        angka_str = str(angka)
        ribuan = ""
        n = len(angka_str)
        for i, digit in enumerate(angka_str[::-1]):
            ribuan = digit + ribuan
            if (i + 1) % 3 == 0 and i != n - 1:
                ribuan = "." + ribuan
        return "Total Pendapatan: Rp " + ribuan

    # URL layanan web Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbwcTkKh4yTQyQVZiSTmtuSVbzEuB4h-ceLEwuoaajbZSKnYTj_mOwRnq37HgSP3FmICrw/exec"

    # Tampilan Streamlit
    st.write("Masukkan Data:")

    # Kolom input
    tanggal = st.date_input("Tanggal")
    tanggal_str = tanggal.strftime('%Y-%m-%d')
    outlet = st.selectbox("Pilih Outlet", ["Pogung Pagi", "Pogung Sore", "Pandega Mixue Pagi", "Pandega Mixue Sore", "Pandega Massiva", "UNY Pagi", "UNY Sore", "Terban", "Jl. Persatuan"])
    pisang_aroma_masuk = st.number_input("Pisang Aroma Masuk", min_value=0)
    pisang_aroma_bonus = st.number_input("Pisang Aroma Bonus", min_value=0)
    pisang_aroma_rusak = st.number_input("Pisang Aroma Rusak", min_value=0)
    pisang_aroma_sisa = st.number_input("Pisang Aroma Sisa", min_value=0)
    pisang_aroma_terjual = st.number_input("Pisang Aroma Terjual", min_value=0)
    cheese_roll_masuk = st.number_input("Cheese Roll Masuk", min_value=0)
    cheese_roll_bonus = st.number_input("Cheese Roll Bonus", min_value=0)
    cheese_roll_rusak = st.number_input("Cheese Roll Rusak", min_value=0)
    cheese_roll_sisa = st.number_input("Cheese Roll Sisa", min_value=0)
    cheese_roll_terjual = st.number_input("Cheese Roll Terjual", min_value=0)
    qris = st.number_input("QRIS", min_value=0)
    tunai = st.number_input("Tunai", min_value=0)
    pengeluaran = st.number_input("Pengeluaran", min_value=0)
    total = qris + tunai - pengeluaran
    jumlah_rupiah = format_rupiah(total)

    # Display the data in a table
    data = {
        "Tanggal": [tanggal_str],
        "Outlet": [outlet],
        "Pisang Aroma Masuk": [pisang_aroma_masuk],
        "Pisang Aroma Bonus": [pisang_aroma_bonus],
        "Pisang Aroma Rusak": [pisang_aroma_rusak],
        "Pisang Aroma Sisa": [pisang_aroma_sisa],
        "Pisang Aroma Terjual": [pisang_aroma_terjual],
        "Cheese Roll Masuk": [cheese_roll_masuk],
        "Cheese Roll Bonus": [cheese_roll_bonus],
        "Cheese Roll Rusak": [cheese_roll_rusak],
        "Cheese Roll Sisa": [cheese_roll_sisa],
        "Cheese Roll Terjual": [cheese_roll_terjual],
        "QRIS": [qris],
        "Tunai": [tunai],
        "Pengeluaran": [pengeluaran],
        "Total": [total],
        "Jumlah Rupiah": [jumlah_rupiah],
        "Disetor": [disetor]
    }

    st.table(data)

    if st.button("Kirim Data"):
        # Membangun URL dengan parameter query string
        url = f"{apps_script_url}?Tanggal={tanggal_str}&Outlet={outlet}&pisang_aroma_masuk={pisang_aroma_masuk}&pisang_aroma_bonus={pisang_aroma_bonus}&pisang_aroma_rusak={pisang_aroma_rusak}&pisang_aroma_sisa={pisang_aroma_sisa}&pisang_aroma_terjual={pisang_aroma_terjual}&cheese_roll_masuk={cheese_roll_masuk}&cheese_roll_bonus={cheese_roll_bonus}&cheese_roll_rusak={cheese_roll_rusak}&cheese_roll_sisa={cheese_roll_sisa}&cheese_roll_terjual={cheese_roll_terjual}&qris={qris}&tunai={tunai}&pengeluaran={pengeluaran}&total={total}&disetor={disetor}"

        # Mengirim permintaan HTTP GET ke Apps Script
        response = requests.get(url)

        if response.status_code == 200:
            st.success("Data berhasil dikirim!")
        else:
            st.error("Terjadi kesalahan saat mengirim data.")


if __name__ == "__main__":
    penjualan_harian()

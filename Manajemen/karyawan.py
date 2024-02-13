import streamlit as st
import requests
import locale

def karyawan():

    def format_rupiah(angka, with_prefix=False, desimal=2):
    locale.setlocale(locale.LC_NUMERIC, 'IND')
    rupiah = locale.format("%.*f", (desimal, angka), True)
    if with_prefix:
        return "Rp. {}".format(rupiah)
    return rupiah
        
    # URL layanan web Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbzNaLqTormZHk8lz9KEPiWxLUv1xp3-sxEXNELN8ejbNaWWT9O9j7EgkfgoBRfXp9NIvQ/exec"
    # Tampilan Streamlit
    st.title("KARYAWAN")
 
    # Kolom input
    tanggal = st.date_input("Tanggal")
    tanggal_str = tanggal.strftime('%Y-%m-%d')
    nama = st.text_input("Nama")
    posisi = st.text_input("Posisi")
    kontak = st.text_input("Kontak")
    alamat = st.text_input("Alamat")
    gaji = st.number_input("Gaji", min_value=0)
    jumlah_rupiah = format_rupiah(gaji)
    st.write(f"{jumlah_rupiah}")
    
    

    if st.button("Kirim Data"):
        # Membangun URL dengan parameter query string
        url = f"{apps_script_url}?nama={nama}&posisi={posisi}&kontak={kontak}&alamat={alamat}&gaji={gaji}&tanggal={tanggal_str}"

        # Mengirim permintaan HTTP GET ke Apps Script
        response = requests.get(url)
        
        if response.status_code == 200:
            st.success("Data berhasil dikirim!")
        else:
            st.error("Terjadi kesalahan saat mengirim data.")

if __name__ == "__main__":
    karyawan()

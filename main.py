import streamlit as st
from akun import login
from Manajemen import pertambahan_aset,suplier,karyawan
from input import penjualan_harian
from Laporan import output
# Inisialisasi status login
if "username" not in st.session_state:
    st.session_state.username = None

# Menampilkan halaman sesuai dengan status login
if st.session_state.username is None:
    login()
else:
    selected_menu = st.sidebar.radio(
        "MENU:",
        ["Input Data", "Laporan Harian", "Laporan Manajemen"]

    if selected_menu == "Input Data":
        selected_page = st.sidebar.radio(
            "Input Data Harian:",
            ["Penjualan Harian", "Produksi Harian", "Suplier", "Pertambahan Aset", "Karyawan"]
        )
        if selected_page == "Penjualan Harian":
            st.title("Penjualan Harian")
            penjualan_harian.penjualan_harian()
        elif selected_page == "Produksi Harian":
            st.title("Produksi Harian")
            produksi_harian.produksi_harian()
        elif selected_page == "Suplier":
            suplier.suplier()
        elif selected_page == "Pertambahan Aset":
            pertambahan_aset.pertambahan_aset()
        elif selected_page == "Karyawan":
            karyawan.karyawan()
        

    elif selected_menu == "Laporan Harian":
        selected_laporan = st.sidebar.radio(
            "Laporan Harian:",
            ["Bahan Baku Harian","Produksi Harian", "Pengeluaran Harian", "Penjualan Harian", "Stok Bahan Baku", "Quality Control"])
        if selected_laporan == "Bahan Baku Harian":
            output.laporan("bahan_baku_harian")
        elif selected_laporan == "Pengeluaran Harian":
            output.laporan("pengeluaran_harian")
        elif selected_laporan == "Produksi Harian":
            output.laporan("produksi_harian")
        elif selected_laporan == "Penjualan Harian":
            output.laporan("penjualan_harian")
        elif selected_laporan == "Stok Bahan Baku":
            output.laporan("stok_bahan_baku")
        elif selected_laporan == "Quality Control":
            output.laporan("qc")


    elif selected_menu == "Laporan Manajemen":
        selected_laporan = st.sidebar.radio(
            "Laporan Manajemen:",
            ["Suplier", "Karyawan", "Pertambahan Aset"])
        if selected_laporan == "Pertambahan Aser":
            output.laporan("Pertambahan Aset")
        elif selected_laporan == "Suplier":
            output.laporan("suplier")
        elif selected_laporan == "Karyawan":
            output.laporan("karyawan")
     

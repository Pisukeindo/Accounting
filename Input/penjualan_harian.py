import streamlit as st
import pandas as pd

def penjualan_harian():

    # Streamlit UI
    st.write("Masukkan Data:")

    # Create an empty DataFrame to store the data
    data_columns = ["Tanggal", "Outlet", "Pisang Aroma Masuk", "Pisang Aroma Bonus", "Pisang Aroma Rusak",
                    "Pisang Aroma Sisa", "Pisang Aroma Terjual", "Cheese Roll Masuk", "Cheese Roll Bonus",
                    "Cheese Roll Rusak", "Cheese Roll Sisa", "Cheese Roll Terjual", "QRIS", "Tunai",
                    "Pengeluaran", "Total", "Disetor"]

    data = pd.DataFrame(columns=data_columns)

    # Create a table to input data
    input_table = st.empty()

    # Input fields
    tanggal = st.date_input("Tanggal")
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
    disetor = st.number_input("Disetor", min_value=0)

    # Button to add a row to the input table
    if st.button("Tambah Baris"):
        data = data.append({
            "Tanggal": tanggal,
            "Outlet": outlet,
            "Pisang Aroma Masuk": pisang_aroma_masuk,
            "Pisang Aroma Bonus": pisang_aroma_bonus,
            "Pisang Aroma Rusak": pisang_aroma_rusak,
            "Pisang Aroma Sisa": pisang_aroma_sisa,
            "Pisang Aroma Terjual": pisang_aroma_terjual,
            "Cheese Roll Masuk": cheese_roll_masuk,
            "Cheese Roll Bonus": cheese_roll_bonus,
            "Cheese Roll Rusak": cheese_roll_rusak,
            "Cheese Roll Sisa": cheese_roll_sisa,
            "Cheese Roll Terjual": cheese_roll_terjual,
            "QRIS": qris,
            "Tunai": tunai,
            "Pengeluaran": pengeluaran,
            "Total": qris + tunai - pengeluaran,
            "Disetor": disetor
        }, ignore_index=True)

    # Display the input data in a table
    input_table.table(data)

if __name__ == "__main__":
    penjualan_harian()


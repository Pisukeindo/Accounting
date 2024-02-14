import streamlit as st
import requests

def penjualan_harian():

    # URL for the Google Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbwcTkKh4yTQyQVZiSTmtuSVbzEuB4h-ceLEwuoaajbZSKnYTj_mOwRnq37HgSP3FmICrw/exec"

    # Streamlit UI
    st.write("Masukkan Data:")

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

    # Display the input data in an HTML table
    st.markdown("""
        <table>
            <tr>
                <th>Tanggal</th>
                <th>Outlet</th>
                <th>Pisang Aroma Masuk</th>
                <th>Pisang Aroma Bonus</th>
                <th>Pisang Aroma Rusak</th>
                <th>Pisang Aroma Sisa</th>
                <th>Pisang Aroma Terjual</th>
                <th>Cheese Roll Masuk</th>
                <th>Cheese Roll Bonus</th>
                <th>Cheese Roll Rusak</th>
                <th>Cheese Roll Sisa</th>
                <th>Cheese Roll Terjual</th>
                <th>QRIS</th>
                <th>Tunai</th>
                <th>Pengeluaran</th>
                <th>Disetor</th>
            </tr>
            <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
        </table>
    """.format(tanggal, outlet, pisang_aroma_masuk, pisang_aroma_bonus, pisang_aroma_rusak,
               pisang_aroma_sisa, pisang_aroma_terjual, cheese_roll_masuk, cheese_roll_bonus,
               cheese_roll_rusak, cheese_roll_sisa, cheese_roll_terjual, qris, tunai, pengeluaran,
               disetor), unsafe_allow_html=True)

    # Button to send data
    if st.button("Kirim Data"):
        # Build the URL with query parameters
        url = f"{apps_script_url}?Tanggal={tanggal}&Outlet={outlet}&pisang_aroma_masuk={pisang_aroma_masuk}&pisang_aroma_bonus={pisang_aroma_bonus}&pisang_aroma_rusak={pisang_aroma_rusak}&pisang_aroma_sisa={pisang_aroma_sisa}&pisang_aroma_terjual={pisang_aroma_terjual}&cheese_roll_masuk={cheese_roll_masuk}&cheese_roll_bonus={cheese_roll_bonus}&cheese_roll_rusak={cheese_roll_rusak}&cheese_roll_sisa={cheese_roll_sisa}&cheese_roll_terjual={cheese_roll_terjual}&qris={qris}&tunai={tunai}&pengeluaran={pengeluaran}&disetor={disetor}"

        # Send an HTTP GET request to the Apps Script
        response = requests.get(url)

        # Display success or error message
        if response.status_code == 200:
            st.success("Data berhasil dikirim!")
        else:
            st.error("Terjadi kesalahan saat mengirim data.")

if __name__ == "__main__":
    penjualan_harian()

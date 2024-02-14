import streamlit as st
import requests

def penjualan_harian():

    # URL for the Google Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbwcTkKh4yTQyQVZiSTmtuSVbzEuB4h-ceLEwuoaajbZSKnYTj_mOwRnq37HgSP3FmICrw/exec"

    # Streamlit UI
    st.write("Masukkan Data:")

    # Display the input data in a dynamic HTML table
    st.markdown("""
        <table id="data-table">
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
                <th>Total</th>
                <th>Disetor</th>
            </tr>
            <tr>
                <td><input type="date" id="tanggal"></td>
                <td>
                    <select id="outlet">
                        <option value="Pogung Pagi">Pogung Pagi</option>
                        <option value="Pogung Sore">Pogung Sore</option>
                        <!-- Add other options here -->
                    </select>
                </td>
                <td><input type="number" id="pisang_aroma_masuk" min="0"></td>
                <td><input type="number" id="pisang_aroma_bonus" min="0"></td>
                <td><input type="number" id="pisang_aroma_rusak" min="0"></td>
                <td><input type="number" id="pisang_aroma_sisa" min="0"></td>
                <td><input type="number" id="pisang_aroma_terjual" min="0"></td>
                <td><input type="number" id="cheese_roll_masuk" min="0"></td>
                <td><input type="number" id="cheese_roll_bonus" min="0"></td>
                <td><input type="number" id="cheese_roll_rusak" min="0"></td>
                <td><input type="number" id="cheese_roll_sisa" min="0"></td>
                <td><input type="number" id="cheese_roll_terjual" min="0"></td>
                <td><input type="number" id="qris" min="0"></td>
                <td><input type="number" id="tunai" min="0"></td>
                <td><input type="number" id="pengeluaran" min="0"></td>
                <td><span id="total">0</span></td>
                <td><input type="number" id="disetor" min="0"></td>
            </tr>
        </table>
        <button onclick="addRow()">Tambah Baris</button>
        <button onclick="kirimData()">Kirim Data</button>

        <script>
            function addRow() {
                var table = document.getElementById("data-table");
                var row = table.insertRow();

                var inputFields = [
                    "tanggal", "outlet", "pisang_aroma_masuk", "pisang_aroma_bonus", "pisang_aroma_rusak",
                    "pisang_aroma_sisa", "pisang_aroma_terjual", "cheese_roll_masuk", "cheese_roll_bonus",
                    "cheese_roll_rusak", "cheese_roll_sisa", "cheese_roll_terjual", "qris", "tunai",
                    "pengeluaran", "total", "disetor"
                ];

                for (var i = 0; i < inputFields.length; i++) {
                    var cell = row.insertCell();
                    var input = document.createElement("input");
                    input.type = (inputFields[i].includes("date")) ? "date" : "number";
                    input.id = inputFields[i] + "_" + table.rows.length;
                    input.min = 0;
                    cell.appendChild(input);
                }
            }

            function kirimData() {
                var url = "{apps_script_url}?";

                var inputFields = [
                    "tanggal", "outlet", "pisang_aroma_masuk", "pisang_aroma_bonus", "pisang_aroma_rusak",
                    "pisang_aroma_sisa", "pisang_aroma_terjual", "cheese_roll_masuk", "cheese_roll_bonus",
                    "cheese_roll_rusak", "cheese_roll_sisa", "cheese_roll_terjual", "qris", "tunai",
                    "pengeluaran", "total", "disetor"
                ];

                for (var i = 0; i < inputFields.length; i++) {
                    var input = document.getElementById(inputFields[i] + "_" + table.rows.length);
                    url += inputFields[i] + "=" + input.value + "&";
                }

                // Remove the last "&" from the URL
                url = url.slice(0, -1);

                var response = fetch(url);

                if (response.status === 200) {
                    alert("Data berhasil dikirim!");
                } else {
                    alert("Terjadi kesalahan saat mengirim data.");
                }
            }
        </script>
    """)

if __name__ == "__main__":
    penjualan_harian()

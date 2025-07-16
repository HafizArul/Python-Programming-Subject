try:
    angka = input("Masukkan angka: ")
    hasil =  10/angka
    print("hasil 10/",angka,": ",hasil)

except ValueError as ve:
    print(f"Hasil error! {ve}")

except TypeError as te:
    print(f"Hasil error! {te}")

except Exception as e:
    print(f"Hasil error! {e}")


# Streamlit
import streamlit as st
st.write("Hello")
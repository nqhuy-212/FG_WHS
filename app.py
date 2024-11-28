import streamlit as st
import pandas as pd
import time

# Initialize a global DataFrame
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["QR Box"])

# Define the callback function
def add_box():
    qr_box = st.session_state.get("qr_box", "")
    if qr_box:  # Only add if not empty
        # Append to the DataFrame in session_state
        st.session_state.df = pd.concat(
            [st.session_state.df, pd.DataFrame({"QR Box": [qr_box]})],
            ignore_index=True
        )
        # Clear the input field
        st.session_state.qr_box = ""

# Create inputs
qr_box = st.text_input("QR thùng", key="qr_box", on_change=add_box)  # Use key to store the input in session_state
st.text_input("Quét mã Pallet")
st.text_input("Quét mã Rack")

# Display the DataFrame
st.write("Current Data:")
st.dataframe(st.session_state.df)

# Add a submit button
submitted = st.button("Lưu")
if submitted:
    st.success("Lưu thành công!")

# Add a clear button to reset the DataFrame
clear = st.button("Xóa")
if clear:
    st.session_state.df = pd.DataFrame(columns=["QR Box"])  # Reset to an empty DataFrame
    st.success("Dữ liệu đã được xóa!")
    st.experimental_rerun()  # Refresh the app to reflect changes


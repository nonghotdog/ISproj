import streamlit as st
import numpy as np
import pandas as pd

# text

st.title("Intelligent System Project")
st.header("header")
st.subheader("subheader")
st.text("text //(Plain Text) //ไม่ Markdown || HTML")

st.header("st.write")
st.text("st.write(*args, unsafe_allow_html=False, **kwargs)")


# status
st.info("info")
st.success("success")
st.warning("warning")
st.error("error")
excepted = ZeroDivisionError("Trying to divide by Zero")
st.exception(excepted) # ข้อยกเว้นที่สร้างขึ้นในบรรทัดก่อนหน้า
def get_number():
    try:
        number = int(st.text_input("ใส่เลข"))
        st.write(f"➥ {number}")
    except ValueError as e:
        st.exception(ValueError("กรอกตัวเลข"))
get_number()

# write
st.write("write //(หลายformat)")
st.write(range(0, 127))

# [diff] .write && .dataframe
st.write(pd.read_csv('data.csv')) # can't interact
st.dataframe(pd.read_csv('data.csv')) # interact

# [diff] .DataFrame && .table
st.dataframe(  # interact
    pd.DataFrame(
        np.random.randn(10, 5),
        columns=('Col %d' % i for i in range(5))
    ).style.highlight_max(axis=0)
)
st.table( # can't interact
    pd.DataFrame(
        np.random.randn(10, 5),
        columns=('Col %d' % i for i in range(5))
    ).style.highlight_min(axis=0)
)

# ex. chart visualization
randomValueChart = np.random.rand(20, 3)
st.line_chart(
    pd.DataFrame(
        columns = ['a', 'b', 'c']
    )
)
st.table(
    pd.DataFrame(
        randomValueChart
    )
)

if st.button('Click'):
    st.text('Clicked! Clicked !! (write)')
    st.text('Clicked! Clicked !! (text)')

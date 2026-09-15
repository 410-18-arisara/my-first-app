import streamlit as st

st.markdown("# :red[🏋️ คำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคูณ เพื่อเช็คสุขภาพเบื้องต้น")

Weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):", min_value=1.0, value=1.0)
height_cm = st.number_input("กรอกน้ำส่วนสูงของคุณ (เซนติเมตร):", min_value=1.0, value=1.0)

if st.button("คำนวณค่า BMI 🎯"):
      # แปลงส่วนสูงจาก cm เป็น เมตร แล้วคำนวณ BMI
      height_m = height_cm / 100
      bmi = Weight / (height_m ** 2)

      st.write("---")
      st.header(f"ค่า BMI ของคุณคือ: **{bmi: .2f}**")

           if bmi < 18.5:
              st.warning(" คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
           elif bmi < 23.0:
              st.success = "สุขภาพดี"
           elif bmi < 25.0:
              st.info = "ท้วม"
           else:
              st.error = "อ้วน"

st.divider()
st.write("นางสาวอริสรา ไทยทัตกุล เลขที่ 18 ม.4/10")

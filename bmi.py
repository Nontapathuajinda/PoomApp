import streamlit as st
st.set_page_config(page_title="Nontapat")
st.title("Bmi Calculation")
n=st.number_input("นํ้าหนัก")
b=st.number_input("ส่วนสูง",step=1,format="%d")
if st.button("Check") :
    bmi=n/(b/100)**2
    st.write(bmi)
    if bmi < 18.5 :
        st.info("นํ้าหนักตํ่ากว่าเกณฑ์")
        st.warning("เสื่องโรคขาดสารอาหาร")
        st.image("1.png")
    elif bmi < 23 :
        st.success("นํ้าหนักสมส่วน")
        st.success("โอกาสมีโรคแทรกซ้อนน้อย")
        st.image("2.png")
    elif bmi < 25 :
        st.warning("นํ้าหนักเกินมาตรฐาน")
        st.warning("ภาวะนํ้าหนักเกินเริ่มต้น")
        st.image("3.png")
    elif bmi < 30 :
        st.error("นํ็าหนักอยู่ในเกณฑ์อ้วน")
        st.warning("ภาวะนํ็าหนักเกินมากระยะอ้วนเริ่มต้น")
        st.image("444.png")
    else:
        st.error("นํ้าหนักอยู่ในเกณฑ์อ้วนมาก")
        st.warning("ภาวะนํ้าหนักเกินมากโรคอ้วน")
        st.image("4.png")


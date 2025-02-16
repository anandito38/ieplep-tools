from function import *

# st.set_page_config(page_title="IFLAB - TOOLS", page_icon="🔥")
st.set_page_config(page_title="IFLAB - TOOLS")
st.title("IFLAB - TOOLS :open_book:")

uploaded_file = st.file_uploader("Upload DOCX or IPYNB file", type=["docx", "ipynb"])

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1]
    
    if file_extension == "docx":
        if st.button("Convert DOCX to PDF"):
            pdf_data = convert_docx_to_pdf(uploaded_file)
            st.success("DOCX conversion successful!")
            st.download_button(label="Download PDF", data=pdf_data, file_name="converted.pdf", mime="application/pdf")
    
    elif file_extension == "ipynb":
        if st.button("Convert IPYNB to PDF"):
            pdf_data = convert_ipynb_to_pdf(uploaded_file)
            st.success("IPYNB conversion successful!")
            st.download_button(label="Download PDF", data=pdf_data, file_name="converted.pdf", mime="application/pdf")
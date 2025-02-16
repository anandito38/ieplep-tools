from library import *

def convert_docx_to_pdf(docx_file):
    doc = Document(docx_file)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    for para in doc.paragraphs:
        pdf.multi_cell(0, 10, para.text)
        pdf.ln()
    
    pdf_bytes = BytesIO()
    pdf.output(pdf_bytes, dest='S')
    return pdf_bytes.getvalue()

def convert_ipynb_to_pdf(ipynb_file):
    notebook_content = nbformat.read(ipynb_file, as_version=4)
    c = Config()
    pdf_exporter = PDFExporter(config=c)
    pdf_data, _ = pdf_exporter.from_notebook_node(notebook_content)
    return pdf_data
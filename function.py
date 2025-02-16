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
    
    latex_content, resources = pdf_exporter.from_notebook_node(notebook_content)

    tex_filename = "notebook.tex"
    with open(tex_filename, "w", encoding="utf-8") as f:
        f.write(latex_content)

    pdf_filename = "notebook.pdf"
    try:
        subprocess.run(["tectonic", tex_filename], check=True)
    except FileNotFoundError:
        raise RuntimeError("Tectonic (tex2pdf) tidak ditemukan. Pastikan tersedia di environment!")

    with open(pdf_filename, "rb") as pdf_file:
        pdf_data = pdf_file.read()

    os.remove(tex_filename)
    os.remove(pdf_filename)

    return pdf_data
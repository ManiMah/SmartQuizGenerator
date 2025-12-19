import pdfplumber as pp

def extract_pdf(file):
    text=""
    with pp.open(file) as pdf:
        for page in pdf.pages:
            text+=page.extract_text()
    return text

def extract_txt(file):
    return file.getvalue().decode("utf-8")

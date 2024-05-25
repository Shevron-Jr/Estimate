from pdf2docx import Converter

def convert_pdf_to_docx(pdf_file, docx_file):
    # Create a Converter object
    cv = Converter(pdf_file)
    # Convert PDF to DOCX
    cv.convert(docx_file, start=0, end=None)
    # Close the Converter object
    cv.close()
    print(f"Converted {pdf_file} to {docx_file}")

# Specify the input PDF file and the output DOCX file
pdf_file = '/Users/oluwasegunmohammed/Downloads/Zainab Resume.pdf'
docx_file = '/Users/oluwasegunmohammed/Downloads/Zainab Resume.docx'

# Convert the PDF to DOCX
convert_pdf_to_docx(pdf_file, docx_file)

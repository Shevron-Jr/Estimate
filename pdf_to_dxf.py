# Converting pdf to dxf file (Inkscape), for easy parsing

import subprocess
import os

def convert_pdf_to_dxf(pdf_file):
    # Define the output DXF file
    dxf_file = os.path.splitext(pdf_file)[0] + '.dxf'
    
    # Run the Inkscape command
    subprocess.run(['/Applications/Inkscape.app/Contents/MacOS/inkscape', pdf_file, '--export-filename=' + dxf_file], check=True)
    
    print(f"Converted {pdf_file} to {dxf_file}")

# Specify the input PDF file
pdf_file = '/Users/oluwasegunmohammed/Downloads/Peterson BIDDING Plans 4.4.24.pdf'

# Convert the PDF to DXF
convert_pdf_to_dxf(pdf_file)

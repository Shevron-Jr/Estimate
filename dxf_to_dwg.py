import subprocess
import os

def convert_dxf_to_dwg(dxf_file):
    # Define the output DWG file
    dwg_file = os.path.abspath(os.path.splitext(dxf_file)[0] + '.dwg')
    
    # Define the path to the ODA File Converter executable
    oda_converter_path = '/Applications/ODAFileConverter.app/Contents/MacOS/ODAFileConverter'
    
    # Define the parameters for the ODA File Converterpyth
    input_dir = os.path.abspath(os.path.dirname(dxf_file))
    output_dir = os.path.abspath(os.path.dirname(dwg_file))
    input_format = 'DXF'
    output_format = 'DWG'
    version = 'ACAD2013'  # Specify the desired DWG version

    # Print paths for debugging
    print(f"ODA Converter Path: {oda_converter_path}")
    print(f"Input Directory: {input_dir}")
    print(f"Output Directory: {output_dir}")
    print(f"Input File: {dxf_file}")
    print(f"Output File: {dwg_file}")

    # Run the ODA File Converter command
    subprocess.run([
        oda_converter_path, 
        input_dir, 
        output_dir, 
        input_format, 
        output_format, 
        version
    ], check=True)
    
    print(f"Converted {dxf_file} to {dwg_file}")

# Specify the input DXF file
dxf_file = '/Users/oluwasegunmohammed/Downloads/Peterson BIDDING Plans 4.4.24.dxf'

# Convert the DXF to DWG
convert_dxf_to_dwg(dxf_file)

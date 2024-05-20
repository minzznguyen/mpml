import nbformat

# Load the Jupyter notebook
file_path = '/Users/jamesnguyen/SchoolResources/AI/image_recognition_project/C2W1A1/C2_W1_Assignment.ipynb'
with open(file_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Extract and concatenate all code cells
code_cells = [cell['source'] for cell in nb.cells if cell.cell_type == 'code']
python_code = '\n\n'.join(code_cells)

# Save the extracted code to a Python file
output_path = '/Users/jamesnguyen/SchoolResources/AI/image_recognition_project/C2W1A1/C2_W1_Assignment.py'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(python_code)

output_path

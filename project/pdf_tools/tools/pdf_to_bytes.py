def pdf_to_bytes(pdf_file_path):
    with open(pdf_file_path, 'rb') as f:
        pdf_bytes = f.read()
    return pdf_bytes



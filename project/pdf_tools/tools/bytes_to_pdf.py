from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from pdf_to_bytes import pdf_to_bytes

def bytes_to_pdf(pdf_bytes, filename):
    # Create a canvas object from the bytes
    pdf_buffer = BytesIO(pdf_bytes)
    pdf = canvas.Canvas(pdf_buffer, pagesize=letter)

    # Set font and write text to the PDF
    pdf.setFont('Helvetica', 12)
    pdf.drawString(100, 750, 'Test')

    # Save the PDF to a file
    with open('../lab/' + filename, 'wb') as f:
        f.write(pdf_buffer.getvalue())

    # Return the PDF bytes
    return pdf_buffer.getvalue()
# Load the bytes of your PDF file into memory
# with open('../lab/test.pdf', 'rb') as f:
#     pdf_bytes = f.read()

# Create a new PDF file with the data from the bytes


my_bytes = pdf_to_bytes('../lab/test.pdf')
bytes_to_pdf(my_bytes,'output.pdf')
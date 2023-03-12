import io
import os
from PIL import Image
from PyPDF4 import PdfFileReader
# import pdf_to_bytes as pdf_to_bytes


def extract_images_from_pdf(pdf_bytes):
    # Load the PDF file from bytes
    pdf_doc = PdfFileReader(io.BytesIO(pdf_bytes))

    # Extract all images in the PDF
    images = []
    for i in range(pdf_doc.getNumPages()):
        page = pdf_doc.getPage(i)
        resources = page.get('/Resources')
        if not resources:
            continue
        xobjects = resources.get('/XObject')
        if not xobjects:
            continue
        for obj_name in xobjects.keys():
            obj = xobjects[obj_name]
            if obj['/Subtype'] == '/Image':
                img_bytes = obj._data
                img_pil = Image.open(io.BytesIO(img_bytes))
                filename = os.path.join(
                    'lab/images', f'image_{len(images)+1}.jpeg')
                img_pil.save(filename)
                images.append(img_pil)

    return images


# # we need the bytes to extract the image
# my_bytes = pdf_to_bytes.pdf_to_bytes('../lab/test.pdf')
# # Extract images from the PDF and save them to files
# extract_images_from_pdf(my_bytes, output_folder='../lab/images')

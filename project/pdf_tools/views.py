from django.shortcuts import render
import tools.bytes_to_pdf as bytes_to_pdf
import tools.pdf_to_bytes as pdf_to_bytes
import tools.extract_images as extract_images
import tools.attach_images as attach_images
import tools.empty_folder as empty_folder


def pdf_tool_extract_attach_images_from_pdf(bytes):

    # extract images from the pdf's bytes
    extract_images.extract_images_from_pdf(bytes)

    # turn the bytes into a pdf at  'lab/input.pdf'
    bytes_to_pdf.from_bytes_to_pdf(bytes)

    # take the input pdf and attach the images at 'lab/output.pdf'
    attach_images.attach_images_as_attachments(
        'lab/pdf/input.pdf', './lab/images/', './lab/output.pdf')

    # delete all received data
    empty_folder.empty_folder('lab/images')
    empty_folder.empty_folder('lab/pdf')


bytes = pdf_to_bytes.pdf_to_bytes('./lab/test/test.pdf')
pdf_tool_extract_attach_images_from_pdf(bytes)

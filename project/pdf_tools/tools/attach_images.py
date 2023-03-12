import os
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import DecodedStreamObject, NameObject, DictionaryObject, createStringObject, ArrayObject


def appendAttachment(pdf_writer, fname, fdata):
    file_entry = DecodedStreamObject()
    file_entry.set_data(fdata)
    file_entry.update({
        NameObject("/Type"): NameObject("/EmbeddedFile")
    })

    efEntry = DictionaryObject()
    efEntry.update({NameObject("/F"): file_entry})

    filespec = DictionaryObject()
    filespec.update({
        NameObject("/Type"): NameObject("/Filespec"),
        NameObject("/F"): createStringObject(fname),
        NameObject("/EF"): efEntry
    })

    if "/Names" not in pdf_writer._root_object.keys():
        embeddedFilesNamesDictionary = DictionaryObject()
        embeddedFilesNamesDictionary.update(
            {NameObject("/Names"): ArrayObject([createStringObject(fname), filespec])})

        embeddedFilesDictionary = DictionaryObject()
        embeddedFilesDictionary.update(
            {NameObject("/EmbeddedFiles"): embeddedFilesNamesDictionary})
        pdf_writer._root_object.update(
            {NameObject("/Names"): embeddedFilesDictionary})
    else:
        pdf_writer._root_object["/Names"]["/EmbeddedFiles"]["/Names"].append(
            createStringObject(fname))
        pdf_writer._root_object["/Names"]["/EmbeddedFiles"]["/Names"].append(
            filespec)


def attach_images_as_attachments(pdf_path, images_folder_path, output_path):
    with open(pdf_path, 'rb') as f:
        pdf_reader = PdfReader(f)
        pdf_writer = PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        for image_filename in os.listdir(images_folder_path):
            image_path = os.path.join(images_folder_path, image_filename)
            with open(image_path, 'rb') as f:
                image_data = f.read()
            appendAttachment(pdf_writer, image_filename, image_data)

        with open(output_path, 'wb') as f:
            pdf_writer.write(f)


# attach_png_to_pdf('../lab/test.pdf',
#                   '../lab/images/image_1.jpeg', '../lab/final.pdf')

import aspose.pdf as ap

# Open document
document = ap.Document(input_file)

document.pages[1].add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

document.save(output_pdf)
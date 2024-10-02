import chesspdftofen
# from PyPDF2 import PdfReader, PdfWriter

# def truncate_pdf(input_pdf_path, output_pdf_path, start_page, end_page):
#     # Create a PdfReader object to read the input PDF
#     reader = PdfReader(input_pdf_path)
#     writer = PdfWriter()

#     # Add the pages from the start_page to the end_page
#     for page_num in range(start_page, end_page):
#         page = reader.pages[page_num]
#         writer.add_page(page)

#     # Write the truncated pages to a new output PDF
#     with open(output_pdf_path, 'wb') as output_pdf:
#         writer.write(output_pdf)

# input_pdf_path = './chess.pdf'
# output_path = './chess_final.pdf'

# truncate_pdf(input_pdf_path, output_path, 5, 7)

for status in chesspdftofen.run('./chess_final.pdf', './output.pdf'):
    print(status)   
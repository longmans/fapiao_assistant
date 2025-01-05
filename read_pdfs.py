import os
import fitz  # PyMuPDF

def find_pdfs(directory):
    pdf_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

def convert_pdf_to_images(pdf_path, output_folder):
    pdf_document = fitz.open(pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        image_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_page_{page_num + 1}.png")
        pix.save(image_path)

if __name__ == "__main__":
    data_directory = os.path.join(os.path.dirname(__file__), 'data')
    pdf_files = find_pdfs(data_directory)
    output_folder = os.path.join(os.path.dirname(__file__), 'output_images')
    os.makedirs(output_folder, exist_ok=True)
    for pdf in pdf_files:
        convert_pdf_to_images(pdf, output_folder)
        print(f"Converted {pdf} to images in {output_folder}")
        break

import os
from read_pdfs import find_pdfs, convert_pdf_to_images
from vqa import get_image_description

def main():
    data_directory = os.path.join(os.path.dirname(__file__), 'data')
    output_folder = os.path.join(os.path.dirname(__file__), 'output_images')
    os.makedirs(output_folder, exist_ok=True)
    
    pdf_files = find_pdfs(data_directory)
    if not pdf_files:
        print("No PDF files found.")
        return
    
    for pdf in pdf_files:
        convert_pdf_to_images(pdf, output_folder)
        print(f"Converted {pdf} to images in {output_folder}")

    image_files = [f for f in os.listdir(output_folder) if f.lower().endswith('.png')]
    if not image_files:
        print("No images found.")
        return
    
    total_price = 0
    for image_file in image_files:
        image_path = os.path.join(output_folder, image_file)
        description = get_image_description(image_path)
        print(f"Description for {image_file}: {description}")
        try:
            price = float(description)
            total_price += price
        except ValueError:
            print(f"Invalid description for {image_file}: {description}")
    print(f"Total price: {total_price:.2f}")

if __name__ == "__main__":
    main()

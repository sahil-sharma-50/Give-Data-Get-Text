import streamlit as st
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def extract_text_from_image(image):
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

with st.sidebar:
    st.title('Connect:')
    st.link_button(":blue[LinkedIn] :computer:", 'https://www.linkedin.com/in/sahilsharma50/', use_container_width=True)
    st.link_button(":grey[GitHub] :desktop_computer:", 'https://github.com/sahilsharma50/', use_container_width=True)

def main():
    st.title('_Give Data Get_ :blue[Text] :paperclip:')

    input_file = st.file_uploader("Upload a File", type=['png', 'jpg', 'jpeg', 'pdf'])

    if input_file is not None:
        file_extension = input_file.name.split('.')[-1].lower()

        if file_extension in ['png', 'jpg', 'jpeg']:
            # Image file: Open the image and extract text
            image = Image.open(input_file)
            extracted_text = extract_text_from_image(image)

            # Display the image and extracted text
            st.image(image, caption='Uploaded Image', use_column_width=True)
            st.subheader('Extracted Text')
            st.code(extracted_text)

        elif file_extension == 'pdf':
            # PDF file: Convert PDF to images and extract text from each page
            st.write("Processing PDF file...")

            # Convert PDF to images
            images = convert_from_bytes(input_file.read())

            # Iterate over each page image and extract text
            for i, image in enumerate(images):
                extracted_text = extract_text_from_image(image)

                # Display the image and extracted text for each page
                st.image(image, caption=f'Page: {i + 1}', use_column_width=True)
                st.subheader(f'Extracted Text from Page: {i + 1}')
                st.code(extracted_text)

        else:
            st.write("Unsupported file format. Please upload an image (PNG, JPG, JPEG) or a PDF.")

# Run the app
if __name__ == "__main__":
    main()

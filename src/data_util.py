import PyPDF2

from src.logger import logging

# Reading the input data file
def read_input_file(file_name):
    # checking the file type
    if file_name.name.endswith(".pdf"):
        # Input file is a PDF
        try:
            # Reading the PDF file
            with open(file_name.name, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = ""
                # Extracting text from each page and adding to text
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()

                logging.info('Input PDF file was read')
                return text

        except Exception as e:
            logging.error(f"Error while reading input PDF file: {e}")
            raise Exception("Error while reading input PDF file.")

    elif file_name.name.endswith(".txt"):
        # Input file is a text
        logging.info('Input Text file was read')
        return file_name.read().decode('utf-8')

    else:
        # raise exception
        raise Exception("Unsupported file format. Only PDF and Text files are supported.")

from pypdf import PdfReader

def analyze_pdf(file_path):
    """Reads a PDF and prints the text from the first page."""
    try:
        # Create a reader object
        reader = PdfReader(file_path)

        # Get the number of pages
        num_pages = len(reader.pages)
        print(f"📄 The document '{file_path}' has {num_pages} page(s).")

        if num_pages > 0:
            # Get the first page
            first_page = reader.pages[1]

            # Extract text
            text = first_page.extract_text()

            print("\n--- Text from Page 1 ---")
            print(text)
            print("------------------------")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# The script will run this when executed
if __name__ == "__main__":
    # Make sure you have a PDF named 'sample.pdf' in the 'level1' folder
    pdf_file = "level1/sample.pdf"
    analyze_pdf(pdf_file)
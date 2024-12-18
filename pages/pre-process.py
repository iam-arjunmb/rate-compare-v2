import streamlit as st
import fitz  # PyMuPDF

# Function to extract text from PDF

import fitz  # PyMuPDF

def function1(uploaded_file):
    # Open the uploaded PDF file as a document
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    
    # Iterate over each page in the PDF
    for page in doc:
        # Extract plain text from the page, encoded as UTF-8
        page_text = page.get_text("text")
        
        # Split the page text into lines
        lines = page_text.split('\n')
        
        # Remove blank lines
        non_blank_lines = [line for line in lines if line.strip() != '']
        
        # Remove commas from each line
        sanitized_lines = [line.replace(",", "") for line in non_blank_lines]
        
        # Join the sanitized lines and add to the overall text
        text += '\n'.join(sanitized_lines) + '\n'
    
    # Return the complete text
    return text


# Function to process the edited text
def function2(edited_text):
    lines = edited_text.split('\n')

    data = {}
    current_country = None
    headers = ["Country", "Counts", "SMS Rates", "Amount"]
    line_index = 0

    while line_index < len(lines):
        line = lines[line_index].strip()

        if line in headers or not line:
            # Skip headers and empty lines
            line_index += 1
            continue

        if current_country is None:
            # This line is a country name
            current_country = line
            data[current_country] = {}
        elif 'Counts' not in data[current_country]:
            # This line is the Counts
            data[current_country]['Counts'] = int(line)
        elif 'SMS Rates' not in data[current_country]:
            # This line is the SMS Rates
            data[current_country]['SMS Rates'] = float(line)
        elif 'Amount' not in data[current_country]:
            # This line is the Amount
            data[current_country]['Amount'] = float(line.replace(',', ''))
            current_country = None  # Reset for the next country

        line_index += 1

    # Extracting SMS rates
    country_sms_rates = {}
    for country, data in data.items():
        if 'SMS Rates' in data:
            country_sms_rates[country] = data['SMS Rates']

    return country_sms_rates


def main():
    st.title("PDF Text Processor")

    # Step 1: Upload PDF file
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        # Step 2: Read and process the PDF text with function1
        processed_text = function1(uploaded_file)
        
        # Step 3: Allow editing of the processed text
        edited_text = st.text_area("Edit the processed text...", value=processed_text, height=300)
        
        # Step 4: Submit edited text and process with function2
        if st.button("Submit"):
            further_processed_text = function2(edited_text)
            st.text_area("Further processed text", value=str(further_processed_text), height=300, key='further_processed_text')
            

if __name__ == "__main__":
    main()

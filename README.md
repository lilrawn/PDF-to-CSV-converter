<<<<<<< HEAD
# Enhanced PDF to CSV Converter

A simple GUI application to convert PDF files to CSV format using the `tabula` library.

## Features

* Select a PDF file to convert
* Choose a page range to extract (e.g., 1-3,5 or 'all')
* Remove blank rows from the output CSV
* Drag-and-drop PDF files from the file explorer (requires `tkinterdnd2` library)
* Progress bar (currently a placeholder, could be developed further)

## Installation

1. Install Python 3.7 or later (https://www.python.org/downloads/)
2. Install required libraries: `pip install tabula pandas tkinterdnd2`
3. Download the `converter.py` script and save it somewhere (e.g., `~/Documents/`)

## Usage

1. Run the script: `python converter.py`
2. Select a PDF file to convert using the "Select PDF and Convert" button
3. Choose a page range to extract (optional)
4. Check the box to remove blank rows from the output CSV (optional)
5. Click "Convert" to start the conversion process
6. Wait for the conversion to complete (a progress bar will appear)
7. The output CSV file will be saved in the same directory as the PDF file

## Known Issues

* The drag-and-drop feature requires the `tkinterdnd2` library, which may not work on all systems.
* The progress bar is currently a placeholder and does not update during the conversion process.

## Development

The project is open-source and hosted on GitHub: https://github.com/lilrawn/enhanced-pdf-to-csv-converter

Feel free to contribute or report issues!
=======
# PDF-to-CSV-converter
This Python script converts data from PDF files into CSV format. It extracts text from each page of a PDF and saves it in a structured CSV format. This tool is ideal for extracting data from reports, invoices, tables, or any other content stored in PDF files, making data analysis and processing much easier.
>>>>>>> 0da3e815afa41daf9630a99cca0f93d83e3ced4c

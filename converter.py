import tabula
import pandas as pd
from tkinter import Tk, filedialog, messagebox, Label, Entry, Button
from tkinter.ttk import Progressbar
import os

def convert_pdf_to_csv(pdf_path, csv_path, page_range, remove_blank_rows):
    try:
        # Notify the user of the process start
        messagebox.showinfo("Processing", "Conversion started. Please wait...")
        
        # Extract tables from the specified page range
        tables = tabula.read_pdf(pdf_path, pages=page_range, multiple_tables=True, lattice=True)
        
        if not tables:
            messagebox.showerror("Error", "No tables found in the PDF.")
            return
        
        # Combine all tables into a single DataFrame
        combined_data = pd.concat(tables, ignore_index=True)
        
        # Data cleaning: Remove blank rows if specified
        if remove_blank_rows:
            combined_data.dropna(how="all", inplace=True)
        
        # Save the combined data as a CSV file
        combined_data.to_csv(csv_path, index=False)
        messagebox.showinfo("Success", f"PDF data successfully converted to CSV:\n{csv_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_pdf_file():
    # Open file dialog to choose the PDF file
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        output_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if output_path:
            page_range = entry_page_range.get() or "all"
            remove_blank_rows = clean_rows_var.get() == 1
            convert_pdf_to_csv(pdf_path, output_path, page_range, remove_blank_rows)

def drag_and_drop_file(event):
    file_path = event.data.strip()
    if os.path.isfile(file_path) and file_path.lower().endswith('.pdf'):
        output_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if output_path:
            page_range = entry_page_range.get() or "all"
            remove_blank_rows = clean_rows_var.get() == 1
            convert_pdf_to_csv(file_path, output_path, page_range, remove_blank_rows)

# Create the main tkinter window
root = Tk()
root.title("Enhanced PDF to CSV Converter")
root.geometry("400x200")

# Labels and entry fields
Label(root, text="Specify Page Range (e.g., 1-3,5 or 'all')").pack(pady=5)
entry_page_range = Entry(root, width=20)
entry_page_range.insert(0, "all")  # Default is 'all'
entry_page_range.pack(pady=5)

# Checkbox for removing blank rows
from tkinter import IntVar, Checkbutton
clean_rows_var = IntVar()
Checkbutton(root, text="Remove Blank Rows", variable=clean_rows_var).pack(pady=5)

# File selection button
Button(root, text="Select PDF and Convert", command=select_pdf_file).pack(pady=10)

# Progress bar (placeholder, could be developed further)
Label(root, text="Progress:").pack()
progress = Progressbar(root, length=300, mode="determinate")
progress.pack(pady=5)

# Allow drag-and-drop (requires a third-party library like `tkdnd`)
try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    root = TkinterDnD.Tk()  # Initialize drag-and-drop enabled window
    root.drop_target_register(DND_FILES)
    root.dnd_bind("<<Drop>>", drag_and_drop_file)
    Label(root, text="Drag and Drop PDFs Here").pack(pady=5)
except ImportError:
    Label(root, text="Drag-and-Drop not available. Install `tkinterdnd2` for this feature.").pack(pady=5)

# Run the Tkinter event loop
root.mainloop()

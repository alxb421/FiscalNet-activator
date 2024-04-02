import os
import shutil
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import messagebox, filedialog

def modify_fiscalnet_file(folder_path):
    # Backup FiscalNet.dll file
    source_file = os.path.join(folder_path, "FiscalNet.dll")
    backup_file = os.path.join(folder_path, "FiscalNet.dll.bck")
    shutil.copy2(source_file, backup_file)

    # Modify XML content
    xml_file = os.path.join(folder_path, "FiscalNet.dll")
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Find and modify <MaxDate> tag
    ns = {"ns0": "http://tempuri.org/DS_Setari.xsd"}
    max_date_element = root.find(".//ns0:MaxDate", ns)
    if max_date_element is not None:
        max_date_element.text = "Activat folosind FiscalNet Activator by Alexandru Balan"

    tree.write(xml_file)

def check_fiscalnet_directory():
    fiscalnet_path = "C:\\FiscalNet"  # Path to the FiscalNet folder
    if os.path.exists(fiscalnet_path):
        modify_fiscalnet_file(fiscalnet_path)
        messagebox.showinfo("FiscalNet Found", "FiscalNet found in C:\\ directory. Modifications done.")
    else:
        messagebox.showerror("FiscalNet Not Found", "FiscalNet is not installed or not in C:\\ directory.")
        response = messagebox.askyesno("Browse for FiscalNet", "Do you want to browse for the FiscalNet folder?")
        if response:
            browse_fiscalnet_directory()

def browse_fiscalnet_directory():
    folder_selected = filedialog.askdirectory(initialdir="C:\\", title="Select FiscalNet Directory")
    if folder_selected:
        modify_fiscalnet_file(folder_selected)
        messagebox.showinfo("FiscalNet Found", f"FiscalNet found in {folder_selected}. Modifications done.")

def show_credits():
    credits_info = """
    FiscalNet Activator
    Version 1.0
    Developed by Alexandru Balan
    """
    messagebox.showinfo("Credits", credits_info)

def show_license():
    license_info = """
    This software is licensed under the GPL V3 License.
    """
    messagebox.showinfo("License", license_info)

# Create main window
window = tk.Tk()
window.title("FiscalNet Activator")

# Create label
label = tk.Label(window, text="FiscalNet Activator", font=("Helvetica", 16))
label.pack(pady=10)

# Check FiscalNet directory button
check_button = tk.Button(window, text="Check FiscalNet Directory", command=check_fiscalnet_directory)
check_button.pack(pady=5)

# Credits button
credits_button = tk.Button(window, text="Credits", command=show_credits)
credits_button.pack(pady=5)

# License button
license_button = tk.Button(window, text="License", command=show_license)
license_button.pack(pady=5)

# Exit button
exit_button = tk.Button(window, text="Exit", command=window.quit)
exit_button.pack(pady=5)

# Run the main event loop
window.mainloop()

# Excel to vCard Converter

This Python script converts data from an Excel file into vCard format. It utilizes the `openpyxl` library to handle Excel files and the `vobject` library to create vCards.

## Prerequisites

Make sure you have Python installed on your system. Additionally, install the required libraries using pip:

```bash
pip install openpyxl vobject
```

## Usage

1. Place your Excel file (`input.xlsx`) containing contact information in the same directory as the script.
2. Run the script using the following command:

    ```bash
    python excel_to_vcard.py
    ```

3. The script will create a `contacts.vcf` file in the same directory, containing the converted vCard data.

## Script Overview

- The script loads data from the `input.xlsx` Excel file.
- It iterates over each row, creating a vCard for each contact.
- Each vCard contains the contact's name and phone number.
- The generated vCards are written to a `contacts.vcf` file.

## Example

Suppose `input.xlsx` contains the following data:

| Name   | Phone      |
|--------|------------|
| Alice  | 1234567890 |
| Bob    | 9876543210 |

Running the script will generate a `contacts.vcf` file with the following content:

```
BEGIN:VCARD
VERSION:3.0
FN:Alice
TEL:1234567890
END:VCARD
BEGIN:VCARD
VERSION:3.0
FN:Bob
TEL:9876543210
END:VCARD
```
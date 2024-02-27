import openpyxl
import vobject

# Load the Excel file
wb = openpyxl.load_workbook('input.xlsx')
sheet = wb.active

# Create a list to store vCards
vcards = []

# Iterate over rows and create vCards
for row in sheet.iter_rows(values_only=True):
    name, number = row
    vcard = vobject.vCard()
    vcard.add('fn').value = name
    vcard.add('tel').value = str(number)  # Convert number to string
    vcards.append(vcard.serialize())

# Write vCards to a file
with open('contacts.vcf', 'w') as f:
    f.write('\n'.join(vcards))

print('VCF file created successfully.')

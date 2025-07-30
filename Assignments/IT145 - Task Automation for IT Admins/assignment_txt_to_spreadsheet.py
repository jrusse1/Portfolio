import openpyxl
with open('Phone_Number_and_Email_Address.txt') as p:
	contents = p.readlines()

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Phone and Email'

row = 1
for line in contents:
	sheet.cell(row= row, column= 1).value = line
	sheet.row_dimensions[row].height = len(line)
	row += 1

wb.save('phone-email.xlsx')
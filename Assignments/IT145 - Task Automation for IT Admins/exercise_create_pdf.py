import PyPDF2

pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    string = pageObj.extractText()
    if string.find('student') >= 0:
        pdfWriter.addPage(pageObj)

pdfOutputFile = open('students.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdfFileObj.close()

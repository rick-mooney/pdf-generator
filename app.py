import PyPDF2
def generate(file, times):
    x = 0
    pdfFile = open(file, 'rb')
    while x < times:
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        pdfWriter = PyPDF2.PdfFileWriter()
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        pdfOutputFile = open('output/file' + str(x) + '.pdf', 'wb')
        pdfWriter.write(pdfOutputFile)
        pdfOutputFile.close()
        x += 1
    pdfFile.close()


generate('sample.pdf', 100)
# input drag and drop file
# output to zip file
# TODO have it prompt a zip file download

import os
from PyPDF2 import PdfFileReader, PdfFileWriter
 
 
def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
 
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
 
        output_filename = '{}_page_{}.pdf'.format(
            fname, page+1)
 
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
 
        print('Created: {}'.format(output_filename))
 
if __name__ == '__main__':
    #Ask user where the PDFs are
    userpdflocation=input('File path to PDF that need split:')
    #Sets the scripts working directory to the location of the PDFs
    pdf_splitter(userpdflocation)
import PyPDF2
import sys

def main():
    pdf_file_path = input("Please enter the pdf file path you want to watermark: ")
    watermark = input("Please enter the watermark pdf file path you want to mark: ")
    
    pdf_to_watermark = PyPDF2.PdfFileReader(open(pdf_file_path,'rb'))
    watermark = PyPDF2.PdfFileReader(open(watermark,'rb'))
    
    watermarked_pdf = PyPDF2.PdfFileWriter()
    
    mark(pdf_to_watermark, watermark, watermarked_pdf, pdf_file_path)

def mark(pdf_to_watermark, watermark, watermarked_pdf, pdf_file_path):
    for i in range(pdf_to_watermark.getNumPages()):
        page = pdf_to_watermark.getPage(i)
        page.mergePage(watermark.getPage(0))
        watermarked_pdf.addPage(page)
        
        with open(pdf_file_path + "_watermarked.pdf", 'wb') as file:
            watermarked_pdf.write(file)
    
if __name__ == '__main__':
    main()
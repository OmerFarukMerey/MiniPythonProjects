import PyPDF2
import sys

def main():
    input_pdfs = sys.argv[1:]
    pdf_combiner(input_pdfs)
    
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merged_pdf_name = input("Please enter the merged pdf name: ")
    if not merged_pdf_name.endswith('.pdf'):
        merged_pdf_name = merged_pdf_name + ".pdf"
    merger.write(merged_pdf_name)
    
if __name__ == '__main__':
    main()
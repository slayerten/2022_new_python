import PyPDF2


def PDFmerge(pdfs, output):

    pdfMerger = PyPDF2.PdfMerger()

    for pdf in pdfs:
        with open(pdf, 'rb') as f:
            pdfMerger.append(f)

    with open(output, 'wb') as f:
        pdfMerger.write(f)


# def getpdfs():

#     pdfs = []
#     for i in range(134):
#         pdfs.append('out_{}.pdf'.format(i))
#     # print(pdfs)
#     return pdfs


def main():

    pdfs = []
    for i in range(134):
        pdfs.append('out_{}.pdf'.format(i))
    # pdfs = getpdfs()
    print(pdfs)
    # pdfs = ['out_0.pdf', 'out_1.pdf']
    output = 'python_turial.pdf'

    PDFmerge(pdfs, output)


if __name__ == '__main__':
    main()

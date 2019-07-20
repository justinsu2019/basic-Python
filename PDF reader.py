import PyPDF2

# ===============从pdf中提取文本===========

pdffile = open(r'WEF_Global_Risks_Report_2019.pdf', 'rb')  # 读取pdf文件
pdfreader = PyPDF2.PdfFileReader(pdffile)  # 读入到pdfreader
# pdfreader.numPages is the page number of the PDF

print([pdfreader.getPage(i).extractText() for i in range(pdfreader.numPages)])


# page0 = pdfreader.getPage(0) get the page from the result
# page0.extractText()) trans result to text

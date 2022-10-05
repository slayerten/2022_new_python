
from bs4 import BeautifulSoup
import requests
import pdfkit
import PyPDF2


base_url = 'https://docs.python.org/zh-cn/3/tutorial/index.html'
total_hrefs = []
response = requests.get(base_url)
# print(response.status_code)
# if response.status_code == 200:
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
linkas = soup.select('div.toctree-wrapper a')

for link in linkas:
    print(link.get('href'))
print(soup.find_all("a", class_="internal"))  # 关键在于class后面的下划线_
# for link in list:
#     print(link.get('href'))
#         # .find_all('a',class = 'reference internal')
total_hrefs = ['https://docs.python.org/zh-cn/3/tutorial/' +
               i.get('href').strip() for i in linkas]
# for a in total_hrefs:
#     print(a)
# total_hrefs = [i for in total_hrefs if '#' not in i]

# if len(total_hrefs):
#     return total_hrefs
#  else:
#     Return None
config = pdfkit.configuration(
    wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
# pdfkit.from_url(
#     'https://docs.python.org/zh-cn/3/tutorial/controlflow.html#if-statements', 'out.pdf', configuration=config)


# def Html2PDF(self, hrefs, save_name='out'):

pdfs = []
for index, href in enumerate(total_hrefs):
    print(href)
    name = 'out_' + "{}.pdf".format(index)
    pdfkit.from_url(href, name, configuration=config)
    pdfs.append(name)

# for pdf in pdfs:
#         self.merger.append(pdf, import_bookmarks=False)
#     self.merger.write('merge.pdf')
#     print('PDF转换完成，请到根目录下查看')

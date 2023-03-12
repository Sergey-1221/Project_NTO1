import aspose.words as aw
import pdfkit

def ptoh():
    doc = aw.Document("input.pdf")
    doc.save("Output.html")

def htop():

    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_url('http://127.0.0.1:8000/tours/client/statement', 'outf.pdf', configuration=config)

htop()
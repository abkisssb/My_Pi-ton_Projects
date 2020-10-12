import pyttsx3 as pt
import PyPDF2 as pd

book = open('fp.pdf', 'rb')
read_pdf = pd.PdfFileReader(book)
pages = read_pdf.numPages
speaker = pt.init()
for page in range(0, pages):
    page = read_pdf.getPage(page)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
import pyttsx3
import PyPDF3

# giving path of the pdf 
path = open("07_required_pdf_for_the_pdf_reader_program.pdf", "rb")

# giving access to the module PyPDF3 of the pdf 
pdfReader = PyPDF3.PdfFileReader(path)

# from where program should start reading 
from_page = pdfReader.getPage(0)

# extracting the text 
text = from_page.extractText()

# making the program to read the pdf 
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
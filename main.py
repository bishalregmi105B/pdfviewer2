from customtkinter import *
import customtkinter 
from tkPDFViewer import tkPDFViewer as pdf

app = customtkinter.CTk()
app.geometry('1360x720')
app.title("PDF Viewer")
customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode('dark')

def newwin(s):
    variable1 = pdf.ShowPdf()
#Add your pdf location and width and height.
    variable2 = variable1.pdf_view(app,pdf_location=s,height=720,width=1360)
    variable2.place(x=1,y=1)
def openfile():
    filename=filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a PDF File",
                                          filetypes = (("Text files",
                                                        "*.pdf*"),
                                                       ("all files",
                                                        "*.*")))
    
    newwin(filename)
    
open = customtkinter.CTkButton(app,text="Open FIle",command=openfile)
open.place(x=1,y=0)
app.mainloop()

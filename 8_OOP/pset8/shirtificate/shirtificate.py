# https://pyfpdf.github.io/fpdf2/Tutorial.html

from fpdf import FPDF

name = input('Name: ')

#Creating pdf object and PDF
pdf = FPDF()
pdf.add_page()


# Image
image_size = 200
image_x = (210-image_size)/2
image_y = (320-image_size)/2
pdf.image("shirtificate.png", image_x, image_y, image_size)


# Fonts
pdf.set_font("helvetica", "B", 25)
pdf.set_text_color(255, 255, 255)
pdf.ln(120)
pdf.cell(0, 0, name + " took CS50", ln=True, align='C')

pdf.set_font("helvetica", "B", 50)
pdf.ln(-100)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 0, "CS50 Shirtificate", ln=True, align='C')

pdf.output("shirtificate.pdf")









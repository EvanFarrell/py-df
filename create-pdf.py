from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def write_to_canvas(packet, content_position_list): #[x, y, message]
	# create a new PDF with Reportlab
	can = canvas.Canvas(packet, pagesize=letter)
	for coords_and_text in content_position_list:
		x, y, message = coords_and_text
		can.drawString(x, y, message)
		can.save()

def write_to_pdf(packet, filename):
	#move to the beginning of the StringIO buffer
	packet.seek(0)
	new_pdf = PdfFileReader(packet)

	# read your existing PDF
	existing_pdf = PdfFileReader(file(filename, "rb"))
	output = PdfFileWriter()

	# add the "watermark" (which is the new pdf) on the existing page
	page = existing_pdf.getPage(0)
	page.mergePage(new_pdf.getPage(0))
	output.addPage(page)

	# finally, write "output" to a real file
	outputStream = file("destination.pdf", "wb")
	output.write(outputStream)
	outputStream.close()

content_position_list = [
	[129, 710, "some name here"]
]

packet = StringIO.StringIO()
write_to_canvas(packet, content_position_list)
write_to_pdf(packet, "name-essay-table.pdf")

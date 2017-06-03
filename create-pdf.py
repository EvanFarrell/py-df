from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class PDFWriter():

	def __init__(file_to_read, file_to_export_to, content_position_list):
		this.file_to_read = file_to_read
		this.file_to_export_to = file_to_export_to
		this.content_position_list = content_position_list

	def editPDF(use_benchmark_grid=False):
		if use_benchmark:
			content_position_list = create_benchmark_grid

		packet = StringIO.StringIO()
		write_to_canvas(packet, this.content_position_list)
		write_to_pdf(packet, this.file_to_read, this.file_to_export_to)

	def write_to_canvas(packet, content_position_list): #[x, y, message]
		# create a new PDF with Reportlab
		can = canvas.Canvas(packet, pagesize=letter)
		can.setFont("Helvetica", 10)
		for coords_and_text in content_position_list:
			x, y, message = coords_and_text
			can.drawString(x, y, message)
		can.save()

	def write_to_pdf(packet, file_to_read, file_to_export_to):
		#move to the beginning of the StringIO buffer
		packet.seek(0)
		new_pdf = PdfFileReader(packet)

		# read your existing PDF
		existing_pdf = PdfFileReader(file(file_to_read, "rb"))
		output = PdfFileWriter()

		# add the "watermark" (which is the new pdf) on the existing page
		page = existing_pdf.getPage(0)
		page.mergePage(new_pdf.getPage(0))
		output.addPage(page)

		# finally, write "output" to a real file
		outputStream = file(file_to_export_to, "wb")
		output.write(outputStream)
		outputStream.close()

	def create_benchmark_grid():
		benchmark_list = []
		for x in range(0, 600, 60):
			for y in range(0, 800, 20):
				benchmark_list.append([x, y, "(" + str(x) + ", " + str(y) + ")"])
		return benchmark_list

	content_position_list = [
		[129, 710, "some name here"],
		[249, 635, "essay line, just under the L"],
		[390, 555, "under D in date"]
	]

if __name__ == '__main__':

	content_position_list = [
	[129, 710, "some name here"],
	[249, 635, "essay line, just under the L"],
	[390, 555, "under D in date"]
	]

	pdf_writer = PDFWriter(
		file_to_read="benchmark.pdf",
		file_to_export_to="destination.pdf",
		content_position_list=content_position_list,
	)

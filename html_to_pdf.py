from xhtml2pdf import pisa
import io

class HtmlToPdf:

    def convert_html_to_pdf(html_content, output_path):
        
        # Create a file-like object to write the PDF data to
        result = io.BytesIO()

        # Configure xhtml2pdf options (optional)
        pdf_options = {
            'page-size': 'A4',
            'margin-top': '10mm',
            'margin-right': '10mm',
            'margin-bottom': '10mm',
            'margin-left': '10mm',
        }

        # Convert HTML to PDF
        pisa.CreatePDF(
            html_content, 
            dest=result, 
            encoding='UTF-8', 
            options=pdf_options
        )

        # Get the generated PDF data
        pdf_data = result.getvalue()

        # Save the PDF data to a file
        with open(output_path, 'wb') as f:
            f.write(pdf_data)

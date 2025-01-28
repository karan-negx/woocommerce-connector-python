import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from jinja2 import Template
from pathlib import Path
from datetime import datetime
from EnvHelper import EnvHelper
from templates import Templates
from invoice_template import InvoiceTemplate

class SendEmail:

    def __init__(self):
        self.envhelper = EnvHelper()

    def render_email_template(self, invoice_data):
        items = InvoiceTemplate().get_items_from_order(invoice_data)
        return Template(Templates.invoice_mail_template()).render(
            company_name = "Cisele",
            invoice_number = invoice_data.get("number"),
            invoice_date = datetime.now().strftime("%d-%m-%Y"),
            customer_name = f"{invoice_data.get("billing").get("first_name")} {invoice_data.get("billing")}",
            items = items,
            company_address = f"Mundka New Delhi, India - 110086",
            company_email = self.envhelper.company_email,
            support_email = self.envhelper.support_email
        )

    def send_invoice_mail(self, invoice_data):
        #get senders and receivers data
        sender_email = self.envhelper.sender_email
        receiver_email = invoice_data.get("billing").get("email", "")
        order_id = invoice_data.get("number")
        invoice_name = f"Invoice-{order_id}.pdf"
        body = self.render_email_template(invoice_data)
        current_file_path = Path(__file__).resolve()
        pdf_path = current_file_path / f"invoices" / invoice_name
        subject = f"Your Invoice from Cisele - Invoice #{order_id}"
        message = MIMEMultipart("alternative")
        try:
            with open(pdf_path, "rb") as pdf_file:
                pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
                pdf_attachment.add_header(
                    "Content-Disposition", "attachment", filename="Invoice.pdf"
                )  # Filename for the attachment
                message.attach(pdf_attachment)
        except FileNotFoundError:
            print("PDF file not found. Ensure the path is correct.")

        # create email template with MIMEMULTIPART
        message["Subject"] = subject
        message["From"] = sender_email
        message['To'] = receiver_email
        message.attach(MIMEText(body, "html"))
        with smtplib.SMTP(self.envhelper.smtp_server, self.envhelper.smtp_port) as server:
            server.starttls()
            server.login(sender_email, self.envhelper.smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
        return True        
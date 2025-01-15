import smtplib
from email.mime.text import MIMEText

def send_email(sender_email, receiver_email, password, subject, body):
  """
  Sends an email using the provided credentials.

  Args:
    sender_email: The email address of the sender.
    receiver_email: The email address of the recipient.
    password: The password for the sender's email account.
    subject: The subject of the email.
    body: The body of the email.

  Returns:
    True if the email was sent successfully, False otherwise.
  """
  try:
    # Create a secure connection to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)

    # Create the email message
    message = MIMEText(body)
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

    # Close the connection
    server.quit()

    return True

  except Exception as e:
    print(f"Error sending email: {e}")
    return False

# Example usage
sender_email = "ciseleindia@gmail.com"
receiver_email = "negikaran926@gmail.com"
password = "hhyj wyeo lcjj kgqs" 
subject = "Test Email from Python"
body = "This is a test email sent from Python."

if send_email(sender_email, receiver_email, password, subject, body):
  print("Email sent successfully!")


   















# from xhtml2pdf import pisa
# import io

# def html_to_pdf(html_content, output_path):
#     result = io.BytesIO()

#     # Configure xhtml2pdf options (optional)
#     pdf_options = {
#         'page-size': 'A4',
#         'margin-top': '10mm',
#         'margin-right': '10mm',
#         'margin-bottom': '10mm',
#         'margin-left': '10mm',
#     }

#     # Convert HTML to PDF
#     pisa.CreatePDF(
#         html_content, 
#         dest=result, 
#         encoding='UTF-8', 
#         options=pdf_options
#     )

#     # Get the generated PDF data
#     pdf_data = result.getvalue()

#     # Save the PDF data to a file
#     with open(output_path, 'wb') as f:
#         f.write(pdf_data)


# # Example usage:
# html_string = """
# <!DOCTYPE html>
# <html>
# <head>
# <style>
# body {
#   font-family: sans-serif;
# }
# .invoice-heading{
#   text-align:center;
# }

# .invoice-header {
#   text-align: center;
#   margin-bottom: 20px;
# }

# .invoice-details {
#   margin-bottom: 20px;
# }

# .invoice-details table {
#   width: 100%;
#   border-collapse: collapse;
# }

# .invoice-details table th,
# .invoice-details table td {
#   border: 1px solid #ddd;
#   padding: 10px;
# }

# .invoice-items {
#   margin-bottom: 20px;
# }

# .invoice-items table {
#   width: 100%;
#   border-collapse: collapse;
# }

# .invoice-items table th,
# .invoice-items table td {
#   border: 1px solid #ddd;
#   padding: 10px;
# }

# .invoice-total {
#   text-align: right;
# }

# .invoice-footer {
#   text-align: center;
#   margin-top: 20px;
# }
# </style>
# </head>
# <body>

# <div>
#   <h1 class="invoice-heading">Tax Invoice</h1>
#   <h3>Invoice No: <span id="invoice-no"></span></h3>
#   <h3>Date: <span id="invoice-date"></span></h3>
# </div>

# <div class="invoice-details">
#   <table>
#     <tr>
#       <td colspan="2">
#       <b>Bill From:</b>
#       <span id="bill-to-name"></span><br>
#           <span id="bill-to-address"></span><br>
#           <span id="bill-to-city"></span>, <span id="bill-to-state"></span> <span id="bill-to-zip"></span><br>
#           <span id="bill-to-email"></span><br>
#           <span id="bill-to-phone"></span></td>
#     </tr>
#     <tr>
#       <td>
#         <b>Shipping Address:</b>
#         <span id="bill-from-name"></span><br>
#             <span id="bill-from-address"></span><br>
#             <span id="bill-from-city"></span>, <span id="bill-from-state"></span> <span id="bill-from-zip"></span><br>
#             <span id="bill-from-email"></span><br>
#            <span id="bill-from-phone"></span>
#       </td>
#       <td>
#         <b>Billing Address:</b>
#         <span id="bill-from-name"></span><br>
#             <span id="bill-from-address"></span><br>
#             <span id="bill-from-city"></span>, <span id="bill-from-state"></span> <span id="bill-from-zip"></span><br>
#             <span id="bill-from-email"></span><br>
#             <span id="bill-from-phone"></span>
#       </td>
#     </tr>
#   </table>
# </div>

# <div class="invoice-items">
#   <table>
#     <thead>
#       <tr>
#         <th>Item Description</th>
#         <th>SKU Code</th>
#         <th>Quantity</th>
#         <th>Rate</th>
#         <th>Discount</th>
#         <th>Taxable</th>
#         <th>Tax</th>
#         <th>Total</th>
#       </tr>
#     </thead>
#     <tbody id="invoice-items-list">
#     </tbody>
#   </table>
# </div>

# <div class="invoice-total">
#   <table>
#     <tr>
#       <th>Total:</th>
#       <td><span id="subtotal"></span></td>
#     </tr>
#     <tr>
#       <th>Payment Type:</th>
#       <td><span id="tax"></span></td>
#     </tr>
#     <tr>
#       <th>Discount:</th>
#       <td><span id="total"></span></td>
#     </tr>
#   </table>
# </div>

# <div class="invoice-footer">
#   <p>Thank you for your business!</p>
# </div>
# </body>
# </html>
# """


# output_file = "output.pdf"

# html_to_pdf(html_string, output_file)
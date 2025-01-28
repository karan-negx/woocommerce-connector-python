from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from woocommerce.import_orders import ImportOrders
from html_to_pdf import HtmlToPdf
from invoice_template import InvoiceTemplate
from send_email import SendEmail

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",  
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/send-invoice/{order_id}")
def send_invoice_by_order_id(order_id):
    return_obj = {
        "data": None,
        "error_message" : None,
        "status_code" : 200
    }
    try:
        order = ImportOrders.get_order_by_id(order_id)
        html_content = InvoiceTemplate.get_invoice_template_with_order_data(order)
        output_path = f"invoices/Invoice-{order_id}.pdf"
        HtmlToPdf.convert_html_to_pdf(html_content, output_path)
        print(f"invoice for order id {order_id} created successfully.")
        return_obj["data"] = f"Invoice created for Order ID {order_id}"
        email_sent = SendEmail().send_invoice_mail(order)
    except Exception as e:
        print(f"Error while getting invoice by order id : {e}")
        return_obj["status_code"] = 503
        return_obj["error_message"] = "Something Went Wrong"
    finally:
        return return_obj

@app.get("/get-invoice/{order_id}")
def get_invoice_by_order_id(order_id:str):
    return_obj = {
        "data": None,
        "error_message" : None,
        "status_code" : 200
    }
    try:
        order = ImportOrders.get_order_by_id(order_id)
        html_content = InvoiceTemplate.get_invoice_template_with_order_data(order)
        output_path = f"invoices/Invoice-{order_id}.pdf"
        HtmlToPdf.convert_html_to_pdf(html_content, output_path)
        print(f"invoice for order id {order_id} created successfully.")
        return_obj["data"] = f"Invoice created for Order ID {order_id}"
    except Exception as e:
        print(f"Error while getting invoice by order id : {e}")
        return_obj["status_code"] = 503
        return_obj["error_message"] = "Something Went Wrong"
    finally:
        return return_obj



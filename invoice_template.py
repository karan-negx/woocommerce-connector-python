from jinja2 import Template
from datetime import datetime
from EnvHelper import EnvHelper
from templates import Templates

class InvoiceTemplate():

    def __init__(self):
        self.envhelper = EnvHelper()

    def generate_invoice_number(self, order_id, date_created):
        date = date_created.split("-")
        return f"BPT-{date[2][2]}{date[1]}{date[0][-2:]}-{order_id}"
    
    def get_items_from_order(self, order):
        items = [{
                "description" : item["name"],
                "quantity" : item["quantity"],
                "rate" : item["subtotal"],
                "discount" : 0,
                "taxable_amount" : item["subtotal_tax"] ,
                "tax" : item["total_tax"],
                "total" : str(int(item["subtotal"]) + int(item["subtotal_tax"])),
            } for item in order["line_items"]]

        if order["shipping_lines"]:
            shipping = [{
                "description" : item["method_title"],
                "quantity" : "1",
                "rate" : item["total"],
                "discount" : 0,
                "taxable_amount" : item["total"] ,
                "tax" : item["total_tax"],
                "total" : str(int(item["total"]) + int(item["total_tax"])),
            } for item in order["shipping_lines"]]
            items.extend(shipping)
        return items

    def get_invoice_template_with_order_data(self, order):
        order_id = order["id"]
        date_created = order["date_created"]
        items = self.get_items_from_order(order)
        return Template(Templates.invoice_template()).render(
            date_now = datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            invoice_no = InvoiceTemplate.generate_invoice_number(order_id, date_created),
            ship_to_name = f"{order["shipping"].get("first_name")} {order["shipping"].get("last_name")}",
            ship_to_address = f"{order["shipping"].get("address_1")} {order["shipping"].get("address_2")}",
            ship_to_city = order["shipping"].get("city",""),
            ship_to_state = order["shipping"].get("state",""),
            ship_to_zip = order["shipping"].get("postcode",""),
            ship_to_email = order["shipping"].get("email",""),
            ship_to_phone = order["shipping"].get("phone",""),
            ship_to_country = order["shipping"].get("Country",""),
            bill_to_name = f"{order["billing"].get("first_name")} {order["billing"].get("last_name")}",
            bill_to_address = f"{order["billing"].get("address_1")} {order["billing"].get("address_2")}",
            bill_to_city = order["billing"].get("city",""),
            bill_to_state = order["billing"].get("state",""),
            bill_to_zip = order["billing"].get("postcode",""),
            bill_to_email = order["billing"].get("email",""),
            bill_to_phone = order["billing"].get("phone",""),
            bill_to_country = order["billing"].get("Country",""),
            items = items,
            total_amount = order["total"],
            payment_type = order["payment_method_title"],
            total_discount = 0
        )
import os
import requests
import base64
from datetime import datetime
from EnvHelper import EnvHelper


class ImportOrders:

 

    def parse_order_data_for_invoice(order):
        order_id = order["id"]
        date_created = order["date_created"]
        return {
            "date_now" : datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "invoice_no" : ImportOrders.generate_invoice_number(order_id, date_created),
            "ship_to_name":f"{order["shipping"].get("first_name")} {order["shipping"].get("last_name")}",
            "ship_to_address": f"{order["shipping"].get("address_1")} {order["shipping"].get("address_2")}",
            "ship_to_city": order["shipping"].get("city",""),
            "ship_to_state":order["shipping"].get("state",""),
            "ship_to_zip":order["shipping"].get("postcode",""),
            "ship_to_email":order["shipping"].get("email",""),
            "ship_to_phone":order["shipping"].get("phone",""),
            "ship_to_country":order["shipping"].get("Country",""),
            "bill_to_name":f"{order["billing"].get("first_name")} {order["billing"].get("last_name")}",
            "bill_to_address": f"{order["billing"].get("address_1")} {order["billing"].get("address_2")}",
            "bill_to_city": order["billing"].get("city",""),
            "bill_to_state":order["billing"].get("state",""),
            "bill_to_zip":order["billing"].get("postcode",""),
            "bill_to_email":order["billing"].get("email",""),
            "bill_to_phone":order["billing"].get("phone",""),
            "bill_to_country":order["billing"].get("Country",""),
            "currency" : order["currency"],
            "date_created" : date_created,
            "shipping_total" : order["shipping_total"],
            "shipping_tax" : order["shipping_tax"],
            "discount_total" : order["discount_total"],
            "discount_tax" : order["discount_tax"],
            "total_amount" : order["total"],
            "total_tax" : order["total_tax"],
            "prices_include_tax" : order["prices_include_tax"],
            "customer_billing" : order["billing"],
            "customer_shipping" : order["shipping"],
            "line_items" : order["line_items"],
            "tax_lines" : order["tax_lines"],
            "shipping_lines" : order["shipping_lines"],
        }

    def get_order_by_id(order_id):
        envhelper = EnvHelper()
        url = f"{os.getenv("base_url")}/orders/{order_id}"
        headers = {
            'Authorization': f'Basic {base64.b64encode(f"{envhelper.consumer_key}:{envhelper.consumer_secret}".encode("utf-8")).decode("utf-8")}'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        order = response.json()
        return order




        
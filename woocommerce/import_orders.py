import os
import requests
import base64
from EnvHelper import EnvHelper


class ImportOrders:


    def parse_order(order):
        return {
            "id" : order["id"],
            "currency" : order["currency"],
            "date_created" : order["date_created"],
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




        
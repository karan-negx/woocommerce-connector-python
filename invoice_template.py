from jinja2 import Template
from datetime import datetime

class InvoiceTemplate():

    def generate_invoice_number(order_id, date_created):
        date = date_created.split("-")
        return f"BPT-{date[2][2]}{date[1]}{date[0][-2:]}-{order_id}"

    def get_invoice_template_with_order_data(order):
        order_id = order["id"]
        date_created = order["date_created"]
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

        return Template(InvoiceTemplate.invoice_template()).render(
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

    def invoice_template():
        return """
            <!DOCTYPE html>
            <html>
            <head>
            <style>
            body {
            font-family: sans-serif;
            }
            .invoice-heading{
            text-align:center;
            }

            .invoice-header {
            text-align: center;
            margin-bottom: 20px;
            }

            .invoice-details {
            margin-bottom: 20px;
            }

            .invoice-details table {
            width: 100%;
            border-collapse: collapse;
            }

            .invoice-details table th,
            .invoice-details table td {
            border: 1px solid #ddd;
            padding: 10px;
            }

            .invoice-items {
            margin-bottom: 20px;
            }

            .invoice-items table {
            width: 100%;
            border-collapse: collapse;
            }

            .invoice-items table th,
            .invoice-items table td {
            border: 1px solid #ddd;
            padding: 10px;
            }

            .invoice-total {
            text-align: right;
            }

            .invoice-footer {
            text-align: center;
            margin-top: 20px;
            }
            </style>
            </head>
            <body>

            <div>
            <h1 class="invoice-heading">Tax Invoice</h1>
            <h3>Invoice No: <span id="invoice-no">{{invoice_no}}</span></h3>
            <h3>Date: <span id="invoice-date">{{date_now}}</span></h3>
            </div>

            <div class="invoice-details">
            <table>
                <tr>
                    <td colspan="2">
                        <b>Bill From:</b>
                        <span id="bill-from-name">Beldoe Apparels</span><br>
                        <span id="bill-from-address">Hind Vihar, Kirari</span><br>
                        <span id="bill-from-city"></span>, <span id="bill-to-state">Delhi</span> <span id="bill-to-zip">110086</span><br>
                        <span id="bill-from-country">India</span>
                        <span id="bill-from-email">ciseleindia@gmail.com</span><br>
                    </td>
                </tr>
                <tr>
                    <td>
                        <b>Shipping Address:</b>
                        <span id="ship-to-name">{{ship_to_name}}</span><br>
                        <span id="ship-to-address">{{ship_to_address}}</span><br>
                        <span id="ship-to-city">{{ship_to_city}}</span>, <span id="ship-to-state">{{ship_to_state}}</span> <span id="ship-to-zip">{{ship_to_zip}}</span><br>
                        <span id="ship-to-email">{{ship_to_email}}</span><br>
                        <span id="ship-to-phone">{{ship_to_phone}}</span>
                    </td>
                    <td>
                        <b>Billing Address:</b>
                        <span id="bill-to-name">{{bill_to_name}}</span><br>
                        <span id="bill-to-address">{{bill_to_address}}</span><br>
                        <span id="bill-to-city">{{bill_to_city}}</span>, <span id="bill-to-state">{{bill_to_state}}</span> <span id="bill-to-zip">{{bill_to_zip}}</span><br>
                        <span id="bill-to-email">{{bill_to_email}}</span><br>
                        <span id="bill-to-phone">{{bill_to_phone}}</span>
                    </td>
                </tr>
            </table>
            </div>

            <div class="invoice-items">
            <table>
                <thead>
                <tr>
                    <th>Item Description</th>
                    <th>SKU Code</th>
                    <th>Quantity</th>
                    <th>Rate</th>
                    <th>Discount</th>
                    <th>Taxable</th>
                    <th>Tax</th>
                    <th>Total</th>
                </tr>
                </thead>
                <tbody id="invoice-items-list">
                    {% for item in items %}
                        <tr style="padding:10px;">
                            <td>{{item.description}}</td>
                            <td>{{item.quantity}}</td>
                            <td>{{item.rate}}</td>
                            <td>{{item.discount}}</td>
                            <td>{{item.taxable_amount}}</td>
                            <td>{{item.tax}}</td>
                            <td>{{item.total}}</td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
            </div>

            <div class="invoice-total">
            <table>
                <tr>
                <th>Total:</th>
                <td><span id="total">{{total_amount}}</span></td>
                </tr>
                <tr>
                <th>Payment Type:</th>
                <td><span id="payment_type">{{payment_type}}</span></td>
                </tr>
                <tr>
                <th>Discount:</th>
                <td><span id="discount">{{total_discount}}</span></td>
                </tr>
            </table>
            </div>

            <div class="invoice-footer">
            <p>Thank you for your business!</p>
            </div>
            </body>
            </html>
            """
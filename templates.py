class Templates():

    def invoice_pdf_template():
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

    def invoice_mail_template():
        return """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Invoice</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 20px;
                        color: #333;
                    }
                    .header {
                        text-align: center; 
                        margin-bottom: 20px;
                    }
                    .invoice-details {
                        width: 100%;
                        border-collapse: collapse;
                        margin-top: 20px;
                    }
                    .invoice-details th, .invoice-details td {
                        padding: 10px;
                        text-align: left;
                        border: 1px solid #ddd;
                    }
                    .total {
                        font-weight: bold;
                    }
                    .footer {
                        margin-top: 40px;
                        text-align: center;
                        font-size: 12px;
                        color: #777;
                    }
                </style>
            </head>
            <body>
                <div class="header">
                    <h1>Invoice from {{ company_name }}</h1>
                    <p>Invoice Number: {{ invoice_number }}</p>
                    <p>Date: {{ invoice_date }}</p>
                </div>
                
                <p>Dear {{ customer_name }},</p>
                <p>Thank you for your business. Please find below the details of your invoice:</p>
                
                <table class="invoice-details">
                    <thead>
                        <tr>
                            <th>Item</th>
                            <th>Description</th>
                            <th>Quantity</th>
                            <th>Unit Price</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for item in items %}
                        <tr>
                            <td>{{ item.name }}</td>
                            <td>{{ item.description }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>${{ item.unit_price }}</td>
                            <td>${{ item.total }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
                
                <p>If you have any questions or need further assistance, feel free to contact us at {{ support_email }}.</p>

                <div class="footer">
                    <p>Best regards,</p>
                    <p>{{ company_name }}<br>{{ company_address }}<br>{{ company_phone }}<br>{{ company_email }}</p>
                </div>
            </body>
            </html>
        """
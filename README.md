# Odoo Projects
A series of Odoo projects that extend the functionalities of the native Odoo modules:
### [helpdesk_extended](https://github.com/Riccino22/odoo_projects/tree/main/helpdesk_extended)
This is an Odoo module that adds two functions to Odoo's helpdesk module: allowing users to submit ticket category suggestions, and sending an error message to the user if the ticket description is less than 15 characters.

### [inventory_extended](https://github.com/Riccino22/odoo_projects/tree/main/inventory_extended)
This is a module that adds two functions to Odoo's stock module: implementing a language model to estimate prices for products in product.template, and sending an error message if an inventory adjustment results in a negative quantity.

### [invt_telegram_adjustment](https://github.com/Riccino22/odoo_projects/tree/main/invt_telegram_adjustment)
This is a Telegram bot for viewing product information and adjusting inventory using the xmlrpc.client library.

### [mail_extended](https://github.com/Riccino22/odoo_projects/tree/main/mail_extended)
This module extends the mail.activity model, allowing for more detailed views of all activities, assigning priority to them, and printing reports.

### [purchase_extended](https://github.com/Riccino22/odoo_projects/tree/main/purchase_extended)
An extension of the purchase module that performs the following actions: sends an error message if a record is saved without data in the order lines, sends an error message if a user tries to delete a record with a date earlier than the can_delete_after field, and allows visibility of certain purchase orders from the website.

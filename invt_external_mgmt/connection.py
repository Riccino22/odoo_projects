import xmlrpc.client
from dotenv import load_dotenv
import os

load_dotenv()

url = 'http://localhost:8069'
db = 'odoo16db'
username = 'riccino'
key = os.environ.get("ODOO_API_KEY")

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())

uid = common.authenticate(db, username, key, {})
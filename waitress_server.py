from waitress import serve
from light_switch import app  # Replace with your actual Flask app import

# Start the server
serve(app, listen='0.0.0.0:8099', url_scheme='https')

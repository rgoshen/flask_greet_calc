from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def app_welcome():
    """Return simple string."""
    return 'welcome'

@app.route('/welcome/home')
def app_welcome_home():
    """Return welcome home."""
    return 'welcome home'

@app.route('/welcome/back')
def app_welcome_back():
    """Return welcome back."""
    return 'welcome back'

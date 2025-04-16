from flask import Blueprint

autosys_bp = Blueprint('autosys', __name__)

from app.api.autosys import routes 
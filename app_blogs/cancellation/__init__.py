from flask import Blueprint

bp = Blueprint('cancellations',__name__)

from app_blogs.cancellation import cancellations
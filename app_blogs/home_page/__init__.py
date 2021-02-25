from flask import Blueprint

bp = Blueprint('home_page',__name__)

from app_blogs.home_page import home_pages
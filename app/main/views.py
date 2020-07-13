from flask import render_template,request,redirect,url_for,abort
# from flask_login import login_required,current_user
from . import main
# from ..requests import get_movies,get_movie,search_movie
# from ..models import Review,User
from .forms import PitchForm,CommentForm,CategoryForm
# from ..import db
# import markdown2
# Review = review.Review

# Views
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # all_category = Pitchcategory.get_categories()
    # all_pitches = Pitch.query.order_by('-id').all()
    # print(all_pitches)

    title = 'Home- Welcome'

    return render_template('index.html', title = title)
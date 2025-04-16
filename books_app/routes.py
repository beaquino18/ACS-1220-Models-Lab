"""Import packages and modules."""
import os
from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from books_app.models import Book, Author, Genre, User

# Import app and db from events_app package so that we can run app
from books_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    all_books = Book.query.all()
    all_users = User.query.all()
    return render_template('home.html', all_books=all_books, all_users=all_users)

@main.route('/profile/<username>')
def profile(username):
    # Find a user where the username matches the URL parameter
    # first_or_404 return the first matching user or automatically return a 404
    #   if no user is found
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('profile.html', user=user)

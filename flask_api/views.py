import os
from flask import Flask, redirect, render_template , request, url_for


def home_view():
    return render_template('myhome.html')

def login_view():
    return render_template('login.html')

def register_view():
    return render_template('register.html')

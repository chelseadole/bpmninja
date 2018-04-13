# Import flask dependencies
from flask import Blueprint, request, render_template
from bpmninja import app


@app.route('/')
def index():
    """Render landing page."""
    return render_template('index.html', title="index")


@app.route('/play')
def play():
    """Render play page, for playing bpmninja."""
    return render_template('play.html', title="play")
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story, story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', prompts=story.prompts)

@app.route('/story', methods=['POST'])
def show_story():
    answers = {prompt: request.form[prompt] for prompt in story.prompts}
    madlib_story = story.generate(answers)
    return render_template('story.html', madlib_story=madlib_story)


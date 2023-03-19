from flask import Flask , request, render_template , session, redirect, url_for
from survey import Question, surveys, satisfaction_survey, personality_quiz
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET KEY'] = 'hello'

debug = DebugToolbarExtension

responses = []

@app.route('/')
def home():
    
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions 
    return render_template('home.html', instructions=instructions, title=title)


@app.route('/questions/<int:question_id>', methods=['POST','GET']) 
def survey_question(question_id):

    questions = satisfaction_survey.questions
    question = questions[question_id]
         
    if question_id < len(questions) -1:
           return redirect(f'/questions/{question_id + 1}')
        
        
      

    return render_template('questions.html')


# @app.route('/answers')


from flask import Flask , request, render_template , session, redirect, url_for
from survey import Question, Survey, satisfaction_survey as survey, personality_quiz
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET KEY'] = 'hello'
app.debug = True
debug = DebugToolbarExtension

responses = []

@app.route('/')
def home():
    
    title = survey.title
    instructions = survey.instructions 
    return render_template('home.html', instructions=instructions, title=title)


@app.route('/questions/<int:question_id>', methods=['POST','GET']) 
def survey_question(question_id):

    
    questions_list = survey.questions
    question = questions_list[question_id]
    
    if question_id < 1 or len(questions_list) -1:
        # return redirect(f'/questions/{question_id + 1}')
        # print(f"THIS IS QUESTION ===> {question.question}")
        
         return render_template('questions.html', questions_list=questions_list, question=question )


@app.route('/answers', methods=["POST"] )
def your_answer():
   
    questions_list = survey.questions
    
    # question = questions_list[id]
    answer = request.form['the-answers']
    responses.append(answer)
    print(responses)

    if len(responses) == len(survey.questions):
        return redirect("/complete")
    else:

        return redirect(f"/questions/{len(responses)}")

@app.route('/complete')
def complete():
    
    return render_template('complete.html')
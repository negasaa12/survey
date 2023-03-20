from flask import Flask , request, render_template , session, redirect, url_for, flash
from survey import Question, Survey, satisfaction_survey as survey, personality_quiz
from flask_debugtoolbar import DebugToolbarExtension


keys = 'responses'


app = Flask(__name__)
app.config['SECRET KEY'] = 'hello'
app.debug = True
debug = DebugToolbarExtension





@app.route('/begin', methods=["POST"])
def handle_responses():
   
   session[keys] = []
   
   return redirect('/questions/0')


@app.route('/')
def home():
    
    title = survey.title
    instructions = survey.instructions 
    return render_template('home.html', instructions=instructions, title=title)


@app.route('/questions/<int:question_id>') 
def survey_question(question_id):

    responses = session.get(keys)

    questions_list = survey.questions
    question = questions_list[question_id]
    
    # if (question_id < 1 or len(questions_list) -1):
       

    if (responses is None):
         
         return redirect('/')
    
    if (len(responses) == len(survey.questions)):
         
         return redirect ("/complete")
        
    if (len(responses) != question_id):
        
        flash(f"INVALID QUESTION ID : {question_id}.")
        
        return redirect(f"/question/{len(responses)}")
            
    
    return render_template('questions.html', questions_list=questions_list, question=question )


@app.route('/answers', methods=["POST"] )
def your_answer():
   
    questions_list = survey.questions
    
    # question = questions_list[id]
    answer = request.form['the-answers']
    responses = session[keys]
    responses.append(answer)
    session[keys] = responses 

    print(responses)

    if (len(responses) == len(survey.questions)):
        return redirect("/complete")
    
    else:

        return redirect(f"/questions/{len(responses)}")



@app.route('/complete')
def complete():
    """SURVEY COMPLETE. SHOWS COMPLETE PAGE."""
    return render_template('complete.html')
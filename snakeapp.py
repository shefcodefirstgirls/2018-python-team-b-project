import os
from flask import Flask, render_template, request
import random, copy
from favouritesnake import collect_tweets

app = Flask(__name__)

snake_questions = {
	'Which country has the most species of snake': ['India', 'Brazil', 'Australia'],
	'Which species is the largest snake measured in captivity': ['Reticulated Python','Boa Constrictor','Green Anaconda'],
	'Which of these python species is found in Africa': ['Ball Python','Carpet Python', 'Reticulated Python'],
	'Which snake is the Kingsnake often confused with due to its bright colours': ['Coral Snake', 'Boomslang', 'Green Tree Python'],
	'How do pythons kill their prey': ['Constriction', 'Venom', 'Ambush'],
	'When Snakes on a Plane was released, two live snakes were set free during a showing in an Arizona cinema, which species were they': ['Western Diamondback Rattlesnake', 'Horned Rattlesnake', 'Pacific Rattlesnake'],
	'What colour pattern do Milk Snakes show': ['White/Black/Red Stripes','Red/Black Diamonds', 'Yellow/Black/White Stripes'],
	"Which snake isn't found in the UK": ['Worm Snake','Common Adder','Grass Snake'],
	'What is the average lifespan of a Royal Python': ['30 years', '20 years', '25 years'],
	'What species was the snake Britney Spears performed with at the 2001 MTV Video Music Awards': ['Albino Burmese Python', 'Rainbow Boa', 'Eyelash Viper']
}

#print(test_questions)

questions = copy.deepcopy(snake_questions)


def shuffle(q):
	selected_keys = []
	i = 0
	while i < len(q):
		current_selection = random.choice(q.keys())
		if current_selection not in selected_keys:
			selected_keys.append(current_selection)
			i = i+1
	return selected_keys

#for i in questions:
#	random.shuffle(questions[i])
#	this_question = test_questions[i]
#	print('{}? {} Correct Answer is: {}'.format(i,questions[i], this_question[0]))


@app.route('/quiz')
def quiz():
	for i in questions:
		random.shuffle(questions[i])
	return render_template('snakesquiz.html', q = questions, o = snake_questions)

@app.route('/answers')
def answers():
	return render_template('answers.html')

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
	correct = 0
	for i in snake_questions.keys():
		answered = request.form[i]
		if snake_questions[i][0] == answered:
			correct = correct + 1
			print(correct)
	return render_template('share.html', score = str(correct))


@app.route('/snakes')
def snaketypes():
	return render_template('snaketypes.html')

@app.route('/favsnake', methods=['POST'])
def favsnake():
	favourite = request.form['text']
	tweets = collect_tweets(favourite)
	tweet = tweets[0]
	return render_template('test.html', tweet = tweet.text)



if __name__ == '__main__':
	app.run(debug=True)
    
#@app.route("/")
#def say_hello():
#    return render_template("index.html")

#@app.route("/<name>")
#def say_hello_to(name):
#    return render_template("hello.html", user=name)

#@app.route("/feedback", methods=["POST"])
#def get_feedback():
#    data = request.values

#    return render_template("feedback.html", form_data=data)

"""
This piece of logic checks whether you are running the app locally or on Heroku
(make an account at https://www.heroku.com/ before the deployment session!). When
running the app on Heroku, the PORT environment/config variable is pre-populated by
Heroku to tell our app the correct port to run on.
"""
if "PORT" in os.environ:
   app.run(host="0.0.0.0", port=int(os.environ["PORT"]))
else:
   app.run(debug=True)

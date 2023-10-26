from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Displays a message to the user that changes based on their favorite dessert"""
    return f"How did you know I liked {users_dessert}?"

@app.route('/madlibs/<adjective>/<noun>')
def mad_libs(adjective, noun):
    """Builds a work appropriate madlib using the user's inputed adj. and noun"""
    return f"In our {adjective} discussion, we explored the {noun} approach to our project."

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Multiplies two numbers based on user's selected numbers"""
    
    if number1.isdigit() == True and number2.isdigit() == True:
        int_number1 = int(number1)
        int_number2 = int(number2)
        result = int_number1 * int_number2
        return f"{number1} times {number2} is {result}"
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    if n.isdigit() == True and word.isalpha() == True:
        int_n = int(n)
        statement = (word + " ") * int_n
        return statement
    else:
        return "Invalid input. Please try again by entering a word and a number!"
    
@app.route('/dicegame')
def dicegame():
    num = random.randint(1,6)
    if num == 6:
        return f"You rolled a {num}. You won!"
    else:
        return f"You rolled a {num}. You lost!"
    
    
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
import random
import os

app = Flask(__name__, template_folder = 'templates')

def is_prime(number):

    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/')
def index():
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)
    
    # Define the range based on the random number
    start_number = (random_number - 1) * 10 + 1
    end_number = random_number * 10
    
    # Find prime numbers in the range
    prime_numbers = [num for num in range(start_number, end_number + 1) if is_prime(num)]
    
    return render_template('index.html', random_number=random_number, start_number=start_number, end_number=end_number, prime_numbers=prime_numbers)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 2000)), debug=True)

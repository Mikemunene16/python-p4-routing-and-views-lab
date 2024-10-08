#!/usr/bin/env python3

from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(f'{text}')
    return f'{text}'


@app.route('/count/<int:num>')
def count(num):
    numbers = '\n'.join(str(i) for i in range(0, num))
    return numbers + '\n'   


@app.route('/math/<int:num1>/<operation>/<int:num2>')  # Changed <string:operation> to <operation>
def math(num1, operation, num2):
    # Perform the appropriate operation based on the operation parameter
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        # Handle division by zero
        if num2 == 0:
            return abort(400, description="Cannot divide by zero")
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return abort(400, description="Invalid operation")
    
    # Return the result as a string
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

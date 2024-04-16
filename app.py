from flask import Flask, render_template, request, redirect, url_for
import pyautogui
import time

app = Flask(__name__)

def spam_message(message, count, delay):
    try:
        count = int(count)
        delay = float(delay)
        if count <= 0 or delay <= 0:
            raise ValueError("Count and delay must be positive numbers.")
    except ValueError as e:
        return str(e)  # Return the error message if conversion fails

    for _ in range(count):
        pyautogui.typewrite(message)
        time.sleep(delay)  # Adjust the delay between each message as needed
        pyautogui.press('enter')
        time.sleep(0.01)  # Adjust the delay after sending each message as needed

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        count = request.form['count']
        delay = request.form['delay']
        result = spam_message(message, count, delay)
        if result:
            return result  # Return any error message from spam_message
        # Redirect to the spamming route after a delay
        return redirect(url_for('spam_with_delay', message=message, count=count, delay=delay))
    return render_template('index.html')

@app.route('/spam_with_delay/<message>/<int:count>/<int:delay>', methods=['GET'])
def spam_with_delay(message, count, delay):
    time.sleep(10)  # 10-second delay only at the start
    spam_message(message, count, delay)
    return "Spamming completed!"

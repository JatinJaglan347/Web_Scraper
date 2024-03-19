from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def substring(unique_strings , content):
    for my_content in unique_strings:
        if(content in my_content or my_content in content):
            return True
        
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        tag = request.form['tag']

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            elements = soup.find_all(tag)

            # Create a set to store unique content from div tags
            unique_content = set()

            # Loop through each element
            for element in elements:
                # Extract the text content of the element and strip whitespace
                content = element.text.strip()
                
                # Check if the content is not empty and not already in the unique_content set
                if substring(unique_content , content) == False:
                    unique_content.add(content)
                    

            # Join the unique content into a formatted string
            extracted_data = '\n'.join(unique_content)

            return render_template('result.html', data=extracted_data)
        except Exception as e:
            error_message = f"An error occurred: {e}"
            return render_template('index.html', error=error_message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


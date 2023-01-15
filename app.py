from flask import Flask, render_template, request, jsonify 
import requests 
  
app = Flask(__name__) 
  
@app.route('/', methods = ['GET']) 
def home(): 
    return render_template('index.html') 
  
@app.route('/send_message', methods = ['POST']) 
def send_message(): 
    user_input = request.form['userInput'] 

    # Get response from API 
    response = requests.get('http://api.example.com/get_response', params = {'userInput': userInput}) 

    # Return response to the chatbox 
    return jsonify({'status': 'OK', 'response': response}) 

  
if __name__ == '__main__': 
    app.run()

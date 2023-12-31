import os
import sys
import playsound
import speech_recognition as sr
from gtts import gTTS
from pdfminer.high_level import extract_text
import csv
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired

#How to use flask(python) to control buttons in html
#Add functionailty of using a button to do control c 




def speak(text):
    tts = gTTS(text=text, lang="en", slow=False)
    audio_filename = "voice.mp3"
    tts.save(audio_filename)
    playsound.playsound(audio_filename)
def readout():
    text = extract_text("./statics/files/file")
    os.remove("./statics/files/file")
    with open("Text.csv", "w") as file:

        writer = csv.writer(file, lineterminator="\r")
        writer.writerow(text)

    #To get the reference page
    with open("Text.csv") as file:
        reader = csv.reader(file)
        ref_page = ""
        ref = 0
        for row in reader:
            row = "".join(row)
            if row.lower() == "references" or "references" in row.lower():
                ref += 1
            if ref > 0:
                ref_page += row 
    print(ref_page) #to check if it actually got the reference page

    #to read aloud the conent of the pdf file that have now been  transfered to the csv file
    with open("Text.csv") as file:
        reader = csv.reader(file)
        stack =[]
        
        for row in reader:
            rows =[]
            ref_checker = ""
            
            
            for i in row:
                if i == "(":
                    stack.append(i)
                    continue
                if i == ")":
                    stack.pop()
                    if ref_checker in ref_page:
                        rows.append("reference")
                if i == "" or len(stack)> 0:
                    if i == " ":
                        if ref_checker in ref_page:
                            rows.append("reference")
                    ref_checker += i
                    
                    continue
                else:
                    
                    ref_checker = ""
                    rows.append(i)
            

            rows = "".join(rows) 
            
            try:
                #add a pause functionality
                speak(rows)
            except AssertionError:
                continue
    os.remove("Text.csv") #To clear the saved content of the pdf that was being read outloud

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'
app.config['UPLOAD_FOLDER'] = 'statics/files'
global files
files = ""
class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Read Aloud!")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        global file
        file = form.file.data # First grab the file
        file.filename = "file"
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        readout()
        
        
    return render_template('index.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)      
from django.shortcuts import render
from.models import InitialInput

from google import genai
from google.genai import types

from .forms import UploadFileForm

import markdown # type: ignore
import html


API_KEY = "!" # INSERT API KEY HERE !!!!
client = genai.Client(api_key=API_KEY)

def markdown_to_html(markdown_text):

    # Convert Markdown to HTML
    html_output = markdown.markdown(markdown_text, extensions=['extra', 'codehilite', 'nl2br'])
    return html_output


def getOutput(input, resume):
    name=input['vieweeName']
    position = input['position']
    einfo = input['vieweeInfo']
    context = input['context']
    
    resume = resume.replace(" ", "_").replace("(","").replace(")","")
    
    filepath = "media/uploads/" + resume
    
    
    resumefull = client.files.upload(
        file = filepath,
    )
    
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=f"Your name is Milo, The Ai Interviewer, you are an interviewing people to be {position} by giving them all 5 questions to answer provided in markdown, here is some info about your company: {context}"
        ),
        contents=[
            resumefull,
            f"My name is{name}I am applying for{position}and my resume is attached, more info about me:{einfo}"]
    )
    
    return markdown_to_html(response.text)


def initialInput(request):
    
    if request.method == "POST":
        
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            output = getOutput(request.POST, form.cleaned_data['resume'].name)
            
            return render(request, 'mainpage/initialoutput.html', {'output':output})
            
    else:
        form = UploadFileForm()
        return render(request, 'mainpage/initialinput.html', {'form': form})
    
            
    
        
        
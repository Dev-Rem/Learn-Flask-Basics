# from flask import Flask, request, render_template
# import openai

# openai.api_key="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"

# app = Flask(__name__)


# @app.route("/", methods=['GET'])
# def index():
#     return render_template('index.html')

# @app.route("/generate-cover-letter", methods=['POST'])
# def generate_cover_letter():
#     job_description = request.form.get('job_description')
#     job_title = request.form.get('job_title')
#     resume_file = request.files['resume_file']
    
#     # Read the resume file
#     try:
#         resume_text = resume_file.read().decode('utf-8')
#     except UnicodeDecodeError:
#         resume_text = resume_file.read().decode('latin-1', errors='replace')
        
#     # Concatenate the job description, job title, and resume text
#     prompt = f"Job Title: {job_title}\n\nJob Description: {job_description}\n\nResume: {resume_text}"
    
#     # Generate the cover letter using ChatGPT
#     response = openai.Completion.create(
#         engine='text-davinci-003',
#         prompt=prompt,
#         max_tokens=200,  
#         temperature=0.7,  
#         n=1,  
#         stop=None,  
#         timeout=10  
#     )

#     # Extract the generated cover letter from the response
#     cover_letter = response.choices[0].text.strip()
#     print(cover_letter)

#     # Render a template to display the generated cover letter
#     # return render_template('cover_letter.html', cover_letter=cover_letter)
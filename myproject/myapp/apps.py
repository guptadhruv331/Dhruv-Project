from django.apps import AppConfig


# from flask import Flask, request, render_template
# import smtplib
# from email.mime.text import MIMEText

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/send_email', methods=['POST'])
# def send_email():
#     name = request.form['name']
#     email = request.form['email']
#     message = request.form['message']

#     # Email configuration
#     to_email = 'your-email@example.com'  # Change this to your email
#     subject = 'New message from contact form'
#     body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

#     # Create the email
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = email
#     msg['To'] = to_email

#     try:
#         # Set up the server
#         with smtplib.SMTP('smtp.example.com', 587) as server:  # Change to your SMTP server

# server
#             server.starttls()
#             server.login('your-email@example.com', 'your-email-password')  # Your email login
#             server.sendmail(email, to_email, msg.as_string())
#         return 'Message sent successfully!'
#     except Exception as e:
#         return f'Failed to send message: {str(e)}'

# if __name__ == '__main__':
#     app.run(debug=True)


# class MyappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'myapp'

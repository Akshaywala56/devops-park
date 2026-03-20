import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime

# Gmail credentials
sender_email = "ghanwatakshay@gmail.com"
app_password = ""  # from Google App Password setup

# List of HR emails
recipients = [
    "ghanwatakshay@gmail.com"
]

# Email content
subject = "Inquiry Regarding DevOps / Site Reliability Engineer Opportunities"

body = """\
Dear HR,

I hope this message finds you well.
I am reaching out to express my interest in exploring any current or upcoming opportunities related to DevOps or Site Reliability Engineering within your esteemed organization.

I have practical experience working with AWS, Jenkins, Docker, Python, and Git, along with monitoring tools like Splunk and New Relic.
My work mainly involves automating deployments, improving cloud infrastructure, and ensuring system reliability through effective CI/CD practices.
I have contributed to enhancing automation efficiency and improving system reliability in my current role.

I have attached my updated resume for your review. I would sincerely appreciate it if you could consider my profile and let me know if there are any suitable openings that align with my skills and experience.

Thank you very much for your time and consideration. I truly appreciate your support.
Have a nice day.

Warm regards,
Akshay Ghanwat
Site reliability Engineer
📧 Email: ghanwatakshay@gmail.com
📞 Phone: 8898491950
🐙 GitHub: github.com/Akshaywala56/devops-park
📝 Blog: techwithakshay.hashnode.dev
"""

# Path to your resume (update this path)
resume_path =r"C:\Users\aghanwa\Downloads\000\akshay_ghanwat.pdf"

# Log failed emails
def log_failure(email, reason):
    with open("failed_emails.log", "a") as f:
        f.write(f"{datetime.now()} - {email} - {reason}\n")

# Send emails one by one
for receiver_email in recipients:
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # Attach email body
    msg.attach(MIMEText(body, "plain"))

    # Attach resume
    try:
        with open(resume_path, "rb") as f:
            attach = MIMEApplication(f.read(), _subtype="pdf")
            attach.add_header('Content-Disposition', 'attachment', filename="Akshay_Ghanwat_Resume.pdf")
            msg.attach(attach)
    except Exception as e:
        print(f"⚠️ Could not attach resume for {receiver_email}: {e}")
        log_failure(receiver_email, f"Attachment error: {e}")
        continue

    # Send mail
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
            print(f"✅ Email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"❌ Error sending to {receiver_email}: {e}")
        log_failure(receiver_email, str(e))

print("\n📄 Any failed emails have been logged in 'failed_emails.log'")

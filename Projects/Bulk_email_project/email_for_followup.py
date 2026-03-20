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

# Email content - FOLLOW-UP
subject = "Following Up: DevOps / Site Reliability Engineer Opportunities"

body = """\
Dear HR,

I hope this message finds you well.

I wanted to follow up on my previous message regarding DevOps and Site Reliability Engineering opportunities within your organization.

I remain genuinely enthusiastic about the possibility of joining your team and contributing to your infrastructure and automation initiatives. With my experience in AWS, Jenkins, Docker, Python, and monitoring tools like Splunk and New Relic, I am confident that I can add value to your organization.

Please let me know if there are any suitable openings or if I can provide any additional information about my background and experience.

Thank you very much for your time and consideration. I look forward to hearing from you.

Warm regards,
Akshay Ghanwat
Site Reliability Engineer
📧 Email: ghanwatakshay@gmail.com
📞 Phone: 8898491950
🐙 GitHub: github.com/Akshaywala56/devops-park
📝 Blog: techwithakshay.hashnode.dev
"""

# Path to your resume (update this path)
resume_path = r"C:\Users\aghanwa\Downloads\000\akshay_ghanwat.pdf"

# Log failed emails
def log_failure(email, reason):
    with open("failed_followup_emails.log", "a") as f:
        f.write(f"{datetime.now()} - {email} - {reason}\n")

# Log successful emails
def log_success(email):
    with open("sent_followup_emails.log", "a") as f:
        f.write(f"{datetime.now()} - {email} - Successfully sent\n")

# Send emails one by one
print("🚀 Starting Follow-up Email Campaign...\n")

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
            print(f"✅ Follow-up email sent successfully to {receiver_email}")
            log_success(receiver_email)
    except Exception as e:
        print(f"❌ Error sending to {receiver_email}: {e}")
        log_failure(receiver_email, str(e))

print("\n" + "="*60)
print("📊 Campaign Summary:")
print("="*60)
print("✅ Successful emails logged in: 'sent_followup_emails.log'")
print("❌ Failed emails logged in: 'failed_followup_emails.log'")
print("="*60)


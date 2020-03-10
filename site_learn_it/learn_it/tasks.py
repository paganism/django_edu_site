from django.core.mail import send_mail
from site_learn_it.celery import app


@app.task
def send_mail_from_form(email_to_answer, email_body):
    """
    Send Email from send form
    """
    email_subject = 'Сообщение из формы обратной связи'

    return send_mail(email_subject, email_body, 'root@core', [email_to_answer, 'admin@learn_it.com'])

from django.core import mail
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "UAClassFinder.settings")
with mail.get_connection() as connection:
    mail.EmailMessage(
        "test",
        "this email was sent automatically. :3",
        to = ["sophieguinan@arizona.edu", "dukeospeed@arizona.edu"],
        from_email = "alert@uaclassfinder.co",
        connection=connection,
    ).send(fail_silently=False)
print("worked?")
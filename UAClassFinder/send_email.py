from django.core import mail
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "UAClassFinder.settings")
# with mail.get_connection() as connection:
#     mail.EmailMessage(
#         "test",
#         "this email was sent automatically. :3",
#         to = ["sophieguinan@arizona.edu", "dukeospeed@arizona.edu"],
#         from_email = "alert@uaclassfinder.co",
#         connection=connection,
#     ).send(fail_silently=False)
# print("worked?")

mail.send_mail(
    'Subject here',
    'Here is the message.',
    'alert@uaclassfinder.co',
    ['2002agarwalyash@gmail.com'],
    fail_silently=False,
)
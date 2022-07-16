#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hello.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()



# from django.contrib.auth.models import User
# user = User.objects.get(username='normaluser')
# user.is_superuser = True
# user.save()


# from django.contrib.auth import get_user_model
# def reset_password(u, password):
#     try:
#         user = get_user_model().objects.get(username=u)
#     except:
#         return "User could not be found"
#     user.set_password(password)
#     user.save()
#     return "Password has been changed successfully"
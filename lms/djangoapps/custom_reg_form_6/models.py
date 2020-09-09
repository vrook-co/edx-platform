from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True)

    branches = (
        ('cs', 'Computer Science & Engineering'),
        ('ec', 'Electronics & Communication Engineering'),
        ('eee', 'Electrical & Electronics Engineering'),
        ('is', 'Information Science & Engineering'),
        ('mech', 'Mechanical Engineering'),
        ('mba', 'Management Studies - MBA'),
    )

    years = (
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
    )

    medium = (
        ('books', 'Books'),
        ('blogs', 'Blogs'),
        ('images', 'Images'),
        ('videos', 'Videos'),
        ('others', 'Others'),
    )

    languages = (
        ('eng', 'English'),
        ('kan', 'Kannada'),
        ('hin', 'Hindi'),
        ('othr', 'Others'),
    )

    student_interests = (
            ('ai/ml', 'AI/ML'),
            ('iot', 'IoT'),
            ('cyber security', 'Cyber Security'),
            ('machine drawing', 'Machine Drawing'),
            ('autonomous vehicles', 'Autonomous Vehicles'),
            ('others', 'Others'),
    )


    branch = models.CharField(
        verbose_name="Branch",
        choices=branches,
        max_length=100,
    )

    year = models.CharField(
        verbose_name="Year",
        choices=years,
        max_length=5,
    )

    preferred_medium = models.CharField(
        verbose_name="Preferred Medium",
        choices=medium,
        max_length=100,
    )


    preferred_language = models.CharField(
        verbose_name="Preferred Language",
        choices=languages,
        max_length=100,
    )

    interests = models.CharField(
        verbose_name="Your Interests",
        choices=student_interests,
        max_length=100,
    )



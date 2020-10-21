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
        ('cs', 'Computer Science Engineering'),
        ('ec', 'Electronics & Communication Engineering'),
        ('eee', 'Electrical & Electronics Engineering'),
        ('is', 'Information Science Engineering'),
        ('mech', 'Mechanical Engineering'),
        ('mba', 'Management Studies - MBA'),
    )

    years = (
        ('1', '1st year'),
        ('2', '2nd year'),
        ('3', '3rd year'),
        ('4', '4th year'),
    )

    medium = (
        ('books', 'Books'),
        ('blogs', 'Blogs'),
        ('articles', 'Articles'),
        ('journals', 'Journals'),
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
            ('cloud computing', 'Cloud Computing'),
            ('robotics', 'Robotics'),
            ('3d printing', '3D Printing'),
            ('machine drawing', 'Machine Drawing'),
            ('autonomous vehicles', 'Autonomous Vehicles'),
            ('entrepreneurship', 'Entrepreneurship'),
            ('others', 'Others'),
    )


    branch = models.CharField(
        verbose_name="Department",
        choices=branches,
        max_length=100,
    )

    year = models.CharField(
        verbose_name="Year of Study",
        choices=years,
        max_length=5,
    )

    preferred_medium = models.CharField(
        verbose_name="Preferred Medium of Learning",
        choices=medium,
        max_length=100,
    )


    preferred_language = models.CharField(
        verbose_name="Preferred Medium of Language",
        choices=languages,
        max_length=100,
    )

    interests = models.CharField(
        verbose_name="Your Interest",
        choices=student_interests,
        max_length=100,
    )



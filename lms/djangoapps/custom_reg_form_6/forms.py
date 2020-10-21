from .models import ExtraInfo
from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)

        self.fields['branch'].error_messages = {
            "required": u"Please select your department.",
            "invalid": u"Sorry, you may have entered a non-existent department.",
        }

        self.fields['year'].error_messages = {
            "required": u"Please select your year of study",
            "invalid": u"Sorry, you may have entered an invalid year.",
        }

        self.fields['preferred_language'].error_messages = {
            "required": u"Your preferred medium of language.",
            "invalid": u"Sorry, you may have entered a foreign language",
        }

        self.fields['preferred_medium'].error_messages = {
            "required": u"Your preferred medium of learning.",
            "invalid": u"Sorry, you may have entered a non-available medium.",
        }

        self.fields['interests'].error_messages = {
            "required": u"Please enter your area of interests.",
            "invalid": u"Sorry, you may have entered a non-available field of interest",
        }

        #self.fields['interests'].widget = CheckboxSelectMultiple()
        #self.fields['interests'].queryset = ExtraInfo.objects.all()

    class Meta(object):
        model = ExtraInfo
        fields = ('branch', 'year', 'preferred_language', 'preferred_medium', 'interests')


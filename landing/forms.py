__author__ = 'chaga'
from django import forms
from .models import UserLead
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import FormActions, StrictButton

class UserLeadForm(forms.ModelForm):
    class Meta:
        model = UserLead
        fields = [
            'f_name',
            'email'
        ]
    def __init__(self, *args, **kwargs):
        super(UserLeadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Enter your email here to be sent a free pdf:',
                'f_name',
                'email'
            ),
            FormActions(
                Submit('enter', 'Get your FREE PDF!', css_class='btn btn-block btn-primary')
            )
        )
from django import forms
# Same App importing
from newsletters.models import NewsLetterUsers


class NewsLetterUsersSignUpForm(forms.ModelForm):
    """Form for input emails"""
    class Meta:
        model = NewsLetterUsers
        fields = ['email']

        def clean_email(self, email=None):
            """Cleaned email data"""
            email = self.clean_email(email)
            return email


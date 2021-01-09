from django import forms

class InquiryForm(forms.Form):
    client_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'client_name',
                'placeholder': 'Your first name',
            }
        )
    )
    client_email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'client_email',
                'placeholder': 'Your Email address',
            }
        ))
    client_message = forms.CharField(
        initial='Hi Joe, there is a project I would like to discuss with you. \n',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'client_message',
                'placeholder': 'Your inquiry',
            }
        )
    )
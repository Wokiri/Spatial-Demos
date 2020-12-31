from django import forms

class InquiryForm(forms.Form):
    client_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'client_name',
                'placeholder': 'Your name',
            }
        )
    )
    client_email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'client_email',
                'placeholder': 'Your Email addres',
            }
        ))
    client_message = forms.CharField(initial='Hi Joe, I would like ',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'client_message',
                'placeholder': 'Your inquiry',
            }
        )
    )
from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(min_length=3, max_length=100)
    email = forms.EmailField(required=False, label='E-mail')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        # Function start with "clean_"
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Input more than 4 words!")
        return message

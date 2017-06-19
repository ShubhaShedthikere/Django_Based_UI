from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class StartForm(forms.Form):
    start_point = forms.CharField(label= " Enter the starting point :", max_length=100)

class EndForm(forms.Form):
    ending_point = forms.CharField(label= " Enter the ending point :", max_length=100)

class MobileNoForm(forms.Form):
     mobile_no= forms.CharField(label= " Enter your mobile number :", max_length=100)
from django import forms

class Signupform(forms.Form):
	username = forms.CharField(max_length=50,required=True)
	email = forms.EmailField(required=True)
	password = forms.CharField(max_length = 30,min_length = 3,required=True)



class Loginform(forms.Form):
	username = forms.CharField(max_length=50,required=True)
	password = forms.CharField(max_length = 30, min_length = 3,required=True	)

from django import forms

class StudentRegForm(forms.Form):
	name = forms.CharField(label='name',max_length = 20)
	password = forms.CharField(label='pwd',max_length = 20, min_length = 8)
	email forms.EmailField()

class StudentLoginForm(forms.Form):
	name = forms.CharField(label='name', max_length = 20)
	password = forms.CharField(label='pwd', max_length = 20, min_length = 8)
	
    

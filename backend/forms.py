from django import forms

class StudentRegForm(forms.Form):
	name = forms.CharField(label='name',max_length = 20)
	pwd = forms.CharField(label='pwd',max_length = 20, min_length = 8)
	email = forms.EmailField(label='email')

class StudentLoginForm(forms.Form):
	name = forms.CharField(label='name', max_length = 20)
	pwd = forms.CharField(label='pwd', max_length = 20, min_length = 8)


class PasswordModifyForm(forms.Form):
	id = forms.IntegerField()
	oldpwd = forms.CharField(label='pwd',max_length = 20, min_length = 8)
	newpwd = forms.CharField(label='pwd',max_length = 20, min_length = 8)
    # TODO: Define form fields here
    


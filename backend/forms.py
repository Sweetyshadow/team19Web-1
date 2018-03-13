from django import forms

class StudentRegForm(forms.Form):
	name = forms.CharField(label='name',max_length = 20)
	studentID = forms.CharField(label='studentID',max_length = 20)
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
    
class TeamAddForm(forms.Form):
	invitecode = forms.CharField(label='invitecode',max_length = 20)
	userid = forms.IntegerField()
	teamname = forms.CharField(label='teamname',max_length = 30)
	
    # TODO: Define form fields here
    

class EmailValidation(forms.Form):
	userid = forms.CharField()
    email = forms.EmailField()

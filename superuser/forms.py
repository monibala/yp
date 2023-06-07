from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from django.contrib.admin import (
      widgets,
      site as admin_site
    )

def GenForm(Model,listHiddenfield=[]):
    data = {field:forms.HiddenInput() for field in listHiddenfield}
    class newform(forms.ModelForm):
        class Meta:
            model = Model
            exclude = ('id',)
            widgets = data
        def __init__(self, *args, **kwargs):
            super(newform, self).__init__(*args, **kwargs)
            for f in Model._meta.fields:
                if "DateTimeField" in str(type(f)):
                    print('DateTimeField is present',f.name)
                    try:
                        self.fields[f.name].widget.attrs['class'] = 'vDateTime'
                    except Exception:
                        pass
                if "ForeignKey" in str(type(f)):
                    print('ForeignKey is present',f.name)
                    try:
                        self.fields[f.name].widget  = widgets.RelatedFieldWidgetWrapper(
                        self.fields[f.name].widget,
                        self.instance._meta.get_field(f.name).remote_field,
                        admin_site
                    )
                    except Exception:
                        pass
                if "ManyToManyField" in str(type(f)):
                    print('ManyToManyField is present',f.name)
                    try:
                        pass
                    except Exception:
                        pass 
                           
    return newform  
class adminform(forms.ModelForm):
	old_password = forms.CharField(label=("old_password"), required=True,
                                    widget=forms.PasswordInput)
	new_password = forms.CharField(label=("new_password"), required=True,
                                    widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('old_password','new_password')
class loginform(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder':'Enter the email'}))
    password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'password'}),max_length=30)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(email=username).exists() is False:
            raise forms.ValidationError("this mail is not registered")
        else:
            return username

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column,Field



STATES = (
    ('', 'Choose...'),
    ('Tokyo', 'Tokyo'),
    ('Osaka', 'Osaka'),
    ('Okayama', 'Okayama')
)


class SignUpForm(forms.Form,forms.ModelForm):
  
    first_name = forms.CharField(max_length=100,label='姓', required=True)
    last_name = forms.CharField(max_length=100, label='名',required=True)
    username = forms.CharField(max_length=100, label='お名前 ',required=True)
    jpst_name = forms.CharField(max_length=100,label='セイ', required=True)
    jpnd_name = forms.CharField(max_length=100, label='メイ',required=True)
    furiganauser = forms.CharField(max_length=100, label='フリガナ ',required=True)
    email = forms.EmailField(max_length=250, label='Eメールアドレス', widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    city = forms.CharField(label='市区町村 ')
    place = forms.CharField(label='それ以降の住所 必須')
    apartment = forms.CharField(label='マンション名等 ')
    
   
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email','zip_code','city','place','apartment')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-4 mb-0'),
                Column('first_name', css_class='form-group col-md-4 mb-0'),
                Column('last_name', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('furiganauser', css_class='form-group col-md-4 mb-0'),
                Column('jpst_name', css_class='form-group col-md-4 mb-0'),
                Column('jpnd_name', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('city', css_class='form-group col-md-4 mb-0'),
                Column('place', css_class='form-group col-md-4 mb-0'),
                Column('apartment', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),

             Submit('submit', 'Sign in')

            
        )
        
        
        


from django.contrib.auth.models import User
from django import forms

# 폼 > html - 프론트단에서 사용자의 입력을 받는 인터페이스
# 장고의 폼 : html의 폼 역활, 데이터 베이스에 저장할 내용을 형식, 제약 조건 설정

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    class Meta:
        moder = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']
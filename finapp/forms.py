from django import forms

class RegForm(forms.Form):
   fname = forms.CharField(max_length = 100)
   nname = forms.CharField(max_length = 100)
   sname = forms.CharField(max_length = 100)
   cname = forms.CharField(max_length = 100)
   cityname = forms.CharField(max_length = 200)
   email = forms.CharField(max_length = 100)
   phone = forms.CharField(max_length = 100)
   uname = forms.CharField(max_length = 100)
   psw = forms.CharField(widget = forms.PasswordInput())
   pswrpt = forms.CharField(widget = forms.PasswordInput())

class InvestReg(forms.Form):
   ifname = forms.CharField(max_length = 100)
   inname = forms.CharField(max_length = 100)
   isname = forms.CharField(max_length = 100)
   #icname = forms.ChoiceField(choices=["10000","Hello","Hello"])
   #icityname = forms.ChoiceField(choices=["10000"])
   iemail = forms.CharField(max_length = 100)
   iphone = forms.CharField(max_length = 100)
   iuname = forms.CharField(max_length = 100)
   ipsw = forms.CharField(widget = forms.PasswordInput())
   ipswrpt = forms.CharField(widget = forms.PasswordInput())

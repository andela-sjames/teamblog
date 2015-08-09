#form used directly in html  file without creating form directly on html page.....
from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.forms import AdminAuthenticationForm
 

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required=True)


    class meta:
        model = AbstractUser
        fields = (('first_name','last_name'),'username','email','password1','password2')



    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_staff = True

        if commit:
            user.save()
        return user



class UserAdminAuthenticationForm(AdminAuthenticationForm):
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        message = ERROR_MESSAGE
        
        if username and password:
            self.user_cache = authenticate(username=username,
            password=password)
            if self.user_cache is None:
                if u'@' in username:
                    # Mistakenly entered e-mail address instead of username?
                    # Look it up.
                    try:
                        user = User.objects.get(email=username)
                    except (User.DoesNotExist, User.MultipleObjectsReturned):
                        # Nothing to do here, moving along.
                        pass
                    else:
                        if user.check_password(password):
                            message = _("Your e-mail address is not your "
                                        "username."
                                        " Try '%s' instead.") % user.username
                raise forms.ValidationError(message)
            # Removed check for is_staff here!
            elif not self.user_cache.is_active:
                raise forms.ValidationError(message)
        self.check_for_test_cookie()
        return self.cleaned_data
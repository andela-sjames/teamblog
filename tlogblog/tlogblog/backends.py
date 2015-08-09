"""from tlogblog.forms import NewAuthenticationForm
from django.contrib.auth.models import check_password, AbstractUser

class NewAuthenticationFormAuthBackend(object):

    def authenticate(self, username=None, password=None):
        try:

            username = NewAuthenticationForm.objects.get(username=username)
            password = NewAuthenticationForm.objects.get(password=password)

            if check_password(password):
                # Authentication success by returning the user
                return user
            else:
                # Authentication fails if None is returned
                return None
        except AbstractUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return NewAuthenticationForm.objects.get(id=user_id)
        except AbstractUser.DoesNotExist:
            return None"""
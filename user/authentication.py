from django.contrib.auth import get_user_model

User = get_user_model()


class EmailAuthBackend:
    """ Authenticate using an email address """

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except (User.DoesNotExist):
            return None

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

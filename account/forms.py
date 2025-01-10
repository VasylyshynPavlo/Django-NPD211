from mongoengine.django.forms import DocumentForm

class LoginForm(DocumentForm):
    class Meta:
        model = user
        fields = ['usernameOrEmail', 'password']
django-userauthcode
===================

Generate Django user authentication codes to verify email addresses and
activate user accounts. Unlike other solutions django-userauthcode does not
need to store any data in your database.


Examples:
---------

### url.conf
```
url(r'^register/$', 'views.register', name='register'),
url(r'^activate/(?P<username>[a-zA-Z0-9_@+.-]+)/(?P<auth_code>[a-zA-Z0-9_-]+)$', 'views.activate', name='activate'),
```

### views.py
```
# Persistend UserAuthCode generator
from userauthcode import UserAuthCode
uac = UserAuthCode(settings.SECRET_KEY)
 

def register(request):

    ...

    username = form.cleaned_data['username']
    email = form.cleaned_data['email']
    password = form.cleaned_data['password']

    user = User.objects.create_user(username, email, password)
    user.is_active = False

    auth_code = uac.auth_code(user)

    r = reverse('activate', kwargs={'auth_code': auth_code, 'username': username })
    url = request.build_absolute_uri(r)

    send_mail('Activation Link', url, 'info@example.com', [email,], fail_silently=False)

    user.save()

    ...


def activate(request, username, auth_code):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExists:
        raise Http404

    if uac.is_valid(user, auth_code):
        user.is_active = True
        user.save()
        messages.info(request, _('Your account has been activated. You can now use your username and password to login.'))
        return redirect('/');
    
    raise Http404
```

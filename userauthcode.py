import hashlib
import string
import random
import base64


""" UserAuthCode generates an authentication code for a Django user object.
    This code can be used to verify the user's email address and to activate
    his account. Unlike other solutions there's no need to store any data in
    your database. """
    

class UserAuthCode(object):
    def __init__(self, secret, salt_len=8, hash=hashlib.sha256):
        self.secret = secret
        self.salt_len = salt_len
        self.hash = hash

    def salt(self):
        s = ''
        for i in range(self.salt_len):
            s += random.choice(string.letters + string.digits)

        return s

    def digest(self, user, salt):
        # Use username, email and date_joined to generate digest
        auth_message = ''.join((self.secret, user.username, user.email,
            str(user.date_joined), salt))
        md = self.hash()
        md.update(auth_message)

        return base64.urlsafe_b64encode(md.digest()).rstrip('=')

    def auth_code(self, user):
        salt = self.salt()
        digest = self.digest(user, salt)

        return salt + digest

    def is_valid(self, user, auth_code):
        salt = auth_code[:self.salt_len]
        digest = auth_code[self.salt_len:]
 
        # CAVEAT: Make sure UserAuthCode cannot be used to reactivate locked
        # profiles.
        if user.last_login != user.date_joined:
            return False

        return digest == self.digest(user, salt)


if __name__ == '__main__':
    import datetime
    class DjangoLikeUserObject(object):
        username = 'johndoe'
        email = 'john@example.org'
        date_joined = datetime.datetime.now()

    user = DjangoLikeUserObject()
    uac = UserAuthCode('Put your secret here.')
    auth_code = uac.auth_code(user)

    print auth_code
    print uac.is_valid(user, auth_code)

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.tokens import PasswordResetTokenGenerator

def active_required(view_func):
    decorated_view = user_passes_test(lambda u: u.is_active, login_url='login')(view_func)
    return decorated_view


# This class is used to generate tokens for password reset and email verification
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(timestamp) + str(user.is_active)

account_activation_token = AccountActivationTokenGenerator()
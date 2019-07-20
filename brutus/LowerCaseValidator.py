import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class LowerCharaterValidation:
    """ Validate if the password has  lowercase characters """
    def validate(self,password,user=None):
        if re.search("[a-z]",password)==None:
            raise ValidationError(_("This password does not contain at least one lower case"),code="Password is weak")

    def get_help_text(self):
        return _("Password must contain at least one Lower Case Character")

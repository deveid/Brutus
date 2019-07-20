import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class ComplexLengthValidation:
    """ Validate if the length of the password has a minmum of 16 characters"""
    def validate(self,password,user=None):
        if len(password) <16:
            raise ValidationError(_("The password must contain 16 characters"),code="Password is weak")

    def get_help_text(self):
        return _("Your Password must contain at least 16 character")

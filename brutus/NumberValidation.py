from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import re

class NumberValidator:
    """ Checks if the password contains 3 Numbers"""

    def validate(self,password,user=None):
        if len(re.findall("\d+",password)) < 3 :
            raise ValidationError(_("Password should contain at least 3 Numbers"),code="Password is weak")

    def get_help_text(self):
        return _("Password must contain at least 3 Numbers")
    
from django.core.exceptions import ValidationError
import re
from django.utils.translation import ugettext as _

class UpperCharacterValidation:
    """Validates if the password contains Uppercase Character"""

    def validate(self,password,user=None):
        if re.search("[A-Z]{2}",password) == None:
            raise ValidationError(_("first two Character of the password must contain 2 UpperCase Character"),code="Password is weak")

    def get_help_text(self):
        return ("The first two Character of the password must contain 2 UpperCase Character")
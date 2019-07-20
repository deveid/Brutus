import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class SymbolValidationError:
    """Checks if the password contains two symbols"""
    
    def validate(self,password,user=None):
        if len(re.findall("[@#$%^&*()!]",password)) < 2 :
            raise ValidationError(_("Password Must Contain at least 2 symbols"),code="Password is Weak")

    def get_help_text(self):
        return ("Password must Contain at least 2 symbols( e.g @#$%^&*)")
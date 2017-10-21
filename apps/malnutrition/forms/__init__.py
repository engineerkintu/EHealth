# I found my self writing lots of forms for SMS and handling the validation
# which was a bit annoying
# # sort of based on django forms, this is a form library that takes the incoming text
# in an sms, assumes that its a series of fields, then parses the text into those fields
from apps.malnutrition.forms.forms import Form
from apps.malnutrition.forms.fields import StringField, GenderField, BooleanField, DateField, FloatField
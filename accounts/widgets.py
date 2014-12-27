from django.forms import TextInput
from django.template.loader import render_to_string

class TimeWidget(TextInput):
    def render(self, name, value, attrs=None):
        context = {
            'name': name,
            'value': value,
        }
        return render_to_string('accounts/widgets/date_time.html', context)

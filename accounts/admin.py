from django.contrib import admin
from .forms import HourForm
from .models import User, Hour


class HourInline(admin.TabularInline):
    model = Hour
    form = HourForm
    extra = 1

class UserAdmin(admin.ModelAdmin):
    
    inlines = (HourInline,)

    class Media:
        css = {
            'all': (
                '//ajax.googleapis.com/ajax/libs/jqueryui/1.10.4/themes/smoothness/jquery-ui.css',
                '/static/css/jquery.timepicker.css',
            )
        }
        js = (
            '/static/js/vendor/jquery-ui-1.10.4.custom.min.js',
            '/static/js/vendor/jquery.timepicker.min.js',
        )


admin.site.register(User, UserAdmin)
    
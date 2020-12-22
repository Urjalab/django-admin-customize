from django.contrib import admin

from .models import Person


class PersonAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'age',
        'salary',
        'is_married',
        'dob',
        '_description',
    )

    ordering = (
        'name',
    )

    search_fields = (
        'name',
    )

    list_filter = (
        'is_married',
        'dob',
    )

    # list_editable = (
    #     'is_married',
    #     'age',
    # )

    list_per_page = 5 # numeric value

    date_hierarchy = 'dob' # not a tuple

    change_list_template = 'demo/index.html'

    fieldsets = (
        ('Basic Info', {
            "fields": (
                'name',
                'age',
            ),
        }),
        ('Other', {
            "fields": (
                'is_married',
                'salary',
                'dob',
            ),
        }),
        ('Description', {
            "fields": (
                'description',
            ),
        })
    )
    

    def _description(self, obj):
        return obj.description[:10] + ' ...'





admin.site.register(Person, PersonAdmin)

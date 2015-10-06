from django.contrib import admin
from authors.models import UserProfile, Abstract
from django.contrib.auth.models import User


class AbstractAdmin(admin.ModelAdmin):
    list_display = ('short_title', 'view_link', 'status', 'date', 'id')

    def short_title(self, obj):
        return ("%s ..." % (obj.title[:100]))
    short_title.short_description = 'Title'

    def view_link(self, obj):
        return u"<a href='/programme/profiles/%d'>%s</a>" % (obj.author.user.id, obj.author.user.last_name)
    view_link.short_description = 'author'
    view_link.allow_tags = True
    


admin.site.register(UserProfile)
admin.site.register(Abstract, AbstractAdmin)



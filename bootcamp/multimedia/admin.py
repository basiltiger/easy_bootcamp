from django.contrib import admin

from embed_video.admin import AdminVideoMixin

from .models import *

class MultimediaAdminMixin(AdminVideoMixin, admin.ModelAdmin):
	pass

class CategorieMediaAdmin(admin.ModelAdmin):
	pass

admin.site.register(CategorieMedia, CategorieMediaAdmin)
admin.site.register(Multimedia, MultimediaAdminMixin)




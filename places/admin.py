from django.contrib import admin
from django.utils.html import format_html

from .models import Places, Image



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ["get_preview"]

    def get_preview(self, obj):
        return format_html('<img src="{}" height={height} />'.format(obj.image.url, height=200))


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ["get_preview"]

    def get_preview(self, obj):
        return format_html('<img src="{}" height={height} />'.format(obj.image.url, height=200))

    fields = ('image', 'get_preview', 'image_number')


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


#admin.site.register(Places)
#admin.site.register(Image)

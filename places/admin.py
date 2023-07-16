from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from .models import Places, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        return format_html('<img src="{}" height={height} />'.format(obj.image.url, height=200))


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 2
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        return format_html('<img src="{}" height={height} />'.format(obj.image.url, height=200))

    fields = ('image', 'get_preview', 'image_number')


@admin.register(Places)
class PlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = (ImageInline,)


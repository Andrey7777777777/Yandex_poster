from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from .models import Places, Image
from download_tools import get_image_preview


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        return get_image_preview(self, obj)


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 2
    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        return get_image_preview(self, obj)

    fields = ('image', 'image_preview', 'image_number')


@admin.register(Places)
class PlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = (ImageInline,)


from django.utils.html import format_html


def get_image_preview(self, obj):
    return format_html('<img src="{}" height={height} />', obj.image.url, height=200)

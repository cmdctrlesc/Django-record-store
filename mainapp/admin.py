from django.contrib import admin
from .models import Record, Label, Artist


class RecordAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ("artist", "title")

    readonly_fields = ("labelname",)

    def labelname(self, obj):
        return obj.label.name


admin.site.register(Record, RecordAdmin)


class LabelAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Label, LabelAdmin)


class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Artist, ArtistAdmin)

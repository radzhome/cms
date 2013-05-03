from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from search.models import SearchKeyword


class SearchKeywordInline(admin.StackedInline):
    model = SearchKeyword
#class SearchKeywordAdmin(admin.ModelAdmin):
#    pass

class FlatPageAdminWithKeywords(FlatPageAdmin):
    inlines = [SearchKeywordInline]

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminWithKeywords)
#admin.site.register(SearchKeyword, SearchKeywordAdmin)

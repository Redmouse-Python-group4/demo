from blog.models import Article, Category, Comment
from django.contrib import admin

# Register your models here.
def make_published(modeladmin, request, queryset):
    queryset.update(is_active=True)
make_published.short_description = "Mark selected article as published"

def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_active=False)
make_unpublished.short_description = "Mark selected article as unpublished"

def make_revert_pub_article(modeladmin, request, queryset):
    for i in queryset:
        i.is_active = not i.is_active
        i.save()
make_revert_pub_article.short_description="Is Active revert"

class ArticleAdmin(admin.ModelAdmin):
    actions = [make_published, make_unpublished, make_revert_pub_article]
    actions_on_bottom = True
    # actions_selection_counter = False
    date_hierarchy = 'date_create'
    # fields = ('is_active', )
    # exclude = ('is_active', )
    readonly_fields = ('date_create', 'date_update')
    fieldsets = (
        (None, {
            'fields': ('title', 'body')
        }),
        ('Advanced options', {
            # 'classes': ('colla pse',),
            'fields': ('is_active', 'category')
        }),
        ('Date Article', {
            'classes': ('collapse',),
            'description': 'Date pub and update',
            'fields': ('date_create', 'date_update')
        }),
    )
    list_display = ('title', 'date_create', 'date_update', 'is_active', 'get_rating')
    list_display_links = ('date_create', 'title' )
    list_editable = ('is_active',)
    list_filter = ('is_active', 'category', 'date_create', 'date_update')
    list_per_page = 3
    ordering = ('is_active', 'date_create', 'date_update')
    radio_fields = {"category": admin.HORIZONTAL}
    # raw_id_fields = ("category",)
    save_as = True
    save_on_top = True
    search_fields = ('title', 'body')

    def delete_view(self, request, object_id, extra_context=None):
        obj = self.get_object(request, object_id)
        obj.title='DELETE %s'%obj.title
        obj.is_active=False
        obj.save()

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
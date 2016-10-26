from blog.models import Category
def get_all_category(req):
    category = Category.objects.filter(is_active=True)
    return {'category': category}
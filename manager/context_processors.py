from manager.models import Category

def allCategories(request):
    categories=Category.objects.all()
    return dict(book_categories=categories)
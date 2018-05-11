from .models import Category

def movies_categories(request):
    """
    Add movies categories to the context.
    """
    return {'MOVIES_CATEGORIES': Category.objects.all()}
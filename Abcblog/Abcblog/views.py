from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from manage_post.models import Article, Category

class IndexView(TemplateView):
    template_name = 'pages/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener artículos recientes (activos)
        context['recent_articles'] = Article.objects.filter(
            status=True
        ).select_related('user_id').prefetch_related('categories').order_by('-created')[:6]
        
        # Obtener artículo destacado (el más reciente)
        context['featured_article'] = Article.objects.filter(
            status=True
        ).select_related('user_id').prefetch_related('categories').first()
        
        # Obtener categorías destacadas
        context['featured_categories'] = Category.objects.filter(
            status=True, 
            featured=True
        ).order_by('-created')[:8]
        
        # Obtener todas las categorías para el menú
        context['all_categories'] = Category.objects.filter(
            status=True
        ).order_by('name')
        
        return context
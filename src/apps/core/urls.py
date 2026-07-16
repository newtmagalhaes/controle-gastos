from django.urls import path

from . import views

urlpatterns = [
    path('', views.MesAtualRedirectView.as_view(), name='home'),
    path('<int:year>/<int:month>/', views.DespesasMensaisView.as_view(), name='despesas_mensais'),
    path('categorias/', views.CategoriasListView.as_view(), name='categorias_list'),
]

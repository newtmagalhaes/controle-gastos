from django.urls import include, path

from . import views

_categorias = [
    path('', views.CategoriasListView.as_view(), name='categorias_list'),
]

_despesas = [
    path('', views.MesAtualRedirectView.as_view(), name='home'),
    path('<int:year>/<int:month>/', views.DespesasMensaisView.as_view(), name='despesas_mensais'),
]

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('despesas/', include(_despesas)),
    path('categorias/', include(_categorias)),
]

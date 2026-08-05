from django.urls import include, path

from . import views

_categorias = [
    path('', views.CategoriasListView.as_view(), name='categorias_list'),
    path('<uuid:slug>/', views.CategoriasUpdateView.as_view(), name='categoria_update'),
    path('<uuid:pk>/despesas/', views.CategoriaBulkUpdateView.as_view(), name='item_despesa_update'),
    path('<uuid:slug>/edit/', views.CategoriasUpdateView.as_view(), name='categoria_update'),
]

_despesas = [
    path('<uuid:pk>/delete/', views.ItemDespesaDeleteView.as_view(), name='item_despesa_delete'),
    path('', views.MesAtualRedirectView.as_view(), name='home'),
    path('<int:year>/<int:month>/', views.DespesasMensaisView.as_view(), name='despesas_mensais'),
]

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('despesas/', include(_despesas)),
    path('categorias/', include(_categorias)),
]

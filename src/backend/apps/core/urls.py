from django.urls import path

from . import views

urlpatterns = [
    path('', views.CategoriasListView.as_view()),
    path('<int:year>/<int:month>/', views.DespesasMensaisView.as_view(), name='despesas_mensais')
]

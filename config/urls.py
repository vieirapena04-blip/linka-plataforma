from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from vitrines import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('v/<slug:slug>/', views.vitrine_publica, name='vitrine_publica'),
    path('vitrines/', views.institucional, {'page': 'vitrines'}, name='vitrines'),
    path('como-funciona/', views.institucional, {'page': 'como-funciona'}, name='como_funciona'),
    path('suporte/', views.institucional, {'page': 'suporte'}, name='suporte'),
    path('termos/', views.institucional, {'page': 'termos'}, name='termos'),
    path('painel/', views.dashboard, name='dashboard'),
    path('painel/produtos/novo/', views.produto_novo, name='produto_novo'),
    path('conta/entrar/', auth_views.LoginView.as_view(template_name='vitrines/login.html'), name='login'),
    path('conta/criar/', views.cadastro, name='cadastro'),
    path('conta/recuperar-senha/', auth_views.PasswordResetView.as_view(template_name='vitrines/password_reset.html', email_template_name='vitrines/password_reset_email.txt'), name='password_reset'),
    path('conta/recuperar-senha/enviado/', auth_views.PasswordResetDoneView.as_view(template_name='vitrines/password_reset_done.html'), name='password_reset_done'),
    path('conta/nova-senha/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='vitrines/password_reset_confirm.html'), name='password_reset_confirm'),
    path('conta/nova-senha/concluida/', auth_views.PasswordResetCompleteView.as_view(template_name='vitrines/password_reset_complete.html'), name='password_reset_complete'),
    path('conta/sair/', auth_views.LogoutView.as_view(), name='logout'),
]

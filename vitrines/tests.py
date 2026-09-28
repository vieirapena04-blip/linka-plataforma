from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class VitrineTests(TestCase):
    def setUp(self):
        self.seller = User.objects.create_user('lara', password='teste-seguro-123')

    def test_public_product_appears_in_home_and_links_to_partner(self):
        from .models import Vitrine, Produto
        shop = Vitrine.objects.create(owner=self.seller, slug='lara-indica', name='Lara Indica')
        product = Produto.objects.create(
            vitrine=shop, name='Sérum facial', description='Produto parceiro',
            category='beleza', price='59.90', partner_url='https://example.com/afiliado', active=True,
        )
        response = self.client.get(reverse('home'))
        self.assertContains(response, product.name)
        self.assertContains(response, product.partner_url)

    def test_seller_can_create_product_only_in_own_showcase(self):
        from .models import Vitrine
        Vitrine.objects.create(owner=self.seller, slug='lara-indica', name='Lara Indica')
        self.client.login(username='lara', password='teste-seguro-123')
        response = self.client.post(reverse('produto_novo'), {
            'name': 'Perfume', 'description': 'Original', 'category': 'beleza',
            'price': '120.00', 'partner_url': 'https://example.com/link-afiliado', 'image_url': '',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.seller.vitrines.first().produtos.count(), 1)

    def test_unauthenticated_user_is_redirected_from_dashboard(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/conta/entrar/', response.url)

    def test_visitor_can_register_and_open_dashboard(self):
        response = self.client.post(reverse('cadastro'), {
            'username': 'novo-vendedor', 'email': 'novo@example.com',
            'password1': 'Senha-Forte-123!', 'password2': 'Senha-Forte-123!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='novo-vendedor').exists())
        dashboard = self.client.get(reverse('dashboard'))
        self.assertEqual(dashboard.status_code, 200)

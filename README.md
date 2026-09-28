# Vitrine Link

MVP Django para vitrines de produtos com links de afiliados. A plataforma não processa pagamentos: o botão redireciona o visitante ao parceiro.

## Incluído
- Login por conta Django e painel privado.
- Vitrine pública por vendedor em `/v/<slug>/`.
- Cadastro de produto com nome, descrição, categoria, preço, imagem por URL e link de parceiro.
- Busca pública por produto.
- Links externos com `nofollow sponsored noopener`.

## Rodar localmente
```bash
python manage.py migrate
python manage.py runserver
```

## Produção
Hospede em serviço Python (Render, Railway, Fly.io etc.). Não envie este projeto para Netlify como ZIP estático. Defina as variáveis de `.env.example`, use PostgreSQL, e configure envio de e-mail antes de habilitar recuperação de senha.

## Limites desta versão
Não há integração automática com APIs de afiliados, rastreamento de cliques, compartilhamento em redes sociais, cadastro público ou recuperação de senha por e-mail. Esses recursos dependem de credenciais e regras de cada parceiro/provedor de e-mail.

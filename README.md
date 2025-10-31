# Brevo Auto Delete

Script automatizado para exclusão de contatos do Brevo usando Selenium.

## Configuração

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure as variáveis de ambiente:
   - Copie o arquivo `.env` e ajuste suas credenciais
   - **IMPORTANTE**: Nunca commite o arquivo `.env` no repositório

3. Execute o script:
```bash
python brevo_auto_delete.py
```

## Variáveis de Ambiente

O arquivo `.env` deve conter:
```
BREVO_EMAIL=seu_email@exemplo.com
BREVO_PASSWORD=sua_senha_aqui
```

## Segurança

- As credenciais são carregadas do arquivo `.env`
- O arquivo `.env` está incluído no `.gitignore` para evitar exposição acidental
- Nunca compartilhe suas credenciais no código fonte
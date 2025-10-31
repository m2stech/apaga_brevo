# 🗑️ Brevo Auto Delete

Script automatizado para exclusão em massa de contatos do Brevo usando Selenium WebDriver.

## ⚠️ **IMPORTANTE - LEIA ANTES DE USAR**

⚠️ **Este script deleta TODOS os contatos do Brevo de forma permanente!**
⚠️ **Use com extrema cautela - não há como desfazer esta ação!**
⚠️ **Recomenda-se fazer backup dos contatos antes de executar**

## 🚀 Instalação e Configuração

### 1. **Clone o repositório**
```bash
git clone https://github.com/m2stech/apaga_brevo.git
cd apaga_brevo
```

### 2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

### 3. **Configure suas credenciais**
Crie um arquivo `.env` na raiz do projeto com suas credenciais do Brevo:

```bash
# Crie o arquivo .env (não está no repositório por segurança)
touch .env
```

Edite o arquivo `.env` e adicione:
```env
# Suas credenciais do Brevo
BREVO_EMAIL=seu_email@exemplo.com
BREVO_PASSWORD=sua_senha_do_brevo
```

### 4. **Instale o ChromeDriver**
- Certifique-se de ter o Google Chrome instalado
- O ChromeDriver deve estar no PATH ou na pasta do projeto
- Download: https://chromedriver.chromium.org/

### 5. **Execute o script**
```bash
python brevo_auto_delete.py
```

## 📋 Como Funciona

O script executa os seguintes passos automaticamente:

1. **Login no Brevo** usando suas credenciais
2. **Navega para a seção Contatos**
3. **Loop de exclusão**:
   - Configura 100 contatos por página
   - Seleciona todos os contatos visíveis
   - Exclui o lote atual
   - Repete até não haver mais contatos
4. **Aguarda confirmação** antes de fechar

## 🔒 Segurança

✅ **Suas credenciais estão seguras:**
- Armazenadas apenas no arquivo `.env` local
- O arquivo `.env` está no `.gitignore`
- Credenciais nunca são enviadas ao repositório
- Cada usuário deve configurar suas próprias credenciais

## 📁 Estrutura do Projeto

```
apaga_brevo/
├── brevo_auto_delete.py    # Script principal
├── requirements.txt        # Dependências Python
├── .gitignore             # Arquivos ignorados pelo Git
├── README.md              # Este arquivo
└── .env                   # Suas credenciais (você deve criar)
```

## 🛠️ Requisitos

- **Python 3.7+**
- **Google Chrome** instalado
- **ChromeDriver** compatível
- **Conta no Brevo** com credenciais válidas
- **Conexão com internet** estável

## ⚠️ Avisos Importantes

- 🚨 **Ação irreversível**: Contatos deletados não podem ser recuperados
- 🕒 **Processo longo**: Pode levar tempo dependendo da quantidade de contatos
- 🔄 **Interrupções**: Se interrompido, pode ser executado novamente
- 💾 **Backup**: Sempre faça backup antes de usar
- 🔐 **Credenciais**: Nunca compartilhe seu arquivo `.env`

## 🆘 Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'dotenv'"
```bash
pip install python-dotenv
```

### Erro: "ChromeDriver not found"
- Baixe o ChromeDriver compatível com sua versão do Chrome
- Coloque no PATH ou na pasta do projeto

### Erro: "Login failed"
- Verifique suas credenciais no arquivo `.env`
- Confirme se a conta do Brevo está ativa
- Tente fazer login manual no site primeiro

## 🤝 Compartilhamento

Para compartilhar este projeto com outras pessoas:

1. **Compartilhe a URL**: `https://github.com/m2stech/apaga_brevo`
2. **Oriente sobre segurança**: Cada pessoa deve criar seu próprio `.env`
3. **Não compartilhe**: Nunca envie seu arquivo `.env` para outros

## 📝 Licença

Este projeto é fornecido "como está" para fins educacionais e de automação.
Use por sua própria conta e risco.
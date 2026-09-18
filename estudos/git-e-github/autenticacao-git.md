---
titulo: "Autenticacao GIT"
categoria: "Git e GitHub"
atualizado_em: "2026-07-01T19:07:00.000Z"
---

# Autenticacao GIT


# Autenticacao

Segue um mapa mental simples, pensado para revisão rápida.

# Mapa Mental — Autenticação no GitHub

```plain text
                     AUTENTICAÇÃO NO GITHUB
                              │
      ┌───────────────────────┼────────────────────────┐
      │                       │                        │
      ▼                       ▼                        ▼
 Nome + Token                SSH                     2FA
 (HTTPS)              (Chaves Criptográficas)   (Segundo fator)
```

---

# 1. Nome + Token (HTTPS)

```plain text
Git
 │
 ▼
git push / git pull
 │
 ▼
GitHub solicita autenticação
 │
 ├── Usuário (Username)
 │
 └── Personal Access Token
        ↓
GitHub valida o Token
        ↓
Acesso autorizado
```

### Como configurar

  1. Faça login no GitHub.

  1. Vá em **Settings**.

  1. Acesse **Developer Settings**.

  1. Clique em **Personal Access Tokens**.

  1. Gere um novo Token.

  1. Copie o Token (ele é exibido apenas uma vez).

  1. Ao executar:

```plain text
git push
```

Informe:

```plain text
Username: seu_usuario

Password: cole o TOKEN aqui
```

> Hoje, no GitHub, o campo "Password" deve receber o **Token**, não a senha da conta.

---

# 2. SSH

```plain text
Seu Computador
        │
        │
Chave Privada
        │
────────Internet────────
        │
GitHub
Chave Pública
        │
GitHub compara as chaves
        │
        ▼
Acesso autorizado
```

### Como configurar

### 1. Gerar a chave

```plain text
ssh-keygen-t ed25519-C"seuemail@email.com"
```

↓

São criados dois arquivos:

```plain text
id_ed25519
```

(Chave privada)

e

```plain text
id_ed25519.pub
```

(Chave pública)

---

### 2. Copiar a chave pública

```plain text
cat ~/.ssh/id_ed25519.pub
```

ou abrir o arquivo e copiar seu conteúdo.

---

### 3. Adicionar ao GitHub

GitHub

↓

Settings

↓

SSH and GPG Keys

↓

New SSH Key

↓

Cole a chave pública.

---

### 4. Testar

```plain text
ssh-Tgit@github.com
```

Se aparecer algo como:

```plain text
Hi Matheus! You've successfully authenticated...
```

Está funcionando.

---

# 3. 2FA (Autenticação em Dois Fatores)

```plain text
Login
 │
 ▼
Usuário
 │
Senha
 │
 ▼
GitHub
 │
 ▼
Solicita código
 │
 ▼
Aplicativo autenticador
 │
 ▼
Código de 6 dígitos
 │
 ▼
GitHub valida
 │
 ▼
Conta liberada
```

### Como configurar

  1. GitHub → **Settings**.

  1. **Password and Authentication**.

  1. **Enable Two-Factor Authentication**.

  1. Escolha um método:

  - Aplicativo autenticador (Google Authenticator, Microsoft Authenticator, Authy etc.)

  - Chave de segurança (Security Key)

  1. Escaneie o QR Code.

  1. Digite o código gerado.

  1. Guarde os códigos de recuperação (*Recovery Codes*).

---

# Resumo

```plain text
                 AUTENTICAÇÃO

HTTPS
│
├── Usuário
└── Token
      ↓
 Autenticado

────────────────────────────

SSH
│
├── Chave Privada
└── Chave Pública
      ↓
 GitHub compara as chaves
      ↓
 Autenticado

────────────────────────────

2FA
│
├── Senha
└── Código do aplicativo
      ↓
 Autenticado
```

## Qual usar?











> **Importante:** o **2FA não substitui** o Token nem o SSH. Ele protege o **login na conta do GitHub**, enquanto o **Token** e o **SSH** são métodos usados para autenticar operações do Git com os repositórios.



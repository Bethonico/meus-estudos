---
titulo: "Principais comandos GIT"
categoria: "Git e GitHub"
nivel: "Iniciante"
status: "Estudando"
atualizado_em: "2026-07-01T19:05:00.000Z"
---

# Principais comandos GIT


Principais comandos git:

# Principais comandos git:

Verificar versão:

```plain text
git--version
```

Configurar nome:

```plain text
git config--global user.name"Matheus"
```

Configurar email:

```plain text
git config--global user.email"email@email.com"
```

Ver configurações:

```plain text
git config--list
```

## Criando um repositório

Entrar na pasta

```plain text
cd projeto
```

Inicializar Git

```plain text
git init
```

## Verificar status

O comando que você mais vai usar.

```plain text
git status
```

Ele mostra:

  - arquivos modificados

  - arquivos novos

  - arquivos prontos para commit

# Adicionar arquivos

Adicionar um arquivo

```plain text
git add arquivo.py
```

Adicionar tudo

```plain text
git add .
```

## Criar um commit

```plain text
git commit-m"Adiciona sistema de login"
```

Boas mensagens:

```plain text
Corrige erro de autenticação

Adiciona tela inicial

Atualiza documentação

Refatora classe Usuario
```

Evite:

```plain text
teste

aaa

commit

atualização
```

## Ver histórico

```plain text
git log
```

Versão resumida

```plain text
git log--oneline
```

## Ver diferenças

Antes de fazer commit:

```plain text
gitdiff
```

## Desfazer alterações

Descartar alterações de um arquivo

```plain text
git restore arquivo.py
```

Remover arquivo da área de stage

```plain text
git restore--staged arquivo.py
```

## Clonar um projeto

```plain text
git clone URL_DO_REPOSITORIO
```

Exemplo

```plain text
git clone https://github.com/usuario/projeto.git
```

## Conectar ao GitHub

Adicionar repositório remoto

```plain text
git remote add origin URL
```

Ver remotos

```plain text
git remote-v
```

## Enviar para GitHub

Primeiro envio

```plain text
git push-u origin main
```

Próximos envios

```plain text
git push
```

## Baixar atualizações

```plain text
git pull
```

ou

```plain text
git fetch
```

Depois

```plain text
git merge
```

Na prática, normalmente usamos:

```plain text
git pull
```

## Branches

Criar branch

```plain text
git branch nova-feature
```

Trocar de branch

```plain text
git checkout nova-feature
```

ou (mais moderno)

```plain text
git switch nova-feature
```

Criar e trocar

```plain text
git switch-c nova-feature
```

Listar branches

```plain text
git branch
```

Excluir branch

```plain text
git branch-d nova-feature
```

## Juntar branches

Estando na `main`

```plain text
git merge nova-feature
```

---

## Ver repositórios remotos

```plain text
git remote-v
```

## Ver histórico bonito

```plain text
git log--oneline--graph--all
```

Muito usado para visualizar as branches.

## Arquivo `.gitignore`

Ignora arquivos que não devem ser enviados.

Exemplo:

```plain text
venv/

.env

__pycache__/

*.pyc

node_modules/
```

## Fluxo completo de trabalho

```plain text
git status

git add .

git commit-m"Implementa cadastro de usuários"

git push
```

Esse ciclo se repete praticamente todos os dias.

## Fluxo ao começar um dia de trabalho

```plain text
git pull

# Trabalha no código

git status

git add .

git commit-m"Implementa filtro de pesquisa"

git push
```

## Comandos que um desenvolvedor usa diariamente

































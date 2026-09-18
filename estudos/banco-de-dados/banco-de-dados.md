---
titulo: "Banco de Dados"
categoria: "Banco de Dados"
atualizado_em: "2026-08-28T18:29:00.000Z"
---

# Banco de Dados


# 





















# SQL





## TIPOS DE REALACIONAMENTOS NO SQL

### 1 para 1

### 1 para MUITOS

### MUITOS PARA MUITOS 



Confira o detalhamento de cada um:

**1. Um para Um (1:1)**

Ocorre quando um registro na **Tabela A** se relaciona com exatamente um registro na **Tabela B**, e vice-versa. Geralmente é usado para dividir tabelas grandes e melhorar a performance ou por questões de segurança. **Beekeeper Studio**



**Exemplo:** `Pessoa` e `Documento`. Cada pessoa tem apenas um CPF e cada CPF pertence a uma única pessoa.

    - **Exemplo:** `Pessoa` e `Documento`. Cada pessoa tem apenas um CPF e cada CPF pertence a uma única pessoa.

**Como implementar:** A chave primária (PK) de uma tabela atua como chave estrangeira (FK) na outra, ou ambas compartilham a mesma chave. Saiba mais detalhes de como fazer isso no artigo sobre [**Relacionamentos de banco de dados um-para-um**](https://www.google.com/url?sa=i&rct=j&url=https%3A%2F%2Fwww.beekeeperstudio.io%2Fblog%2Fone-to-one-database-relationships-complete-guide&ved=2ahUKEwimhr6EzdWVAxXMGbkGHc79B1sQy_kOegoIAAgACAAIDRAF&opi=89978449&cd=&psig=AOvVaw32tohutQb1owQDE6ygUaxe&ust=1784236493693000).

    - **Como implementar:** A chave primária (PK) de uma tabela atua como chave estrangeira (FK) na outra, ou ambas compartilham a mesma chave. Saiba mais detalhes de como fazer isso no artigo sobre [**Relacionamentos de banco de dados um-para-um**](https://www.google.com/url?sa=i&rct=j&url=https%3A%2F%2Fwww.beekeeperstudio.io%2Fblog%2Fone-to-one-database-relationships-complete-guide&ved=2ahUKEwimhr6EzdWVAxXMGbkGHc79B1sQy_kOegoIAAgACAAIDRAF&opi=89978449&cd=&psig=AOvVaw32tohutQb1owQDE6ygUaxe&ust=1784236493693000).

**2. Um para Muitos (1:N)**

Este é o relacionamento mais comum. Um registro na **Tabela A (Pai)** pode ter vários registros associados na **Tabela B (Filho)**, mas cada registro na Tabela B pertence a apenas um registro na Tabela A. **DataCamp**



**Exemplo:** `Cliente` e `Pedidos`. Um cliente pode fazer vários pedidos, mas um pedido específico pertence a apenas um cliente.

    - **Exemplo:** `Cliente` e `Pedidos`. Um cliente pode fazer vários pedidos, mas um pedido específico pertence a apenas um cliente.

**Como implementar:** A chave primária da tabela "Um" (o `ID do Cliente`) é adicionada como chave estrangeira na tabela "Muitos" (`id_cliente` na tabela de pedidos). Veja exemplos práticos de modelagem no portal [**DevMedia**](https://www.google.com/url?sa=i&rct=j&url=https%3A%2F%2Fwww.devmedia.com.br%2Fmodelagem-1-n-ou-n-n%2F38894&ved=2ahUKEwimhr6EzdWVAxXMGbkGHc79B1sQy_kOegoIAAgACAAIFBAF&opi=89978449&cd=&psig=AOvVaw32tohutQb1owQDE6ygUaxe&ust=1784236493693000).

    - **Como implementar:** A chave primária da tabela "Um" (o `ID do Cliente`) é adicionada como chave estrangeira na tabela "Muitos" (`id_cliente` na tabela de pedidos). Veja exemplos práticos de modelagem no portal [**DevMedia**](https://www.google.com/url?sa=i&rct=j&url=https%3A%2F%2Fwww.devmedia.com.br%2Fmodelagem-1-n-ou-n-n%2F38894&ved=2ahUKEwimhr6EzdWVAxXMGbkGHc79B1sQy_kOegoIAAgACAAIFBAF&opi=89978449&cd=&psig=AOvVaw32tohutQb1owQDE6ygUaxe&ust=1784236493693000).

**3. Muitos para Muitos (N:N)**

Neste tipo, vários registros de uma **Tabela A** se relacionam com vários registros de uma **Tabela B**. **DevMedia**



**Exemplo:** `Aluno` e `Curso`. Um aluno pode se matricular em vários cursos, e um curso possui vários alunos.

    - **Exemplo:** `Aluno` e `Curso`. Um aluno pode se matricular em vários cursos, e um curso possui vários alunos.

**Como implementar:** No SQL, não é possível criar esse tipo de ligação diretamente. É necessário criar uma **tabela intermediária** (ou tabela de junção/associativa). Ela conterá as chaves estrangeiras das duas tabelas originais, quebrar a relação em duas de *Um para Muitos*, e pode até receber atributos adicionais específicos daquele vínculo (como a data de matrícula).

    - **Como implementar:** No SQL, não é possível criar esse tipo de ligação diretamente. É necessário criar uma **tabela intermediária** (ou tabela de junção/associativa). Ela conterá as chaves estrangeiras das duas tabelas originais, quebrar a relação em duas de *Um para Muitos*, e pode até receber atributos adicionais específicos daquele vínculo (como a data de matrícula).



## CRUD no SQL



CONCEITOS:  chaves primarias e estrangeiras

PRIMARIA: chaves com identificadores únicos (ID)

```sql
id INTEGER PRIMARY KEY,

#Para auto incrementar
id int AUTO_INCREMENT PRIMARY KEY
```

ESTRANGEIRAS: primary keys de outras tabelas associadas na tabela principal(ou alguma fora da sua origem)

```sql
FOREIGN KEY (usuario_id)
REFERENCES usuarios(id)
```





C = CREATE

```sql
CREATE TABLE usuarios (
id INTEGER PRIMARY KEY,
nome VARCHAR(100),
email VARCHAR(100),
idade INTEGER
);
```



INSERT = inserir valores na tabela

```sql
INSERT INTO nome_da_tabela (coluna1, coluna2, coluna3)
VALUES (valor1, valor2, valor3);
```

VALUES = associação entre valores



```sql
INSERT INTO usuarios (nome, idade)
VALUES ('Carlos', 30);
```



R = SELECT

SELECT * FROM usuário

ordenar, filtrar e muitas coisas com o SELECT



U = UPDATE



D = DELETE















## Resumo geral da tabela (ideal para o Notion)



























```sql
CREATE table livros (
id INTEGER PRIMARY KEY,
titulo TEXT NOT NULL,
```

```sql
arquivo_url TEXT NOT NULL,
capa_url TEXT NOT NULL,
audio_url TEXT NOT NULL,
```

```sql
favorito INTEGER DEFAULT 0,
data_adicao timestamp default current_timestamp,
status_leitura TEXT DEFAULT 'Não iniciado' CHECK (status_leitura IN('Não iniciado','LENDO','LIDO')),
ranking_livro TEXT DEFAULT 'BOM' CHECK (ranking_livro IN('GOAT','MUITO BOM','BOM','MANEIRINHO','RUIM','LIXO')),
progresso_percentual REAL DEFAULT 0.00,
ultima_posicao_leitura TEXT,
data_ultima_sicronizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
```

```sql
);
```

## Explicação resumida de cada comando

## `CREATE TABLE`

Cria uma nova tabela no banco de dados.

---

## `INTEGER PRIMARY KEY`

Define uma coluna inteira que identifica cada registro de forma única.

---

## `TEXT`

Armazena textos.

---

## `NOT NULL`

Impede que o campo fique vazio.

---

## `DEFAULT`

Define um valor padrão caso nenhum seja informado.

Exemplo:

```plain text
favoritoINTEGERDEFAULT0
```

Se você não informar o valor, ele será `0`.

---

## `CURRENT_TIMESTAMP`

Insere automaticamente a data e hora atuais.

Exemplo:

```plain text
data_adicaoTIMESTAMPDEFAULTCURRENT_TIMESTAMP
```

---

## `CHECK`

Cria uma regra para validar os dados.

Exemplo:

```plain text
CHECK(status_leituraIN (...))
```

Só permite os valores definidos.

---

## `IN`

Verifica se um valor pertence a uma lista.

Exemplo:

```plain text
IN ('A','B','C')
```

---

## `REAL`

Armazena números decimais.

Exemplo:

```plain text
0.7512.599.99
```

---

## `TIMESTAMP`

Armazena data e hora.

Exemplo:

```plain text
2026-07-15 10:32:55
```

---



















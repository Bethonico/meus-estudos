---
titulo: "POO"
categoria: "Programação"
nivel: "Intermediário"
status: "Estudando"
atualizado_em: "2026-07-05T19:10:00.000Z"
---

# POO


POO

## CONSEITOS BASES (objeto, método, atributos, Instancia)


**Objeto:** É uma instância da classe . É a representação de algo real ou abstrato que possui **Atributos** (características ou dados) e **Métodos** (ações ou comportamentos).

Nas minhas palavras: E o conceito de objeto, os objetos tem suas características e essas características são os **ATRIBUTOS** e os objetos tem um objetivo ou responsabilidades que são os **METODOS.**

**ATRIBUTOS: São as variáveis que armazenar as informações e características de um objeto.**

**METODOS: São as funções associadas ao objeto.**

**ESTADO: Se o objeto tiver um atributo mutável e a forma como ele se apresenta naquele momento.**

**INSTANCIA: Objeto criado a partir de uma classe

EXEMPLO CONCEITUAL:**

Uma televisão.

Atributos:

```plain text
Volume

Canal

Ligada
```

Métodos:

```plain text
Ligar()

Desligar()

TrocarCanal()

AumentarVolume()
```

**EXEMPLO EM CODIGOS:**



## CLASSE

**CONCEITO: E a estrutura logica que vai definir como vai ser o objeto, especificando atributos e métodos que o tipo de objeto ira possuir.**

**EXEMPLO CONCEITUAL:**

```plain text
Classe: Pessoa
```

Essa classe pode gerar vários objetos:

```plain text
Objeto 1
nome = João

Objeto 2
nome = Maria

Objeto 3
nome = Carlos
```

**EXEMPLO EM CODIGOS:**

```python
classPessoa:

def__init__(self,nome,idade):
self.nome=nome# atributo
self.idade=idade# atributo

deffalar(self):# método
print(f"Olá, meu nome é{self.nome}.")
```

Depois:

```python
pessoa1=Pessoa("João",20)
```

A memória fica parecida com isto:

```plain text
Classe Pessoa
│
├── atributos
│      nome
│      idade
│
└── métodos
       falar()
```







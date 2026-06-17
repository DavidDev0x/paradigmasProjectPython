# Migração LE1 Java -> Python

Projeto convertido a partir da linguagem educacional **LE1**.

## Como executar os exemplos

Na raiz deste diretório:

```bash
python -m le1.exemplos
```

## Como executar os testes básicos

```bash
python test_migracao.py
```

Os testes cobrem todos os operadores implementados:

- `+`, `-` binário e `-` unário;
- `and`, `or`, `not`;
- `==`;
- `++`;
- `length`;
- erros de tipo, incluindo o caso equivalente a `True + 2`.

## Observação sobre tipagem forte

Python considera `bool` uma subclasse de `int`, então a migração usa checagens com `type(valor) is int` nos pontos críticos. Assim, `ValorInteiro(True)` é rejeitado e expressões como `ExpSoma(ValorBooleano(True), ValorInteiro(2))` não são avaliadas como soma numérica.
# Migração LE2 Java -> Python

Este projeto contém a migração da linguagem educacional LE2 de Java para Python.
A estrutura de pacotes foi preservada a partir do Java, com nomes de arquivos e métodos em `snake_case`.

## Como executar os exemplos

Na raiz do projeto:

```bash
python -m le2.plp.expressions2.exemplos
```

## Como testar rapidamente

```bash
python testes_le2.py
```
# LF1 migrada de Java para Python

Projeto convertido a partir de `lf1.zip`, preservando a estrutura de pacotes e uma classe por arquivo `.py`.

## Como executar os exemplos

Na raiz do projeto descompactado:

```bash
python -m lf1.plp.exemplos
```

O método principal solicitado está em:

```python
from lf1.plp.exemplos import Exemplos
Exemplos.executar_todos()
```

## Resultado dos testes executados

- Exemplo1: `let fun f x = x + 1 in f(2)` → `3`
- Exemplo2: escopo dinâmico → `6`
- Exemplo3: função com variável externa → `6`
- Exemplo4: multiplicação recursiva → `12`
- Exemplo4 bônus: `square(7)` → `49`
- Operadores: `+`, `-`, menos unário, `==`, `and`, `or`, `not`, `++`, `length`
- Erros testados: `True + 2`, `length(1)`, `string and boolean`, variável duplicada

# LI1 migrada para Python

Projeto migrado a partir da implementação Java da linguagem educacional LI1 / Imperative1.

## Executar exemplos

```bash
python -m li1.plp.imperative1.exemplos
```

## Rodar teste simples

```bash
python -m compileall -q .
python - <<'PY'
from li1.plp.imperative1.exemplos import Exemplos
resultados = Exemplos().executar_todos()
for chave, valor in resultados.items():
    print(f'{chave}: {valor}')
PY
```

## Observações da migração

- Interfaces Java foram convertidas para classes `ABC`.
- Métodos em camelCase foram convertidos para snake_case.
- `HashMap` virou `dict`; `Stack<HashMap<...>>` virou `list[dict]`.
- Valores primitivos fazem validação estrita: `ValorInteiro(True)` gera erro, pois `bool` não é aceito como `int`.
- O arquivo `while_.py` recebe sufixo porque `while` é palavra reservada em Python.

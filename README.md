# 📊 Manipulação de Listas em Python

Este repositório contém implementações de algoritmos fundamentais utilizando listas (arrays) em Python, com foco em lógica de programação, estruturas de dados e análise de complexidade.

---

## 🚀 Objetivo

Este projeto foi desenvolvido com o objetivo de:

* Consolidar fundamentos de programação
* Praticar manipulação de listas
* Implementar algoritmos clássicos
* Entender análise de complexidade (Big O)
* Evoluir o raciocínio lógico

---

## 📂 Estrutura do Projeto

Cada arquivo representa um algoritmo ou operação específica:

* `Bubble_sort.py` → Ordenação de lista
* `Busca_Linear.py` → Busca sequencial
* `Busca_binária.py` → Busca eficiente em lista ordenada
* `Média_array.py` → Cálculo de média
* `Somando_array.py` → Soma de elementos
* `Remover_duplicatas.py` → Remoção de valores repetidos
* `maior_numero_da_lista.py` → Maior valor e índice
* `menor_numero_da_lista.py` → Menor valor e índice
* `test_arrays.py` → Testes automatizados

---

## 🧠 Algoritmos Implementados

### 🔍 Busca Linear

Percorre a lista elemento por elemento até encontrar o valor desejado.

* Complexidade: **O(n)**
* Uso: listas pequenas ou não ordenadas

---

### ⚡ Busca Binária

Divide o problema pela metade a cada iteração.

* Complexidade: **O(log n)**
* Requisito: lista ordenada
* Muito mais eficiente que a busca linear

---

### 🔃 Bubble Sort

Algoritmo simples de ordenação que compara elementos adjacentes.

* Complexidade: **O(n²)**
* Uso educacional (não recomendado em produção)

---

### 🔝 Maior / 🔽 Menor

Percorre a lista para encontrar:

* Maior valor e seu índice

* Menor valor e seu índice

* Complexidade: **O(n)**

---

### 📊 Média

Calcula a média dos valores da lista.

* Complexidade: **O(n)**

---

### ➕ Soma

Soma todos os elementos da lista.

Inclui:

* Versão iterativa

* Versão recursiva

* Complexidade: **O(n)**

---

### ♻️ Remoção de Duplicados

Remove elementos repetidos mantendo a ordem original.

* Complexidade: **O(n²)**

---

## 🧪 Testes

O projeto inclui testes automatizados utilizando `pytest`.

### ▶️ Como rodar:

```bash
pip install pytest
pytest
```

---

## 📈 Complexidade dos Algoritmos

| Algoritmo          | Complexidade |
| ------------------ | ------------ |
| Busca Linear       | O(n)         |
| Busca Binária      | O(log n)     |
| Bubble Sort        | O(n²)        |
| Maior / Menor      | O(n)         |
| Média              | O(n)         |
| Soma               | O(n)         |
| Remover Duplicados | O(n²)        |

---

## 🛠️ Tecnologias

* Python 3
* Pytest

---

## 📌 Melhorias Futuras

* [ ] Refatorar estrutura para módulos
* [ ] Adicionar mais algoritmos (Merge Sort, Quick Sort)
* [ ] Melhorar performance da remoção de duplicados (O(n))
* [ ] Adicionar documentação técnica mais detalhada

---

## 👨‍💻 Autor

Desenvolvido como parte da evolução em Estruturas de Dados e Algoritmos.

---

## 💡 Observação

Este projeto tem foco educacional e demonstra fundamentos essenciais que servem como base para desenvolvimento de sistemas mais complexos.

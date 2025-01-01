# Test-DPEP

Para executar as questões propostas, configure o ambiente:

## Requisitos:

Python 3.10 ou superior

## Configuração:


Clone o Repositório e entre na pasta do projeto

```bash
$ git clone https://github.com/gustavofbs/Test-DPEP

$ cd Test-DPEP/
```

Cria uma virtualenv (venv) e ative ela

```bash
$ python3 -m venv venv

$ source venv/bin/activate 
```

Instale as dependências

```bash
$ pip install -r requirements.txt
```

Para executar via terminal uma questão específica, pode fazer:

```bash
$ python3 <FILE_PATH>

# Caso não saiba o FILE_PATH da questão, digite para encontrá-lo:

$ pwd
```



Configure a sua `.env` - Serão necessárias nas questões 2 e 4

```bash
OPENAI_API_KEY=<YOUR_KEY>
```


## Q1

O programa **manipulaCSV** em Python recebe um arquivo CSV que contém informações de vendas: 

Colunas: 

- Produto 
- Quantidade 
- Preço

É retornado o produto com maior valor arrecadado. 

## Q2

Utilizando a biblioteca LangChain, a aplicação implementa um modelo de linguagem para responder perguntas com o seguinte fluxo:

- O usuário fornece um texto
- O usuário fornece perguntas sobre o texto

A resposta do modelo é retornado, como pode ser visualizado em um exemplo abaixo (via terminal):

![outputQ2](/assets/outputQ2.png)

## Q3

O programa implementa a função `analisar_numeros`, que recebe uma lista de números e retorna as seguintes informações:

- Média dos números
- Maior número
- Menor número
- Quantidade de números pares

Foram realizados testes para confirmar as saídas esperadas

## Q4

Utilizando LangChain e o modelo de linguagem de IA OpenAI GPT, implementei um script 
que: 

- O usuário descreve um problema
- Existe a possibilidade do usuário refinar o problema com novas informações
- São geradas três soluções alternativas para o problema fornecido

Em relação aos princípios de Engenharia de Prompts que utilizei, foram:

### Clareza e Especificidade
O script utiliza mensagens claras para definir o papel do modelo e a tarefa esperada. Por exemplo:

- **SystemMessage:** "Você é um assistente de IA que ajuda a resolver problemas fornecendo três soluções alternativas."

    - Essa instrução fixa o contexto, restringe o escopo e orienta o modelo a focar em soluções alternativas para problemas.

- **HumanMessage:** A entrada do usuário é tratada de forma explícita, garantindo que o problema seja interpretado corretamente.

Essas mensagens iniciais eliminam ambiguidades e ajudam o modelo a se concentrar nos objetivos.

### Contexto Iterativo e Histórico
O script incorpora refinamentos ao problema de forma incremental, mantendo um histórico cumulativo. Isso é alcançado por meio de:

- **HumanMessage** dinâmica: Cada refinamento do usuário é concatenado ao problema inicial, criando um contexto mais detalhado a cada iteração.

    - Exemplo: O problema é atualizado com: Problema inicial: {problema}\nRefinamento: {refinamento}.

Essa abordagem melhora o entendimento do modelo, garantindo que ele tenha todas as informações relevantes em cada etapa.

###  Direcionamento Explícito para Respostas Estruturadas

O prompt para a geração de soluções contém instruções detalhadas, solicitando explicitamente um formato estruturado:

- **HumanMessage:** "Por favor, forneça três soluções alternativas detalhadas."

O número de soluções (três) e o nível de detalhe esperado são especificados, restringindo o espaço de respostas e melhorando a consistência e a utilidade.

### Modularidade nos Prompts

*Observação:* Não categorizo como um "Princípio de Engenharia de Prompts" mas sim como uma forma de organização que é operado dentro desses princípios.

O script foi feito de forma modular, separando os prompts em três etapas:

- **Prompt Inicial:** Define o papel do modelo e solicita a descrição inicial do problema.

- **Prompt de Refinamento:** Integra novos detalhes, criando um contexto atualizado.

- **Prompt de Soluções:** Direciona o modelo a gerar três soluções detalhadas.

Essa separação modular facilita a manutenção do contexto e a adaptação do script a outras tarefas.

#### A seguir, uma exemplo de como funciona a aplicação (via terminal):

![outputQ4](/assets/outputQ4.png)

## Q5

O objetivo é retornar o último lançamento programado pelo ano especificado.

Atributos principais do retorno:

- Nome da Missão
- Data de Lançamento
- Status
- Foguete
- Local de Lançamento:

Para conferir se o resultado está correto ou não, pode utilizar a URL [Rocket Launch](https://rocketlaunch.org/past-rocket-launches) como referência e filtrar em `From Date` e `To Date`


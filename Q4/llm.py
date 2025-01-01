from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

# Carregar variáveis de ambiente
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Configurar modelo
modelo = ChatOpenAI(model="gpt-3.5-turbo")

# Instanciar console para saída estilizada
console = Console()

# Função para criar prompt inicial
def criar_prompt_inicial():
    return [
        SystemMessage(content="Você é um assistente de IA que ajuda a resolver problemas fornecendo três soluções alternativas."),
        HumanMessage(content="Por favor, descreva o problema que você deseja resolver."),
    ]

# Função para refinar o problema
def criar_prompt_refinamento(problema, refinamento):
    return [
        SystemMessage(content="Você é um assistente de IA que ajuda a resolver problemas fornecendo três soluções alternativas."),
        HumanMessage(content=f"Problema inicial: {problema}\nRefinamento: {refinamento}"),
    ]

# Função para gerar soluções
def criar_prompt_solucoes(problema):
    return [
        SystemMessage(content="Você é um assistente de IA que ajuda a resolver problemas fornecendo três soluções alternativas."),
        HumanMessage(content=f"Problema descrito: {problema}\nPor favor, forneça três soluções alternativas detalhadas."),
    ]

# Loop principal para interação do usuário
console.print(Panel("Bem-vindo ao [bold green]Assistente de Resolução de Problemas[/bold green]!", expand=False))
mensagens = criar_prompt_inicial()
resposta = modelo.invoke(mensagens)

problema = Prompt.ask("[bold cyan]Por favor, descreva o problema que você deseja resolver[/bold cyan]")

while True:
    refinamento = Prompt.ask("[bold yellow]Deseja adicionar mais informações ou refinar o problema?[/bold yellow] ([green]digite 'continuar' para receber as soluções[/green])")
    if refinamento.lower() == 'continuar':
        break
    mensagens = criar_prompt_refinamento(problema, refinamento)
    resposta = modelo.invoke(mensagens)
    problema += f" {refinamento}"  # Incorporar refinamento ao problema

# Gerar soluções para o problema final
mensagens = criar_prompt_solucoes(problema)
resposta = modelo.invoke(mensagens)
console.print(Panel("[bold magenta]Soluções alternativas para o problema:[/bold magenta]", expand=False))
console.print(resposta.content, style="cyan")
console.print(Panel("[bold red]Encerrando o programa.[/bold red]", expand=False))

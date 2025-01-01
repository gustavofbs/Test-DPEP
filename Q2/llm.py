from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
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

# Função para configurar o prompt para perguntas sobre o texto
def criar_prompt_para_perguntas():
    return ChatPromptTemplate.from_messages([
        SystemMessage(content="Você é um assistente que responde perguntas sobre um texto fornecido."),
        HumanMessage(content="Texto: {texto}\nPergunta: {pergunta}")
    ])

# Entrada do texto do usuário
console.print(Panel("[bold green]Digite um texto para análise[/bold green]", expand=False))
texto_usuario = Prompt.ask("[bold cyan]Texto[/bold cyan]")

# Configurar o prompt
prompt = criar_prompt_para_perguntas()

# Loop para perguntas
while True:
    pergunta = Prompt.ask("\n[bold yellow]Digite sua pergunta (ou 'sair' para encerrar)[/bold yellow]")
    if pergunta.lower() == "sair":
        console.print(Panel("[bold red]Encerrando o programa.[/bold red]", expand=False))
        break

    # Substituir placeholders no prompt manualmente
    mensagens = [
        SystemMessage(content="Você é um assistente que responde perguntas sobre um texto fornecido."),
        HumanMessage(content=f"Texto: {texto_usuario}\nPergunta: {pergunta}")
    ]

    # Gerar resposta usando o modelo com invoke
    resposta = modelo.invoke(mensagens)
    console.print(Panel(f"[bold magenta]Resposta:[/bold magenta]\n{resposta.content}", expand=False, style="cyan"))
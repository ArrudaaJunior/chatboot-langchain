from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

from openai import OpenAI

try:
    from config import OPENAI_API_KEY
except ImportError:
    raise ImportError("Arquivo de configuração não encontrado. Verifique se o config.py está presente e configurado corretamente.")

numero_de_dias = 7
numero_de_criancas = 2
atividade = "praia"

modelo_do_prompt = PromptTemplate.from_template(
    "Crie um roteiro de viagem de {numero_de_dias} dias, para uma família com {numero_de_criancas} crianças, que gostam de {atividade}."
)

prompt = modelo_do_prompt.format(numero_de_dias=numero_de_dias, 
                                 numero_de_criancas=numero_de_criancas, 
                                 atividade=atividade)

print(prompt)

chave = OpenAI(api_key=OPENAI_API_KEY)

resposta = chave.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)

print(resposta)

roteiro_viagem = resposta.choices[0].message.content
print(roteiro_viagem)

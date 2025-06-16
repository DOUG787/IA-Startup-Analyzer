import openai
import os

# Configure sua API Key como variável de ambiente ou diretamente aqui (não recomendado em produção)
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_startup(description):
    prompt = f"""
Você é um analista de Venture Capital especializado em tecnologia. Avalie a seguinte descrição de startup com base nos critérios:

1. Inovação (0 a 10)
2. Potencial de Escalabilidade (0 a 10)
3. Acesso e demanda de mercado (0 a 10)
4. Comentário técnico (1 parágrafo)

Descrição:
\"\"\"{description}\"\"\"

Retorne o resultado como um dicionário Python.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    result_text = response.choices[0].message["content"]

    try:
        # Executa o retorno como dicionário (com segurança limitada)
        result_dict = eval(result_text, {"__builtins__": {}})
        return result_dict
    except Exception as e:
        return {"Erro": f"Não foi possível interpretar a resposta da IA. Detalhes: {e}"}

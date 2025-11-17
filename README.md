# ResearcherBasicAIAgent

Agente de investigación básico en Python utilizando LangChain 1.x y OpenAI.  
Incluye herramientas de búsqueda web (DuckDuckGo), Wikipedia y guardado local en `.txt`.  
Devuelve respuestas estructuradas usando un modelo Pydantic.

## Características

- LLM: `gpt-4o-mini` vía `langchain-openai`
- Herramientas:
  - DuckDuckGoSearchRun (búsqueda web)
  - WikipediaQueryRun (enciclopedia)
  - save_to_txt (persistencia local)
- Salida estructurada: `topic`, `summary`, `sources`, `tools_used`
- Implementado con la API moderna de LangChain: `create_agent` + `ToolStrategy`

## Estructura del proyecto

```
ResearcherBasicAIAgent/
├── main.py
├── tools.py
├── requirements.txt
├── .gitignore
├── .env.example
└── run.sh   (opcional)
```

Archivos locales ignorados:

```
.env
venv/
__pycache__/
```

## Requisitos

- Python 3.11 o 3.12
- OpenAI API Key

## Instalación

```bash
git clone https://github.com/estanimolinas/ResearcherBasicAIAgent.git
cd ResearcherBasicAIAgent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Variables de entorno

```bash
cp .env.example .env
```

Editar:

```
OPENAI_API_KEY=tu_api_key_real
```

## Ejecución

```bash
python main.py
```

Se solicitará:

```
¿Qué querés investigar?
```

El agente usará herramientas cuando sea necesario y generará un objeto estructurado, además de guardar el resultado en `research_output.txt`.

## Script opcional: run.sh

```
#!/usr/bin/env bash
set -e
if [ -d "venv" ]; then
  source venv/bin/activate
  python main.py
else
  echo "Crear entorno: python3 -m venv venv"
fi
```

## Licencia

MIT License.

from pathlib import Path

content = """# DevMentor

Assistente de programação desenvolvido em Python com Streamlit e integrado à API do Google Gemini. O DevMentor oferece uma interface de chat para fazer perguntas sobre programação e receber explicações e exemplos de código.

## Funcionalidades

- Interface de chat baseada em Streamlit.
- Respostas geradas pela API do Google Gemini.
- Histórico de mensagens mantido durante a sessão do aplicativo.
- Configuração da chave da API por variável de ambiente/segredo, sem armazená-la no código-fonte.

> Observação: o histórico de conversa é mantido na sessão do Streamlit e não é persistido em um banco de dados.

## Tecnologias

- Python
- Streamlit
- Google Gen AI SDK (`google-genai`)
- `python-dotenv` para carregar variáveis de ambiente durante o desenvolvimento local

## Executar localmente

### 1. Pré-requisitos

- Python instalado.
- Uma chave da API Gemini obtida no [Google AI Studio](https://aistudio.google.com/).

### 2. Clonar o repositório

```bash
git clone https://github.com/monikylbecker-ship-it/DevMentor.git
cd DevMentor
```

### 3. Criar e ativar um ambiente virtual

Windows PowerShell:

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar a chave da API

Crie um arquivo `.env` na raiz do projeto (somente para uso local) com o seguinte conteúdo:

```env
GOOGLE_API_KEY=sua_chave_real_aqui
```

Substitua `sua_chave_real_aqui` pela sua chave. **Nunca envie o arquivo `.env` ao GitHub nem compartilhe sua chave.**

### 6. Iniciar a aplicação

```bash
streamlit run app.py
```

O Streamlit exibirá o endereço local no terminal; abra-o no navegador.

## Publicação no Streamlit Community Cloud

1. Envie `app.py`, `requirements.txt`, `.gitignore` e `README.md` ao repositório GitHub.
2. No [Streamlit Community Cloud](https://share.streamlit.io/), selecione o repositório `monikylbecker-ship-it/DevMentor`.
3. Configure o arquivo principal como `app.py` e a branch como `main`.
4. Em **Settings → Secrets**, configure:

   ```toml
   GOOGLE_API_KEY = "sua_chave_real_aqui"
   ```

5. Salve e publique/reinicie o aplicativo, se necessário.

Não inclua a chave real neste README nem em arquivos versionados.

## Estrutura do projeto

```text
DevMentor/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

Arquivos locais como `.env`, ambientes virtuais e `__pycache__/` devem permanecer fora do repositório.

## Segurança

- Guarde a chave Gemini em variáveis de ambiente localmente e em **Secrets** na hospedagem.
- Não registre nem publique chaves de API.
- Se uma chave for exposta, revogue-a e gere outra no Google AI Studio.

## Melhorias futuras

- Persistência de conversas em banco de dados.
- Testes automatizados.
- Mensagens de erro mais claras para falhas da API.
- Validação de disponibilidade dos modelos Gemini configurados.

## Licença

Nenhuma licença foi especificada neste repositório. Adicione um arquivo `LICENSE` caso deseje definir formalmente como outras pessoas podem utilizar, modificar ou distribuir o projeto.
"""
path = Path("/mnt/data/README_DevMentor.md")
path.write_text(content, encoding="utf-8")
print(f"Arquivo criado: {path}")

# Plataforma de Votação Escolar

## 📌 Descrição
Projeto integrador: desenvolvimento de uma plataforma escolar para votação de representantes, com painel administrativo para professores e interface simples para alunos.

## 🎯 Objetivos
- Permitir que **alunos** realizem votos de forma segura e prática.  
- Oferecer aos **professores** ferramentas para gerenciar alunos, candidatos e acompanhar resultados.  
- Garantir **transparência** e **usabilidade** no processo de votação escolar.  

## ⚙️ Tecnologias
- **Backend:** FastAPI (Python)  
- **Frontend:** React ou Vue.js (a definir)  
- **Banco de Dados:** PostgreSQL (em nuvem, futuro)  
- **Hospedagem:** Render (plano gratuito)  

## 🧩 Funcionalidades
- Login de alunos e professores  
- Cadastro de candidatos (professor)  
- Registro de votos (aluno)  
- Apuração e resultados em tempo real  
- Dashboard com estatísticas  

## 🚀 Como rodar localmente
1. Clone o repositório:
   ```bash
   git clone https://github.com/RickHre/plataforma-votacao-escolar.git
   ```
2. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Acesse no navegador:
   - API: `http://localhost:8000`  
   - Swagger UI: `http://localhost:8000/docs`

## 📄 Licença
Este projeto está licenciado sob os termos da **MIT License**.


Projeto integrador 6. Desenvolvimento de plataforma para votação / gestão.

## 🗺️ Roadmap do Projeto

- [x] Criar repositório no GitHub
- [x] Adicionar licença MIT
- [x] Configurar README inicial
- [x] Estrutura mínima do FastAPI (`main.py`, `requirements.txt`)
- [x] Implementar rotas de autenticação (login/cadastro)
- [ ] Implementar rotas de alunos (listar/cadastrar)
- [ ] Implementar rotas de candidatos (listar/cadastrar)
- [ ] Implementar rotas de votação (registrar voto/apuração)
- [ ] Criar dashboard para professores
- [ ] Integrar banco PostgreSQL em nuvem
- [ ] Deploy no Render

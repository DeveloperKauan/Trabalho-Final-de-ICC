## 🗺️ ROADMAP: TERMO ICC

Nosso plano de projeto, dividido em fases.

### Fase 0: Configuração Inicial (O "Hello, World!")
- [ ] Estrutura básica do projeto (`index.html`, `style.css`, `main.py`).
- [ ] Configurar o PyScript no `index.html`.
- [ ] Prova de Conceito: Fazer o Python (PyScript) escrever "Olá, Mundo!" na página.
- [ ] Fazer o `index.html` conseguir carregar e executar o código do `main.py`.

### Fase 1: Lógica do Jogo (O Cérebro)
- [ ] Encontrar e adicionar as listas de palavras (respostas e palpites válidos).
- [ ] Criar a lógica para carregar os arquivos de palavras (`.txt` ou `.json`) dentro do Python.
- [ ] Criar a função que seleciona a "Palavra do Dia" (baseado na data).
- [ ] **(CRÍTICO)** Criar a função `validar_palpite(palpite, resposta)`.
- [ ] Garantir que a lógica de validação lida com letras repetidas (Ex: se a palavra é "CASAS" e o palpite é "DATAS", o primeiro 'A' fica verde e o segundo 'A' fica cinza).
- [ ] Garantir que a lógica de validação lida com letras "presentes" repetidas (Ex: se a palavra é "SONDA" e o palpite é "ARARA", apenas um 'A' fica amarelo).
- [ ] Criar a função que checa se o palpite existe na lista de palavras válidas.

### Fase 2: Interface (O Rosto)
- [ ] Criar o grid 6x5 no `index.html` (com `divs`).
- [ ] Criar o teclado virtual no `index.html` (com `<button>`).
- [ ] Estilizar o grid e o teclado com `style.css` (layout, cores, fontes).
- [ ] Criar as classes CSS para o feedback (`.correto`, `.presente`, `.ausente`).
- [ ] Criar as classes CSS para as animações (virar a letra, tremer por erro).

### Fase 3: Interatividade (A "Cola")
- [ ] Fazer o Python (`main.py`) "enxergar" os elementos do HTML (grid, teclado).
- [ ] Capturar input do teclado físico (via `addEventListener` no Python).
- [ ] Capturar clique no teclado virtual (via `addEventListener` no Python).
- [ ] Fazer o Python atualizar o grid visualmente enquanto o usuário digita.
- [ ] Criar a função `processar_palpite()` (o que acontece ao dar "Enter").
- [ ] Ligar o "Enter" à função `processar_palpite`.
- [ ] Fazer o Python aplicar as classes de cor (CSS) no grid após a validação.
- [ ] Fazer o Python atualizar as cores das teclas do teclado virtual.
- [ ] Implementar as mensagens de erro (ex: "Palavra não existe", "Faltam letras").

### Fase 4: Recursos Adicionais (O Polimento)
- [ ] Salvar o progresso do dia no `localStorage` (para o usuário poder recarregar a página).
- [ ] Carregar o progresso do `localStorage` ao iniciar o jogo.
- [ ] Criar o modal (popup) de estatísticas.
- [ ] Salvar as estatísticas (vitórias, sequência) no `localStorage`.
- [ ] Criar a função de "Compartilhar" (copiar os emojis 🟩🟨⬛).

### Fase 5: Finalização
- [ ] Testar em diferentes navegadores (Chrome, Firefox, Safari).
- [ ] Testar em celular (responsividade).
- [ ] Fazer o deploy (hospedar no GitHub Pages).

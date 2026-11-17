# Alcateia Welcome Bot

Bot separado que envia uma mensagem automática no canal `#Entrada` quando alguém entra no servidor.

## Variáveis de ambiente na hospedagem

- `DISCORD_TOKEN`: token do bot. Cadastre somente como variável secreta no painel da hospedagem. Nunca coloque o token neste repositório ou no chat.
- `WELCOME_CHANNEL_NAME`: canal de boas-vindas. Padrão: `Entrada`.
- `SERVER_NAME`: nome exibido na mensagem. Padrão: `Alcateia Cheats 2.0`.

Comando de inicialização: `python main.py`.

## Permissões no Discord

- Ative **Server Members Intent** no Discord Developer Portal.
- O cargo do bot precisa poder ver `#Entrada` e enviar mensagens nele.

Este bot é independente do bot de vendas. Não usa nem altera o token do bot de vendas.

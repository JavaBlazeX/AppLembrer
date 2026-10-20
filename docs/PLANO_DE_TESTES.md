# Plano de testes — AppLembrer

## Testes técnicos automatizados

Executar `python -m pytest -q` e guardar captura do resultado. Os testes cobrem abertura da página, criação, listagem, edição, conclusão, exclusão e rejeição de entradas inválidas.

## Testes com cinco pessoas

Convidar cinco pessoas reais para testar a aplicação. Para cada pessoa, registrar:

- Nome e data
- O que testou e funcionou
- O que testou e não funcionou e o que deve ser corrigido
- Funcionalidades não testadas
- Capturas de tela de problemas, quando aplicável

### Roteiros sugeridos

1. Cadastrar um lembrete de estudo e verificar se aparece na lista.
2. Editar título e horário e confirmar se as alterações persistem.
3. Criar um lembrete fictício de medicamento e conferir a categoria.
4. Concluir, reabrir e excluir um lembrete.
5. Buscar, filtrar e atualizar a página para verificar a persistência.

## Laudo de qualidade

Após os testes, descrever erros reais, correções realizadas e evidências (prints antes/depois). Não declarar como implementadas notificações ou repetição automática: esta versão não possui essas funcionalidades.

## Roteiro do vídeo (aproximadamente 5 minutos)

- 0:00–0:40: objetivo e público do AppLembrer
- 0:40–1:30: apresentação da interface
- 1:30–2:30: criação e edição de lembretes
- 2:30–3:30: conclusão, filtros, exclusão e persistência
- 3:30–4:20: tecnologias, organização do repositório e testes
- 4:20–5:00: resultados reais dos testes e melhorias realizadas

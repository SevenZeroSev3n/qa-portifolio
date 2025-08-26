# Plano de Teste v0.1 — App: Sauce Demo (prática)

## Objetivo
Validar funcionalidades essenciais de autenticação e fluxo básico de compra, garantindo que usuários consigam entrar, navegar e finalizar compras sem erros críticos.

## Escopo (In-Scope)
- Login (válido e inválido)
- Listagem de produtos e detalhes
- Carrinho: adicionar/remover itens
- Checkout: aplicação de cupom e finalização
- API básica (status/estrutura) quando aplicável

## Fora de Escopo (Out-of-Scope) nesta fase
- Integrações de pagamento reais
- Performance e carga
- Acessibilidade avançada

## Riscos & Assunções
- Risco: validação de cupom intermitente pode bloquear checkout.
- Assunção: ambiente web estável em Chrome/Windows.

## Ambiente
- Web: Chrome (versão atual), Windows 10

## Dados de Teste
- Usuário válido (ex.: standard_user / secret_sauce)
- Usuário inválido (email/senha aleatórios)
- Cupom válido (ex.: ABC10) e inválido (ex.: XYZ99)

## Critérios de Saída
- Smoke verde (login, adicionar ao carrinho, checkout) sem bugs críticos abertos.
- Casos de teste executados e bug reports documentados com evidências.

## Entregáveis
- Casos de teste (10+ App #1)
- Bug reports (3–5) com evidências
- Automação mínima de UI (login)
- Mini suite de API (3 asserts)
- README com prints/gif e “aprendizados”

# Enviando SMS com Python e Twilio SMS API 
---
## Pré requisitos

Para conseguir rodar o código fonte deste projeto são necessários alguns pré requisitos:
- Ter uma conta criada na plataforma da [Twilio](https://www.twilio.com/pt-br/)
- Ter um [Número de Telefone](https://www.twilio.com/pt-br/docs/phone-numbers) na plataforma da Twilio
- Ter o [Python](https://www.python.org/) instalado
- Ter a [Biblioteca](https://www.twilio.com/pt-br/docs/libraries/python) da Twilio para Python instalado

### Variáveis de ambiente
São necessárias 4 variáveis de ambiente para evitar exposição de dados sensíveis como tokens e números de telefone: `TWILIO_ACCOUNT_SID` para seu Account SID da Twilio, `TWILIO_AUTH_TOKEN` para o token da API, `SMS_SENDER` para o número de telefone obtido na Twilio e `SMS_RECEIVER` que será o número que irá receber o SMS.

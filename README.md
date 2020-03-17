# Power On/power OFF <br>
# Fazer login na IBM Cloud
- ibmcloud login 
- ibmcloud target --cf
- ibmcloud target -g Default

# Criando a imagem docker
 - Faça o download do repositório: git clone https://github.com/lucas2179/PowerOff-Functions.git
 - Mova para o diretório do projeto: cd PowerOff-Functions
 - Faça o login no container registry: ibmcloud cr login
 - ibmcloud cr build --no-cache --quiet --tag us.icr.io/your-namespace/powerenv .

# Criando a acao
ibmcloud fn action create PowerOff --docker us.icr.io/your-namespace/powerenv poweroff.py

# Parametros para rodar a function
- key: Deve ser uma apikey de infraestrutura classica
- poweraction: Pode ser on(ligar) ou off(desligar)<br>

# Exemplo de entrada
```
{
  "username": "chaves api ibm *infraestrutura classica",
  "key": "api key infraestrutura classica",
  "vsiname":"nomevsi",
  "poweraction":"off/on",
   "vsiid": "idvsi"
}
```

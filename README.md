# Power On/power OFF <br>
- Fazer login na IBM Cloud
```
ibmcloud login
```
- Target no Cloud Foundry
```
ibmcloud target --cf
```
- Target no resource group default
```
ibmcloud target -g Default
```
# Criando a imagem docker
 - Faça o download do repositório:
 ```
 git clone https://github.com/lucas2179/PowerOff-Functions.git
 ```
 - Mova para o diretório do projeto: 
 ```
 cd PowerOff-Functions
 ```
 - Faça o login no container registry: 
 ```
 ibmcloud cr login
 ```
 - Faça o build da imagem
 ```
 ibmcloud cr build --no-cache --quiet --tag us.icr.io/your-namespace/powerenv .
 ```
# Criando a action no IBM Cloud Functions
```
ibmcloud fn action create PowerOff --docker us.icr.io/your-namespace/powerenv poweroff.py
```

# Parametros para rodar a function
- key: Deve ser uma apikey de infraestrutura classica
- poweraction: Pode ser on(ligar) ou off(desligar)<br>
- username: Usuário que criou a apikey de infraestrutura clássica
- vsiid: Id da vsi
- vsiname: Nome da vsi


# Obtendo o username da API Key de Infraestrutura Clássica

- No portal, clicar em Gerenciar > Acesso(IAM) > Usuários
- Selecione o usuário que criou a chave
- Role a página até a sessão "Senha da VPN"
- Copie o username desta sessão. Normalmente será o número da conta + "_"+ email do usuário. Exemplo: 1753401_exemplo@exemplo.com

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

# Determinando o período de execução
- Login to the IBM Cloud Console using your Credentials (username and password)

- Click on the Three Line Menu (Hamburger Menu) and click on "Functions"

- Click on "Actions" and check if you Action appear on the list. In my example, I'm using the "itiroaction01" name for the action name.

- Click on "Trigger" item and click on the "Create" button.

- Click on "Create Trigger".

- Click on "Periodic"

- Type the name on "Trigger Name" field.

- Select the days and hours that the function will be executed. You can select a pre defined period on "Select pattern" field.

- In the JSON Payload, type:
```
{
  "username": "<softlayer_username>",
  "key": "<softlayer_api_key>",
  "vsiname":"<name_of_the_vsi>",
  "poweraction":"<power_action>",
  "vsiid": "<id_vsi>"
}
```


OBS: Change <id_vsi> with the ID of the VSI that needs to Powered On/Off.

16. Click on "Create" button.

17. In the next screen, click on "Add" button to associate an action with the Trigger.

18. Click on "Select Existing" Button.

19. Click on "Select an Action" field and Select you action.

20. Click on Add.

21. Your Function is now created with a Trigger and a Action!

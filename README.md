#Power On/power OFF
#Fazer login na IBM Cloud
- ibmcloud login 
- ibmcloud target --cf
- ibmcloud target -g Default

#Criando a imagem docker
 - Faça o download do repositório: git clone https:

#Criando a acao
ibmcloud fn action create PowerOff --docker lucassouza21/powerenv poweroff.py
Parametros
{
  "username": "chaves api ibm *infraestrutura classica",
  "key": "api key infraestrutura classica",
  "vsiname":"nomevsi",
  "poweraction":"off/on",
   "vsiid": "idvsi"
}

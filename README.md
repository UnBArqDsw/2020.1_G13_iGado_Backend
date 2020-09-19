# iGado Backend

Documentação disponível em nossa [Wiki](https://unbarqdsw.github.io/2020.1_G13_iGado/#/). 

**Número da Lista**: 13<br>
**Código da Disciplina**: FGA0208-T01<br>

## Alunos
|Matrícula | Aluno | Git |
| :-: | :-- | :-- |
| 16/0133394 | Lucas Fellipe Carvalho Moreira| [@lucasfcm9](https://github.com/lucasfcm9) | 
| 17/0145514 | Iuri de Souza Severo Alves| [@iurisevero](https://github.com/iurisevero) | 
| 17/0129411 | Guilherme Mendes Pereira | [@guilherme-mendes](https://github.com/guilherme-mendes) | 
| 17/0138798 | Caio Vinícius Fernandes de Araújo | [@caiovfernandes](https://github.com/caiovfernandes) | 
| 17/0013910 | João Pedro José Santos da Silva Guedes | [@sudjoao](https://github.com/sudjoao) | 

## Sobre 
Descreva o seu projeto em linhas gerais. 

## Screenshots
Adicione 3 ou mais screenshots do projeto em termos de interface e funcionamento.

## Instalação 
**Linguagens**: Python, utilizando o microframework Flask<br>
**Tecnologias**: Docker, docker-compose<br>

### Instalação do Docker e do Docker-compose
Para instalar o docker e o docker-compose, tanto para Linux quanto para MacOS, basta seguir a documentação do [Docker](https://docs.docker.com/).
* Como instalar [Docker Engine](https://docs.docker.com/engine/install/)
* Como instalar [Docker Desktop para Mac](https://docs.docker.com/docker-for-mac/install/)
* Como instalar [Docker Engine para Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
* Como instalar [Docker-compose](https://docs.docker.com/compose/install/)

Após instalar o docker e o docker-compose, basta entrar na pasta geral do projeto
```
$cd 2020.1_G13_iGado_Backend
```
E executar o comando
```
$docker-compose up --build
```
> Às vezes pode ser necessário executar o comando como administrador, adicionando a palavra ```sudo``` antes dele
Após a finalização da build, a API estará rodando e pode ser testada através da rota
```
http://localhost/ping
```
Que irá retornar
```
{
    "status": "success",
    "message": "pong!"
}
```
Se tudo ocorrer corretamente

## Uso 
Explique como usar seu projeto caso haja algum passo a passo após o comando de execução.

## Vídeo
Adicione 1 ou mais vídeos com a execução do projeto final.

## Outros 
Quaisquer outras informações sobre seu projeto podem ser descritas abaixo.

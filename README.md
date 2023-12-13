# Detecção e Contagem de Pessoas com YOLO e Python

## Descrição do Projeto
Este projeto tem como objetivo utilizar o modelo YOLO (You Only Look Once) em conjunto com Python para realizar a detecção e contagem de pessoas em ambientes específicos (neste caso, escolar). Serão realizados testes na faculdade Una Itabira, visando mapear o fluxo de entrada e saída de pessoas no campus.

## Local dos Testes
Os testes serão concentrados na portaria principal do campus, localizada no térreo do prédio. Esta escolha estratégica permite uma análise mais focalizada no local de maior intensidade de movimento de pessoas, garantindo informações mais ricas e eficazes durante os períodos de detecção.

## Objetivo
O principal propósito deste projeto é estabelecer um sistema de monitoramento que contribua para o controle de fluxo de pessoas em diferentes cenários. 
Através da detecção e contagem de pessoas, espera-se obter insights valiosos para a gestão de dias letivos e demais interesses da instituição no campus.

### Ferramenta
O projeto utiliza o modelo YOLO para a detecção em tempo real, aproveitando a capacidade única do algoritmo de realizar a detecção de objetos em uma única passagem pela rede neural. A implementação será realizada em Python, aproveitando as bibliotecas e ferramentas disponíveis para análise de imagens.

## Instruções de Uso

### Criação de um ambiente vitual (opcional):
Instale o virtualenv, se ainda não estiver instalado:<br>
``` pip install virtualenv ```

Crie um ambiente virtual:<br>
``` python -m venv venv ```

Ative o ambiente virtual (Linux/Mac):<br>
``` source venv/bin/activate ```

Ative o ambiente virtual (Windows):<br>
``` .\venv\Scripts\activate ```

### Instalação das Dependências: 
Certifique-se de ter as bibliotecas necessárias instaladas. Utilize o arquivo requirements.txt para instalar as dependências: <br>
``` pip install -r requirements.txt ```

### Configuração do Modelo YOLO: 
O dataset do modelo v8 utilizado é fornecido pela Ultralytics e pré-configurado no código, desta forma:

``` python
model = YOLO("yolov8n.pt")
```

Sendo o arquivo yolov8n.py localizado na raiz do projeto.
Você pode treinar o modelo com um número específico de épocas, se desejar.

``` python
model = YOLO("yolov8n.pt")
results = model.train(data='coco128.yaml', epochs=100, imgsz=640) # < Adicionar linha
```

### Execução do Script: 
Execute o script principal counter.py para iniciar a detecção e contagem de pessoas.<br>
``` python counter.py ```

O script principal possui uma conexão opcional com um servidor WebSocket que pode ser configurada pelo usuário.<br>
Você pode ativar um servidor de testes provido pelo projeto utilizando o comando: ``` python server.py ```<br>
A porta e funções do servidor podem ser alteradas conforme o necessário.

Você pode ativar o uso de WebSockets no script principal adicionando o argumento "websockets", desta forma:<br>
``` python counter.py websockets ```

### Análise dos Resultados: 
Os resultados serão apresentados no console e, se desejado, podem ser exportados para análises posteriores.

Caso tenha executado o projeto com um ambiente virtual, desative desta forma:<br>
``` deactivate ```

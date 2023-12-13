# Detecção e Contagem de Pessoas com YOLO e Python

## Descrição do Projeto
Este projeto tem como objetivo utilizar o modelo YOLO (You Only Look Once) em conjunto com Python para realizar a detecção e contagem de pessoas em ambientes específicos. Neste caso, serão realizados testes na faculdade Una Itabira, visando mapear o fluxo de entrada e saída de pessoas no campus.

## Local dos Testes
Os testes serão concentrados na portaria principal do campus, localizada no térreo do prédio. Esta escolha estratégica permite uma análise mais focalizada e precisa do movimento de pessoas, garantindo a eficácia na detecção.

## Objetivo
O principal propósito deste projeto é estabelecer um sistema de monitoramento que contribua para o controle de fluxo de pessoas em diferentes cenários, como dias de aula, eventos, provas, concursos, entre outros. Através da detecção e contagem de pessoas, espera-se obter insights valiosos para a gestão e segurança do campus.

## Cenários de Aplicação

Dias de Aula: Avaliar o número de pessoas presentes nos dias letivos, auxiliando na otimização de recursos e segurança.
Eventos: Monitorar a participação em eventos, permitindo ajustes logísticos e aprimoramento da experiência do público.
Provas e Concursos: Garantir controle de acesso em situações que demandam maior segurança e organização.
Metodologia
O projeto utilizará o modelo YOLO para a detecção em tempo real, aproveitando a capacidade única do algoritmo de realizar a detecção de objetos em uma única passagem pela rede neural. A implementação será realizada em Python, aproveitando as bibliotecas e ferramentas disponíveis para análise de imagens.

## Instruções de Uso
Instalação das Dependências: Certifique-se de ter as bibliotecas necessárias instaladas. Utilize o arquivo requirements.txt para instalar as dependências.

pip install -r requirements.txt
Configuração do Modelo YOLO: Faça a configuração do modelo YOLO, seguindo as instruções no arquivo yolo_config.yaml. Certifique-se de possuir os pesos (weights) adequados para a detecção de pessoas.

Execução do Script: Execute o script principal detect_people.py para iniciar a detecção e contagem de pessoas na portaria principal.

python detect_people.py
Análise dos Resultados: Os resultados serão apresentados no console e, se desejado, podem ser exportados para análises posteriores.
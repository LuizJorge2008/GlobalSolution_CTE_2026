# GlobalSolution_CTE_2026

INTEGRANTES
NOMES                         |                RM
JORGE LUIZ MARQUES ARAUJO                    573754
GUILHERME LOPES                              569292
DALEXANDRO                                   568784



DESCRICAO DO AMBIENTE ESCOLHIDO
O ambiente escolhido para o desenvolvimento do projeto foi uma sala de estudos comunitária climatizada.
Esse ambiente foi selecionado por ser um espaço destinado ao aprendizado e à concentração, onde fatores como temperatura, qualidade do ar e nível de ruído podem influenciar o conforto das pessoas. Para realizar a simulação, foram considerados três parâmetros ambientais: temperatura (°C), concentração de partículas finas PM2,5 (µg/m³) e nível de ruído (dB(A)).


OBJETIVO DA SOLUCAO
O objetivo do projeto é desenvolver um programa em Python capaz de simular o monitoramento das condições ambientais de uma sala de estudos.
O sistema permite que o usuário informe diferentes leituras de temperatura, PM2,5 e ruído, comparando os valores com limites de referência previamente estabelecidos. A partir desses dados, o programa identifica condições críticas, calcula médias, valores mínimos e máximos, contabiliza ocorrências e determina o percentual de leituras críticas.
Ao final, apresenta uma classificação geral das condições ambientais e gera automaticamente um relatório em formato .txt com os resultados da análise. A aplicação possui finalidade acadêmica e utiliza dados simulados, não substituindo avaliações ambientais profissionais.


INSTRUCOE DE USO DO PROGRAMA
Passo 1: Baixe o arquivo GS.py disponível neste repositório.
Passo 2: Abra a pasta do projeto no Visual Studio Code.
Passo 3: Abra o terminal e execute o comando:

py GS.py

Passo 4: No menu principal, escolha uma das opções disponíveis:

1 — Cadastrar informações: permite realizar uma nova sequência de leituras ambientais.
2 — Visualizar ciclos: apresenta os ciclos cadastrados durante a execução.
0 — Sair: encerra o programa.

Passo 5: Ao cadastrar um ciclo, informe a quantidade de leituras desejadas e os valores de temperatura, PM2,5 e ruído solicitados.

Passo 6: Após finalizar as leituras, o programa exibirá os resultados estatísticos, os alertas e a classificação ambiental, além de gerar um relatório .txt na pasta em que o programa foi executado.

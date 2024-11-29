# FiapCap1Fase4

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto
Automação e inteligência na FarmTech Solutions

## 👨‍🎓 Integrantes: 
Gustavo Beu Gomes RM:560543

## 📜 Descrição
Projeto de Automação da FarmTech Solutions
O projeto desenvolvido ao longo das fases foi concebido para criar um sistema inteligente de monitoramento e controle agrícola, integrando hardware, software e técnicas de programação para otimizar recursos hídricos e gerenciar informações críticas sobre o ambiente de cultivo. Este sistema é baseado no microcontrolador ESP32, sensores de umidade, temperatura, luminosidade (LDR), além de um relé para controle de dispositivos externos.

Fase 1: Configuração Inicial e Prototipagem
Na primeira fase, o foco foi criar um sistema de prototipagem funcional no ambiente simulado Wokwi. O ESP32 foi configurado para ler dados de sensores de temperatura e umidade (DHT22) e um sensor LDR para medir a luminosidade. A saída dos dados foi configurada para ser exibida no Monitor Serial.

Objetivo:

Garantir a conectividade do ESP32.
Configurar os sensores e testar a coleta de dados.
Fase 2: Integração com Banco de Dados
Nesta fase, o projeto evoluiu para um sistema conectado, capaz de armazenar dados em um banco SQL. Usando bibliotecas como MySQL Connector e cx_Oracle, implementamos um CRUD para:

Registrar leituras de sensores.
Consultar e atualizar informações do sistema.
Gerar relatórios históricos que auxiliem na tomada de decisões para a irrigação.
Fase 3: Visualização e Controle Avançado
O objetivo aqui foi ampliar as funcionalidades do projeto, integrando controle de dispositivos externos (como bombas d’água) e exibição de dados em um display LCD. Elementos chave desta fase incluem:

Controle por Relé: Atuador ligado ao ESP32 para ligar/desligar dispositivos conforme os dados coletados.
Exibição em LCD: Dados de temperatura e umidade são exibidos em um display I2C.
Monitoramento Visual: Uso do Serial Plotter para criar gráficos em tempo real, representando as leituras dos sensores.
O código foi otimizado para gerenciar memória do ESP32, utilizando tipos de dados mais eficientes e reduzindo o consumo de recursos. Justificativas foram adicionadas como comentários no código para destacar as mudanças feitas.

Fase 4: Refinamento e Herança
O repositório original da Fase 3 foi herdado e reestruturado como parte da Fase 4, agora dentro de um template padrão definido pelo tutor. Isso garantiu uniformidade na estrutura de código e documentação do projeto.

Além disso, ajustes críticos foram realizados para:

Compatibilidade de Hardware: Garantir que os componentes sejam corretamente reconhecidos pelo ESP32, mesmo com bibliotecas originalmente voltadas para AVR.
Melhorias no Monitor Serial e LCD: Exibição de dados consistentes, com gráficos mais detalhados no Serial Plotter.
Conclusão
Este projeto destacou a aplicação prática de IoT (Internet das Coisas) e Big Data na agricultura, propondo soluções para:

Economia de Recursos: Reduzir desperdício de água e energia, acionando dispositivos apenas quando necessário.
Escalabilidade: Adaptação para diferentes ambientes agrícolas com necessidades específicas.
Análise de Dados: Registro histórico e monitoramento em tempo real para decisões baseadas em dados.
O sistema final entrega um ambiente controlado, visualmente informativo e alinhado com as demandas reais do setor agrícola, reforçando o papel da tecnologia na modernização da agricultura.

## 🔧 Como executar o código

Pré-Requisitos e Instalação do Projeto: Controle de Relé com ESP32 e Sensores no Wokwi
Para executar o projeto de controle de relé utilizando o ESP32 com sensores como DHT22 (temperatura e umidade), LDR (luminosidade) e LCD I2C (exibição de informações), você precisará configurar seu ambiente de desenvolvimento corretamente. Aqui está o guia detalhado para instalar os pré-requisitos e executar o código, utilizando Wokwi como plataforma de simulação.

Fase 1: Pré-Requisitos
1.1. Wokwi - Plataforma de Simulação
Para testar seu código sem utilizar hardware físico, você pode usar o Wokwi, uma plataforma de simulação online que oferece suporte para microcontroladores como o ESP32.

Passos para usar o Wokwi:

Acesse www.wokwi.com.
Crie uma conta se necessário ou faça login com sua conta do Google.
Crie um novo projeto, selecionando o ESP32 como o microcontrolador desejado.
1.2. Bibliotecas Necessárias
Antes de executar o código no Wokwi, é necessário garantir que você tenha as bibliotecas corretas para interação com os sensores e o display LCD. O Wokwi tem suporte para várias bibliotecas comuns, como as de DHT22 e LCD I2C, mas você pode precisar usar bibliotecas personalizadas em projetos mais complexos.

DHT22 Sensor: Para interagir com o sensor de temperatura e umidade.
LiquidCrystal_I2C: Para comunicação com o display LCD via I2C.
Wire Library: Para a comunicação I2C, já pré-configurada no Wokwi.
Fase 2: Baixando o Código e Configurando o Wokwi
2.1. Baixando o Código
Se você já tem o código pronto em um repositório GitHub ou em seu computador:

Repositório GitHub: Se o código estiver disponível, faça o download do arquivo .zip ou clone o repositório para seu computador.
Editor de Código no Wokwi: Após acessar o Wokwi, você pode copiar e colar o código diretamente no editor do Wokwi.
2.2. Configurando o Wokwi
Acesse o Wokwi e crie um novo projeto.
Adicione os Componentes:
No painel esquerdo, busque os componentes e adicione-os ao seu projeto. Para esse exemplo, você precisará do ESP32, LCD I2C, DHT22, LDR, e Relé.
Conecte os componentes conforme descrito no código:
LCD I2C: Conecte os pinos SDA e SCL aos pinos correspondentes do ESP32.
DHT22: Conecte o pino de dados ao pino GPIO 15.
LDR: Conecte ao pino A0 para leitura analógica.
Relé: Conecte ao pino GPIO 3 para controle de ativação.
Fase 3: Testando o Código no Wokwi
3.1. Simulando no Wokwi
Suba o código: Copie e cole o código no editor do Wokwi.
Inicie a simulação: Clique em Start Simulation. O Wokwi irá compilar e simular o comportamento do ESP32 com os sensores e o display LCD.
Monitore a saída no Serial Plotter: Você pode monitorar a saída dos sensores e ver as leituras de temperatura, umidade e luminosidade diretamente na interface do Wokwi, ou utilizando o Serial Plotter para visualizar gráficos.
3.2. Monitor Serial no Wokwi
O Serial Monitor do Wokwi mostra a leitura de dados em tempo real. No caso do projeto de controle de relé, você verá a temperatura, umidade, valores do LDR e o estado do relé. O código já está configurado para exibir essas informações no Monitor Serial do Wokwi, onde você pode monitorar e verificar se os sensores estão funcionando corretamente.

3.3. Testando a Lógica de Relé
Relé Ligado/Desligado: O estado do relé será controlado com base nas leituras dos sensores e nos botões. Quando um valor específico for lido (como umidade baixa ou luminosidade fraca), o relé será acionado.
A LCD I2C mostrará a temperatura e a umidade em tempo real, além do status do relé.
Fase 4: Ajustes Finais e Validação
4.1. Teste Final
Antes de concluir, verifique o comportamento esperado:

Os dados de temperatura e umidade devem ser atualizados no LCD e no Monitor Serial.
A leitura do LDR e os botões devem ser refletidos no estado do relé, tanto no código quanto na simulação do Wokwi.
4.2. Ajustes de Conexões
Caso algum componente não esteja funcionando como esperado (por exemplo, o display LCD não mostrar os dados), revise as conexões virtuais no Wokwi, especialmente os pinos SDA e SCL do LCD, que devem estar corretamente conectados aos pinos de I2C do ESP32.

Conclusão
Com os passos descritos acima, você configurou e simulou com sucesso o controle de relé e sensores no ESP32 usando a plataforma Wokwi. Essa abordagem permite testar o código sem a necessidade de hardware físico, o que é útil para depuração e ajustes iniciais.


Explicação da Parte Python da Atividade
Objetivo Geral
A parte Python da atividade serve como uma interface entre os dados coletados pelos sensores no ESP32 e o banco de dados. Ela é utilizada para realizar operações CRUD (Create, Read, Update, Delete), processar informações e permitir consultas e manipulações personalizadas. Isso possibilita um monitoramento eficiente e a integração dos dados do sistema com ferramentas analíticas ou dashboards.

Pré-requisitos
Antes de executar o código Python, certifique-se de atender aos seguintes pré-requisitos:

Ambiente de Desenvolvimento Configurado:

O Python deve estar instalado em sua máquina. Certifique-se de que sua versão é compatível com as bibliotecas utilizadas no projeto.
Bibliotecas Necessárias:

Você precisará de bibliotecas para conectar ao banco de dados (como MySQL Connector ou cx_Oracle).
O ambiente também deve incluir pacotes para manipulação de dados, como pandas, caso seja necessário.
Banco de Dados Configurado:

O banco de dados deve estar configurado com a estrutura exigida pelo projeto (tabelas de sensores, histórico de irrigação etc.).
As credenciais e endereços do servidor de banco de dados devem ser conhecidos e inseridos corretamente no script.
Acesso ao Projeto:

O código deve estar acessível em um repositório ou em sua máquina local. Certifique-se de ter baixado todos os arquivos necessários.
Passo a Passo de Execução
Baixe o Projeto:

Acesse o repositório do projeto (por exemplo, no GitHub) e faça o download ou clone-o para sua máquina.
Prepare o Ambiente:

Certifique-se de que o Python e as bibliotecas requeridas estão instalados.
Configure as variáveis de ambiente (se necessário), como PATH para banco de dados.
Configure o Banco de Dados:

Certifique-se de que o banco está em execução e que a estrutura necessária (tabelas, relacionamentos) já foi criada.
Verifique se o usuário que acessará o banco possui permissões adequadas.
Execute o Código Python:

Inicie o script principal através de sua IDE ou terminal. O script geralmente oferece as seguintes funcionalidades:
Coleta de dados do ESP32.
Armazenamento desses dados no banco de dados.
Visualização das informações armazenadas.
Teste Funcionalidades:

Use as opções disponíveis para verificar se os dados dos sensores estão sendo registrados corretamente no banco.
Realize operações CRUD para garantir que as funcionalidades de atualização, leitura e exclusão também estão operando conforme esperado.
Exemplo de Fluxo de Trabalho
Ao iniciar o script, os dados enviados pelo ESP32 são coletados e processados.
Esses dados são armazenados no banco de dados para criar um histórico.
O sistema exibe as leituras em tempo real e permite gerar relatórios com base nas consultas feitas no banco.
Justificativa
Essa integração da parte Python é essencial para transformar os dados brutos dos sensores em informações úteis e acessíveis. Além disso, ela permite futuras expansões do sistema, como análises preditivas ou integração com plataformas de visualização, melhorando a automação e o monitoramento agrícola.

Explicação da Integração do Scikit-learn e do Streamlit
Objetivo Geral
A integração dessas ferramentas adiciona funcionalidades de aprendizado de máquina (ML) e visualização interativa ao sistema. O Scikit-learn é usado para realizar análises preditivas ou classificações com base nos dados coletados, enquanto o Streamlit serve como interface gráfica, permitindo aos usuários interagirem com os modelos e visualizarem resultados de maneira amigável.

Pré-requisitos
Instalação das Bibliotecas Necessárias:

Certifique-se de que as bibliotecas Scikit-learn e Streamlit estão instaladas:
pip install scikit-learn streamlit
Outras dependências importantes incluem pandas, numpy, e ferramentas de visualização como matplotlib ou seaborn, dependendo do que você deseja exibir.
Dados Preparados no Banco:

Para usar o Scikit-learn, os dados coletados pelo sistema (como leituras de sensores ou históricos de irrigação) devem ser estruturados em um formato que permita o treinamento ou inferência de modelos de ML.
Integração do Scikit-learn
Preparação dos Dados:

Os dados do banco de dados são lidos e processados para formar datasets com variáveis explicativas (inputs, como umidade e temperatura) e uma variável alvo (output, como estado do relé: ligado/desligado).
Normalizações ou pré-processamentos podem ser realizados com ferramentas do Scikit-learn, como StandardScaler.
Treinamento de Modelos:

Escolha um modelo apropriado (como regressão logística, árvores de decisão ou um classificador k-Nearest Neighbors) para o problema.
Divida os dados em conjunto de treinamento e teste para avaliar o desempenho do modelo.
Inferência Preditiva:

Após o treinamento, o modelo pode ser usado para prever decisões futuras, como o acionamento de relés com base nas leituras de sensores.
Integração do Streamlit
Configuração do Streamlit:

Um arquivo Python dedicado ao Streamlit deve ser criado para servir como interface, com um comando típico para execução:
streamlit run app.py
Criação da Interface:

A interface permite a entrada de dados pelo usuário ou a seleção de registros do banco de dados para predições.
Visualizações interativas, como gráficos de tendência ou heatmaps, podem ser adicionadas para analisar os resultados.
Interatividade:

O Streamlit permite criar sliders, caixas de seleção e botões que facilitam a parametrização do modelo e a exploração dos dados.
Fluxo de Uso
Carregar Dados:

A aplicação Streamlit carrega os dados coletados do banco, processados e preparados para análise.
Visualização Inicial:

O usuário pode visualizar gráficos interativos com os dados de sensores, ajustando filtros para diferentes variáveis, como períodos ou condições específicas.
Teste do Modelo de ML:

O modelo treinado com Scikit-learn pode ser testado com entradas personalizadas no Streamlit, e os resultados são exibidos instantaneamente na interface.
Análise de Resultados:

A aplicação exibe métricas de desempenho, como acurácia, precisão ou erro médio, permitindo ao usuário avaliar a eficácia do modelo.
Benefícios
A combinação de Scikit-learn e Streamlit aprimora o sistema, oferecendo:

Predição Automatizada: Decisões inteligentes baseadas nos dados coletados.
Visualização Amigável: Dados e resultados de aprendizado de máquina acessíveis para não-especialistas.
Flexibilidade: Expansão futura para novos modelos ou mais interatividade.
Essa integração transforma o projeto em uma solução avançada e prática para a análise de dados agrícolas.






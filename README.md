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






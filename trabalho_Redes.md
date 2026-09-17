Trabalho Prático 1 — Servidor Web utilizando Sockets

Valor: 4,0 pontos

Nesta atividade, você deverá desenvolver um servidor Web utilizando Sockets TCP, aplicando na prática os conteúdos estudados nas camadas de Aplicação e Transporte.

O trabalho poderá ser realizado individualmente ou em grupos de até 4 alunos. A linguagem de programação é livre, porém não será permitido utilizar frameworks ou servidores Web prontos, como Flask, Django, FastAPI, Express, Spring Boot ou equivalentes. O objetivo é que a comunicação seja implementada diretamente por meio de Sockets.

O servidor deverá utilizar TCP e interpretar requisições HTTP GET, permanecendo em execução para atender requisições sequenciais.
Requisitos principais

O servidor deverá:

    criar e configurar um Socket TCP;

    utilizar uma porta para receber conexões;

    aguardar e aceitar conexões de clientes;

    receber e exibir a requisição HTTP;

    identificar o recurso solicitado;

    implementar a rota /, apresentando a página principal;

    implementar a rota /sobre, apresentando informações sobre Socket, TCP e HTTP;

    responder com HTTP/1.1 200 OK para recursos existentes;

    responder com HTTP/1.1 404 Not Found quando o recurso solicitado não existir;

    enviar a resposta HTTP e o conteúdo HTML diretamente pelo Socket;

    permitir testes utilizando um navegador Web.

O teste poderá ser realizado localmente utilizando, por exemplo:

http://localhost:8080

ou:

http://127.0.0.1:8080

O acesso ao servidor a partir de outro computador da mesma rede e a implementação de recursos adicionais poderão ser realizados como aprofundamento, mas não são necessários para obtenção da pontuação total.
Entrega

A entrega deverá conter:

    código-fonte completo do servidor;

    relatório em PDF com as evidências de execução solicitadas no enunciado;

Caso o trabalho seja desenvolvido em grupo, somente um integrante deverá realizar a postagem, informando no campo de texto da entrega o nome completo de todos os participantes.

Atenção: a correção do trabalho está condicionada à apresentação em aula. A ausência na apresentação implicará nota zero, conforme orientações descritas no enunciado.

Consulte abaixo todos os requisitos, evidências e critérios de avaliação antes da entrega.

Critérios de Avaliação — 4,0 pontos

A nota será composta pelos seguintes critérios:

    Implementação do servidor com Socket TCP — 1,0 ponto
    Será verificado se o programa cria corretamente um Socket TCP, realiza a associação com uma porta, entra em modo de escuta, aceita conexões, recebe dados e envia respostas ao cliente.
    Implementação das requisições e respostas HTTP — 1,0 ponto
    O servidor deverá interpretar requisições HTTP do tipo GET e gerar respostas HTTP válidas. Deverão ser implementadas corretamente:
        rota /;
        rota /sobre;
        resposta 200 OK;
        resposta 404 Not Found para recursos inexistentes.
    Funcionamento e testes da aplicação — 0,8 ponto
    Será avaliado se o servidor executa corretamente e pode ser acessado por um navegador Web. O aluno deverá demonstrar o funcionamento das rotas e do tratamento de erro, além de apresentar no terminal as requisições recebidas.
    Relatório e evidências de execução — 0,6 ponto
    O relatório deverá apresentar, de forma organizada:
        código-fonte desenvolvido;
        servidor em execução;
        acesso à página principal;
        acesso à rota /sobre;
        teste da resposta 404 Not Found;
        requisições HTTP exibidas no terminal.
    Compreensão dos conceitos de Redes — 0,6 ponto
    Será considerada a qualidade das respostas das questões teóricas e a capacidade de explicar, durante a apresentação, os conceitos relacionados a:
        Socket;
        TCP;
        HTTP;
        endereço IP;
        número de porta;
        relação entre Camada de Aplicação e Camada de Transporte.

Total: 4,0 pontos

A pontuação poderá ser reduzida quando a solução funcionar parcialmente, quando houver ausência de evidências ou quando o aluno não conseguir explicar o funcionamento do próprio código durante a apresentação.

O uso de frameworks ou servidores Web prontos, quando contrário ao enunciado da atividade, compromete o objetivo do trabalho e poderá resultar em perda significativa de pontuação no critério de implementação.

A apresentação em aula é obrigatória para a correção do trabalho.
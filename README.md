# trabalhoSDRest

Este repositório contém códigos referentes a um sistema distribuído composto por cliente, middleware e servidores, onde a comunicação entre os mesmos foi realizada utilizando o protocolo REST, e a programação foi realizada com a linguagem de programação Python, utilizando o framework Flask.

O cliente (simula_cliente.py) envia para o middleware (middleware.py) uma requisição para transformação de um texto. O middleware recebe o texto enviado pelo cliente e o encaminha para dois servidores diferentes. O servidor 1 (servidor1.py) realiza a função de uppercase no texto recebido e o retorna para o middleware. O servidor 2 (servidor2.py) retira todos os espaços em branco presentes no texto recebido e o retorna para o middleware. Após receber os dois textos transformados, o middleware os encaminha para o cliente. 

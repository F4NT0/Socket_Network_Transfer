# Trabalho final de Redes de Computadores

* Implementar uma aplicação com o protocolo UDP que simule o comportamento de um Protocolo de Transferência de Arquivos orientado a conexão.

### O que deve ser implementado

1. Estabelecimento e encerramento da conexão da aplicação
2. Sequenciamento das Mensagens
3. Controle de erro das Mensagens
4. Envio de dados (arquivos devem ser selecionados do computador)
5. Controle de Congestionamento

**Implementar 3 técnicas de controle de congestionamento do Protocolo TCP**

1. `Slow Start`: Possui um crescimento exponencial. A idéia que a aplicação comece com a transmissão de um pacote e vá aumentando a taxa de envio (2,4,8,16,...) á medida que as confirmações cheguem do destino.
2. `Congestion Avoidance`: Esta técnica faz um crescimento linear e é utilizada após o _Slow Start_.
3. `Fast Retransmit`: É uma técnica que faz a retransmissão imediata de um pacote ao Receber 3 ACKs duplicados.

* A aplicação terá que definir um tamanho de janela de congestionamento, que será o limite do funcionamento da técnica de _Slow Start_ e inicio do _Congestion Avoidance_.
* A retransmissão de um pacote poderá acontecer por dois problemas: `timeout` e a `recepção de 3 ACKs duplicados`.
  * No caso do `timeout`, a aplicação volta ao inicio do Slow Star, ou seja, começa a retransmissão com 1 pacote e vai crescendo exponencialmente
  * No caso da `recepção de 3 ACKs duplicados`, ocorrerá uma retransmissão imediata somente do pacote identificado pelo ACK, o tamanho da janela de congestionamento cai pela metade e a técnica de Congestion Avoidance é continuada.
* Os números de sequência devem começar em zero e ir incrementando de acordo com a quantidade de pacotes que está sendo transmitida.
* O número do ACK representa o número de sequência mais 1, ou seja, indica o número do pacote que o destino deseja receber.
* O controle de erro deve ser realizado pela própria aplicação através de um **algoritmo de cálculo de CRC** já existente.
* O valor do CRC deve ser incluído no pacote e o destino, ao recebê-lo,deve recalcular o CRC para identificar se o pacote chegou corretamente.
* Caso o pacote esteja correto, um ACK do número de sequência mais 1 deve ser enviado.
* Caso não esteja correto, o detino deve somente descartar o pacote recebido.
* Todo o pacote recebido pelo destino deve ser confirmado e o destino deve ter um controle dos números de sequência que já recebeu.
* Ele não pode confirmar a recepção de um pacote com um determinado número de sequência se o pacote com número de sequência menor não foi confirmado. Neste caso, um ACK com o número de sequência do último pacote já confirmado deve ser transmitido.

**Envio de Arquivo**

* O usuário que utiliza a aplicação deve escolher um Arquivo qualquer do sistema operacional para enviar para o destino, sendo esse passado como parâmetro.
  * Esse Arquivo deverá ser dividido em partes de 300 bytes e enviado para o destino, seguindo a implementação das técnicas de controle de congestionamento mencionadas acima.
  * O destino, conforme for recebendo todos os pacotes que fazem parte do arquivo original,deve remotá-lo e salvá-lo em um arquivo.
* Todos os pacotes do nível de aplicação devem ter 300 bytes, inclusive o último pacote, assim a aplicação deve controlar o padding caso o último pacote não chegue a esse valor. 
* Após a transmissão de todos os Arquivos, iremos utilizar o comando `md5sum` ou `shasum` na origem e no destino para validar o recebimento correto do arquivo.
* Durante o envio do arquivo, a aplicação deve imprimir um log na tela do que está acontecendo na transmissão,tando do lado da maquina origem como da maquina destino. Será necessário utilizar a função _sleep_ para que seja possível visualizar a troca de mensagens.

**Tipo de Socket**

* Quanto ao tipo de Socket a ser utilizado na aplicação para a comunicação, deve-se observar que a comunicação deve ser implementado com **Socket UDP** chamado **Datagram Socket** para envio e recebimento das mensagens.

**Perda de pacotes**

Para a perda de pacotes ocorra será necessário utilizar o _netem_ para linux, o _clumsy_ caso use o Windows ou o _Network Link Conditioner_ para o Mac.

### Regras da Professora

1. Não pode entregar depois do prazo (23/11).
2. Trabalho deve compilar e funcionar, senão não vai ser aceito.
3. Copias de outro trabalho é zero automatico.

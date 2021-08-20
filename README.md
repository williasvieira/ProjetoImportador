# ProjetoImportador
Projeto da disciplina Laboratorio de Banco de Dados.<br>
<h1>Descrição do Problema</h1>
Este ano temos as eleições municipais brasileiras onde milhares de pessoas se
candidataram para os cargos de vereador, prefeito e vice-prefeito. O TSE (Tribunal Superior
Eleitoral) construiu um sistema disponível em (http://divulgacandcontas.tse.jus.br/divulga/#/).
A aplicação Web que pode ser acessada neste endereço, solicita os dados ao servidor de
aplicação, transformando os dados do PostgreSQL no formato amplamente conhecido
chamado JSON (https://www.json.org/json-pt.html). Ele nada mais é do que um arquivo
texto utilizado para envio e recebimento de dados entre aplicações, que inclusive podem ser
escritas em linguagens diferentes.<br>
Devido a um erro humano, todo o banco de dados SQL foi apagado restando somente os
arquivos JSON contendo os dados da Aplicação. Como estudante e futuro profissional de
computação, seu dever é refazer a ESTRUTURA do banco de dados analisando os dados
contidos nestes arquivos. Em seguida, deve-se realizar a importação dos dados que estão
em formato JSON para dentro do novo banco criado.<br>
Os arquivos JSON possuem um formato que podem ser lidos e manipulados por
QUALQUER linguagem de programação de alto nível que conhecemos. Dentre elas
podemos destacar: C/C++, JAVA, Python, PHP, Ruby, Javascript e outras inúmeras
linguagens descritas aqui (https://www.json.org/json-pt.html).<br>
O arquivos contendo os dados dos candidatos estão disponíveis aqui:<br>
https://facom.ufms.br/~/marcio/candidatos.zip<br>
No arquivo ZIP existem 8.607 arquivos JSON que representam cada um dos 8.607
candidatos de Mato Grosso do Sul. Precisamos fazer uma engenharia reversa a partir deste
dados, propondo uma estrutura no banco de dados PostgreSQL para armazená-los.
Observe com cuidado para que nenhum dado fique de fora do banco de dados.
Depois de analisar os dados que estes arquivos contém, criando a estrutura do banco de
dados, como você importará os dados de 8.607 candidatos neste banco dados? Não é
viável fazer isso manualmente, você pode utilizar alguma linguagem de programação que
você domina para este trabalho.

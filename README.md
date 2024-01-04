O DCE está organizando um campeonato de futebol entre alunos da UNIFEI. Para tanto,
precisa cadastrar as equipes participantes. Uma equipe deve ser composta de alunos de
um mesmo curso. Para participar da equipe, basta ao aluno estar regularmente
matriculado.
No sentido de atender essa demanda do DCE, você deverá implementar um sistema que
permita manter um cadastro das equipes participantes. Para tanto, implemente as classes
-Curso e Estudante, descritas a seguir.
Curso;
Atributos: sigla, nome;
Estudante.
-Atributos: nroMatric, nome, Curso.
Implemente essas classes com construtores contendo dois e três atributos,
respectivamente. Em seguida, utilize o código a seguir para popular duas listas com
instâncias de cursos e estudantes (este código deve ficar no controlador apropriado).
c1 = Curso("CCO", "Ciência da Computação")
c2 = Curso("SIN", "Sistemas de Informação")
c3 = Curso("EEL", "Engenharia Elétrica")
listaCurso = []
listaCurso.append(c1)
listaCurso.append(c2)
listaCurso.append(c3)
#Inserir mais cursos, se quiser
listaEstudante = []
listaEstudante.append(Estudante(1001, "José da Silva", c1))
listaEstudante.append(Estudante(1002, "João de Souza", c1))
listaEstudante.append(Estudante(1003, "Rui Santos", c2))
#Inserir mais 7 alunos, totalizando pelo menos 10 na lista
- Questão 1 – Criação de equipes 
Elabore uma aplicação com interface gráfica para criação de equipes. A interface da
aplicação deve apresentar um combo box, o qual deve conter o nome dos cursos
cadastrados. Após a escolha de um curso, deve-se realizar a inclusão de estudantes na
equipe do curso escolhido. Para tanto, a interface deve prover um campo Entry para
digitação do número de matrícula dos alunos. Após a digitação de um número de
matrícula, o programa deve verificar se o mesmo é um número de matrícula válido e se o
referido aluno está matriculado no curso selecionado no combo box. Caso essas duas
condições sejam satisfeitas, deve inseri-lo em uma lista chamada listaEstEquipe. Caso o
número de matrícula seja inválido, ou o aluno selecionado esteja matriculado em outro
curso, deve-se dar uma mensagem de erro. A interface deve prover um botão com o
rótulo “Cria Equipe” que deve ser selecionado quando todos os alunos que compõem a
equipe tiverem sido escolhidos. Neste momento, deve-se gerar um objeto da classe
Equipe, contendo o curso escolhido no combo box e a lista de estudantes que compõem a
equipe (listaEstEquipe). O objeto gerado deve ser armazenado na lista denominada
listaEquipe. Seu código deve salvar a listaEquipe num arquivo, de modo que os dados
das equipes não sejam perdidos (a lista deverá ser recuperada toda vez que o programa
iniciar). Os dados de cursos e estudantes não precisam ser salvos, pois o código
fornecido irá construir as listas de cursos e estudantes toda vez que o programa for
executado. Para simplificar a implementação, poderá haver apenas 1 equipe para cada
curso. Assim, as equipes poderão ser identificadas pela sigla do curso.
- Questão 2 – Consulta de Equipes 
Implemente uma interface que permita consultar equipes a partir da sigla do curso. Sua
interface deve prover um campo para digitação da sigla. Após a digitação da sigla do
curso, deve-se checar se o mesmo existe, em seguida deve-se verificar se existe alguma
equipe daquele curso. Se a sigla do curso for inexistente, deve-se dar a seguinte
mensagem: “Esta sigla de curso não existe”. Se o curso existir, mas não houver equipe
daquele curso, deve-se dar a mensagem: “Não existe equipe desse curso”. Caso exista
uma equipe do curso, deve-se exibir o nome de todos os alunos cadastrados na equipe.
- Questão 3 – Dados do campeonato
Implemente um interface para exibição de dados estatísticos sobre o campeonato. A
interface deve exibir:
-Número de equipes: XX
-Número total de estudantes: XX
-Média de estudante por equipe: XX
O número total de estudantes é a quantidade de estudantes que estão participando do
campeonato. A média de estudantes por equipe é o número total de estudantes dividido
pelo número de equipes.
Você deve implementar um menu com as opções:
- Criar Equipe
- Consultar Equipe
- Imprimir dados
Importante: Você deve criar um arquivo chamado main.py, o qual deve conter o código
que gera o menu. Este arquivo deve conter um cabeçalho no qual deve constar seu nome
e seu número de matrícula.
Você deve zipar os arquivos da prova, produzindo um único arquivo .zip. Este arquivo
deve ser nomeado com o seu número de matrícula

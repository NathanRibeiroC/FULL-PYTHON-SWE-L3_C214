# L3_C214 :snake:
[![Build - Linux](https://github.com/NathanRibeiroC/L3_C214/actions/workflows/build-linux.yaml/badge.svg)](https://github.com/NathanRibeiroC/L3_C214/actions/workflows/build-linux.yaml)
[![Build - Windows](https://github.com/NathanRibeiroC/L3_C214/actions/workflows/build-windows.yaml/badge.svg)](https://github.com/NathanRibeiroC/L3_C214/actions/workflows/build-windows.yaml)
[![Python 3V's](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-360/)

## Descrição 

O intuito deste repositório é apresentar uma solução para a lista 3 de C214 100% em Python, utilizando conceitos de engenharia de Software, tal como build automatizada, integração contínua, testes automatizados, etc.
A seguir serão mostradas duas etapas, para configuração de um ambiente Python que seja capaz de rodar o projeto.

## Sugestão de como importar o ambiente virtual

É altamente recomendável ao trabalhar com projetos python, utilizar de [ambientes virtuais](https://csguide.cs.princeton.edu/software/virtualenv), os ambientes virtuais Python ajudam a desacoplar e isolar versões do Python e pacotes pip associados. Isso permite que os usuários finais instalem e gerenciem seu próprio conjunto de pacotes que são independentes daqueles fornecidos pelo sistema. Os ambientes virtuais permitem que você tenha um ambiente estável, reproduzível e portátil. Você controla quais versões de pacotes são instaladas e quando são atualizadas.
Existem várias maneiras de se configurar um ambiente virtual em python, vou listar aqui alguns bons links que podem ajudar nessa configuração: [:link:](https://docs.python.org/3/library/venv.html), [:link:](https://realpython.com/lessons/creating-virtual-environment/), [:link:](https://towardsdatascience.com/virtual-environments-for-absolute-beginners-what-is-it-and-how-to-create-one-examples-a48da8982d4b), [:link:](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

Uma vez escolhido o método para criação do ambiente virtual, é só verificar uma maneira de criar o ambiente segundo o arquivo  `environment.yml`. Também deixarei listado aqui algumas boas maneiras de se fazer isso: [:link:](https://developer.akamai.com/blog/2017/06/21/how-building-virtual-python-environment), [:link:](https://gist.github.com/luiscape/19d2d73a8c7b59411a2fb73a697f5ed4), [:link:](https://www.jetbrains.com/help/pycharm/managing-dependencies.html), [:link:](https://www.codegrepper.com/code-examples/python/conda+create+requirements.txt).

Minha recomendação é utilizar o [Anaconda](https://conda.io/projects/conda/en/latest/index.html) para realização da gerência de dependências e de ambientes virtualizados, de forma mais simples. E seguir as seguintes etapas:

- [Dowload do Anaconda](https://www.anaconda.com/products/individual)

<details>
  <summary> Expanda para mais detalhes da instalação do arquivo .exe </summary>
  
  ### Siga esses passos para instalar corretamente
  
  1. Ao executar o .exe baixado esta tela de instalação aparecerá a priori, pode clicar em "Next".
  
  <p align="center">
  <img width="491" height="382" src="https://user-images.githubusercontent.com/80288857/137563463-b7b0c16a-0f95-410b-ba77-5fbd2ffdd5c7.png">
  </p>
  
  2. Pode concordar com os termos e clicar em "I agree".
  
  <p align="center">
  <img width="491" height="382" src="https://user-images.githubusercontent.com/80288857/137563617-58f08695-f702-4930-a57a-ff3e2828cfc5.png">
  </p>
  
  3. É interessante clicar em "Just Me".
  
  <p align="center">
  <img width="491" height="382" src="https://user-images.githubusercontent.com/80288857/137563781-66177e59-b3d1-4493-865c-9d7e5cb37b75.png">
  </p>
  
  4. É muito importante instalar o Anaconda em ProgramData ou qualquer diretório que não tenha espaço, caso contrário pode ocasionar em problemas, ao tentar associar o interpretador do python presente no ambiente virtual Anaconda à alguma IDE, porém o caminho mais utilizado para instalação é a pasta ProgramData.
  
  <p align="center">
  <img width="491" height="382" src="https://user-images.githubusercontent.com/80288857/137563978-8a973682-bedd-49d7-a5df-49f3c8e472e1.png">
  </p>
  
  5. É muito interessante selecionar as duas opções, primeiro pelo fato de que adicionar o Anaconda às variáveis de sistema do Windows, vai permitir usar o CONDA direto do terminal da IDE e do cmd Windows. E segundo pelo fato de configurar o interpretador do Anaconda como padrão pode facilitar na configuração do interpretador em algumas IDEs, não é o caso do Pycharm que é a IDE sugerida e que em breve será abordado como fazer a configuração do interpretador nele.
  
  <p align="center">
  <img width="491" height="382" src="https://user-images.githubusercontent.com/80288857/137564214-fc854c0c-e5ef-48bb-aeb6-bb52b3c5351b.png">
  </p>
  
  6. Espere terminar a instalação, cique em "Next". 
  
  <p align="center">
  <img width="491" height="382" src="https://user-images.githubusercontent.com/80288857/137564757-2609ef04-9a3c-4b79-a70e-8c084c4d2441.png">
  </p>
  
  7. Clique em "Finish".
  
  <p align="center">
  <img width="491" height="382" src="https://user-images.githubusercontent.com/80288857/137564847-523096a1-9980-45d9-bdef-e5e71599740d.png">
  </p>
  
  8. Se quiser visualizar a pasta de instalação no diretório ProgramData, para ajudar a pegar o caminho do interpretador nas etapas posteriores, que por padrão o Windows oculta, logo para visualizá-lo, dentro do disco local que você instalou, vá em exibir e selecione a checkbox Itens ocultos.
  
  <p align="center">
  <img width="1335" height="461" src="https://user-images.githubusercontent.com/80288857/137565439-ea47219f-249d-4c28-bc85-ac5aaf605d0c.png">
  </p>

</details>

- Para verificar se a instalação ocorreu de forma correta, abra o prompt de comando do windows `WINDOWS+R` e digite `cmd`, digite `conda --version` o terminal deve exibir `conda <versão_atual>`.
- Clone o repositório deste projeto, `git clone`, em algum caminho de sua preferência.
- Agora criaremos o ambiente virtual a partir do arquivo `environment.yml`, logo abra o prompt de comando e navegue até o diretório raiz do repositório que foi clonado. E digite o seguinte comando: `conda env create -f environment.yml` 

<details>
  <summary> Expanda para mais detalhes da criação do ambiente virtual </summary>
  
  ### Verifique se as etapas realizadas acima para configuração do ambiente virtual resultaram nas seguintes respostas do terminal ou parecido
  
  1. Navegação até o repositório clonado
  
  <p align="center">
  <img width="963" height="502" src="https://user-images.githubusercontent.com/80288857/137566178-f15b5a3f-7f30-46ab-a743-3143ef345f36.png">
  </p>
  
  2. Criação a partir do arquivo .yml

  <p align="center">
  <img width="962" height="284" src="https://user-images.githubusercontent.com/80288857/137566227-e186bf9b-4211-406c-8fd8-ef3b6ba39fd1.png">
  </p>

  3. O terminal mostrará as dependências instalando

  <p align="center">
  <img width="963" height="494" src="https://user-images.githubusercontent.com/80288857/137566263-b8d58969-7f59-49f1-b8bb-6cc10485d7a7.png">
  </p>

  4. E a ativação do ambiente
  
  <p align="center">
  <img width="960" height="464" src="https://user-images.githubusercontent.com/80288857/137566287-b100361d-b1e9-44e2-86c8-3e2b4e472e27.png">
  </p>

</details>

- É interessante verificar no anaconda navigator se o ambiente foi criado da forma correta. Digite `anaconda-navigator` no prompt de comando para abrir o navigator, ele já vem instalado com o anaconda.

<details>
  <summary> Expanda para mais detalhes da criação do ambiente virtual </summary>
  
  ### Verifique se as etapas realizadas acima para configuração do ambiente virtual resultaram nas seguintes respostas do terminal ou parecido
  
  Uma vez dentro do Navigator, vá em Environmets e veja se o ambiente my (nome do environment definido no arquivo environment.yml) foi criado, se você clicar nele, poderá ver as dependências que foram instaladas, bem como a versão do python. Você pode instalar outras dependências também, porém não recomendo. Uma coisa interessante de citar é que o Anaconda já elimina conflitos automaticamente todas as vezes que uma dependência é instalada, coisa que nem sempre é feita ao usar o pip.
  
  <p align="center">
  <img width="963" height="502" src="https://user-images.githubusercontent.com/80288857/137566754-8dd83938-04b7-4a4b-b07a-0efc81d6111b.png">
  </p>
  
</details>

- Uma vez criado o ambiente, deve-se verificar como trabalhar com esse ambiente dentro da IDE utilizada, que será abordado melhor no próximo tópico

## Associação do ambiente virtual à IDE

Existem várias IDEs utilizadas para desenvolvimento em linguagem python, e cada uma tem uma maneira de fazer a associação do ambiente virtual e a seleção do interpretador Python. Listarei aqui como fazer esse processo em 3 IDEs. Porém recomendo fortemente o uso do Pycharm, principalmente pelo fato de que ele fará a associação das variáveis ao sistema de forma automática, eliminando assim, problemas referente ao uso de imports relativos entre os módulos da solução.
- Pycharm [:link:](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html), [:link:](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)

<details>
  <summary> Passo a passo da configuração do interpretador no Pycharm </summary>
  
  ##
  
  1. Abra a pasta do projeto no Pycharm. Por você ter aberto o projeto pela primeira vez, o Pycharm identificará o arquivo .yml e te sugerirá que um novo ambiente virtual pode ser criado a partir desse arquivo e o interpretador deste começar a ser usado no projeto. Daria certo também, porém a configuração anterior do ambiente, antes da associação com a IDE serve para qualquer IDE.
  
  <p align="center">
  <img width="600" height="170" src="https://user-images.githubusercontent.com/80288857/137567040-b707a759-a187-4619-9920-5949c31f7ae3.png">
  </p>
  
  2. Uma vez que você abriu a pasta do projeto do Pycharm. Vá em File --> Settings.
  
  <p align="center">
  <img width="1300" height="700" src="https://user-images.githubusercontent.com/80288857/137567037-3aa5843a-6f3a-483d-9a93-597a6054373d.png">
  </p>

  3. Vá em Project --> Add
  
  <p align="center">
  <img width="980" height="720" src="https://user-images.githubusercontent.com/80288857/137567043-0efa329a-c34f-4628-a2f9-ee2e6790ba91.png">
  </p>  
  
  4. Vá em System Interpreter --> clique nos ...
  
  <p align="center">
  <img width="825" height="570" src="https://user-images.githubusercontent.com/80288857/137567045-b9741bee-9267-4864-a280-21185d71ddd0.png">
  </p>    

  5. Clique no ícone de exibir arquivos ocultos, para o Pycharm mostrar o ProgramData.
  
  <p align="center">
  <img width="420" height="480" src="https://user-images.githubusercontent.com/80288857/137567048-7e20ba58-13f9-4179-a0f1-8f5ab4627042.png">
  </p>      

  6. Navegue até o ambiente virtual "my", criado a partir do environment.yml,  faça o seguinte caminho: ProgramData --> anaconda --> envs --> my --> python.exe. Clique em Ok.
  
  <p align="center">
  <img width="430" height="490" src="https://user-images.githubusercontent.com/80288857/137567050-f8abd289-a0dc-4cef-9e2a-50d7df9c37f3.png">
  </p>  

  7. Já será possível visualizar o interpretador configurado de acordo com o ambiente virtual criado anteriormente.
  
  <p align="center">
  <img width="973" height="700" src="https://user-images.githubusercontent.com/80288857/137567053-83494582-1162-4e87-be64-63e95a5c087e.png">
  </p>  

  8. Vá em src --> main.py. Clique com o direito na tela do arquivo main.py e clique em Run 'main'.
  
  <p align="center">
  <img width="1320" height="720" src="https://user-images.githubusercontent.com/80288857/137567055-496ad2b9-716c-4a48-b207-d595b697eaf0.png">
  </p> 
  
  9. O projeto já estará funcionando.
  
  <p align="center">
  <img width="1314" height="716" src="https://user-images.githubusercontent.com/80288857/137567057-5b1c89ee-56b6-4cd7-81ef-ece2afcf3b64.png">
  </p>  
  
</details>

- Visual Studio Code [:link:](https://medium.com/@joaolggross/como-configurar-o-vs-code-com-anaconda-e-jupyter-notebooks-b05258bf65c1), [:link:](https://code.visualstudio.com/docs/python/environments)
- Sublime Text [:link:](https://docs.anaconda.com/anaconda/user-guide/tasks/integration/sublime/), [:link:](http://damnwidget.github.io/anaconda/anaconda_settings/)

## Funcionamento

![Animação](https://user-images.githubusercontent.com/80288857/137222805-89ee24c0-9659-4ab1-a5a6-691969ba627b.gif)

No GIF acima, foi mostrado o funcionamento do projeto, assim como sua interface gráfica. Via combo box, filtramos o conteúdo dos arquivos e assim que o botão é clicado, um arquivo csv com seu conteúdo é gerado. Na implementação feita, foi extendido um pouco ainda as funcionalidades da lista e pode-se filtrar também por plataforma e publisher, ou pode-se optar pelo formato padrão e filtrar só por plataforma ou só por publisher.
Se caso uma busca já tiver sido efetuada e outra for efetuada em seguida, o arquivo .csv é substituído pelo conteúdo da busca mais recente, porém isto foi apenas conveniente para implementação e para não ficar ocupando a pasta resources com muitos arquivos.







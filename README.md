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

Uma vez escolhido o método para criação do ambiente virtual, é só verificar uma maneira de criar o ambiente segundo o arquivo  `requirements.txt`. Também deixarei listado aqui algumas boas maneiras de se fazer isso: [:link:](https://developer.akamai.com/blog/2017/06/21/how-building-virtual-python-environment), [:link:](https://gist.github.com/luiscape/19d2d73a8c7b59411a2fb73a697f5ed4), [:link:](https://www.jetbrains.com/help/pycharm/managing-dependencies.html), [:link:](https://www.codegrepper.com/code-examples/python/conda+create+requirements.txt).

Minha recomendação é utilizar o [Anaconda](https://conda.io/projects/conda/en/latest/index.html) para realização da gerência de dependências e de ambientes virtualizados, de forma mais simples. E seguir as seguintes etapas:

- [Dowload do Anaconda](https://www.anaconda.com/products/individual)

<details>
  <summary> Expanda para mais detalhes da instalação do arquivo .exe </summary>
  
  ## Siga esses passos para instalar corretamente
  1. Ao executar o .exe baixado esta tela de instalação aparecerá a priori, pode clicar em "Next".
  <p align="center">
  <img width="491" height="382" src="https://user-images.githubusercontent.com/80288857/137563463-b7b0c16a-0f95-410b-ba77-5fbd2ffdd5c7.png">
  </p>
  2. Pode concordar com os termos e clicar em "I agree"
  <p align="center">
  <img width="491" height="382" src="https://user-images.githubusercontent.com/80288857/137563617-58f08695-f702-4930-a57a-ff3e2828cfc5.png">
  </p>
  3. É interessante clicar em "Just Me"
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
</details>

- Para criar o ambiente [abrir o anaconda prompt](https://stackoverflow.com/questions/47914980/how-to-access-anaconda-command-prompt-in-windows-10-64-bit/55545141#:~:text=Go%20with%20the%20mouse%20to,%22Anaconda%20Prompt%22%20will%20open.), digitar no terminal `pip install -r requirements.txt` ou se preferir usar a sintaxe conda `conda create --name <env_name> --file requirements.txt`
- É interessante verificar no [anaconda navigator](https://docs.anaconda.com/anaconda/navigator/getting-started/) se o ambiente foi criado da forma correta
- Uma vez criado o ambiente, deve-se verificar como trabalhar com esse ambiente dentro da IDE utilizada, que será abordado melhor no próximo tópico
- Após seguir esse passo a passo, já é possível rodar o projeto em um ambiente adequado na IDE que for preferida

## Associação do ambiente virtual à IDE

Existem várias IDEs utilizadas para desenvolvimento em linguagem python, e cada uma tem uma maneira de fazer a associação do ambiente virtual e a seleção do interpretador Python. Listarei aqui como fazer esse processo em 3 IDEs. Porém recomendo fortemente o uso do Pycharm, principalmente pelo fato de que ele fará a associação das variáveis ao sistema de forma automática, eliminando assim, problemas referente ao uso de imports relativos entre os módulos da solução.
- Pycharm [:link:](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html), [:link:](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)
- Visual Studio Code [:link:](https://medium.com/@joaolggross/como-configurar-o-vs-code-com-anaconda-e-jupyter-notebooks-b05258bf65c1), [:link:](https://code.visualstudio.com/docs/python/environments)
- Sublime Text [:link:](https://docs.anaconda.com/anaconda/user-guide/tasks/integration/sublime/), [:link:](http://damnwidget.github.io/anaconda/anaconda_settings/)

## Funcionamento

![Animação](https://user-images.githubusercontent.com/80288857/137222805-89ee24c0-9659-4ab1-a5a6-691969ba627b.gif)

No GIF acima, foi mostrado o funcionamento do projeto, assim como sua interface gráfica. Via combo box, filtramos o conteúdo dos arquivos e assim que o botão é clicado, um arquivo csv com seu conteúdo é gerado. Na implementação feita, foi extendido um pouco ainda as funcionalidades da lista e pode-se filtrar também por plataforma e publisher, ou pode-se optar pelo formato padrão e filtrar só por plataforma ou só por publisher.
Se caso uma busca já tiver sido efetuada e outra for efetuada em seguida, o arquivo .csv é substituído pelo conteúdo da busca mais recente, porém isto foi apenas conveniente para implementação e para não ficar ocupando a pasta resources com muitos arquivos.







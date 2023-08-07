# QGISSPARQL:Layer2Triple

# Visão geral

**Repositório**: https://github.com/LambdaGeo/qgisparql-Layer2Triple/

**Criadores**: [Sérgio Souza Costa](https://github.com/profsergiocosta) e  [Nerval Junior](https://github.com/nervaljunior)

### Este plugin visa exportar os dados de uma camada de dado geográfico no sistema de informação geográfica QGIS (https://qgis.org/).

# Layer2Triple
## An application for exporting geographic data

![](https://img.shields.io/badge/Language-Python-blue)![](https://img.shields.io/badge/Compiler-QGIS-brightgreen) ![](https://img.shields.io/badge/IDE-Microsoft%20Visual%20Studio%202022-blue) ![](https://img.shields.io/badge/Environment-Windows-red) ![](https://img.shields.io/badge/Environment-Linux-purple) ![](https://img.shields.io/badge/User%20Interface-GUI%20%2B%20CLI-yellowgreen)

---

O Plugin Layer2triple é um complemento do QGIS que permite a criação de arquivos RDF (Resource Description Framework) no formato Turtle (.ttl). Para isso é feito a conversão de camadas vetoriais em uma linguagem de triplas RDF para o formato Terse Triple Language. Ele abre uma janela de diálogo com uma tabela na qual o usuário pode selecionar atributos de uma camada vetorial e definir o valor RDF correspondente. Assim, o usuário pode selecionar quais atributos deseja incluir no arquivo RDF.  O usuário pode salvar o arquivo e fornecer uma URL para os recursos RDF. 

O Plugin tem como objetivo exportar dados em formato RDF (Resource Description Framework) a partir de uma camada de dados vetoriais (camada que representa dados geográficos como pontos, linhas ou polígonos) e possibilitar a criação de ontologias que são modelos conceituais de domínios específicos. 

A seguir na figura 1 podemos ver a interface gr**á**fica principal do plugin ******Layer2triple******

![Figura 1- Interface Inicial do Plugin Layer2triple](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5e2cde0b-74e4-41c6-899c-e4463f395bab/Untitled.png)

Figura 1- Interface Inicial do Plugin Layer2triple

Na interface gráfica do plugin **Layer2triple ,**que é ****possível ver na Figura 2, conseguimos visualizar na parte superior informações sobre o layer que foi carregado, a URL base, o tipo do RDF ,o prefixo, uma subseção de agregações de constantes, e uma área para escolhermos as opções de configurações e vocabulário. Já na segunda parte, temos a tabela de atributo, onde serão carregados os atributos necessários para a exportação. Além disso, temos uma seção para agregações de constantes que mostraremos no decorrer desse conteúdo. Nessa interface encontramos também o botão para salvar as exportações. Ao seu lado, está o botão “cancelar”, cuja finalidade é fazer o cancelamento de toda execução como também fechar a interface gráfica.

![Figura 2- Subdivisão do plugin Layer2triple](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c4bad5e7-1dbc-4997-9457-133d29b8b4f9/Untitled.png)

Figura 2- Subdivisão do plugin Layer2triple

## Instalação dos Plugins

Para utilizarmos precisamos ter o Plugin instalado. 

Para fazer a instalação dos complementos basta seguirmos os passos descritos na pagina a seguir

[Instalação dos complementos (2)](https://www.notion.so/Instala-o-dos-complementos-2-6e4865644d854bdcbb190e59e631196f?pvs=21)

# Preparação do ambiente

Para rodar os Plugins dentro do ********QGIS********  precisamos preparar o ambiente. Para isso basta seguirmos os passos descritos na pagina a seguir 

[Preparação de ambiente (2)](https://www.notion.so/Prepara-o-de-ambiente-2-3aa25837e201446b8f86bd4da0969202?pvs=21)


---

## Como utilizar 


> `💡 As capturas de tela para esta documentação foram tiradas no QGIS 3.26.3 em execução no Windows. Dependendo da sua configuração, as telas que você encontra podem parecer um pouco diferentes. No entanto, todos os mesmos botões ainda estarão disponíveis e as instruções funcionarão em qualquer sistema operacional. Você precisará do QGIS 3.4 (a versão mais recente no momento de redação) para usar este curso.`



> `💡 Antes de iniciar este exercício, o Plugin **Layer2Triple** deve estar instalado no seu computador.`


Vamos começar imediatamente!

Para utilizarmos o **Layer2Triple** basta abrir o **QGIS** na barra de menu e passar o mouse por cima do vetor através do qual será possível ver as ferramentas nos permitindo, assim, manipular camadas vetoriais. Dessa forma será possível acessar em célula QGISPARQL os plugins da **DBCells**. 

Na Figura 1 a seguir, podemos ver a **área dos plugins ativos indicada** com a seta de número 3.  Indo em vetor na barra de menu como mostrado na seta de número 1,podemos então abrir o plugin **Layer2Triple** e selecionar o plugin desejado, no caso o **Layer2Triple** mostrado na seta de número 2.

<div align="center">
  <img src="https://github.com/LambdaGeo/qgisparql-Layer2Triple/assets/108685222/bac31c85-387e-49ac-aefb-9795fa5e5b3c" alt="Figura 1: Menu de ferramentas">
  <p> Figura 1: Menu de ferramentas </p>
</div>


## Passo 1: Carregando Layer dentro do QGIS

Para utilizarmos o **Layer2Triple** primeiramente vamos carregar uma camada vetorial abrindo um projeto  dentro do **QGIS.** Para isso podemos ir em “Abrir projeto” selecionando na barra de menu como mostrado na Figura 3 a seguir ou através do atalho(Ctrl+O)

![Figura 3- Abrir projeto QGIS](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e0cc7492-f767-4f06-bf3f-a0411cc600c1/Untitled.png)

Figura 3- Abrir projeto QGIS

Podemos assim, selecionar o projeto do QGIS que tenham camadas vetoriais como mostrado na Figura 4.

QGIS reconhece camadas vetoriais e matriciais.

![Figura 4-escolha do projeto QGIS](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/26c3bb03-4f1f-495c-b00e-d15379472935/Untitled.png)

Figura 4-escolha do projeto QGIS

Ao ser carregado o projeto podemos ver a o dado gerado de maneira gráfica como mostrado na figura 5.  Nela temos a parte de camadas carregadas no painel "Camadas" do QGIS, as quais podemos selecionar para utilizarmos dentro do Plugin Layer2triple.

Com um mapa, que é formado por camadas vetoriais carregado, podemos começar a utilizar o plugin layer2triple.

![Figura 5-Camadas carregadas](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8755d002-d568-49d7-8d8d-68ad7f5b1f07/Untitled.png)

Figura 5-Camadas carregadas

Depois de selecionar a camada vetorial a ser utilizada, basta abrir na barra de menu e passando o mouse por cima de “vetor”, será possível acessar em célula QGISPARQL os plugins da **DBCells**. 

Na imagem a seguir podemos então abrir o plugin **Layer2triple** indo em vetor na barra de menu como mostrado na seta de número 1, e selecionar a o plugin que queremos, no caso o **Layer2triple** mostrado na seta de número 2 na figura 6.

![Figura 6- abrir a interface do Layer2triple ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d92df568-eac2-43f8-8bac-0395ac1632bd/Untitled.png)

Figura 6- abrir a interface do Layer2triple 

A Figura 7 é possivel ver o plugin aberto com as camadas carregadas, prontas para serem manipuladas dentro do Layer2triple.

![Figura 7- layer carregado dentro do plugin ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a4640a6a-f76b-433a-9b22-b7cb24f0d768/Untitled.png)

Figura 7- layer carregado dentro do plugin 

## Passo 2: Load vocabulary

O Plugin Layer2Triple permite carregar vocabulários personalizados para mapear os atributos da camada vetorial em triplas RDF. Para carregar um vocabulário, siga as etapas descritas no decorrer desse tutorial.

Com a camada geográfica aberta podemos então carregar o vocabulário que queremos exportar.

![Figura 8- Plugin com layer carregado](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0b0ad576-38ca-44e2-9335-b15261bd6189/Untitled.png)

Figura 8- Plugin com layer carregado

Para isso vamos abrir a caixa de dialogo indo em **Vocabulary>Load Vocabulary** onde faremos o carregamento do vocabulário desejado como mostrado na Figura 9.  Clique no botão "Carregar Vocabulário". Será exibida a janela "Carregar Vocabulário"

![Figura 9- layer carregado dentro do plugin ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d83e0e58-46d6-432d-a8bc-c7e60efe36cb/Untitled.png)

Figura 9- layer carregado dentro do plugin 

Preencha as informações do vocabulário, incluindo o formato (por exemplo, TTL) e a URL do namespace. Clique em "OK" para carregar o vocabulário.

![Figura 10-Load Vocabulary](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/97f5ebf2-cae1-4839-a32a-374e7acd0ff2/Untitled.png)

Figura 10-Load Vocabulary

Ao abrirmos essa caixa de dialogo podemos colocar as informações de prefixo, URL e formato que pode ser turtle(.ttl) ou Extensible Markup Language(.xml) como podemos ver na Figura 11.

![Figura 11- Inserindo vocabulário](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cf89d431-dc72-4f7d-9be0-a96c1305deba/Untitled.png)

Figura 11- Inserindo vocabulário

Dessa forma, os atributos serão carregados na tabela de atributos como podemos ver na Figura 12 e uma mensagem de sucesso caso todos atributos sejam carregados.

![Figura 12- Carregando vocabulário](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bc5dffd0-1410-4239-8f1a-f74d1251ada6/Untitled.png)

Figura 12- Carregando vocabulário

Assim, depois que os atributos forem carregados, apertando em “Load layer” como podemos ver na Figura 13 podemos fazer o carregamento da camada que foi aberta onde automaticamente carregará os atributos.

![Figura 13- carregamento do layer para manipulação no plugin ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1acb57fb-d04f-4bad-9605-870cf7cb03e6/Untitled.png)

Figura 13- carregamento do layer para manipulação no plugin 

Para podermos ter certeza que esse processo foi concluído com sucesso ao efetuar o carregamento iremos receber uma mensagem de sucesso como mostrado na Figura 14. 

![Figura 14- Sucesso no carregamento do layer](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7417bbfe-d06b-459d-9fe6-6ba70dac5455/Untitled.png)

Figura 14- Sucesso no carregamento do layer

Agora sim podemos partir para o Mapeamento dos atributos!! Vamos imediatamente!!

# Mapeamento dos atributos

Após configurar as opções iniciais e carregar os vocabulários, é necessário mapear os atributos da camada vetorial em triplas RDF. Na tabela "Atributos" na janela principal do Plugin Layer2Triple, você encontrará uma lista de conceitos disponíveis. Para mapear um atributo, siga as etapas abaixo:

- Selecione o conceito correspondente ao atributo na coluna "Concepts".
- Escolha o tipo de mapeamento na coluna "Type":
1. "Valor Constante": Insira um valor constante para o atributo.
2. "Atributo da Camada": Selecione um atributo da camada vetorial.
3. "Vocabulário": Selecione um conceito do vocabulário carregado.
- Preencha o valor correspondente ao mapeamento selecionado.

Para facilitar o processo, caso seja uma quantidade muito grande podemos usar a filtragem para acharmos mais rapidamente o atributo desejado como mostrado na Figura 15.

![Figura 15- mostrando uso da filtragem para seleção de conceitos](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9dfa557f-f629-482c-8915-8afe27855bc5/Untitled.png)

Figura 15- mostrando uso da filtragem para seleção de conceitos

Repita essas etapas para mapear todos os atributos desejados.

## Passo 3: Settings 🛠️

Nessa seção de configurações, podemos ver no decorrer desse tutorial, como abrir configurações ja salvas e como salvar configurações.

# Abrir configurações

- nao incluir essa parte aqui, talvez no relatório
    
    no exemplo que mostraremos temos um arquivo de configuração do tipo JSON onde contem informações necessárias para formar uma tabela de atributos. [](http://atributos.ne)Nela contem dados necessários para o software trabalhar com vocabularios RDF (Resource Description Framework)
    
    Primeiramente em sua estrutura teremos a chave, “TRIPLEPREFIX”, por exemplo que pode conter o valor “obs”, como mostrado no código a seguir. Isso indica que “obs” é um prefixo utilizado para identificar termos de vocabulários relacionado a observações. podemos tambem ter uma chave que contenha URLS para identificar termos especificos. já o valor “qb:Observation” , onde “qb” identifica vocabularios relacionados ao Datacube vocabulary, e observation é uma observação especifica dentro desse vocabulario.
    
    ```markup
    {"TRIPLEPREFIX": "obs", "TRIPLEURL": "https://purl.org/dbcells/observation#", "TRIPLETYPE": "qb:Observation"
    ```
    

Antes de fazermos as conversões da camada vetorial em triplas RDF, faz-se 

Aqui nessa seção podemos abrir configurações iniciais que já temos salvas em nosso computador  como mostrado na Figura 16. Para essa tarefa basta clicar em “**Settings**”, como mostrado na seta de numero 1, e depois em “**Open**”  para carregarmos tais configurações para tabela de atributos.                  

     

![Figura 16-abrir configurações](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/47496012-bf34-4075-a4d5-bd4c153d7a98/Untitled.png)

Figura 16-abrir configurações

Inicialmente podemos fazer o carregamento do layer, que contém os vocabulários (Arquivo JSON) como mostrado na seta de numero 1 na Figura 17.

![Figura 17- arquivo de configurações para tabela de atributos](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/91ea596a-a483-4860-b880-a1e2ed09d738/Untitled.png)

Figura 17- arquivo de configurações para tabela de atributos

o arquivo JSON “configura”, contém salvo todos os vocabulários necessários para gerar os dados

Antes de converter a camada vetorial em triplas RDF, é necessário configurar algumas opções iniciais. Na janela principal do Plugin Layer2Triple, você encontrará as seguintes configurações:
URL Base: Insira a URL base para a geração das URIs das triplas RDF.
Prefixo: Insira o prefixo a ser utilizado nas URIs das triplas RDF.
Tipo RDF: Selecione o tipo RDF para as observações (por exemplo, qb:Observation).

![Figura 18-configurações optativas](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/de922272-bdc9-4989-8868-e3f781430325/Untitled.png)

Figura 18-configurações optativas

# Salvando configurações

E caso você queira salvar uma configurações vocabulários para geração de dados em sua máquina basta usar a funcionalidade de salvar configurações do plugin disponivel dentro de “**Settings**”, como mostrado na seta de numero 1 como mostrado na Figura 19, e depois em “********Save********”  para escolher uma pasta em que deseja salvar tais configurações.   

![Figura 19- Salvar configurações](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2562fc39-63b3-4e62-9448-2162d2f6f3d6/Untitled.png)

Figura 19- Salvar configurações

## Passo 4: Fazendo exportação de dados

# Exportando…

Neste tutorial para a exportação das observações, e inserção dos dados da base de dados, foi utilizado o Plugin, do QGIS, Layer2Triple, que permite a criação de arquivos RDF no formato Turtle (.ttl).

Com o uso da linguagem de triplas RDF, é feita a conversão de camadas vetoriais nessa mesma linguagem, na qual é transformada  para o formato Terse Triple Language.

Nesse plugin, é possível exportar dados RDF, a partir de camadas vetoriais que representam os dados geográficos, em vários formatos, pontos, linhas ou mesmo polígonos, e, com isso, criar uma ontologia de um domínio específico.

## Definição dos atributos

Após o carregamento dos vocabulários, é feita a modelagem das informações. Inicialmente é selecionado o tipo observação (RDF type), e estabelecido o prefixo “obs”, seguida da url base. 

Para seleção de conceitos selecionaremos uma medida estatística de media de pastagem. Então “dbc:measure:mean” representa a medida do tipo média e selecionaremos “Layer attribute” pois o valor “mean_past”, que é a media de pastagem, é um valor que advém do atributo.

Pronto, com isso conseguimos selecionar uma informação a ser exportada como mostrado na Figura 20.

![Figura 20- Selecionando dados estatísticos de média de pastagem](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/791043e2-8017-45db-ba02-90982a0a66b1/Screenshot_117.png)

Figura 20- Selecionando dados estatísticos de média de pastagem

Para fazer a agregação de constantes, precisa-se de um link, selecionando “qb:DataSet” em predicate, e essas informações irão ficar interligadas na classe “qb:DataSet”, selecionada no RDF Type, com um prefixo, e uma URL semelhante a URL base anterior.

![Figura 12- agregações de constantes](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2179f56c-222b-4e16-a930-8a97b21206eb/Screenshot_119.png)

Figura 12- agregações de constantes

Em seguida, é selecionado atributo de valor constante referente ao período, sdmx-dimension:refPeriod, e a área

![Figura 13-selecionando período e área ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/90d98121-34c2-4877-9342-449c2d20665b/Screenshot_120.png)

Figura 13-selecionando período e área 

Após isso, é selecionado o vocabulário relacionado a medida em questão, que especifica o tipo de característica (feature) do conjunto de dados, no caso, dbc-code:landcover-pastp. Em seguida, também seleciona-se o atributo relacionado ao script .lua relacionado a esse conjunto de dados, dbc-attribute:scriptFile, e o atributo que especifica o local onde o arquivo de origem do conjunto de dados está localizado, dbc-attribute:sourceFile, que nesse caso refere-se a um arquivo TIF:

![Figura 14- adição das URLs ](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/64766ac7-b1d5-48e7-9b7e-2ecac4df849b/Screenshot_121.png)

Figura 14- adição das URLs 

Vale ressaltar que ambos os atributos File, encontram-se no repositório referente a base de dados, LambdaGeo/brlucc-database.

Com isso, é possível gerar um arquivo TTL, que representa o conjunto de observações, referente a média de pastagem

Na primeira parte, são estabelecidos os prefixos referentes as URL bases.

```jsx
@prefix dbc-attribute: <http://purl.org/linked-data/dbcells/attribute#> .
@prefix dbc-code: <http://purl.org/linked-data/dbcells/code#> .
@prefix dbc-measure: <http://purl.org/linked-data/dbcells/measure#> .
@prefix ds: <https://purl.org/dbcells/dataset#> .
@prefix obs: <https://purl.org/dbcells/observation#> .
@prefix qb: <http://purl.org/linked-data/cube#> .
@prefix sdmx-dimension: <http://purl.org/linked-data/sdmx/2009/dimension#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
```

Em seguida, são definidas as observações, e seu respectivo tipo qb:dDataSet. Pode-se observar que cada observação tem uma medida de média estabelecida anteriormente (dbc-measure:mean) igual a um número representado em notação científica para zero.

```jsx
obs:00000703-6e8b-4840-8c77-ec83f8d8ba41 a qb:Observation ;
    qb:DataSet ds:f77ce462-8b99-48b8-b628-cc9d6d6c6c5a ;
    dbc-measure:mean 0e+00 ;
    sdmx-dimension:refArea <https://purl.org/dbcells/epsg4326#R0_0830Cx-59_3750Cy-1_7214> .

obs:0000f377-0ab2-4f46-9fa7-dfe744be3a05 a qb:Observation ;
    qb:DataSet ds:f77ce462-8b99-48b8-b628-cc9d6d6c6c5a ;
    dbc-measure:mean 0e+00 ;
    sdmx-dimension:refArea <https://purl.org/dbcells/epsg4326#R0_0830Cx-59_3750Cy-3_2214> .

obs:0001c2d9-7278-45cf-a738-42effbb9e203 a qb:Observation ;
    qb:DataSet ds:f77ce462-8b99-48b8-b628-cc9d6d6c6c5a ;
    dbc-measure:mean 4.45e-01 ;
    sdmx-dimension:refArea <https://purl.org/dbcells/epsg4326#R0_0830Cx-41_7917Cy-14_3047> .

obs:00021978-8eee-4e49-9631-759e8deb338b a qb:Observation ;
    qb:DataSet ds:f77ce462-8b99-48b8-b628-cc9d6d6c6c5a ;
    dbc-measure:mean 3.75e-01 ;
    sdmx-dimension:refArea <https://purl.org/dbcells/epsg4326#R0_0830Cx-63_7083Cy-11_8881> .

obs:0002230f-25dd-4a30-b549-f890ab25b50e a qb:Observation ;
    qb:DataSet ds:f77ce462-8b99-48b8-b628-cc9d6d6c6c5a ;
    dbc-measure:mean 3.21875e-01 ;
    sdmx-dimension:refArea <https://purl.org/dbcells/epsg4326#R0_0830Cx-54_7917Cy-21_0547> .

obs:00024793-eafb-476f-b8a5-43359a5ef6e6 a qb:Observation ;
    qb:DataSet ds:f77ce462-8b99-48b8-b628-cc9d6d6c6c5a ;
    dbc-measure:mean 3.496875e-01 ;
    sdmx-dimension:refArea <https://purl.org/dbcells/epsg4326#R0_0830Cx-45_5417Cy-2_0547> .

obs:00032806-502c-4edc-a7a2-9939272d3963 a qb:Observation ;
    qb:DataSet ds:f77ce462-8b99-48b8-b628-cc9d6d6c6c5a ;
    dbc-measure:mean 0e+00 ;
    sdmx-dimension:refArea <https://purl.org/dbcells/epsg4326#R0_0830Cx-62_5417Cy1_6119> .

obs:000486e3-e6fa-40c0-814a-10aa86285c73 a qb:Observation ;
    qb:DataSet ds:f77ce462-8b99-48b8-b628-cc9d6d6c6c5a ;
    dbc-measure:mean 2.921875e-01 ;
    sdmx-dimension:refArea <https://purl.org/dbcells/epsg4326#R0_0830Cx-40_6250Cy-14_6381> .

obs:00049eea-1fa0-4397-b26c-e2a6fa7ad821 a qb:Observation ;
    qb:DataSet ds:f77ce462-8b99-48b8-b628-cc9d6d6c6c5a ;
    dbc-measure:mean 0e+00 ;
    sdmx-dimension:refArea <https://purl.org/dbcells/epsg4326#R0_0830Cx-55_2083Cy-13_8881> .

obs:0006d257-64a0-4586-8b96-332fc690304a a qb:Observation ;
    qb:DataSet ds:f77ce462-8b99-48b8-b628-cc9d6d6c6c5a ;
    dbc-measure:mean 0e+00 ;
    sdmx-dimension:refArea <https://purl.org/dbcells/epsg4326#R0_0830Cx-39_7083Cy-9_5547> .

obs:0006fa38-edc2-4397-9078-9f84c040f9eb a qb:Observation ;
    qb:DataSet ds:f77ce462-8b99-48b8-b628-cc9d6d6c6c5a ;
    dbc-measure:mean 0e+00 ;
    sdmx-dimension:refArea <https://purl.org/dbcells/epsg4326#R0_0830Cx-56_3750Cy-12_8881> .

obs:000760e4-0746-4656-ae4e-31fe68401abd a qb:Observation ;
    qb:DataSet ds:f77ce462-8b99-48b8-b628-cc9d6d6c6c5a ;
    dbc-measure:mean 0e+00 ;
    sdmx-dimension:refArea <https://purl.org/dbcells/epsg4326#R0_0830Cx-61_4583Cy0_1953> .

obs:0007b4d7-7032-4473-8d78-5a9b744aac0a a qb:Observation ;
    qb:DataSet ds:f77ce462-8b99-48b8-b628-cc9d6d6c6c5a ;
    dbc-measure:mean 0e+00 ;
    sdmx-dimension:refArea <https://purl.org/dbcells/epsg4326#R0_0830Cx-56_2917Cy-10_8881> .

obs:0007df07-3d18-4c42-a529-bd7e56e78e39 a qb:Observation ;
    qb:DataSet ds:f77ce462-8b99-48b8-b628-cc9d6d6c6c5a ;
    dbc-measure:mean 0e+00 ;
    sdmx-dimension:refArea <https://purl.org/dbcells/epsg4326#R0_0830Cx-43_0417Cy-2_5547> .

obs:0007fe19-f22b-425c-8567-26462d8aa042 a qb:Observation ;
    qb:DataSet ds:f77ce462-8b99-48b8-b628-cc9d6d6c6c5a ;
    dbc-measure:mean 2.51875e-01 ;
    sdmx-dimension:refArea <https://purl.org/dbcells/epsg4326#R0_0830Cx-49_2083Cy-22_0547> .
```

A última parte do código fornece informações adicionais sobre o conjunto de dados, como os atributos associados, os links para os arquivos de script e de origem, e o período de referência.

```jsx
ds:f77ce462-8b99-48b8-b628-cc9d6d6c6c5a a qb:dataSet ;
    dbc-attribute:feature dbc-code:landcover-pastp ;
    dbc-attribute:scriptFile "<https://github.com/LambdaGeo/brlucc-database/blob/main/scripts/2010/pastp_2010.lua>" ;
    dbc-attribute:sourceFile "<https://github.com/LambdaGeo/brlucc-database/blob/main/data/tif/2010/brasil2010pastp1.tif>" ;
    sdmx-dimension:refPeriod 2010 .
```

# QGISSPARQL:Layer2Triple

# Overview

**Repository**: https://github.com/LambdaGeo/qgisparql-Layer2Triple/

**Creators**: [Sérgio Souza Costa](https://github.com/profsergiocosta) and [Nerval Junior](https://github.com/nervaljunior)

### This plugin aims to export data from a layer of geographic information in the QGIS geographic information system (https://qgis.org/).

<table align="right">
  <tr>
    <td height="43px">
      <b>
        <a href="README-pt.md">Português 🇧🇷</a>
      </b>
    </td>
  </tr>
  <tr>
    <td height="43px">
      <a href="README.md">English 🇺🇸</a>
    </td>
  </tr>
</table>

# Layer2Triple
## An application for exporting geographic data

![](https://img.shields.io/badge/Language-Python-blue) 
![](https://img.shields.io/badge/Compiler-QGIS-brightgreen) 
![](https://img.shields.io/badge/IDE-Microsoft%20Visual%20Studio%202022-blue) 
![](https://img.shields.io/badge/Environment-Windows-red) 
![](https://img.shields.io/badge/Environment-Linux-purple) 
![](https://img.shields.io/badge/User%20Interface-GUI%20%2B%20CLI-yellowgreen)

---

The Layer2triple Plugin is an extension for QGIS that allows the creation of RDF (Resource Description Framework) files in Turtle (.ttl) format. This involves converting vector layers into an RDF triple language in the Terse Triple Language format. It opens a dialog window with a table where the user can select attributes from a vector layer and define the corresponding RDF value. This way, the user can choose which attributes to include in the RDF file. The user can save the file and provide a URL for the RDF resources.

The Plugin aims to export data in RDF (Resource Description Framework) format from a vector data layer (a layer that represents geographic data such as points, lines, or polygons) and enable the creation of ontologies, which are conceptual models of specific domains.

In Figure 1 below, you can see the main graphical interface of the **Layer2triple** plugin:

![Figura 1- Interface Inicial do Plugin Layer2triple](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/231f97b8-c03f-410c-a078-d673b40e3394)

**Figure 1 - Initial Interface of Layer2triple Plugin**

In the graphical interface of the **Layer2triple** plugin, as shown in Figure 2, you can find information about the loaded layer at the top, including the base URL, RDF type, prefix, a subsection of constant aggregations, and an area to choose configuration options and vocabulary. In the second part, there is an attribute table where the necessary attributes for export will be loaded. Additionally, there is a section for constant aggregations, which will be explained later in this content. In this interface, you will also find the button to save exports. Next to it is the "Cancel" button, which is used to cancel the entire execution and close the graphical interface.

![Figura 2- Subdivisão do plugin Layer2triple](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/b4a9d031-fbf3-4581-8389-af8594b1f36a)

**Figure 2 - Subdivision of Layer2triple Plugin**

## Plugin Installation

To use this tool, it needs to be installed.

To install the plugin, follow the steps described on the following page: 
[Instalação dos complementos](https://github.com/LambdaGeo/qgisparql-layer2triple/blob/documentation/instalando%20complementos.md)

# Environment Setup

To run the plugins within **QGIS**, it is necessary to prepare the environment. Follow the steps described on the following page: 
[Preparação de ambiente](https://github.com/LambdaGeo/qgisparql-layer2triple/blob/documentation/preparando%20o%20ambiente.md)


---

## How to Use

> `💡 Screenshots for this documentation were taken in QGIS 3.26.3 running on Windows. Depending on your setup, the screens you encounter may look slightly different. However, all the same buttons will still be available, and the instructions will work on any operating system. You will need QGIS 3.4 (the latest version at the time of writing) to use this tutorial.`

> `💡 Before starting this exercise, the **Layer2Triple** plugin must be installed on your computer.`


Let's get started right away!

To use **Layer2Triple**, simply open **QGIS** from the menu bar and hover over the vector through which you can see the tools, allowing you to manipulate vector layers. This way, you can access the **DBCells** plugins in the QGISPARQL cell.

## Step 1: Loading a Layer in QGIS

To use **Layer2Triple**, first, let's load a vector layer by opening a project within **QGIS**. You can do this by going to "Open Project," selecting it from the menu bar as shown in Figure 3 below, or using the shortcut (Ctrl+O).

![Figura 3- Abrir projeto QGIS](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/4102803a-d485-472e-8f45-b8663b9a26e5)

**Figure 3 - Open QGIS Project**

You can then select the QGIS project that contains vector layers, as shown in Figure 4.

QGIS recognizes both vector and raster layers.

![Figura 4-escolha do projeto QGIS](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/dea0caa8-5f61-4c72-bc8e-046dc662e656)

**Figure 4 - Choose QGIS Project**

Once the project is loaded, you can see the data generated graphically, as shown in Figure 5. In this figure, we have the layers loaded in the "Layers" panel of QGIS, which we can select for use within the Layer2triple Plugin.

With a map, formed by loaded vector layers, we can begin to use the Layer2triple plugin.

![Figura 5-Camadas carregadas](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/6f79d9e2-fc57-4422-8e80-66013f6b2a92)

**Figure 5 - Loaded Layers**

After selecting the vector layer to be used, simply open the plugin **Layer2Triple** from the menu bar by hovering over "Vector". This will allow you to access the **DBCells** plugins in the QGISPARQL cell.

In the image below, you can open the **Layer2Triple** plugin by going to "Vector" in the menu bar, as shown by arrow number 1, and selecting the desired plugin, in this case, **Layer2Triple** indicated by arrow number 2 in Figure 6.

![Figura 6- abrir a interface do Layer2triple ](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/bf18733d-30b3-4346-b3ba-965eca7e74a0)

**Figure 6 - Open the Layer2Triple Interface**

In Figure 7, you can see the plugin opened with the loaded layers, ready to be manipulated within Layer2Triple.
![Figura 7- layer carregado dentro do plugin](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/ff931177-2d89-429b-9365-b72d6fc80cc1)

**Figure 7 - Loaded Layer within the Plugin**

## Step 2: Load Vocabulary

The Layer2Triple Plugin allows you to load custom vocabularies to map vector layer attributes into RDF triples. To load a vocabulary, follow the steps described in this tutorial.

With the geographic layer open, you can then load the vocabulary you want to export.

![Figura 8- Plugin com layer carregado](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/113d157c-dd37-4dca-bc8e-d330b3127ac4)

**Figure 8 - Plugin with Loaded Layer**

To do this, open the dialog box by going to **Vocabulary > Load Vocabulary**, where you will load the desired vocabulary as shown in Figure 9. Click the "Load Vocabulary" button. The "Load Vocabulary" window will be displayed.

![Figura 9- layer carregado dentro do plugin](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/0a26549a-5af6-4179-989b-32b93d2fc208)

**Figure 9 - Loaded Layer within the Plugin**

Fill in the vocabulary information, including the format (e.g., TTL) and the URL of the namespace. Click "OK" to load the vocabulary.

![Figura 10-Load Vocabulary](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/89073102-2424-4dc3-8c08-54c22066214b)

**Figure 10 - Load Vocabulary**

When you open this dialog box, you can enter the prefix, URL, and format information. The format can be Turtle (.ttl) or Extensible Markup Language (.xml), as shown in Figure 11.

![Figura 11- Inserindo vocabulário](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/3eaec409-27bb-49b9-96f9-98924fc1179c)

**Figure 11 - Inserting Vocabulary**

This way, the attributes will be loaded into the attribute table, as shown in Figure 12, along with a success message if all attributes are loaded successfully.

![Figura 12- Carregando vocabulário](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/ea79834f-8f15-40a3-b9f5-1d819a00fa84)

**Figure 12 - Loading Vocabulary**

After the attributes are loaded, by clicking on "Load Layer" as shown in Figure 13, you can load the opened layer, which will automatically load the attributes.

![Figura 13- carregamento do layer para manipulação no plugin](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/534a4433-37f5-4ea3-9d26-67a0b0118cf0)

**Figure 13 - Loading Layer for Manipulation in the Plugin**

To ensure that this process was completed successfully, upon loading, you will receive a success message as shown in Figure 14.

![Figura 14- Sucesso no carregamento do layer](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/cafceccd-f5c6-4dd7-b7f1-529ce86e56ae)

**Figure 14 - Successful Layer Loading**

Now we can move on to Attribute Mapping! Let's get started right away!!

# Attribute Mapping

After configuring the initial options and loading vocabularies, it is necessary to map the attributes of the vector layer into RDF triples. In the "Attributes" table in the main Layer2Triple Plugin window, you will find a list of available concepts. To map an attribute, follow the steps below:

- Select the corresponding concept for the attribute in the "Concepts" column.
- Choose the mapping type in the "Type" column:
  1. "Constant Value": Enter a constant value for the attribute.
  2. "Layer Attribute": Select an attribute from the vector layer.
  3. "Vocabulary": Select a concept from the loaded vocabulary.
- Fill in the value corresponding to the selected mapping.

To facilitate the process, in case there is a large number of attributes, you can use filtering to quickly find the desired attribute, as shown in Figure 15.

![Figura 15- mostrando uso da filtragem para seleção de conceitos](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/d862772a-1d1b-401f-8cf8-a08bc3e594de)

**Figure 15 - Demonstrating the Use of Filtering for Concept Selection**

Repeat these steps to map all the desired attributes.

## Step 3: Settings 🛠️

In this settings section, you will learn in the course of this tutorial how to open saved configurations and how to save configurations.

# Open Configurations

Before we proceed with converting the vector layer into RDF triples, there is a step to be done.

In this section, you can open previously saved configurations on your computer, as shown in Figure 16. To do this, click on "**Settings**," as indicated by arrow number 1, and then on "**Open**" to load these configurations into the attribute table.

![Figura 16-abrir configurações](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/754251a8-6a67-4053-a1fa-d3d192377de4)

**Figure 16 - Open Configurations**

Initially, you can load the layer, which contains the vocabularies (JSON file), as shown in arrow number 1 in Figure 17.

![Figura 17- arquivo de configurações para tabela de atributos](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/5621f36d-434c-4469-bc50-401e8512e15c)

**Figure 17 - Configuration File for Attribute Table**

The JSON file "configura" contains all the saved vocabularies necessary to generate the data.

Before converting the vector layer into RDF triples, it is necessary to configure some initial options. In the main Layer2Triple Plugin window, you will find the following settings:
- Base URL: Enter the base URL for generating RDF triple URIs.
- Prefix: Enter the prefix to be used in RDF triple URIs.
- RDF Type: Select the RDF type for observations (e.g., qb:Observation).
  
![Figura 18-configurações optativas](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/e57cbedb-7459-4e1b-aba5-d5cb59dc3a91)

**Figure 18 - Optional Settings**

# Saving Configurations

If you want to save configurations and vocabularies for data generation on your machine, use the plugin's save configurations functionality available under "**Settings**," as shown by arrow number 1 in Figure 19, and then click on "**Save**" to choose a folder to save these configurations.

![Figura 19- Salvar configurações](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/359c9941-651f-4009-b90c-95a44c0f8e5c)

**Figure 19 - Save Configurations**

## Step 4: Data Export

# Exporting...

In this tutorial for exporting observations and inserting data from the database, the Layer2Triple Plugin from QGIS was used. This plugin allows the creation of RDF files in Turtle (.ttl) format.

Using the RDF triple language, vector layers are converted into this language and then transformed into the Terse Triple Language format.

In this plugin, you can export RDF data from vector layers that represent geographic data, in various formats, such as points, lines, or polygons, and thus create an ontology for a specific domain.

## Definition of Attributes

After loading the vocabularies, the information is modeled. Initially, the observation type (RDF type) is selected, and the prefix "obs" is established, followed by the base URL.

For the selection of concepts, we will choose a statistical measure of pasture mean. So, "dbc:measure:mean" represents the measure of the mean type, and we will select "Layer attribute" because the value "mean_past," which is the mean pasture, is a value that comes from the attribute.

There you go! With this, we can select information to be exported, as shown in Figure 20.

![Figura 20- Selecionando dados estatísticos de média de pastagem](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/484c69bc-3a6e-4f97-bf01-8afb2eb180c2)

**Figure 20 - Selecting Statistical Data for Pasture Mean**

To perform the constant aggregation, a link is needed. Select "qb:DataSet" in the predicate, and this information will be interconnected in the "qb:DataSet" class, selected in the RDF Type, with a prefix and a URL similar to the previous base URL.

![Figura 21- agregações de constantes](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/4ec09b68-c9da-49ae-b785-7c923952099a)

**Figure 21 - Constant Aggregations**

Next, the attribute of constant value related to the period, sdmx-dimension:refPeriod, and the area is selected.

![Figura 22-selecionando período e área](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/130fc3e8-e9bf-417e-9b33-995fecadd39e)

**Figure 22 - Selecting Period and Area**

After that, the vocabulary related to the measure in question is selected, specifying the type of feature of the dataset, in this case, dbc-code:landcover-pastp. Then, the attribute related to the .lua script associated with this dataset, dbc-attribute:scriptFile, and the attribute specifying the location where the dataset source file is located, dbc-attribute:sourceFile, are also selected. In this case, it refers to a TIF file.

![Figura 23- adição das URLs](https://github.com/LambdaGeo/qgisparql-layer2triple/assets/108685222/a667ed9d-8374-4f71-91dc-61a647d50201)

**Figure 23 - Adding URLs**

It is worth noting that both File attributes are located in the repository related to the database, LambdaGeo/brlucc-database.

With this, it is possible to generate a TTL file representing the set of observations related to pasture mean.

In the first part, prefixes related to the base URLs are established.

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

Next, the observations and their respective type qb:DataSet are defined. It can be observed that each observation has a mean measure established earlier (dbc-measure:mean), equal to a number represented in scientific notation for zero.

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
The last part of the code provides additional information about the dataset, such as associated attributes, links to script and source files, and the reference period.

```jsx
ds:f77ce462-8b99-48b8-b628-cc9d6d6c6c5a a qb:dataSet ;
    dbc-attribute:feature dbc-code:landcover-pastp ;
    dbc-attribute:scriptFile "<https://github.com/LambdaGeo/brlucc-database/blob/main/scripts/2010/pastp_2010.lua>" ;
    dbc-attribute:sourceFile "<https://github.com/LambdaGeo/brlucc-database/blob/main/data/tif/2010/brasil2010pastp1.tif>" ;
    sdmx-dimension:refPeriod 2010 .
```

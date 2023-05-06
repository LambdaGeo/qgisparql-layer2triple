# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Layer2Triple
                                 A QGIS plugin
 Layer2Triple
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-04-03
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Sergio Costa
        email                : sergio.costa@ufma.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from PyQt5.QtCore import Qt
from qgis.PyQt.QtWidgets import QAction, QTableWidgetItem, QTableWidget, QCheckBox, QComboBox, QLineEdit, QFileDialog,QProgressDialog
import time
from qgis.core import QgsProject, Qgis, QgsVectorLayer, QgsRasterLayer,   QgsMultiPolygon

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .Layer2Triple_main import Layer2TripleMain
from .VocabularyDialog import VocabularyDialog
import os.path


import uuid 

from functools import partial

import re

from rdflib import Namespace, Literal, URIRef,RDF, Graph

from rdflib.namespace import DC, FOAF


import json


 
settings = {

    "TRIPLEPREFIX" : "obs",
    "TRIPLEURL" : "https://purl.org/dbcells/observation#",
    "TRIPLETYPE" : "qb:Observation",

    "NAMESPACES" : {
        #'dbc': (Namespace("http://www.purl.org/linked-data/dbcells#"), 'ttl'),
        #'geo' : (Namespace ("http://www.opengis.net/ont/geosparql"), 'xml'),
        #'sdmx' : (Namespace ("http://purl.org/linked-data/sdmx/2009/dimension#"), 'ttl'),
        #'dbc-attribute' : (Namespace ("http://www.purl.org/linked-data/dbcells/attribute#"), "ttl"),
        #'dbc-measure' : (Namespace ("http://www.purl.org/linked-data/dbcells/measure#"), "ttl"),
        #'dbc-code' : (Namespace ("http://www.purl.org/linked-data/dbcells/code#"), "ttl"),
        #'qb' : (Namespace ("http://purl.org/linked-data/cube#"), "ttl")
    }
 }

# depois vou remover essa variavel, evitar isso
namespaces = settings["NAMESPACES"]

def validade_url(s):
    if (type(s) != str ):
        return False

    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return (re.match(regex, s) is not None) 


def parse_ifs(value):
  if value is None:
      return ""
  try:
      n = int(value)
      return n
  except:
      try: 
        n = float (value)
        return n
      except:
        return value


class Layer2Triple:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'Layer2Triple_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&QGISSPARQL')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

        self.concepts = []
        self.fields_name = []

        self.load_vocabularies()

        #self.vocab_dialog = 

    def load_vocabularies(self):
        for key, value in namespaces.items():
            self.load_vocabulary(key, str(value[0]), value[1])

    def load_vocabulary(self, prefix, namespace, format):
        g = Graph()
        g.parse(namespace, format=format)
        q = """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX owl: <http://www.w3.org/2002/07/owl#>

            SELECT ?p
            WHERE 
            {
                { ?p rdf:type owl:Class} UNION
               { ?p rdf:type owl:DatatypeProperty} UNION
               { ?p rdf:type owl:ObjectProperty} UNION
               { ?p rdf:type rdf:Property}    
            }
        """

        # Apply the query to the graph and iterate through results
        
        i = len(self.concepts) # o inicial para adicionar no table attributues

        for r in g.query(q):
            attr = r["p"].split("#") 
            name = prefix+":"+attr[1]
            self.concepts.append(name)
        
        if prefix not in namespaces:
            namespaces[prefix] = (Namespace(namespace), format)


    def fill_table (self, start):

                
        for c in self.concepts:
            self.dlg.comboRDFType.addItem(c)
            self.dlg.comboRDFType_2.addItem(c)
            self.dlg.comboBoxPredicate.addItem(c)

        self.dlg.tableAttributes.setRowCount(len(self.concepts))
        self.dlg.tableAttributes.setColumnCount(3)
        self.dlg.tableAttributes.setHorizontalHeaderLabels(["Concept", "Type", "Value"])


        for c in self.concepts[start:]:
            self.dlg.tableAttributes.setCellWidget(start, 0, QCheckBox( c))
            comboBox = QComboBox()
            comboBox.textActivated.connect(partial(self.combo_changed, start))
            comboBox.addItem("Constant Value")
            comboBox.addItem("Layer Attribute")
            comboBox.addItem("Vocabulary")
            self.dlg.tableAttributes.setCellWidget(start, 1, comboBox)
            self.dlg.tableAttributes.setCellWidget(start, 2, QLineEdit())
            #self.dlg.tableAttributes.setCellWidget(start, 1, self.attributes_combo())
            start += 1

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('Layer2Triple', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToVectorMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/Layer2Triple/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Layer2Triple'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginVectorMenu(
                self.tr(u'&QGISSPARQL'),
                action)
            self.iface.removeToolBarIcon(action)


    def update_vocabularies(self):        
        self.fill_table(0)
        if ("TRIPLEPREFIX" in settings):
            self.dlg.lineURLBase.setText(settings["TRIPLEURL"])
            self.dlg.linePrefix2.setText(settings["TRIPLEPREFIX"])
            self.dlg.comboRDFType.setCurrentText(settings["TRIPLETYPE"])


    def show_group (self):
        if self.dlg.groupBoxConstants.isVisible():
            self.dlg.groupBoxConstants.setVisible(False)
        else:
            self.dlg.groupBoxConstants.setVisible(True)
        

    def comboID_clicked (self):
        if self.dlg.comboID.currentText() == "Layer Attribute":
            self.dlg.comboAttributeID.setEnabled(True)
        else:
            self.dlg.comboAttributeID.setEnabled(False)

    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = Layer2TripleMain()

            self.vocab_dlg = VocabularyDialog()

            #self.dlg.buttonLoad.clicked.connect(handle_dialog_vocabulary)

            self.vocab_dlg.buttonBox.accepted.connect(self.handle_dialog_vocabulary)
            self.dlg.buttonBox.accepted.connect(self.save_file)
            self.dlg.buttonBox.rejected.connect(self.close)
            self.dlg.button_load_layer.clicked.connect(self.load_fields)
            self.dlg.actionSave.triggered.connect(self.save_setting)
            self.dlg.actionOpen.triggered.connect(self.open_setting)
            self.dlg.actionLoad_Vocabulary.triggered.connect(self.show_dialog_vocabulary)

            self.dlg.pushShowGroup.clicked.connect(self.show_group)

            self.dlg.groupBoxConstants.setStyleSheet("QGroupBox { border: 0px; }")

            self.update_vocabularies()

            self.dlg.comboID.textActivated.connect(self.comboID_clicked)

        self.dlg.groupBoxConstants.setVisible(False)

        self.update_comboLayer()

        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        #result = self.dlg.exec_()
        # See if OK was pressed
        #if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
        #    pass

    def show_dialog_vocabulary(self):
        self.vocab_dlg.show()

    def handle_dialog_vocabulary(self):
        format = self.vocab_dlg.comboFormat.currentText()
        namespace = self.vocab_dlg.lineURL.text()
        prefix = self.vocab_dlg.linePrefix.text()
        start = len (self.concepts)
        print (prefix, namespace, format)
        self.load_vocabulary(prefix, namespace, format)
        self.fill_table(start)

    def load_fields(self):
        
        try:
            self.layer = QgsProject.instance().mapLayersByName(self.dlg.comboLayer.currentText())[0]
            self.fields_name = []        

            fields = self.layer.fields()
            for field in fields:
                self.fields_name.append(field.name())

            self.fill_table(0)

            for attr in self.fields_name:
                self.dlg.comboAttributeID.addItem(attr)

            self.iface.messageBar().pushMessage(
                "Success", "Load Layer fields",
                level=Qgis.Success, duration=3
            )
        except:
            
            self.iface.messageBar().pushMessage(
            "Error", "No layer loading",
            level=Qgis.Info, duration=3)

    def update_comboLayer(self):

        self.dlg.comboLayer.clear()

        for layer in QgsProject.instance().mapLayers().values():
            if type(layer) == QgsVectorLayer:
                self.dlg.comboLayer.addItem(layer.name())
                

    def combo_changed(self,row, s):
        if (s == "Layer Attribute"):
            self.dlg.tableAttributes.setCellWidget(row, 2, self.attributes_combo())
        elif (s == "Vocabulary"):
            self.dlg.tableAttributes.setCellWidget(row, 2, self.vocabularies_combo())
        else:
            self.dlg.tableAttributes.setCellWidget(row, 2, QLineEdit())


    def attributes_combo(self):
        comboBox = QComboBox()
        for attr in self.fields_name:
            comboBox.addItem(attr)
        return comboBox

    def vocabularies_combo(self):
        comboBox = QComboBox()
        for c in self.concepts:
            comboBox.addItem(c)
        return comboBox

    def toURL (self, str):
        rdf_attr = str
        rdf = rdf_attr.split(":")
        rdf_attr = rdf[1]
        #print (rdf)
        #print (namespaces)
        namespace = namespaces[rdf[0]][0]
        #print (namespace, rdf_attr)
        return namespace[rdf_attr]


    def save_setting(self):
        try:
            path =str(QFileDialog.getSaveFileName(caption="Defining output file", filter="JSON settings file(*.json)")[0])
            with open(path, "w") as file:
                # Grava o dicionário settings no arquivo JSON
                
                json.dump(settings, file)
                self.iface.messageBar().pushMessage(
                        "Success","saved configuration",
                        level=Qgis.Success, duration=3
                    )
        except:
            pass
            
                

    def open_setting(self):
            global namespaces
            global settings
            try:
                path =str(QFileDialog.getOpenFileName(caption="Defining input file", filter="JSON settings file(*.json)")[0])
                if path:
                    self.dlg.setVisible(False) 
                
                    with open(path, "r") as file:
                        
                        content = file.read()
                        settings = json.loads(content)
                        # Grava o dicionário settings no arquivo JSON
                        #self.iface.mainWindow().showMaximized() 
                        progress = QProgressDialog("loading settings...", "Cancel", 0, 100, self.iface.mainWindow())
                        progress.setWindowModality(Qt.WindowModal)
                        progress.setMinimumDuration(0)
                        progress.setAutoClose(True)
                        progress.setAutoReset(False)
                        progress.show()
                        
                        for i in range(0, 101, 25):
                            progress.setValue(i)

                            if i == 0:
                                progress.setLabelText("Carregando configurações...")
                            elif i == 25:
                                progress.setLabelText("Configurações carregadas, carregando vocabulários...")
                            elif i == 50:
                                progress.setLabelText("Vocabulários carregados, atualizando vocabulários...")
                            elif i == 75:
                                progress.setLabelText("Vocabulários atualizados, finalizando...")
                            
                            # eliminar essa gambiarra, considerando que na configuracao so tera a URL
                            settings["NAMESPACES"] = {k: (lambda x: (Namespace(x[0]), x[1]  ))(v) for k, v in  settings["NAMESPACES"].items() } #incluir o namespace
                            namespaces = settings["NAMESPACES"]
                            self.load_vocabularies()
                            self.update_vocabularies()

                        progress.setValue(100)
                        progress.setLabelText("Carregamento concluído!")
                            
                        progress.close()
                            
                        self.iface.messageBar().pushMessage(
                            "Success",
                        "configuration uploaded successfully...",
                            level=Qgis.Success, duration=3
                        )
                    self.dlg.setVisible(True) 
            except:
                self.iface.messageBar().pushMessage(
                            "Error",
                        "configuration not uploaded...",
                            level=Qgis.Warning, duration=3
                        )
                progress.close()
                self.dlg.setVisible(True) 
                
                pass

    def save_file(self):
        try:
            path =str(QFileDialog.getSaveFileName(caption="Defining output file", filter="Terse RDF Triple Language(*.ttl)")[0])
            
            mVocab = {}
            saveAttrs = {}
            save_constants = {}
            save_vocabs = {}
            
            for row in range(self.dlg.tableAttributes.rowCount()): 
                check = self.dlg.tableAttributes.cellWidget(row, 0) 
                if check.isChecked():
                    rdf_attr = check.text()
                    rdf = rdf_attr.split(":")
                    rdf_attr = rdf[1]
                    namespace = namespaces[rdf[0]][0]
                    url_rdf = namespace[rdf_attr]

                    combo_type = self.dlg.tableAttributes.cellWidget(row, 1)

                    if (combo_type.currentText() == "Layer Attribute"):
                        combo = self.dlg.tableAttributes.cellWidget(row, 2)
                        attribute = combo.currentText()
                        saveAttrs[attribute] = rdf_attr
                        #print ("url_rdf",url_rdf, type(url_rdf))
                        mVocab[attribute] =  url_rdf
                    elif (combo_type.currentText() == "Vocabulary"):
                        combo = self.dlg.tableAttributes.cellWidget(row, 2)
                        attribute = combo.currentText()
                        url_v = self.toURL(attribute)
                        save_constants[rdf_attr] = url_v
                        mVocab[rdf_attr] =  url_rdf   
                    else:
                        line_edit = self.dlg.tableAttributes.cellWidget(row, 2)
                        save_constants[rdf_attr] = parse_ifs(line_edit.text())
                        mVocab[rdf_attr] =  url_rdf         
            
            if self.dlg.checkSelected.isChecked():
                    features = self.layer.selectedFeatures() 
            else:
                    features = self.layer.getFeatures()

            triples = {}
            for feature in features:

                    triple = {  }
                    mVocab['asWkt'] = URIRef("http://www.opengis.net/ont/geosparql#asWKT")
                    if self.dlg.checkGeometries.isChecked():
                        pol = QgsMultiPolygon()
                        pol.fromWkt (feature.geometry().asWkt())
                        triple['asWkt'] = pol.polygonN(0).asWkt()


                    for key in saveAttrs:
                        triple[key] = feature[key]
                    
            
                   #triples[str(uuid.uuid4())] = triple
                    if self.dlg.comboID.currentText() == "Layer Attribute":
                        attr = feature [self.dlg.comboAttributeID.currentText()]
                        triples[attr] = triple
                    else:
                        triples[str(uuid.uuid4())] = triple



            g = Graph()
          
            
            url_main = self.dlg.lineURLBase.text()
            mainNamespace = Namespace(url_main)
            
            prefix_main = self.dlg.linePrefix2.text()
            g.bind(prefix_main, mainNamespace)


            g.bind("geo", Namespace("http://www.opengis.net/ont/geosparql#"))

            constants_p_o = []
            for key in save_constants:
                    attr = key
                    value = save_constants[key]
                    predicate = mVocab[attr]
                    if (isinstance(value, URIRef)):
                        object = value
                    else:
                        object = Literal(value)
                        if (validade_url(value)): # talvez deveria ver pelo schema
                            object = URIRef(value)
                    constants_p_o.append ((predicate, object))


            if self.dlg.checkConstant.isChecked (): # aggregar em um dataset, por exemplo
                
                aggregNamespace = Namespace(self.dlg.lineURLBase_2.text())
            
                g.bind(self.dlg.linePrefix2_2.text(), aggregNamespace)

                aggregate = aggregNamespace[str(uuid.uuid4())] 

                attribute = self.dlg.comboRDFType_2.currentText()
                url_aggregate = self.toURL(attribute)

                g.add((aggregate, RDF.type, url_aggregate))


                for (p, o) in constants_p_o:
                    g.add((aggregate,p, o))

            for prefix, name in namespaces.items():
                g.bind(prefix,name[0])
                #print (prefix, name[0])

            for id, attributes in triples.items():
                subject = mainNamespace[id]
                #g.add((subject, RDF.type, QB.Observation))
                attribute = self.dlg.comboRDFType.currentText()
                url_v = self.toURL(attribute)
                g.add((subject, RDF.type, url_v))
            
                for attr, value in attributes.items():
                    predicate = mVocab[attr]
                    #print ("predicate",predicate, type(predicate))
                    object = Literal(value)
                    if (validade_url(value)): # talvez deveria ver pelo schema
                        object = URIRef(value)
                    
                    g.add((subject, predicate, object))

                QB = Namespace ("http://purl.org/linked-data/cube#")

                if self.dlg.checkConstant.isChecked (): # aggregar em um dataset, por exemplo
                    attribute_p = self.dlg.comboBoxPredicate.currentText()
                    url_p = self.toURL(attribute_p)
                    g.add((subject, url_p, aggregate)) # generalizar
                else:
                    for (p, o) in constants_p_o:
                         g.add((subject,p, o))


            s = g.serialize(format="turtle")
            #print(s)   
            
            f = open(path,"w+",encoding="utf-8") 
            print ("saving ..."+path)
            f.write (s)
            f.close()

            self.iface.messageBar().pushMessage(
                    "Success", "Output file written at " + path,
                    level=Qgis.Success, duration=3
             )
        except:
            pass
        
    def close(self):
        self.dlg.setVisible(False)
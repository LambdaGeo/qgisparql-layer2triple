# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sergio/.local/share/QGIS/QGIS3/profiles/default/python/plugins/qgisparql-layer2triple/Layer2Triple_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Layer2TripleDialogBase(object):
    def setupUi(self, Layer2TripleDialogBase):
        Layer2TripleDialogBase.setObjectName("Layer2TripleDialogBase")
        Layer2TripleDialogBase.resize(667, 372)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(Layer2TripleDialogBase.sizePolicy().hasHeightForWidth())
        Layer2TripleDialogBase.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Layer2TripleDialogBase)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QVBoxLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Layer2TripleDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboLayer = QtWidgets.QComboBox(Layer2TripleDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboLayer.sizePolicy().hasHeightForWidth())
        self.comboLayer.setSizePolicy(sizePolicy)
        self.comboLayer.setObjectName("comboLayer")
        self.horizontalLayout_3.addWidget(self.comboLayer)
        self.button_load_layer = QtWidgets.QPushButton(Layer2TripleDialogBase)
        self.button_load_layer.setObjectName("button_load_layer")
        self.horizontalLayout_3.addWidget(self.button_load_layer)
        self.checkSelected = QtWidgets.QCheckBox(Layer2TripleDialogBase)
        self.checkSelected.setChecked(True)
        self.checkSelected.setObjectName("checkSelected")
        self.horizontalLayout_3.addWidget(self.checkSelected)
        self.checkGeometries = QtWidgets.QCheckBox(Layer2TripleDialogBase)
        self.checkGeometries.setObjectName("checkGeometries")
        self.horizontalLayout_3.addWidget(self.checkGeometries)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Layer2TripleDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.linePrefix = QtWidgets.QLineEdit(Layer2TripleDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linePrefix.sizePolicy().hasHeightForWidth())
        self.linePrefix.setSizePolicy(sizePolicy)
        self.linePrefix.setObjectName("linePrefix")
        self.horizontalLayout.addWidget(self.linePrefix)
        self.labelRDF = QtWidgets.QLabel(Layer2TripleDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRDF.sizePolicy().hasHeightForWidth())
        self.labelRDF.setSizePolicy(sizePolicy)
        self.labelRDF.setObjectName("labelRDF")
        self.horizontalLayout.addWidget(self.labelRDF)
        self.lineURL = QtWidgets.QLineEdit(Layer2TripleDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineURL.sizePolicy().hasHeightForWidth())
        self.lineURL.setSizePolicy(sizePolicy)
        self.lineURL.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineURL.setObjectName("lineURL")
        self.horizontalLayout.addWidget(self.lineURL)
        self.label_2 = QtWidgets.QLabel(Layer2TripleDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboFormat = QtWidgets.QComboBox(Layer2TripleDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboFormat.sizePolicy().hasHeightForWidth())
        self.comboFormat.setSizePolicy(sizePolicy)
        self.comboFormat.setObjectName("comboFormat")
        self.comboFormat.addItem("")
        self.comboFormat.addItem("")
        self.horizontalLayout.addWidget(self.comboFormat)
        self.buttonLoad = QtWidgets.QToolButton(Layer2TripleDialogBase)
        self.buttonLoad.setObjectName("buttonLoad")
        self.horizontalLayout.addWidget(self.buttonLoad)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelID = QtWidgets.QLabel(Layer2TripleDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelID.sizePolicy().hasHeightForWidth())
        self.labelID.setSizePolicy(sizePolicy)
        self.labelID.setMinimumSize(QtCore.QSize(0, 0))
        self.labelID.setObjectName("labelID")
        self.horizontalLayout_2.addWidget(self.labelID)
        self.comboID = QtWidgets.QComboBox(Layer2TripleDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboID.sizePolicy().hasHeightForWidth())
        self.comboID.setSizePolicy(sizePolicy)
        self.comboID.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboID.setObjectName("comboID")
        self.comboID.addItem("")
        self.comboID.addItem("")
        self.horizontalLayout_2.addWidget(self.comboID)
        self.label_4 = QtWidgets.QLabel(Layer2TripleDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboAttributeID = QtWidgets.QComboBox(Layer2TripleDialogBase)
        self.comboAttributeID.setEnabled(True)
        self.comboAttributeID.setEditable(False)
        self.comboAttributeID.setObjectName("comboAttributeID")
        self.horizontalLayout_2.addWidget(self.comboAttributeID)
        spacerItem = QtWidgets.QSpacerItem(26, 26, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(Layer2TripleDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.comboRDFType = QtWidgets.QComboBox(Layer2TripleDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboRDFType.sizePolicy().hasHeightForWidth())
        self.comboRDFType.setSizePolicy(sizePolicy)
        self.comboRDFType.setObjectName("comboRDFType")
        self.horizontalLayout_4.addWidget(self.comboRDFType)
        self.label_7 = QtWidgets.QLabel(Layer2TripleDialogBase)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.linePrefix2 = QtWidgets.QLineEdit(Layer2TripleDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linePrefix2.sizePolicy().hasHeightForWidth())
        self.linePrefix2.setSizePolicy(sizePolicy)
        self.linePrefix2.setText("")
        self.linePrefix2.setObjectName("linePrefix2")
        self.horizontalLayout_4.addWidget(self.linePrefix2)
        self.label_6 = QtWidgets.QLabel(Layer2TripleDialogBase)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.lineURLBase = QtWidgets.QLineEdit(Layer2TripleDialogBase)
        self.lineURLBase.setText("")
        self.lineURLBase.setObjectName("lineURLBase")
        self.horizontalLayout_4.addWidget(self.lineURLBase)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.atributos = QtWidgets.QLabel(Layer2TripleDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.atributos.sizePolicy().hasHeightForWidth())
        self.atributos.setSizePolicy(sizePolicy)
        self.atributos.setObjectName("atributos")
        self.verticalLayout_2.addWidget(self.atributos)
        self.tableAttributes = QtWidgets.QTableWidget(Layer2TripleDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableAttributes.sizePolicy().hasHeightForWidth())
        self.tableAttributes.setSizePolicy(sizePolicy)
        self.tableAttributes.setObjectName("tableAttributes")
        self.tableAttributes.setColumnCount(0)
        self.tableAttributes.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableAttributes)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Layer2TripleDialogBase)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_5.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.formLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(Layer2TripleDialogBase)
        QtCore.QMetaObject.connectSlotsByName(Layer2TripleDialogBase)

    def retranslateUi(self, Layer2TripleDialogBase):
        _translate = QtCore.QCoreApplication.translate
        Layer2TripleDialogBase.setWindowTitle(_translate("Layer2TripleDialogBase", "Layer2Triple"))
        self.label_3.setText(_translate("Layer2TripleDialogBase", "Layer"))
        self.button_load_layer.setText(_translate("Layer2TripleDialogBase", "Load Layer"))
        self.checkSelected.setText(_translate("Layer2TripleDialogBase", "Selected features"))
        self.checkGeometries.setText(_translate("Layer2TripleDialogBase", "Export Geometries"))
        self.label.setText(_translate("Layer2TripleDialogBase", "Prefix"))
        self.linePrefix.setText(_translate("Layer2TripleDialogBase", "amz"))
        self.labelRDF.setText(_translate("Layer2TripleDialogBase", "URL"))
        self.lineURL.setText(_translate("Layer2TripleDialogBase", "http://purl.org/ontology/dbcells/amazon"))
        self.label_2.setText(_translate("Layer2TripleDialogBase", "Format"))
        self.comboFormat.setItemText(0, _translate("Layer2TripleDialogBase", "ttl"))
        self.comboFormat.setItemText(1, _translate("Layer2TripleDialogBase", "xml"))
        self.buttonLoad.setText(_translate("Layer2TripleDialogBase", "Load Vocabulary"))
        self.labelID.setText(_translate("Layer2TripleDialogBase", " ID"))
        self.comboID.setItemText(0, _translate("Layer2TripleDialogBase", "Universally Unique Identifier - UUID"))
        self.comboID.setItemText(1, _translate("Layer2TripleDialogBase", "Layer Attribute"))
        self.label_4.setText(_translate("Layer2TripleDialogBase", "Attribute"))
        self.label_5.setText(_translate("Layer2TripleDialogBase", "RDF Type"))
        self.label_7.setText(_translate("Layer2TripleDialogBase", "Prefix"))
        self.label_6.setText(_translate("Layer2TripleDialogBase", "URL Base"))
        self.atributos.setText(_translate("Layer2TripleDialogBase", "Attributes"))
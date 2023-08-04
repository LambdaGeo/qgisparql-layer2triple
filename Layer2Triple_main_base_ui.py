# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sergio/.local/share/QGIS/QGIS3/profiles/default/python/plugins/qgisparql-layer2triple/Layer2Triple_main_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 563)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QVBoxLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboLayer = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboLayer.sizePolicy().hasHeightForWidth())
        self.comboLayer.setSizePolicy(sizePolicy)
        self.comboLayer.setObjectName("comboLayer")
        self.horizontalLayout_3.addWidget(self.comboLayer)
        self.button_load_layer = QtWidgets.QPushButton(self.centralwidget)
        self.button_load_layer.setObjectName("button_load_layer")
        self.horizontalLayout_3.addWidget(self.button_load_layer)
        self.checkSelected = QtWidgets.QCheckBox(self.centralwidget)
        self.checkSelected.setChecked(True)
        self.checkSelected.setObjectName("checkSelected")
        self.horizontalLayout_3.addWidget(self.checkSelected)
        self.checkGeometries = QtWidgets.QCheckBox(self.centralwidget)
        self.checkGeometries.setObjectName("checkGeometries")
        self.horizontalLayout_3.addWidget(self.checkGeometries)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelID = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelID.sizePolicy().hasHeightForWidth())
        self.labelID.setSizePolicy(sizePolicy)
        self.labelID.setMinimumSize(QtCore.QSize(0, 0))
        self.labelID.setObjectName("labelID")
        self.horizontalLayout_2.addWidget(self.labelID)
        self.comboID = QtWidgets.QComboBox(self.centralwidget)
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
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboAttributeID = QtWidgets.QComboBox(self.centralwidget)
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
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.comboRDFType = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboRDFType.sizePolicy().hasHeightForWidth())
        self.comboRDFType.setSizePolicy(sizePolicy)
        self.comboRDFType.setObjectName("comboRDFType")
        self.horizontalLayout_4.addWidget(self.comboRDFType)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.linePrefix2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linePrefix2.sizePolicy().hasHeightForWidth())
        self.linePrefix2.setSizePolicy(sizePolicy)
        self.linePrefix2.setText("")
        self.linePrefix2.setObjectName("linePrefix2")
        self.horizontalLayout_4.addWidget(self.linePrefix2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.lineURLBase = QtWidgets.QLineEdit(self.centralwidget)
        self.lineURLBase.setText("")
        self.lineURLBase.setObjectName("lineURLBase")
        self.horizontalLayout_4.addWidget(self.lineURLBase)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.pushShowGroup = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushShowGroup.sizePolicy().hasHeightForWidth())
        self.pushShowGroup.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushShowGroup.setFont(font)
        self.pushShowGroup.setFlat(True)
        self.pushShowGroup.setObjectName("pushShowGroup")
        self.verticalLayout_2.addWidget(self.pushShowGroup)
        self.groupBoxConstants = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxConstants.sizePolicy().hasHeightForWidth())
        self.groupBoxConstants.setSizePolicy(sizePolicy)
        self.groupBoxConstants.setTitle("")
        self.groupBoxConstants.setFlat(True)
        self.groupBoxConstants.setObjectName("groupBoxConstants")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxConstants)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.groupBoxConstants)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.comboRDFType_2 = QtWidgets.QComboBox(self.groupBoxConstants)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboRDFType_2.sizePolicy().hasHeightForWidth())
        self.comboRDFType_2.setSizePolicy(sizePolicy)
        self.comboRDFType_2.setObjectName("comboRDFType_2")
        self.horizontalLayout_6.addWidget(self.comboRDFType_2)
        self.label_9 = QtWidgets.QLabel(self.groupBoxConstants)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.linePrefix2_2 = QtWidgets.QLineEdit(self.groupBoxConstants)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linePrefix2_2.sizePolicy().hasHeightForWidth())
        self.linePrefix2_2.setSizePolicy(sizePolicy)
        self.linePrefix2_2.setText("")
        self.linePrefix2_2.setObjectName("linePrefix2_2")
        self.horizontalLayout_6.addWidget(self.linePrefix2_2)
        self.label_10 = QtWidgets.QLabel(self.groupBoxConstants)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.lineURLBase_2 = QtWidgets.QLineEdit(self.groupBoxConstants)
        self.lineURLBase_2.setText("")
        self.lineURLBase_2.setObjectName("lineURLBase_2")
        self.horizontalLayout_6.addWidget(self.lineURLBase_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkConstant = QtWidgets.QCheckBox(self.groupBoxConstants)
        self.checkConstant.setObjectName("checkConstant")
        self.horizontalLayout_8.addWidget(self.checkConstant)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.groupBoxConstants)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.comboBoxPredicate = QtWidgets.QComboBox(self.groupBoxConstants)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxPredicate.sizePolicy().hasHeightForWidth())
        self.comboBoxPredicate.setSizePolicy(sizePolicy)
        self.comboBoxPredicate.setObjectName("comboBoxPredicate")
        self.horizontalLayout_9.addWidget(self.comboBoxPredicate)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBoxConstants)
        self.groupBoxAttributes = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxAttributes.sizePolicy().hasHeightForWidth())
        self.groupBoxAttributes.setSizePolicy(sizePolicy)
        self.groupBoxAttributes.setObjectName("groupBoxAttributes")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxAttributes)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_bar = QtWidgets.QLineEdit(self.groupBoxAttributes)
        self.search_bar.setText("")
        self.search_bar.setObjectName("search_bar")
        self.verticalLayout.addWidget(self.search_bar)
        self.tableAttributes = QtWidgets.QTableWidget(self.groupBoxAttributes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableAttributes.sizePolicy().hasHeightForWidth())
        self.tableAttributes.setSizePolicy(sizePolicy)
        self.tableAttributes.setObjectName("tableAttributes")
        self.tableAttributes.setColumnCount(0)
        self.tableAttributes.setRowCount(0)
        self.verticalLayout.addWidget(self.tableAttributes)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBoxAttributes)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.pushButtonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_5.addWidget(self.pushButtonCancel)
        self.pushButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSave.setEnabled(False)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout_5.addWidget(self.pushButtonSave)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.formLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 22))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuVocabulary = QtWidgets.QMenu(self.menubar)
        self.menuVocabulary.setObjectName("menuVocabulary")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionLoad_Vocabulary = QtWidgets.QAction(MainWindow)
        self.actionLoad_Vocabulary.setObjectName("actionLoad_Vocabulary")
        self.menuSettings.addAction(self.actionSave)
        self.menuSettings.addAction(self.actionOpen)
        self.menuVocabulary.addAction(self.actionLoad_Vocabulary)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuVocabulary.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Layer2Triple"))
        self.label_3.setText(_translate("MainWindow", "Layer"))
        self.button_load_layer.setText(_translate("MainWindow", "Load Layer"))
        self.checkSelected.setText(_translate("MainWindow", "Selected features"))
        self.checkGeometries.setText(_translate("MainWindow", "Export Geometries"))
        self.labelID.setText(_translate("MainWindow", " ID"))
        self.comboID.setItemText(0, _translate("MainWindow", "Universally Unique Identifier - UUID"))
        self.comboID.setItemText(1, _translate("MainWindow", "Layer Attribute"))
        self.label_4.setText(_translate("MainWindow", "Attribute"))
        self.label_5.setText(_translate("MainWindow", "Class"))
        self.label_7.setText(_translate("MainWindow", "Prefix"))
        self.label_6.setText(_translate("MainWindow", "URL Base"))
        self.pushShowGroup.setText(_translate("MainWindow", "> Aggregating Constants"))
        self.label_8.setText(_translate("MainWindow", "Class"))
        self.label_9.setText(_translate("MainWindow", "Prefix"))
        self.label_10.setText(_translate("MainWindow", "URL Base"))
        self.checkConstant.setText(_translate("MainWindow", "Aggregate ?"))
        self.label_11.setText(_translate("MainWindow", "Predicate: "))
        self.groupBoxAttributes.setTitle(_translate("MainWindow", "Attributes"))
        self.pushButtonCancel.setText(_translate("MainWindow", "Cancel"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuVocabulary.setTitle(_translate("MainWindow", "Vocabulary"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionLoad_Vocabulary.setText(_translate("MainWindow", "Load Vocabulary"))

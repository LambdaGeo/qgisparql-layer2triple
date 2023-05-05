# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sergio/.local/share/QGIS/QGIS3/profiles/default/python/plugins/qgisparql-layer2triple/Vocabulary_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VocabularyDialog(object):
    def setupUi(self, VocabularyDialog):
        VocabularyDialog.setObjectName("VocabularyDialog")
        VocabularyDialog.resize(518, 119)
        self.gridLayout = QtWidgets.QGridLayout(VocabularyDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(VocabularyDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.linePrefix = QtWidgets.QLineEdit(VocabularyDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linePrefix.sizePolicy().hasHeightForWidth())
        self.linePrefix.setSizePolicy(sizePolicy)
        self.linePrefix.setObjectName("linePrefix")
        self.horizontalLayout.addWidget(self.linePrefix)
        self.labelRDF = QtWidgets.QLabel(VocabularyDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRDF.sizePolicy().hasHeightForWidth())
        self.labelRDF.setSizePolicy(sizePolicy)
        self.labelRDF.setObjectName("labelRDF")
        self.horizontalLayout.addWidget(self.labelRDF)
        self.lineURL = QtWidgets.QLineEdit(VocabularyDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineURL.sizePolicy().hasHeightForWidth())
        self.lineURL.setSizePolicy(sizePolicy)
        self.lineURL.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineURL.setObjectName("lineURL")
        self.horizontalLayout.addWidget(self.lineURL)
        self.label_2 = QtWidgets.QLabel(VocabularyDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboFormat = QtWidgets.QComboBox(VocabularyDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboFormat.sizePolicy().hasHeightForWidth())
        self.comboFormat.setSizePolicy(sizePolicy)
        self.comboFormat.setObjectName("comboFormat")
        self.comboFormat.addItem("")
        self.comboFormat.addItem("")
        self.horizontalLayout.addWidget(self.comboFormat)
        self.buttonLoad = QtWidgets.QToolButton(VocabularyDialog)
        self.buttonLoad.setObjectName("buttonLoad")
        self.horizontalLayout.addWidget(self.buttonLoad)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(VocabularyDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(VocabularyDialog)
        self.buttonBox.accepted.connect(VocabularyDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(VocabularyDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(VocabularyDialog)

    def retranslateUi(self, VocabularyDialog):
        _translate = QtCore.QCoreApplication.translate
        VocabularyDialog.setWindowTitle(_translate("VocabularyDialog", "Dialog"))
        self.label.setText(_translate("VocabularyDialog", "Prefix"))
        self.linePrefix.setText(_translate("VocabularyDialog", "amz"))
        self.labelRDF.setText(_translate("VocabularyDialog", "URL"))
        self.lineURL.setText(_translate("VocabularyDialog", "http://purl.org/ontology/dbcells/amazon"))
        self.label_2.setText(_translate("VocabularyDialog", "Format"))
        self.comboFormat.setItemText(0, _translate("VocabularyDialog", "ttl"))
        self.comboFormat.setItemText(1, _translate("VocabularyDialog", "xml"))
        self.buttonLoad.setText(_translate("VocabularyDialog", "Load Vocabulary"))

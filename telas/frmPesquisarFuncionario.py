# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmPesquisarFuncionario.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_frmPesquisarFuncionario(object):
    def setupUi(self, frmPesquisarFuncionario):
        frmPesquisarFuncionario.setObjectName(_fromUtf8("frmPesquisarFuncionario"))
        frmPesquisarFuncionario.resize(794, 504)
        frmPesquisarFuncionario.setMinimumSize(QtCore.QSize(794, 504))
        frmPesquisarFuncionario.setMaximumSize(QtCore.QSize(794, 504))
        font = QtGui.QFont()
        font.setPointSize(11)
        frmPesquisarFuncionario.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/folder_saved_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmPesquisarFuncionario.setWindowIcon(icon)
        frmPesquisarFuncionario.setSizeGripEnabled(True)
        frmPesquisarFuncionario.setModal(True)

        self.grbTipoPesquisa = QtGui.QGroupBox(frmPesquisarFuncionario)
        self.grbTipoPesquisa.setGeometry(QtCore.QRect(10, 10, 191, 91))
        self.grbTipoPesquisa.setObjectName(_fromUtf8("grbTipoPesquisa"))

        self.radBtnNome = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnNome.setGeometry(QtCore.QRect(20, 40, 61, 23))
        self.radBtnNome.setObjectName(_fromUtf8("radBtnNome"))

        self.radBtncPF = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtncPF.setGeometry(QtCore.QRect(20, 60, 51, 23))
        self.radBtncPF.setObjectName(_fromUtf8("radBtncPF"))

        self.radBtnRg = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnRg.setGeometry(QtCore.QRect(90, 20, 51, 23))
        self.radBtnRg.setObjectName(_fromUtf8("radBtnRg"))

        self.radBtnNumCarteira = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnNumCarteira.setGeometry(QtCore.QRect(90, 40, 91, 23))
        self.radBtnNumCarteira.setObjectName(_fromUtf8("radBtnNumCarteira"))

        self.radBtnPis = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnPis.setGeometry(QtCore.QRect(90, 60, 91, 23))
        self.radBtnPis.setObjectName(_fromUtf8("radBtnPis"))

        self.radBtnCodigo = QtGui.QRadioButton(self.grbTipoPesquisa)
        self.radBtnCodigo.setGeometry(QtCore.QRect(20, 20, 63, 23))
        self.radBtnCodigo.setObjectName(_fromUtf8("radBtnCodigo"))

        self.txtPesquisar = QtGui.QLineEdit(frmPesquisarFuncionario)
        self.txtPesquisar.setGeometry(QtCore.QRect(210, 70, 441, 25))
        self.txtPesquisar.setObjectName(_fromUtf8("txtPesquisar"))

        self.btnPesquisar = QtGui.QPushButton(frmPesquisarFuncionario)
        self.btnPesquisar.setGeometry(QtCore.QRect(660, 70, 31, 27))
        self.btnPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btnPesquisar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))

        self.tabPesquisar = QtGui.QTableWidget(frmPesquisarFuncionario)
        self.tabPesquisar.setGeometry(QtCore.QRect(10, 110, 771, 381))
        self.tabPesquisar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabPesquisar.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabPesquisar.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabPesquisar.setObjectName(_fromUtf8("tabPesquisar"))
        self.tabPesquisar.setColumnCount(33)
        self.tabPesquisar.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(17, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(18, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(19, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(20, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(21, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(22, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(23, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(24, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(25, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(26, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(27, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(28, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(29, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(30, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(31, item)
        item = QtGui.QTableWidgetItem()
        self.tabPesquisar.setHorizontalHeaderItem(32, item)
        self.tabPesquisar.verticalHeader().setVisible(False)
        self.tabPesquisar.verticalHeader().setCascadingSectionResizes(True)

        self.retranslateUi(frmPesquisarFuncionario)
        QtCore.QMetaObject.connectSlotsByName(frmPesquisarFuncionario)
        frmPesquisarFuncionario.setTabOrder(self.radBtnNome, self.radBtncPF)
        frmPesquisarFuncionario.setTabOrder(self.radBtncPF, self.radBtnRg)
        frmPesquisarFuncionario.setTabOrder(self.radBtnRg, self.radBtnNumCarteira)
        frmPesquisarFuncionario.setTabOrder(self.radBtnNumCarteira, self.txtPesquisar)
        frmPesquisarFuncionario.setTabOrder(self.txtPesquisar, self.btnPesquisar)
        frmPesquisarFuncionario.setTabOrder(self.btnPesquisar, self.tabPesquisar)

    def retranslateUi(self, frmPesquisarFuncionario):
        frmPesquisarFuncionario.setWindowTitle(_translate("frmPesquisarFuncionario", "Pesquisar Funcionario", None))
        self.grbTipoPesquisa.setTitle(_translate("frmPesquisarFuncionario", "Tipo Pesquisa", None))
        self.radBtnNome.setToolTip(_translate("frmPesquisarFuncionario", "Nome", None))
        self.radBtnNome.setWhatsThis(_translate("frmPesquisarFuncionario", "Item de seleção para a pesquisa por nome", None))
        self.radBtnNome.setText(_translate("frmPesquisarFuncionario", "Nome", None))
        self.radBtncPF.setToolTip(_translate("frmPesquisarFuncionario", "CPF", None))
        self.radBtncPF.setWhatsThis(_translate("frmPesquisarFuncionario", "Item de seleção para a pesquisa por CPF", None))
        self.radBtncPF.setText(_translate("frmPesquisarFuncionario", "CPF", None))
        self.radBtnRg.setToolTip(_translate("frmPesquisarFuncionario", "RG", None))
        self.radBtnRg.setWhatsThis(_translate("frmPesquisarFuncionario", "Item de seleção para a pesquisa por RG", None))
        self.radBtnRg.setText(_translate("frmPesquisarFuncionario", "RG", None))
        self.radBtnNumCarteira.setToolTip(_translate("frmPesquisarFuncionario", "Número Carteira", None))
        self.radBtnNumCarteira.setWhatsThis(_translate("frmPesquisarFuncionario", "<html><head/><body><p>Item de seleção para a pesquisa por número carteira</p></body></html>", None))
        self.radBtnNumCarteira.setText(_translate("frmPesquisarFuncionario", "Nº Carteira", None))
        self.radBtnPis.setToolTip(_translate("frmPesquisarFuncionario", "PIS/PASEP", None))
        self.radBtnPis.setWhatsThis(_translate("frmPesquisarFuncionario", "<html><head/><body><p>Item de seleção para a pesquisa por PIS/PASEP</p></body></html>", None))
        self.radBtnPis.setText(_translate("frmPesquisarFuncionario", "PIS/PASEP", None))
        self.radBtnCodigo.setToolTip(_translate("frmPesquisarFuncionario", "RG", None))
        self.radBtnCodigo.setWhatsThis(_translate("frmPesquisarFuncionario", "Item de seleção para a pesquisa por RG", None))
        self.radBtnCodigo.setText(_translate("frmPesquisarFuncionario", "Codigo", None))
        self.txtPesquisar.setToolTip(_translate("frmPesquisarFuncionario", "Pesquisar", None))
        self.txtPesquisar.setWhatsThis(_translate("frmPesquisarFuncionario", "Campo de inserir os dados para pesquisar", None))
        self.txtPesquisar.setPlaceholderText(_translate("frmPesquisarFuncionario", "Pesquisa", None))
        self.btnPesquisar.setWhatsThis(_translate("frmPesquisarFuncionario", "Botão para pesquisar as informações", None))
        self.tabPesquisar.setWhatsThis(_translate("frmPesquisarFuncionario", "Tabela dos dados pesquisados", None))
        item = self.tabPesquisar.horizontalHeaderItem(0)
        item.setText(_translate("frmPesquisarFuncionario", "Cod.", None))
        item = self.tabPesquisar.horizontalHeaderItem(1)
        item.setText(_translate("frmPesquisarFuncionario", "Nome", None))
        item = self.tabPesquisar.horizontalHeaderItem(2)
        item.setText(_translate("frmPesquisarFuncionario", "Sobrenome", None))
        item = self.tabPesquisar.horizontalHeaderItem(3)
        item.setText(_translate("frmPesquisarFuncionario", "CPF", None))
        item = self.tabPesquisar.horizontalHeaderItem(4)
        item.setText(_translate("frmPesquisarFuncionario", "RG", None))
        item = self.tabPesquisar.horizontalHeaderItem(5)
        item.setText(_translate("frmPesquisarFuncionario", "Expeditor", None))
        item = self.tabPesquisar.horizontalHeaderItem(6)
        item.setText(_translate("frmPesquisarFuncionario", "UF", None))
        item = self.tabPesquisar.horizontalHeaderItem(7)
        item.setText(_translate("frmPesquisarFuncionario", "Data", None))
        item = self.tabPesquisar.horizontalHeaderItem(8)
        item.setText(_translate("frmPesquisarFuncionario", "Sexo", None))
        item = self.tabPesquisar.horizontalHeaderItem(9)
        item.setText(_translate("frmPesquisarFuncionario", "Endereço", None))
        item = self.tabPesquisar.horizontalHeaderItem(10)
        item.setText(_translate("frmPesquisarFuncionario", "Número", None))
        item = self.tabPesquisar.horizontalHeaderItem(11)
        item.setText(_translate("frmPesquisarFuncionario", "Complemento", None))
        item = self.tabPesquisar.horizontalHeaderItem(12)
        item.setText(_translate("frmPesquisarFuncionario", "Bairro", None))
        item = self.tabPesquisar.horizontalHeaderItem(13)
        item.setText(_translate("frmPesquisarFuncionario", "Mãe", None))
        item = self.tabPesquisar.horizontalHeaderItem(14)
        item.setText(_translate("frmPesquisarFuncionario", "Pai", None))
        item = self.tabPesquisar.horizontalHeaderItem(15)
        item.setText(_translate("frmPesquisarFuncionario", "Cidade", None))
        item = self.tabPesquisar.horizontalHeaderItem(16)
        item.setText(_translate("frmPesquisarFuncionario", "Estado", None))
        item = self.tabPesquisar.horizontalHeaderItem(17)
        item.setText(_translate("frmPesquisarFuncionario", "CEP", None))
        item = self.tabPesquisar.horizontalHeaderItem(18)
        item.setText(_translate("frmPesquisarFuncionario", "Admissão", None))
        item = self.tabPesquisar.horizontalHeaderItem(19)
        item.setText(_translate("frmPesquisarFuncionario", "Demissão", None))
        item = self.tabPesquisar.horizontalHeaderItem(20)
        item.setText(_translate("frmPesquisarFuncionario", "Nº Carteira", None))
        item = self.tabPesquisar.horizontalHeaderItem(21)
        item.setText(_translate("frmPesquisarFuncionario", "Serie", None))
        item = self.tabPesquisar.horizontalHeaderItem(22)
        item.setText(_translate("frmPesquisarFuncionario", "UF", None))
        item = self.tabPesquisar.horizontalHeaderItem(23)
        item.setText(_translate("frmPesquisarFuncionario", "Emissão", None))
        item = self.tabPesquisar.horizontalHeaderItem(24)
        item.setText(_translate("frmPesquisarFuncionario", "PIS/PASEP", None))
        item = self.tabPesquisar.horizontalHeaderItem(25)
        item.setText(_translate("frmPesquisarFuncionario", "Estado Civil", None))
        item = self.tabPesquisar.horizontalHeaderItem(26)
        item.setText(_translate("frmPesquisarFuncionario", "Deficiencia", None))
        item = self.tabPesquisar.horizontalHeaderItem(27)
        item.setText(_translate("frmPesquisarFuncionario", "Cate. Trabalho", None))
        item = self.tabPesquisar.horizontalHeaderItem(28)
        item.setText(_translate("frmPesquisarFuncionario", "Setor", None))
        item = self.tabPesquisar.horizontalHeaderItem(29)
        item.setText(_translate("frmPesquisarFuncionario", "Cargo", None))
        item = self.tabPesquisar.horizontalHeaderItem(30)
        item.setText(_translate("frmPesquisarFuncionario", "Observação", None))
        item = self.tabPesquisar.horizontalHeaderItem(31)
        item.setText(_translate("frmPesquisarFuncionario", "Jornada", None))
        item = self.tabPesquisar.horizontalHeaderItem(32)
        item.setText(_translate("frmPesquisarFuncionario", "Situação", None))


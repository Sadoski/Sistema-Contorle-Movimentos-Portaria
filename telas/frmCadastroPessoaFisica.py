# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmCadastroPessoaFisica.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import datetime
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

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

class Ui_frmCadastroPessoaFisica(object):
    def setupUi(self, frmCadastroPessoaFisica):
        frmCadastroPessoaFisica.setObjectName(_fromUtf8("frmCadastroPessoaFisica"))
        frmCadastroPessoaFisica.resize(791, 439)
        frmCadastroPessoaFisica.setMinimumSize(QtCore.QSize(791, 439))
        frmCadastroPessoaFisica.setMaximumSize(QtCore.QSize(791, 439))
        font = QtGui.QFont()
        font.setPointSize(11)
        frmCadastroPessoaFisica.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/pessoa_fisica.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmCadastroPessoaFisica.setWindowIcon(icon5)
        frmCadastroPessoaFisica.setSizeGripEnabled(True)
        frmCadastroPessoaFisica.setModal(True)

        self.grbBotoes = QtGui.QGroupBox(frmCadastroPessoaFisica)
        self.grbBotoes.setGeometry(QtCore.QRect(10, 380, 771, 51))
        self.grbBotoes.setTitle(_fromUtf8(""))
        self.grbBotoes.setObjectName(_fromUtf8("grbBotoes"))

        self.btnNovo = QtGui.QPushButton(self.grbBotoes)
        self.btnNovo.setGeometry(QtCore.QRect(260, 10, 88, 27))
        self.btnNovo.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/filenew.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNovo.setIcon(icon)
        self.btnNovo.setObjectName(_fromUtf8("btnNovo"))

        self.btnSalvar = QtGui.QPushButton(self.grbBotoes)
        self.btnSalvar.setEnabled(False)
        self.btnSalvar.setGeometry(QtCore.QRect(360, 10, 88, 27))
        self.btnSalvar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/filesave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon1)
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))

        self.btnCancelar = QtGui.QPushButton(self.grbBotoes)
        self.btnCancelar.setEnabled(False)
        self.btnCancelar.setGeometry(QtCore.QRect(560, 10, 88, 27))
        self.btnCancelar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon2)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))

        self.btnDeletar = QtGui.QPushButton(self.grbBotoes)
        self.btnDeletar.setEnabled(False)
        self.btnDeletar.setGeometry(QtCore.QRect(660, 10, 88, 27))
        self.btnDeletar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/critical.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDeletar.setIcon(icon3)
        self.btnDeletar.setObjectName(_fromUtf8("btnDeletar"))

        self.btnEditar = QtGui.QPushButton(self.grbBotoes)
        self.btnEditar.setEnabled(False)
        self.btnEditar.setGeometry(QtCore.QRect(460, 10, 88, 27))
        self.btnEditar.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/Save-as_37111.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEditar.setIcon(icon4)
        self.btnEditar.setObjectName(_fromUtf8("btnEditar"))

        self.lblPesquisar = QtGui.QLabel(self.grbBotoes)
        self.lblPesquisar.setGeometry(QtCore.QRect(10, 20, 111, 19))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(118, 116, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lblPesquisar.setPalette(palette)
        self.lblPesquisar.setObjectName(_fromUtf8("lblPesquisar"))

        self.grbDados = QtGui.QGroupBox(frmCadastroPessoaFisica)
        self.grbDados.setEnabled(False)
        self.grbDados.setGeometry(QtCore.QRect(10, 10, 771, 361))
        self.grbDados.setTitle(_fromUtf8(""))
        self.grbDados.setObjectName(_fromUtf8("grbDados"))

        self.txtComplemento = QtGui.QLineEdit(self.grbDados)
        self.txtComplemento.setGeometry(QtCore.QRect(10, 170, 331, 24))
        self.txtComplemento.setMaxLength(50)
        self.txtComplemento.setObjectName(_fromUtf8("txtComplemento"))

        self.txtEstado = QtGui.QLineEdit(self.grbDados)
        self.txtEstado.setEnabled(False)
        self.txtEstado.setGeometry(QtCore.QRect(540, 220, 181, 25))
        self.txtEstado.setMaxLength(50)
        self.txtEstado.setObjectName(_fromUtf8("txtEstado"))

        self.btnPesquisarCidade = QtGui.QPushButton(self.grbDados)
        self.btnPesquisarCidade.setGeometry(QtCore.QRect(730, 219, 31, 26))
        self.btnPesquisarCidade.setText(_fromUtf8(""))
        self.btnPesquisarCidade.setFocusPolicy(QtCore.Qt.NoFocus)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisarCidade.setIcon(icon5)
        self.btnPesquisarCidade.setObjectName(_fromUtf8("btnPesquisarCidade"))

        self.lblEstado = QtGui.QLabel(self.grbDados)
        self.lblEstado.setGeometry(QtCore.QRect(540, 200, 51, 19))
        self.lblEstado.setObjectName(_fromUtf8("lblEstado"))

        self.lblComplemento = QtGui.QLabel(self.grbDados)
        self.lblComplemento.setGeometry(QtCore.QRect(10, 150, 101, 16))
        self.lblComplemento.setObjectName(_fromUtf8("lblComplemento"))

        self.txtCidade = QtGui.QLineEdit(self.grbDados)
        self.txtCidade.setEnabled(False)
        self.txtCidade.setGeometry(QtCore.QRect(150, 220, 381, 25))
        self.txtCidade.setMaxLength(75)
        self.txtCidade.setObjectName(_fromUtf8("txtCidade"))

        self.lblCidade = QtGui.QLabel(self.grbDados)
        self.lblCidade.setGeometry(QtCore.QRect(150, 200, 51, 19))
        self.lblCidade.setObjectName(_fromUtf8("lblCidade"))

        self.txtCpf = QtGui.QLineEdit(self.grbDados)
        self.txtCpf.setGeometry(QtCore.QRect(10, 70, 161, 25))
        self.txtCpf.setMaxLength(14)
        self.txtCpf.setObjectName(_fromUtf8("txtCpf"))

        self.lblRg = QtGui.QLabel(self.grbDados)
        self.lblRg.setGeometry(QtCore.QRect(180, 50, 91, 19))
        self.lblRg.setObjectName(_fromUtf8("lblRg"))

        self.txtCep = QtGui.QLineEdit(self.grbDados)
        self.txtCep.setGeometry(QtCore.QRect(10, 220, 131, 25))
        self.txtCep.setObjectName(_fromUtf8("txtCep"))

        self.txtNumero = QtGui.QLineEdit(self.grbDados)
        self.txtNumero.setGeometry(QtCore.QRect(620, 120, 141, 25))
        self.txtNumero.setMaxLength(11)
        self.txtNumero.setObjectName(_fromUtf8("txtNumero"))

        self.txtNome = QtGui.QLineEdit(self.grbDados)
        self.txtNome.setGeometry(QtCore.QRect(10, 20, 751, 25))
        self.txtNome.setMaxLength(75)
        self.txtNome.setObjectName(_fromUtf8("txtNome"))

        self.lblBairro = QtGui.QLabel(self.grbDados)
        self.lblBairro.setGeometry(QtCore.QRect(350, 150, 51, 19))
        self.lblBairro.setObjectName(_fromUtf8("lblBairro"))

        self.txtEndereco = QtGui.QLineEdit(self.grbDados)
        self.txtEndereco.setGeometry(QtCore.QRect(10, 120, 601, 25))
        self.txtEndereco.setMaxLength(50)
        self.txtEndereco.setObjectName(_fromUtf8("txtEndereco"))

        self.lblEndereco = QtGui.QLabel(self.grbDados)
        self.lblEndereco.setGeometry(QtCore.QRect(10, 100, 66, 19))
        self.lblEndereco.setObjectName(_fromUtf8("lblEndereco"))

        self.txtRg = QtGui.QLineEdit(self.grbDados)
        self.txtRg.setGeometry(QtCore.QRect(180, 70, 141, 25))
        self.txtRg.setMaxLength(15)
        self.txtRg.setObjectName(_fromUtf8("txtRg"))

        self.lblNome = QtGui.QLabel(self.grbDados)
        self.lblNome.setGeometry(QtCore.QRect(10, 0, 141, 19))
        self.lblNome.setObjectName(_fromUtf8("lblNome"))

        self.txtBairro = QtGui.QLineEdit(self.grbDados)
        self.txtBairro.setGeometry(QtCore.QRect(350, 170, 411, 25))
        self.txtBairro.setMaxLength(50)
        self.txtBairro.setObjectName(_fromUtf8("txtBairro"))

        self.lblNumero = QtGui.QLabel(self.grbDados)
        self.lblNumero.setGeometry(QtCore.QRect(620, 100, 66, 19))
        self.lblNumero.setObjectName(_fromUtf8("lblNumero"))

        self.txtMae = QtGui.QLineEdit(self.grbDados)
        self.txtMae.setGeometry(QtCore.QRect(10, 270, 561, 25))
        self.txtMae.setMaxLength(75)
        self.txtMae.setObjectName(_fromUtf8("txtMae"))

        self.lblCep = QtGui.QLabel(self.grbDados)
        self.lblCep.setGeometry(QtCore.QRect(10, 200, 31, 19))
        self.lblCep.setObjectName(_fromUtf8("lblCep"))

        self.lblMae = QtGui.QLabel(self.grbDados)
        self.lblMae.setGeometry(QtCore.QRect(10, 250, 31, 19))
        self.lblMae.setObjectName(_fromUtf8("lblMae"))

        self.lblCpf = QtGui.QLabel(self.grbDados)
        self.lblCpf.setGeometry(QtCore.QRect(10, 50, 81, 19))
        self.lblCpf.setObjectName(_fromUtf8("lblCpf"))

        self.lblPai = QtGui.QLabel(self.grbDados)
        self.lblPai.setGeometry(QtCore.QRect(10, 300, 31, 19))
        self.lblPai.setObjectName(_fromUtf8("lblPai"))

        self.txtPai = QtGui.QLineEdit(self.grbDados)
        self.txtPai.setGeometry(QtCore.QRect(10, 320, 561, 25))
        self.txtPai.setMaxLength(75)
        self.txtPai.setObjectName(_fromUtf8("txtPai"))

        self.dateData = QtGui.QDateEdit(self.grbDados)
        self.dateData.setDate(QDate.currentDate())
        self.dateData.setGeometry(QtCore.QRect(450, 70, 110, 26))
        self.dateData.setCalendarPopup(True)
        self.dateData.setObjectName(_fromUtf8("dateData"))

        self.lblDataNas = QtGui.QLabel(self.grbDados)
        self.lblDataNas.setGeometry(QtCore.QRect(450, 50, 71, 16))
        self.lblDataNas.setObjectName(_fromUtf8("lblDataNas"))

        self.grbSexo = QtGui.QGroupBox(self.grbDados)
        self.grbSexo.setGeometry(QtCore.QRect(570, 50, 191, 51))
        self.grbSexo.setObjectName(_fromUtf8("grbSexo"))

        self.radBtnMasculino = QtGui.QRadioButton(self.grbSexo)
        self.radBtnMasculino.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radBtnMasculino.setObjectName(_fromUtf8("radBtnMasculino"))

        self.radBtnFeminino = QtGui.QRadioButton(self.grbSexo)
        self.radBtnFeminino.setGeometry(QtCore.QRect(100, 20, 82, 17))
        self.radBtnFeminino.setObjectName(_fromUtf8("radBtnFeminino"))

        self.txtExpeditor = QtGui.QLineEdit(self.grbDados)
        self.txtExpeditor.setGeometry(QtCore.QRect(330, 70, 113, 24))
        self.txtExpeditor.setObjectName(_fromUtf8("txtExpeditor"))

        self.lblExpeditor = QtGui.QLabel(self.grbDados)
        self.lblExpeditor.setGeometry(QtCore.QRect(330, 50, 71, 16))
        self.lblExpeditor.setObjectName(_fromUtf8("lblExpeditor"))

        self.lblEstado.setBuddy(self.txtEstado)
        self.lblComplemento.setBuddy(self.txtComplemento)
        self.lblCidade.setBuddy(self.txtCidade)
        self.lblRg.setBuddy(self.txtRg)
        self.lblBairro.setBuddy(self.txtBairro)
        self.lblEndereco.setBuddy(self.txtEndereco)
        self.lblNome.setBuddy(self.txtNome)
        self.lblNumero.setBuddy(self.txtNumero)
        self.lblCep.setBuddy(self.txtCep)
        self.lblMae.setBuddy(self.txtMae)
        self.lblCpf.setBuddy(self.txtCpf)
        self.lblPai.setBuddy(self.txtMae)

        self.retranslateUi(frmCadastroPessoaFisica)
        QtCore.QMetaObject.connectSlotsByName(frmCadastroPessoaFisica)
        frmCadastroPessoaFisica.setTabOrder(self.txtNome, self.txtCpf)
        frmCadastroPessoaFisica.setTabOrder(self.txtCpf, self.txtRg)
        frmCadastroPessoaFisica.setTabOrder(self.txtRg, self.txtExpeditor)
        frmCadastroPessoaFisica.setTabOrder(self.txtExpeditor, self.dateData)
        frmCadastroPessoaFisica.setTabOrder(self.dateData, self.radBtnMasculino)
        frmCadastroPessoaFisica.setTabOrder(self.radBtnMasculino, self.radBtnFeminino)
        frmCadastroPessoaFisica.setTabOrder(self.radBtnFeminino, self.txtEndereco)
        frmCadastroPessoaFisica.setTabOrder(self.txtEndereco, self.txtNumero)
        frmCadastroPessoaFisica.setTabOrder(self.txtNumero, self.txtComplemento)
        frmCadastroPessoaFisica.setTabOrder(self.txtComplemento, self.txtBairro)
        frmCadastroPessoaFisica.setTabOrder(self.txtBairro, self.txtCep)
        frmCadastroPessoaFisica.setTabOrder(self.txtCep, self.txtMae)
        frmCadastroPessoaFisica.setTabOrder(self.txtMae, self.txtPai)

    def retranslateUi(self, frmCadastroPessoaFisica):
        frmCadastroPessoaFisica.setWindowTitle(_translate("frmCadastroPessoaFisica", "Cadastro Pessoa Física", None))
        self.btnNovo.setToolTip(_translate("frmCadastroPessoaFisica", "Novo", None))
        self.btnNovo.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Botão para cadastrar uma novo registro da pessoa física</p></body></html>", None))
        self.btnNovo.setText(_translate("frmCadastroPessoaFisica", "Novo", None))
        self.btnSalvar.setToolTip(_translate("frmCadastroPessoaFisica", "Salvar", None))
        self.btnSalvar.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Botão para salvar um novo registro da pessoa física</p></body></html>", None))
        self.btnSalvar.setText(_translate("frmCadastroPessoaFisica", "Salvar", None))
        self.btnCancelar.setToolTip(_translate("frmCadastroPessoaFisica", "Cancelar", None))
        self.btnCancelar.setWhatsThis(_translate("frmCadastroPessoaFisica", "Botão para cancelar a operação ", None))
        self.btnCancelar.setText(_translate("frmCadastroPessoaFisica", "Cancelar", None))
        self.btnDeletar.setToolTip(_translate("frmCadastroPessoaFisica", "Deletar", None))
        self.btnDeletar.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Botão de deletar o registro da pessoa física</p></body></html>", None))
        self.btnDeletar.setText(_translate("frmCadastroPessoaFisica", "Deletar", None))
        self.btnEditar.setToolTip(_translate("frmCadastroPessoaFisica", "Editar", None))
        self.btnEditar.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Botão para salvar o registo editado da pessoa física</p></body></html>", None))
        self.btnEditar.setText(_translate("frmCadastroPessoaFisica", "Editar", None))
        self.lblPesquisar.setText(_translate("frmCadastroPessoaFisica", "[F12] Pesquisar", None))
        self.txtComplemento.setToolTip(_translate("frmCadastroPessoaFisica", "Complemento", None))
        self.txtComplemento.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Campo do complemento do endereço da pessoa física</p></body></html>", None))
        self.txtEstado.setToolTip(_translate("frmCadastroPessoaFisica", "Estado", None))
        self.txtEstado.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Campo do nome do estado onde fica localizado a cidade a pessoa física</p></body></html>", None))
        self.lblEstado.setText(_translate("frmCadastroPessoaFisica", "Estado", None))
        self.lblComplemento.setText(_translate("frmCadastroPessoaFisica", "Complemento", None))
        self.txtCidade.setToolTip(_translate("frmCadastroPessoaFisica", "Cidade", None))
        self.txtCidade.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Campo do nome da cidade onde fica localizado a pessoa física</p></body></html>", None))
        self.lblCidade.setText(_translate("frmCadastroPessoaFisica", "Cidade", None))
        self.txtCpf.setToolTip(_translate("frmCadastroPessoaFisica", "CPF", None))
        self.txtCpf.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Campo do numero do CPF da pessoa física</p></body></html>", None))
        self.txtCpf.setInputMask(_translate("frmCadastroPessoaFisica", "000.000.000-00; ", None))
        self.lblRg.setToolTip(_translate("frmCadastroPessoaFisica", "Expeditor", None))
        self.lblRg.setText(_translate("frmCadastroPessoaFisica", "RG", None))
        self.txtCep.setToolTip(_translate("frmCadastroPessoaFisica", "CEP", None))
        self.txtCep.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Campo do número do CEP da cidade onde fica localizada a pessoa física</p></body></html>", None))
        self.txtCep.setInputMask(_translate("frmCadastroPessoaFisica", "00000-000; ", None))
        self.txtNumero.setToolTip(_translate("frmCadastroPessoaFisica", "Número", None))
        self.txtNumero.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Campo do número do endereço da pessoa física</p></body></html>", None))
        self.txtNome.setToolTip(_translate("frmCadastroPessoaFisica", "Nome", None))
        self.txtNome.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Campo do nome completo da pessoa física</p></body></html>", None))
        self.lblBairro.setText(_translate("frmCadastroPessoaFisica", "Bairro", None))
        self.txtEndereco.setToolTip(_translate("frmCadastroPessoaFisica", "Endereço", None))
        self.txtEndereco.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Campo do endereço da pessoa jurídica</p></body></html>", None))
        self.lblEndereco.setText(_translate("frmCadastroPessoaFisica", "Endereço", None))
        self.txtRg.setToolTip(_translate("frmCadastroPessoaFisica", "RG", None))
        self.txtRg.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Campo do número do RG da pessoa física</p></body></html>", None))
        self.lblNome.setText(_translate("frmCadastroPessoaFisica", "Nome", None))
        self.txtBairro.setToolTip(_translate("frmCadastroPessoaFisica", "Bairro", None))
        self.txtBairro.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Campo do nome do bairro do endereço da pessoa física</p></body></html>", None))
        self.lblNumero.setText(_translate("frmCadastroPessoaFisica", "Numero", None))
        self.txtMae.setToolTip(_translate("frmCadastroPessoaFisica", "Mãe", None))
        self.txtMae.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Campo do nome da mãe da pessoa física</p></body></html>", None))
        self.lblCep.setText(_translate("frmCadastroPessoaFisica", "CEP", None))
        self.lblMae.setText(_translate("frmCadastroPessoaFisica", "Mãe", None))
        self.lblCpf.setText(_translate("frmCadastroPessoaFisica", "CPF", None))
        self.lblPai.setText(_translate("frmCadastroPessoaFisica", "Pai", None))
        self.txtPai.setToolTip(_translate("frmCadastroPessoaFisica", "Pai", None))
        self.txtPai.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Campo do nome do pai da pessoa física</p></body></html>", None))
        self.dateData.setToolTip(_translate("frmCadastroPessoaFisica", "Data", None))
        self.dateData.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Campo da data de nascimento da pessoa física</p></body></html>", None))
        self.lblDataNas.setText(_translate("frmCadastroPessoaFisica", "Data Nas.", None))
        self.grbSexo.setTitle(_translate("frmCadastroPessoaFisica", "Sexo", None))
        self.radBtnMasculino.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Item de escolha do sexo da pessoa física</p></body></html>", None))
        self.radBtnMasculino.setText(_translate("frmCadastroPessoaFisica", "Masculino", None))
        self.radBtnFeminino.setWhatsThis(_translate("frmCadastroPessoaFisica", "<html><head/><body><p>Item de escolha do sexo da pessoa física</p></body></html>", None))
        self.radBtnFeminino.setText(_translate("frmCadastroPessoaFisica", "Feminino", None))
        self.txtExpeditor.setToolTip(_translate("frmCadastroPessoaFisica", "Expeditor", None))
        self.txtExpeditor.setWhatsThis(_translate("frmCadastroPessoaFisica", "Campo do orgão expeditor do RG", None))
        self.lblExpeditor.setText(_translate("frmCadastroPessoaFisica", "Expeditor", None))


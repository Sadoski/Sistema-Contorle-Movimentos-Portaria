import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from classes.classMensagemBox import MensagemBox
from classes.classValidator import Validator
from controller.getSetContatoEmail import ContatoEmail
from controller.getSetContatoTelefone import ContatoTelefone
from controller.getSetFornecedor import Fornecedor
from controller.getSetPessoaFisica import PessoaFisica
from controller.getSetPessoaJuridica import PessoaJuridica
from dao.empresaDao import EmpresaDao
from dao.fornecedorDao import FornecedorDao
from dao.pesquisarPessoaFisicaDao import PesquisarPessoaFisicaDao
from dao.pesquisarPessoaJuridicaDao import PesquisarPessoaJuridicaDao
from telas.frmCadFornecedor import Ui_frmCadastroFornecedor
from telas.frmPesquisarFornecedor import Ui_frmPesquisarFornecedor
from telas.frmPesquisarPessoaFisicaJuridica import Ui_frmPesquisarPessoaFisicaJuridica


class CadastroFornecedores(QtGui.QDialog):
    def __init__(self, cadatra, cancela, deleta, edita):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_frmCadastroFornecedor()
        self.ui.setupUi(self)
        self.validator = Validator()
        self.mensagem = MensagemBox()
        self.idFornecedor = int()
        self.idPessoa = int()
        self.idPessoaFisica = int()
        self.idPessoaJurirdica = int()
        self.editar = False
        self.contatoAdd = []
        self.contatoRemove = []
        self.contatoAtualizar = []
        self.emailAdd = []
        self.emailRemove = []
        self.emailAtualizar = []
        self.cada = cadatra
        self.canc = cancela
        self.dele = deleta
        self.edit = edita

        self.ui.btnNovo.setEnabled(self.cada)

        self.ui.txtContatoEmail.setValidator(self.validator)
        self.ui.txtContatoTelefone.setValidator(self.validator)
        self.ui.txtEnderecoEmail.setValidator(self.validator)

        self.ui.btnNovo.clicked.connect(self.novo)
        self.ui.btnSalvar.clicked.connect(self.cadastro)
        self.ui.btnCancelar.clicked.connect(self.cancelar)
        self.ui.btnEditar.clicked.connect(self.atualizar)
        self.ui.btnDeletar.clicked.connect(self.deletar)
        self.ui.btnPesquisarEmpresa.clicked.connect(self.pesquisarPessoaFisicaJuridica)


        self.ui.txtCodigo.textChanged.connect(self.numberCodigo)
        self.ui.txtNumeroTelefone.textChanged.connect(self.numberTelefone)
        self.ui.txtObservacao.textChanged.connect(self.textEdite)

        self.ui.radBtnPessoaFisica.clicked.connect(self.botaoNovo)
        self.ui.radBtnPessoaJuridica.clicked.connect(self.botaoNovo)

        self.ui.btnAddTelefone.clicked.connect(self.addContatoTelefone)
        self.ui.btnRemoverTelefone.clicked.connect(self.delContatoTelefone)

        self.ui.btnAddEmail.clicked.connect(self.addContatoEmail)
        self.ui.btnRemoverEmail.clicked.connect(self.delContatoEmail)

        self.ui.txtCodigo.returnPressed.connect(self.setCliente)

        self.ui.txtCodigo.editingFinished.connect(self.setClienteEditFinish)


    def numberCodigo(self):
        if self.ui.txtCodigo.text().isnumeric() == False:
            self.ui.txtCodigo.backspace()

    def numberTelefone(self):
        if self.ui.txtNumeroTelefone.text().isnumeric() == False:
            self.ui.txtNumeroTelefone.backspace()

    def textEdite(self):
        if (len(self.ui.txtObservacao.toPlainText()) > 255):
            self.ui.txtObservacao.textCursor().deletePreviousChar()

    def novo(self):
        __pesDao = EmpresaDao()
        __retorno = __pesDao.pesquisaCodigoFrom()
        if __retorno != []:
            self.limparCampos()
            self.ui.grbTipoPessoa.setEnabled(self.cada)
            self.ui.radBtnPessoaFisica.setCheckable(self.cada)
            self.ui.radBtnPessoaJuridica.setCheckable(self.cada)
            self.ui.btnNovo.setEnabled(False)
            self.ui.btnSalvar.setEnabled(self.cada)
            self.ui.btnEditar.setEnabled(False)
            self.ui.btnCancelar.setEnabled(self.canc)
            self.ui.btnDeletar.setEnabled(False)
        else:
            MensagemBox().warning('Atenção', "Cadastre uma empresa primeiro")

    def botaoNovo(self):
        self.ui.txtCodigo.clear()
        self.ui.txtCnpj.clear()
        self.ui.txtInscricaoEstadua.clear()
        self.ui.txtRazaoSocial.clear()
        self.ui.txtFantasia.clear()

        self.ui.grbDadosPessoaFisicaJuridica.setEnabled(True)
        self.ui.tabWiAdicionais.setEnabled(True)

        self.deletarContatoTelefone()
        self.deletarContatoEmail()


    def cancelar(self):
        self.limparCampos()
        self.deletarContatoTelefone()
        self.deletarContatoEmail()
        self.desativarCampos()

    def desativarCampos(self):
        self.ui.grbDadosPessoaFisicaJuridica.setEnabled(False)
        self.ui.tabWiAdicionais.setEnabled(False)
        self.ui.btnNovo.setEnabled(self.cada)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(False)
        self.ui.btnDeletar.setEnabled(False)

    def botoesEditar(self):
        self.ui.grbDadosPessoaFisicaJuridica.setEnabled(False)
        self.limparCampos()
        self.ui.grbTipoPessoa.setEnabled(False)
        self.ui.radBtnPessoaFisica.setCheckable(self.edit)
        self.ui.radBtnPessoaJuridica.setCheckable(self.edit)
        self.ui.grbAtivo.setEnabled(self.edit)
        self.ui.radBtnAtivo.setCheckable(self.edit)
        self.ui.radBtnDesativo.setCheckable(self.edit)
        self.ui.tabWiAdicionais.setEnabled(self.edit)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(False)
        self.ui.btnEditar.setEnabled(self.edit)
        self.ui.btnCancelar.setEnabled(self.canc)
        self.ui.btnDeletar.setEnabled(self.dele)

    def ativarCampos(self):
        self.ui.grbDadosPessoaFisicaJuridica.setEnabled(self.cada)
        self.ui.tabWiAdicionais.setEnabled(self.cada)
        self.ui.btnNovo.setEnabled(False)
        self.ui.btnSalvar.setEnabled(self.cada)
        self.ui.btnEditar.setEnabled(False)
        self.ui.btnCancelar.setEnabled(self.canc)
        self.ui.btnDeletar.setEnabled(False)


    def limparCampos(self):
        self.idFornecedor = int()
        self.idPessoa = int()
        self.idPessoaFisica = int()
        self.idPessoaJurirdica = int()
        self.ui.grbTipoPessoa.setEnabled(True)
        self.ui.radBtnPessoaFisica.setCheckable(False)
        self.ui.radBtnPessoaJuridica.setCheckable(False)
        self.ui.grbTipoPessoa.setEnabled(False)
        self.ui.txtCodigo.setEnabled(True)
        self.ui.btnPesquisarEmpresa.setEnabled(True)
        self.editar = False
        self.ui.txtCodigo.clear()
        self.ui.txtCnpj.clear()
        self.ui.txtInscricaoEstadua.clear()
        self.ui.txtRazaoSocial.clear()
        self.ui.txtFantasia.clear()

        self.ui.txtObservacao.clear()

        self.ui.txtContatoTelefone.clear()
        self.ui.txtNumeroTelefone.clear()
        self.ui.txtEnderecoEmail.clear()
        self.ui.txtContatoEmail.clear()


        self.contatoAdd.clear()
        self.contatoRemove.clear()
        self.contatoAtualizar.clear()
        self.emailAdd.clear()
        self.emailRemove.clear()
        self.emailAtualizar.clear()

        self.deletarContatoTelefone()
        self.deletarContatoEmail()

        self.ui.tabWiAdicionais.setCurrentIndex(0)

        self.ui.radBtnAtivo.setCheckable(False)
        self.ui.radBtnDesativo.setCheckable(False)

    def deletarContatoTelefone(self):
        for i in reversed(range(self.ui.tabContatoTelefone.rowCount())):
            self.ui.tabContatoTelefone.removeRow(i)

    def deletarContatoEmail(self):
        for i in reversed(range(self.ui.tabContatoEmail.rowCount())):
            self.ui.tabContatoEmail.removeRow(i)

    def addContatoTelefone(self):

        if self.ui.txtContatoTelefone.text() != "" and self.ui.txtNumeroTelefone.text() != "":
            if len(self.ui.txtNumeroTelefone.text()) == 10 or len(self.ui.txtNumeroTelefone.text()) == 11:
                __contato = str(self.ui.txtContatoTelefone.text())
                __telefone = str(self.ui.txtNumeroTelefone.text())
                if self.editar == False:
                    add = [(__contato, __telefone)]
                    self.contatoAdd.append([__contato, __telefone])
                    self.inserirTabelaTelefone(add)

                elif self.editar == True:
                    add = [(__contato, __telefone)]
                    self.contatoAtualizar.append([__contato, __telefone])
                    self.inserirTabelaTelefone(add)

                self.ui.txtContatoTelefone.clear()
                self.ui.txtNumeroTelefone.clear()

                self.ui.txtContatoTelefone.setFocus()
            elif len(self.ui.txtNumeroTelefone.text()) >11:
                self.mensagem.warning( 'Mensagem', "Atenção contem digitos do telefone a mais")
            else:
                self.mensagem.warning( 'Mensagem', "Atenção esta faltando digitos do telefone")
        else:
            self.mensagem.warning( 'Mensagem', "Por favor preencha os campos de contato e telefone")

    def inserirTabelaTelefone(self, dado):

        linha = self.ui.tabContatoTelefone.rowCount()
        for info in dado:
            self.ui.tabContatoTelefone.insertRow(linha)
            __contato = info[0]
            __telefone = info[1]


            self.ui.tabContatoTelefone.setItem(linha, 0, QtGui.QTableWidgetItem(str(__contato)))
            self.ui.tabContatoTelefone.setItem(linha, 1, QtGui.QTableWidgetItem(str(__telefone)))


            linha += 1

    def cellClickTelefone(self):
        index = self.ui.tabContatoTelefone.currentRow()
        list=[]
        columcount = self.ui.tabContatoTelefone.columnCount()
        row = self.ui.tabContatoTelefone.currentItem().row()
        for x in range(0, columcount, 1):
            cell =self.ui.tabContatoTelefone.item(row, x).text()
            list.append(cell)

        if list in self.contatoAtualizar:
            self.contatoAtualizar.remove(list)
            self.ui.tabContatoTelefone.removeRow(index)
        else:
            self.ui.tabContatoTelefone.removeRow(index)
            if index >= 0:
                self.contatoRemove.append(self.contatoAdd[index])
                del self.contatoAdd[index]
            else:
                MensagemBox().warning( 'Mensagem',"Impossivel realizar essa ação, por favor selecione um item da lista para excluir")

    def delContatoTelefone(self):
        index = self.ui.tabContatoTelefone.currentRow()

        if self.editar == False:
            self.ui.tabContatoTelefone.removeRow(index)
            if index >= 0:
                del self.contatoAdd[index]
            else:
                MensagemBox().warning('Mensagem', "Impossivel realizar essa ação, por favor selecione um item da lista para excluir")
        elif self.editar == True:
            self.cellClickTelefone()

    def inserirTabelaEmail(self, dado):

        linha = self.ui.tabContatoEmail.rowCount()
        for info in dado:
            self.ui.tabContatoEmail.insertRow(linha)
            __contato = info[0]
            __email = info[1]

            self.ui.tabContatoEmail.setItem(linha, 0, QtGui.QTableWidgetItem(str(__contato)))
            self.ui.tabContatoEmail.setItem(linha, 1, QtGui.QTableWidgetItem(str(__email)))

            linha += 1

    def addContatoEmail(self):
        if self.ui.txtContatoEmail.text() != "" and self.ui.txtEnderecoEmail.text() != "":
                __contato = str(self.ui.txtContatoEmail.text())
                __email = str(self.ui.txtEnderecoEmail.text())
                if self.editar == False:
                    add = [(__contato, __email)]
                    self.emailAdd.append([__contato, __email])
                    self.inserirTabelaEmail(add)

                elif self.editar == True:
                    add = [(__contato, __email)]
                    self.emailAtualizar.append([__contato, __email])
                    self.inserirTabelaEmail(add)

                self.ui.txtContatoEmail.clear()
                self.ui.txtEnderecoEmail.clear()

                self.ui.txtContatoEmail.setFocus()
        else:
            self.mensagem.warning( 'Mensagem', "Por favor preencha os campos de contato e telefone")

    def cellClickEmail(self):
        index = self.ui.tabContatoEmail.currentRow()
        list = []
        columcount = self.ui.tabContatoEmail.columnCount()
        row = self.ui.tabContatoEmail.currentItem().row()
        for x in range(0, columcount, 1):
            cell = self.ui.tabContatoEmail.item(row, x).text()
            list.append(cell)

        if list in self.emailAtualizar:
            self.emailAtualizar.remove(list)
            self.ui.tabContatoEmail.removeRow(index)
        else:
            self.ui.tabContatoEmail.removeRow(index)
            if index >= 0:
                self.emailRemove.append(self.emailAdd[index])
                del self.emailAdd[index]
            else:
                MensagemBox().warning('Mensagem', "Impossivel realizar essa ação, por favor selecione um item da lista para excluir")


    def delContatoEmail(self):
        index = self.ui.tabContatoEmail.currentRow()

        if self.editar == False:
            self.ui.tabContatoEmail.removeRow(index)
            if index >= 0:
                del self.emailAdd[index]
            else:
                MensagemBox().warning('Mensagem', "Impossivel realizar essa ação, por favor selecione um item da lista para excluir")
        elif self.editar == True:
            self.cellClickEmail()

    def setCliente(self):
        cliente = FornecedorDao()
        pesDao = EmpresaDao()
        if self.ui.radBtnPessoaFisica.isChecked():
            cli = cliente.pesquisarFornecedorIdFisico(self.ui.txtCodigo.text())
            emp = pesDao.pesquisaEmpresaJuridica(self.ui.txtCodigo.text())
            if emp == []:
                if cli == []:
                    clien = cliente.pesquisarPessoaFisica(self.ui.txtCodigo.text())
                    if clien == []:
                        self.mensagem.warning('Mensagem', "Atenção não existe nenhum cadastro neste codigo")
                        self.ui.txtCnpj.clear()
                        self.ui.txtInscricaoEstadua.clear()
                        self.ui.txtRazaoSocial.clear()
                        self.ui.txtFantasia.clear()
                    else:
                        for empres in clien:
                            self.ui.txtCnpj.setText(str(empres[0]))
                            self.ui.txtInscricaoEstadua.setText(str(empres[1]))
                            self.ui.txtRazaoSocial.setText(str(empres[2]))
                            self.ui.txtFantasia.setText(str(empres[3]))
                else:
                    self.mensagem.warning( 'Mensagem', "Atenção já tem um cadastro deste cliente")
            else:
                self.mensagem.warning('Mensagem', "Atenção já tem um cadastro como empresa  não poder ser fornecedor")

        elif self.ui.radBtnPessoaJuridica.isChecked():
            cli = cliente.pesquisarFornecedorIdJuridico(self.ui.txtCodigo.text())
            emp = pesDao.pesquisaEmpresaJuridica(self.ui.txtCodigo.text())
            if emp == []:
                if cli == []:
                    clien = cliente.pesquisarPessoaJuridica(self.ui.txtCodigo.text())
                    if clien == []:
                        self.mensagem.warning('Mensagem', "Atenção não existe nenhum cadastro neste codigo")
                        self.ui.txtCnpj.clear()
                        self.ui.txtInscricaoEstadua.clear()
                        self.ui.txtRazaoSocial.clear()
                        self.ui.txtFantasia.clear()
                    else:
                        for empres in clien:
                            self.ui.txtCnpj.setText(str(empres[0]))
                            self.ui.txtInscricaoEstadua.setText(str(empres[1]))
                            self.ui.txtRazaoSocial.setText(str(empres[2]))
                            self.ui.txtFantasia.setText(str(empres[3]))
                else:
                    self.mensagem.warning( 'Mensagem', "Atenção já tem um cadastro deste cliente")
            else:
                self.mensagem.warning('Mensagem', "Atenção já tem um cadastro como empresa  não poder ser fornecedor")

    def setClienteEditFinish(self):
        cliente = FornecedorDao()
        pesDao = EmpresaDao()
        if self.ui.radBtnPessoaFisica.isChecked():
            cli = cliente.pesquisarFornecedorIdFisico(self.ui.txtCodigo.text())
            emp = pesDao.pesquisaEmpresaJuridica(self.ui.txtCodigo.text())
            if emp == []:
                if cli == []:
                    clien = cliente.pesquisarPessoaFisica(self.ui.txtCodigo.text())
                    if clien == []:
                        self.ui.txtCnpj.clear()
                        self.ui.txtInscricaoEstadua.clear()
                        self.ui.txtRazaoSocial.clear()
                        self.ui.txtFantasia.clear()
                    else:
                        for empres in clien:
                            self.ui.txtCnpj.setText(str(empres[0]))
                            self.ui.txtInscricaoEstadua.setText(str(empres[1]))
                            self.ui.txtRazaoSocial.setText(str(empres[2]))
                            self.ui.txtFantasia.setText(str(empres[3]))

        elif self.ui.radBtnPessoaJuridica.isChecked():
            cli = cliente.pesquisarFornecedorIdJuridico(self.ui.txtCodigo.text())
            emp = pesDao.pesquisaEmpresaJuridica(self.ui.txtCodigo.text())
            if emp == []:
                if cli == []:
                    clien = cliente.pesquisarPessoaJuridica(self.ui.txtCodigo.text())
                    if clien == []:
                        self.ui.txtCnpj.clear()
                        self.ui.txtInscricaoEstadua.clear()
                        self.ui.txtRazaoSocial.clear()
                        self.ui.txtFantasia.clear()
                    else:
                        for empres in clien:
                            self.ui.txtCnpj.setText(str(empres[0]))
                            self.ui.txtInscricaoEstadua.setText(str(empres[1]))
                            self.ui.txtRazaoSocial.setText(str(empres[2]))
                            self.ui.txtFantasia.setText(str(empres[3]))

    def pesquisarPessoaFisicaJuridica(self):
        self.dialogFisicoJuridico = QDialog(self)
        self.__pesquisarFisicaJuridica = Ui_frmPesquisarPessoaFisicaJuridica()
        self.__pesquisarFisicaJuridica.setupUi(self.dialogFisicoJuridico)
        self.colunasTabela()
        self.__pesquisarFisicaJuridica.txtPesquisar.setValidator(self.validator)

        self.__pesquisarFisicaJuridica.txtPesquisar.returnPressed.connect(self.pesquisarFisicoJuridico)

        self.__pesquisarFisicaJuridica.btnPesquisar.clicked.connect(self.pesquisarFisicoJuridico)

        self.__pesquisarFisicaJuridica.tabPesquisar.doubleClicked.connect(self.setarCamposFisicoJuridico)

        self.dialogFisicoJuridico.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.dialogFisicoJuridico.exec_()

    def colunasTabela(self):
        if self.ui.radBtnPessoaFisica.isChecked():
            self.__pesquisarFisicaJuridica.tabPesquisar.setColumnCount(18)
            self.__pesquisarFisicaJuridica.tabPesquisar.setRowCount(0)
            self.__pesquisarFisicaJuridica.tabPesquisar.setHorizontalHeaderLabels(["Cod.", "Nome", "Apelido", "CPF", "RG", "Expeditor", "UF", "Aniversario", "Sexo", "Mãe", "Pai", "Endereço", "Número", "Complemento", "Bairro", "Cidade", "Estado", "CEP"])
        elif self.ui.radBtnPessoaJuridica.isChecked():
            self.__pesquisarFisicaJuridica.tabPesquisar.setColumnCount(12)
            self.__pesquisarFisicaJuridica.tabPesquisar.setRowCount(0)
            self.__pesquisarFisicaJuridica.tabPesquisar.setHorizontalHeaderLabels(["Cod.", "Razão Social", "Fantasia", "CNPJ", "Ins. Estadual", "Endereço", "Número", "Complemento", "Bairro", "Cidade" , "Estado", "CEP"])


    def pesquisarFisicoJuridico(self):
        if self.__pesquisarFisicaJuridica.radBtnCodigo.isChecked():
            if self.ui.radBtnPessoaFisica.isChecked():
                __codigo = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaFisicaDao()
                __retorno = __pesDao.pesquisaCodigo(__codigo)
                self.setarTabelaPesquisaFisica(__retorno)
            elif self.ui.radBtnPessoaJuridica.isChecked():
                __codigo = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaJuridicaDao()
                __retorno = __pesDao.pesquisaCodigo(__codigo)
                self.setarTabelaPesquisaJuridico(__retorno)
        elif self.__pesquisarFisicaJuridica.radBtnRazaoSocial.isChecked():
            if self.ui.radBtnPessoaFisica.isChecked():
                __razao = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaFisicaDao()
                __retorno = __pesDao.pesquisaNome(__razao)
                self.setarTabelaPesquisaFisica(__retorno)
            elif self.ui.radBtnPessoaJuridica.isChecked():
                __razao = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaJuridicaDao()
                __retorno = __pesDao.pesquisaRazaoSocial(__razao)
                self.setarTabelaPesquisaJuridico(__retorno)

        elif self.__pesquisarFisicaJuridica.radBtnFantasia.isChecked():
            if self.ui.radBtnPessoaFisica.isChecked():
                __fantasia = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaFisicaDao()
                __retorno = __pesDao.pesquisaApelido(__fantasia)
                self.setarTabelaPesquisaFisica(__retorno)
            elif self.ui.radBtnPessoaJuridica.isChecked():
                __fantasia = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaJuridicaDao()
                __retorno = __pesDao.pesquisaFantasia(__fantasia)
                self.setarTabelaPesquisaJuridico(__retorno)
        elif self.__pesquisarFisicaJuridica.radBtnCnpj.isChecked():
            if self.ui.radBtnPessoaFisica.isChecked():
                __cnpj = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaFisicaDao()
                __retorno = __pesDao.pesquisaCpf(__cnpj)
                self.setarTabelaPesquisaFisica(__retorno)
            elif self.ui.radBtnPessoaJuridica.isChecked():
                __cnpj = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaJuridicaDao()
                __retorno = __pesDao.pesquisaCnpj(__cnpj)
                self.setarTabelaPesquisaJuridico(__retorno)

        elif self.__pesquisarFisicaJuridica.radBtnInsEstadual.isChecked():
            if self.ui.radBtnPessoaFisica.isChecked():
                __inscricao = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaFisicaDao()
                __retorno = __pesDao.pesquisaRg(__inscricao)
                self.setarTabelaPesquisaFisica(__retorno)
            elif self.ui.radBtnPessoaJuridica.isChecked():
                __inscricao = self.__pesquisarFisicaJuridica.txtPesquisar.text()
                __pesDao = PesquisarPessoaJuridicaDao()
                __retorno = __pesDao.pesquisaInsEstadual(__inscricao)
                self.setarTabelaPesquisaJuridico(__retorno)

        else:
            self.mensagem.warning( 'Atenção', "Selecione uma das opções de pesquisa")


    def setarTabelaPesquisaFisica(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarFisicaJuridica.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            nome = pesqui[1]
            apelido = pesqui[2]
            cpf = pesqui[3]
            rg = pesqui[4]
            expeditor = pesqui[5]
            uf = pesqui[6]
            aniversario = pesqui[7]
            sexo = pesqui[8]
            mae = pesqui[9]
            pai = pesqui[10]
            endereco = pesqui[11]
            numero = pesqui[12]
            complemento = pesqui[13]
            bairro = pesqui[14]
            cidade = pesqui[15]
            estado = pesqui[16]
            cep = pesqui[17]


            # preenchendo o grid de pesquisa
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(nome)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(apelido)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cpf)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(rg)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(expeditor)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(uf)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(aniversario)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(sexo)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(mae)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(pai)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(numero)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(complemento)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(cep)))

            linha += 1

    def setarTabelaPesquisaJuridico(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarFisicaJuridica.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            razao = pesqui[1]
            fantasia = pesqui[2]
            cnpj = pesqui[3]
            inscricao = pesqui[4]
            endereco = pesqui[5]
            numero = pesqui[6]
            complemento = pesqui[7]
            bairro = pesqui[8]
            cidade = pesqui[9]
            estado = pesqui[10]
            cep = pesqui[11]


            # preenchendo o grid de pesquisa
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(razao)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(fantasia)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(cnpj)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(inscricao)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(numero)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(complemento)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisarFisicaJuridica.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(cep)))

            linha += 1



    def setarCamposFisicoJuridico(self):
        fornecedor = FornecedorDao()
        if self.ui.radBtnPessoaFisica.isChecked():
            itens = []

            for item in self.__pesquisarFisicaJuridica.tabPesquisar.selectedItems():
                itens.append(item.text())

            codigo = str(itens[0])
            nome = str(itens[1])
            apelido = str(itens[2])
            cpf = str(itens[3])
            rg = str(itens[4])
            expeditor = str(itens[5])
            uf = str(itens[6])
            aniversario = str(itens[7])
            sexo = str(itens[8])
            endereco = str(itens[9])
            numero = str(itens[10])
            complemento = str(itens[11])
            bairro = str(itens[12])
            cidade = str(itens[13])
            estado = str(itens[14])
            cep = str(itens[15])

            if self.ui.radBtnPessoaFisica.isChecked():
                cli = fornecedor.pesquisarFornecedoresFisico(codigo)
                pesDao = EmpresaDao()
                emp = pesDao.pesquisaEmpresaJuridica(codigo)
                if emp == []:
                    if cli == []:
                        __dados = PessoaFisica(None, codigo, None, nome, apelido, cpf, rg, expeditor, uf, aniversario, sexo, endereco, numero, complemento, bairro, None, None, None, cidade, estado, cep)
                        self.setCamposFisicoJuridico(__dados)
                        self.dialogFisicoJuridico.close()
                    else:
                        MensagemBox().warning('Mensagem', "Atenção já tem um cadastro desta pessoa")
                else:
                    self.mensagem.warning('Mensagem', "Atenção já tem um cadastro como empresa  não poder ser fornecedor")

        elif self.ui.radBtnPessoaJuridica.isChecked():
            itens = []

            for item in self.__pesquisarFisicaJuridica.tabPesquisar.selectedItems():
                itens.append(item.text())


            codigo = str(itens[0])
            razao = str(itens[1])
            fantasia = str(itens[2])
            cnpj = str(itens[3])
            inscricao = str(itens[4])
            endereco = str(itens[5])
            numero = str(itens[6])
            complemento = str(itens[7])
            bairro = str(itens[8])
            cidade = str(itens[9])
            estado = str(itens[10])
            cep = str(itens[11])

            cli = fornecedor.pesquisarFornecedoresJuridico(codigo)
            pesDao = EmpresaDao()
            emp = pesDao.pesquisaEmpresaJuridica(codigo)
            if emp == []:
                if cli == []:
                    __dados = PessoaJuridica(None, codigo, None, razao, fantasia, cnpj, inscricao, endereco, numero, complemento, bairro, None, cidade, estado, cep, None)
                    self.setCamposFisicoJuridico(__dados)
                    self.dialogFisicoJuridico.close()
                else:
                    MensagemBox().warning('Mensagem', "Atenção já tem um cadastro desta pessoa")
            else:
                self.mensagem.warning('Mensagem', "Atenção já tem um cadastro como empresa  não poder ser fornecedor")

    def setCamposFisicoJuridico(self, campos):
        if self.ui.radBtnPessoaFisica.isChecked():
            self.ui.txtCodigo.setText(campos.getIdPesFisica)
            self.ui.txtCnpj.setText(campos.getCpf)
            self.ui.txtInscricaoEstadua.setText(campos.setRg)
            self.ui.txtFantasia.setText(campos.getApelido)
            self.ui.txtRazaoSocial.setText(campos.getNome)
        elif self.ui.radBtnPessoaJuridica.isChecked():
            self.ui.txtCodigo.setText(campos.getIdPesJuridica)
            self.ui.txtCnpj.setText(campos.getCnpj)
            self.ui.txtInscricaoEstadua.setText(campos.setInscricao)
            self.ui.txtFantasia.setText(campos.getFantasia)
            self.ui.txtRazaoSocial.setText(campos.getRazao)

    def cadastrarTelefone(self):
        cli = FornecedorDao()
        i = 0
        for lista in self.contatoAdd:
            a = self.contatoAdd[i]

            contato = a[0]
            telefone = a[1]

            __descricao = ContatoTelefone(None, contato, telefone, self.idFornecedor)
            cli.cadastrarTelefone(__descricao)
            id = cli.ultimoRegistro()
            cli.cadastrarTelefoneFornecedor(id, self.idFornecedor)

            i += 1

    def cadastrarEmail(self):
        cli = FornecedorDao()
        i = 0
        for lista in self.emailAdd:
            a = self.emailAdd[i]

            contato = a[0]
            email = a[1]

            __descricao = ContatoEmail(None, contato, email, self.idFornecedor)
            cli.cadastrarEmail(__descricao)
            id = cli.ultimoRegistro()
            cli.cadastrarEmailFornecedor(id, self.idFornecedor)

            i += 1

    def cadastro(self):
        __pesDao = EmpresaDao()
        __retorno = __pesDao.pesquisaCodigoFrom()
        if __retorno != []:
            if self.ui.txtCodigo.text() != '' and self.ui.txtCnpj.text() != '' and self.ui.txtInscricaoEstadua.text() != '' and self.ui.txtFantasia.text() != '' and self.ui.txtRazaoSocial.text() != '':
                fornecedorDao = FornecedorDao()
                if self.ui.radBtnPessoaFisica.isChecked():
                    idPessoa = fornecedorDao.pesquisarPessoaFis(self.ui.txtCodigo.text())
                    fornecedor = Fornecedor(None, idPessoa, self.ui.txtCodigo.text(), None, None, None, None, None, self.ui.txtObservacao.toPlainText(), 1, None)
                    fornecedorDao.cadastrarFornecedorFisico(fornecedor)
                    self.idFornecedor = fornecedorDao.ultimoRegistro()


                    if self.contatoAdd != []:
                        self.cadastrarTelefone()

                    if self.emailAdd != []:
                        self.cadastrarEmail()

                    self.cancelar()

                elif self.ui.radBtnPessoaJuridica.isChecked():
                    idPessoa = fornecedorDao.pesquisarPessoaJur(self.ui.txtCodigo.text())
                    fornecedor = Fornecedor(None, idPessoa, None, self.ui.txtCodigo.text(), None, None, None, None, self.ui.txtObservacao.toPlainText(), 1, None)
                    fornecedorDao.cadastrarFornecedorJuridica(fornecedor)
                    self.idFornecedor = fornecedorDao.ultimoRegistro()

                    if self.contatoAdd != []:
                        self.cadastrarTelefone()

                    if self.emailAdd != []:
                        self.cadastrarEmail()

                    self.cancelar()

            else:
                self.mensagem.warning( 'Atenção', "Preencha os campos obrigatorio")

    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == (QtCore.Qt.Key_F12):
            self.dialog = QDialog(self)
            self.__pesquisarFornecedor = Ui_frmPesquisarFornecedor()
            self.__pesquisarFornecedor.setupUi(self.dialog)

            self.__pesquisarFornecedor.txtPesquisar.setValidator(self.validator)

            self.__pesquisarFornecedor.txtPesquisar.returnPressed.connect(self.pesquisar)

            self.__pesquisarFornecedor.btnPesquisar.clicked.connect(self.pesquisar)

            self.__pesquisarFornecedor.tabPesquisar.doubleClicked.connect(self.setarCampos)

            self.dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.dialog.exec_()

    def pesquisar(self):
        __pesDao = FornecedorDao()
        if self.__pesquisarFornecedor.radBtnCodigo.isChecked():
            __codigo = self.__pesquisarFornecedor.txtPesquisar.text()
            __retorno = __pesDao.pesquisaCodigoFisica(__codigo)
            self.setarTabelaPesquisaEditar(__retorno)

        elif self.__pesquisarFornecedor.radBtnRazaoSocial.isChecked():
            __razao = self.__pesquisarFornecedor.txtPesquisar.text()
            __retorno = __pesDao.pesquisarNomeFisica(__razao)
            self.setarTabelaPesquisaEditar(__retorno)

        elif self.__pesquisarFornecedor.radBtnFantasia.isChecked():
            __fantasia = self.__pesquisarFornecedor.txtPesquisar.text()
            __retorno = __pesDao.pesquisaApelidoFisica(__fantasia)
            self.setarTabelaPesquisaEditar(__retorno)

        elif self.__pesquisarFornecedor.radBtnCnpj.isChecked():
            __cnpj = self.__pesquisarFornecedor.txtPesquisar.text()
            __retorno = __pesDao.pesquisaCpfFisica(__cnpj)
            self.setarTabelaPesquisaEditar(__retorno)

        elif self.__pesquisarFornecedor.radBtnInsEstadual.isChecked():
            __inscricao = self.__pesquisarFornecedor.txtPesquisar.text()
            __retorno = __pesDao.pesquisaRgFisica(__inscricao)
            self.setarTabelaPesquisaEditar(__retorno)

        else:
            self.mensagem.warning('Atenção', "Selecione uma das opções de pesquisa")

    def setarTabelaPesquisaEditar(self, __retorno):
        qtde_registros = len(__retorno)
        self.__pesquisarFornecedor.tabPesquisar.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            # capturando os dados da tupla

            codigo = pesqui[0]
            tipo = pesqui[1]
            nome = pesqui[2]
            apelido = pesqui[3]
            cpf = pesqui[4]
            rg = pesqui[5]
            expeditor = pesqui[6]
            uf = pesqui[7]
            aniversario = pesqui[8]
            endereco = pesqui[9]
            numero = pesqui[10]
            complemento = pesqui[11]
            bairro = pesqui[12]
            cidade = pesqui[13]
            estado = pesqui[14]
            cep = pesqui[15]
            site = pesqui[16]
            obs = pesqui[17]
            if pesqui[18] == 1:
                situacao = "Ativo"
            else:
                situacao = "Inativo"


            # preenchendo o grid de pesquisa
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 0, QtGui.QTableWidgetItem(str(codigo)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 1, QtGui.QTableWidgetItem(str(tipo)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 2, QtGui.QTableWidgetItem(str(nome)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 3, QtGui.QTableWidgetItem(str(apelido)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 4, QtGui.QTableWidgetItem(str(cpf)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 5, QtGui.QTableWidgetItem(str(rg)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 6, QtGui.QTableWidgetItem(str(expeditor)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 7, QtGui.QTableWidgetItem(str(uf)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 8, QtGui.QTableWidgetItem(str(aniversario)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 9, QtGui.QTableWidgetItem(str(endereco)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 10, QtGui.QTableWidgetItem(str(numero)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 11, QtGui.QTableWidgetItem(str(complemento)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 12, QtGui.QTableWidgetItem(str(bairro)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 13, QtGui.QTableWidgetItem(str(cidade)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 14, QtGui.QTableWidgetItem(str(estado)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 15, QtGui.QTableWidgetItem(str(cep)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 16, QtGui.QTableWidgetItem(str(site)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 17, QtGui.QTableWidgetItem(str(obs)))
            self.__pesquisarFornecedor.tabPesquisar.setItem(linha, 18, QtGui.QTableWidgetItem(str(situacao)))

            linha += 1

    def setarCampos(self):
        clienteDao = FornecedorDao()
        itens = []

        for item in self.__pesquisarFornecedor.tabPesquisar.selectedItems():
            itens.append(item.text())

        codigo = str(itens[0])
        tipo = str(itens[1])
        razao = str(itens[2])
        fantasia = str(itens[3])
        cnpj = str(itens[4])
        insEstadual = str(itens[5])
        expeditor = str(itens[6])
        uf = str(itens[7])
        aniversario = str(itens[8])
        endereco = str(itens[9])
        numero = str(itens[10])
        complemento = str(itens[11])
        bairro = str(itens[12])
        cidade = str(itens[13])
        estado = str(itens[14])
        cep = str(itens[15])
        site = str(itens[16])
        obs = str(itens[17])
        if itens[18] == 'Ativo':
            situacao = True
        else:
            situacao = False

        idPessoa = clienteDao.pesquisarPessoaCodigo(codigo)
        idPessoaFisico = clienteDao.pesquisarPessoaFisicaId(str(idPessoa))
        idPessoaJuridica = clienteDao.pesquisarPessoaJuridicaId(idPessoa)

        __dados = Fornecedor(codigo, idPessoa, idPessoaFisico, idPessoaJuridica, cnpj, insEstadual, fantasia, razao, obs, situacao, tipo)
        self.botoesEditar()
        self.setCampos(__dados)
        self.pesquisarTelefone(codigo)
        self.pesquisaEmail(codigo)
        self.dialog.close()

    def setCampos(self, campos):
        self.ui.txtCodigo.setEnabled(False)
        self.ui.btnPesquisarEmpresa.setEnabled(False)

        if campos.getTipo == "PESSOA FÍSICA":
            self.ui.radBtnPessoaFisica.setChecked(True)
            self.idPessoaFisica = campos.getIdPessoaFisica
            self.ui.txtCodigo.setText(str(campos.getIdPessoaFisica))
        elif campos.getTipo == "PESSOA JURÍDICA":
            self.idPessoaJurirdica = campos.getIdPessoaJuridica
            self.ui.radBtnPessoaJuridica.setChecked(True)
            self.ui.txtCodigo.setText(str(campos.getIdPessoaJuridica))

        self.idFornecedor = int(campos.getIdFornecedor)
        self.idPessoa = int(campos.getIdPessoa)

        self.ui.txtCnpj.setText(campos.getCnpj)
        self.ui.txtInscricaoEstadua.setText(campos.getInscricaoEstadual)
        self.ui.txtFantasia.setText(campos.getFantasia)
        self.ui.txtRazaoSocial.setText(campos.getRazaoSocial)

        if campos.getSituacao == True:
            self.ui.radBtnAtivo.setChecked(True)
        else:
            self.ui.radBtnDesativo.setChecked(True)

        self.ui.txtObservacao.setText(str(campos.getObservacao))
        self.editar = True

    def pesquisarTelefone(self, campos):
        empresaDao = FornecedorDao()
        id = empresaDao.pesquisaTelefone(campos)
        if id != []:
            self.setTabelaTelefone(id)

    def setTabelaTelefone(self, __retorno):
        qtde_registros = len(__retorno)
        self.ui.tabContatoTelefone.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            idContato = pesqui[0]
            contato = pesqui[1]
            telefone = pesqui[2]


            self.ui.tabContatoTelefone.setItem(linha, 0, QtGui.QTableWidgetItem(str(contato)))
            self.ui.tabContatoTelefone.setItem(linha, 1, QtGui.QTableWidgetItem(str(telefone)))

            lista = (idContato, contato, telefone)
            self.contatoAdd.append(lista)


            linha += 1

    def pesquisaEmail(self, campos):
        empresaDao = FornecedorDao()
        id = empresaDao.pesquisaEmail(campos)
        if id != []:

            self.setTabelaEmail(id)

    def setTabelaEmail(self, __retorno):
        qtde_registros = len(__retorno)
        self.ui.tabContatoEmail.setRowCount(qtde_registros)

        linha = 0
        for pesqui in __retorno:
            idEmail = pesqui[0]
            contato = pesqui[1]
            email = pesqui[2]

            self.ui.tabContatoEmail.setItem(linha, 0, QtGui.QTableWidgetItem(str(contato)))
            self.ui.tabContatoEmail.setItem(linha, 1, QtGui.QTableWidgetItem(str(email)))

            lista = (idEmail, contato, email)
            self.emailAdd.append(lista)

            linha += 1

    def deletarTelefone(self):
        emp = FornecedorDao()
        i = 0
        for lista in self.contatoRemove :
            a = self.contatoRemove[i]

            idTelefone = int(a[0])

            emp.deletarTelefone(idTelefone, self.idFornecedor)
            pesquisa = emp.pesquisaTelefoneFornecedor(idTelefone, self.idFornecedor)
            if pesquisa == "":
                emp.deletarContatoTelefone(idTelefone)

            i += 1

    def deletarEmail(self):
        emp = FornecedorDao()
        i = 0
        for lista in self.emailRemove:
            a = self.emailRemove[i]

            idEmail = a[0]

            emp.deletarEmail(idEmail, self.idFornecedor)
            pesquisa = emp.pesquisaEmailFornecedor(idEmail, self.idFornecedor)
            if pesquisa == "":
                emp.deletarContatoEmail(idEmail)

            i += 1

    def atualizaTelefone(self):
        emp = FornecedorDao()
        i = 0
        for lista in self.contatoAtualizar:
            a = self.contatoAtualizar[i]

            contato = a[0]
            telefone = a[1]

            __descricao = ContatoTelefone(None, contato, telefone, self.idFornecedor)
            emp.cadastrarTelefone(__descricao)
            id = emp.ultimoRegistro()
            emp.cadastrarTelefoneFornecedor(id, self.idFornecedor)

            i += 1

    def atualizaEmail(self):
        emp = FornecedorDao()
        i = 0
        for lista in self.emailAtualizar:
            a = self.emailAtualizar[i]

            contato = a[0]
            email = a[1]

            __descricao = ContatoEmail(None, contato, email, self.idFornecedor)
            emp.cadastrarEmail(__descricao)
            id = emp.ultimoRegistro()
            emp.cadastrarEmailFornecedor(id, self.idFornecedor)

            i += 1

    def atualizar(self):
        if self.contatoRemove  != []:
            self.deletarTelefone()

        if self.emailRemove != []:
            self.deletarEmail()

        if self.contatoAtualizar != []:
            self.atualizaTelefone()

        if self.emailAtualizar != []:
            self.atualizaEmail()


        if self.ui.radBtnAtivo.isChecked():
            ativo = 1
        elif self.ui.radBtnDesativo.isChecked():
            ativo = 0

        empresaDao = FornecedorDao()
        empresa = Fornecedor(self.idFornecedor, self.idPessoa, self.idPessoaFisica, self.idPessoaJurirdica, self.ui.txtCnpj.text(), self.ui.txtInscricaoEstadua.text(), self.ui.txtFantasia.text(), self.ui.txtRazaoSocial.text(), self.ui.txtObservacao.toPlainText(), ativo, None)
        empresaDao.atualizarFornecedor(empresa)

        self.cancelar()

    def deletar(self):
        fisicaDao = FornecedorDao()
        desca = fisicaDao.pesquisarTabelaDesca(str(self.idFornecedor))
        nf = fisicaDao.pesquisarTabelaNf(str(self.idFornecedor))

        if desca == [] or nf == []:
            try:
                _fromUtf8 = QtCore.QString.fromUtf8
            except AttributeError:
                def _fromUtf8(s):
                    return s

            self.msgBox = QtGui.QMessageBox()
            self.msgBox.setWindowTitle('Menssagem')
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(_fromUtf8("./imagens/question.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.msgBox.setWindowIcon(icon)
            self.msgBox.setIconPixmap(QtGui.QPixmap(_fromUtf8("./imagens/icon-question.png")))
            self.msgBox.setText("Tem certeza que deseja excluir esse registro")
            btnSim = QtGui.QPushButton('Sim')
            self.msgBox.addButton(btnSim, QtGui.QMessageBox.YesRole)
            btnNao = QtGui.QPushButton('Não')
            self.msgBox.addButton(btnNao, QtGui.QMessageBox.NoRole)
            btnSim.clicked.connect(self.simDeletar)
            btnNao.clicked.connect(self.fechar)
            btnNao.setFocus()
            self.msgBox.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.msgBox.exec_()
        else:
            MensagemBox().warning('Atenção', 'Impossivel fazer essa operação, pois essa pessoa esta relacionada com outro formulario')

    def simDeletar(self):
            motoDao = FornecedorDao()
            codigo = self.idFornecedor
            a = motoDao.deletarFornecedor(str(codigo))
            if self.contatoAdd != []:
                self.deletarTelefoneFrom()

            if self.emailAdd != []:
                self.deletarEmailFrom()

            if self.contatoRemove != []:
                self.deletarTelefone()

            if self.emailRemove != []:
                self.deletarEmail()

            if a  == True:
                MensagemBox().informacao('Mensagem', 'Cadastro deletar com sucesso!')
                self.desativarCampos()
            else:
                MensagemBox().critico('Erro', 'Erro ao deletar as informações no banco de dados')

            self.cancelar()
            self.msgBox.close()

    def fechar(self):
        self.msgBox.close()

    def deletarTelefoneFrom(self):
        emp = FornecedorDao()
        i = 0
        for lista in self.contatoAdd :
            a = self.contatoAdd[i]

            idTelefone = int(a[0])

            emp.deletarTelefone(idTelefone, str(self.idFornecedor))
            pesquisa = emp.pesquisaTelefoneFornecedor(idTelefone, str(self.idFornecedor))
            if pesquisa == "":
                emp.deletarContatoTelefone(idTelefone)

            i += 1

    def deletarEmailFrom(self):
        emp = FornecedorDao()
        i = 0
        for lista in self.emailAdd:
            a = self.emailAdd[i]

            idEmail = a[0]

            emp.deletarEmail(idEmail, str(self.idFornecedor))
            pesquisa = emp.pesquisaEmailFornecedor(idEmail, str(self.idFornecedor))
            if pesquisa == "":
                emp.deletarContatoEmail(idEmail)

            i += 1
import json
import os
import psycopg2

from flask import Flask

#app = Flask(__name__)
#Diretorio onde os arquivos json estão salvos
path = "C:\\Users\\willi\\Documents\\lbd\\candidatos"


#@app.route('/politiciansdata')
def divudacaoconta():

    arquivos = listarArquivos()
    return save(arquivos)

#le os arquivos e os retorna em formato mapeado
def lerJson(arquivo):
    with open(path + "\\" + arquivo,'r',encoding='utf8') as f:
        return json.load(f)

#lista os arquivos da pasta para poder importar
def listarArquivos():
    for _,_, arquivo in os.walk(path):
        return arquivo

#faz a magia
def save(arquivos):
    try:
        connection = psycopg2.connect(user="postgres",password="minhasenha",host="localhost",port="5433",database="trabalholbd")
                                                                #sua senha                                    e nome do db

        cursor = connection.cursor()
        for arquivo in arquivos:
            body = lerJson(arquivo)
            sql = """INSERT INTO candidatos(
                    id, nomeurna, 
                    numero,idcandidatosuperior, 
                    nomecompleto, descricaosexo, 
                    datadenascimento, tituloeleitor, 
                    cpf, descricaoestadocivil, 
                    descricaocorraca, descricaosituacao,
                    nacionalidade, grauinstrucao,
                    ocupacao, gastocampanha1t, 
                    gastocampanha2t, sgufnascimento, 
                    nomemunicipionascimento, localcandidatura, 
                    ufcandidatura,  ufsuperiorcandidatura, 
                    dataultimaatualizacao,  fotourl, 
                    fotodataultimaatualizacao, descricaototalizacao, 
                    nomecoligacao, composicaocoligacao, 
                    numeroprocessodrap, numeroprocessodrapencrypt, 
                    numeroprocesso, numeroprocessoencrypt,
                    numeroprocessoprestcontas, numeroprocessoprestcontasencrypt, 
                    numeroprotocolo, idcargo, 
                    idpartido, totaldebens, 
                    id_eleicao_candidato, 
                    motivos, codigosituacaocandidato, 
                    descricaosituacaocandidato, st_substituido, 
                    descricaonaturalidade, st_motivo_ausencia_requisito, 
                    st_motivo_conduta_vedada, cnpjcampanha, gastocampanha, 
                    st_motivo_abuso_poder, st_motivo_compra_voto, 
                    ds_motivo_outros, st_motivo_gasto_ilicito, 
                    st_motivo_ind_partido, st_motivo_ficha_limpa, 
                    st_divulga_arquivos, st_divulga_bens, 
                    st_divulga, st_reeleicao)
                    VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            insert = (body.get("id"), body.get("nomeUrna"),
                      body.get("numero"), body.get("idCandidatoSuperior"),
                      body.get("nomeCompleto"), body.get("descricaoSexo"),
                      body.get("dataDeNascimento"), body.get("tituloEleitor"),
                      body.get("cpf"), body.get("descricaoEstadoCivil"),
                      body.get("descricaoCorRaca"), body.get("descricaoSituacao"),
                      body.get("nacionalidade"), body.get("grauInstrucao"),
                      body.get("ocupacao"), body.get("gastoCampanha1T"),
                      body.get("gastoCampanha2T"), body.get("sgUfNascimento"),
                      body.get("nomeMunicipioNascimento"), body.get("localCandidatura"),
                      body.get("ufCandidatura"), body.get("ufSuperiorCandidatura"),
                      body.get("dataUltimaAtualizacao"), body.get("fotoUrl"),body.get("fotoDataUltimaAtualizacao"),
                      body.get("descricaoTotalizacao"), body.get("nomeColigacao"),
                      body.get("composicaoColigacao"), body.get("numeroProcessoDrap"),
                      body.get("numeroProcessoDrapEncrypt"), body.get("numeroProcesso"),
                      body.get("numeroProcessoEncrypt"), body.get("numeroProcessoPrestContas"),
                      body.get("numeroProcessoPrestContasEncrypt"), body.get("numeroProtocolo"),
                      body.get("cargo").get("codigo"), body.get("partido").get("numero"),
                      body.get("totalDeBens"), body.get("eleicao").get("id"),
                      body.get("motivos"),
                      body.get("codigoSituacaoCandidato"), body.get("descricaoSituacaoCandidato"),
                      body.get("st_SUBSTITuido"), body.get("descricaoNaturalidade"),
                      body.get("st_MOTIVO_AUSENCIA_REQUISITO"), body.get("st_MOTIVO_CONDUTA_VEDADA"),
                      body.get("cnpjcampanha"), body.get("gastoCampanha"),
                      body.get("st_MOTIVO_ABUSO_PODER"), body.get("st_MOTIVO_COMPRA_VOTO"),
                      body.get("ds_MOTIVO_OUTROS"), body.get("st_MOTIVO_GASTO_ILICITO"),
                      body.get("st_MOTIVO_IND_PARTIDO"), body.get("st_MOTIVO_FICHA_LIMPA"),
                      body.get("st_DIVULGA_ARQUIVOS"), body.get("st_DIVULGA_BENS"),
                      body.get("st_DIVULGA"), body.get("st_REELEICAO"))
            cursor.execute(sql,insert)
            connection.commit()


            cargo = body.get("cargo")
            sql = """INSERT INTO public.candidato_cargo(
                    id_candidato, id_cargo, sigla, codsuperior, titular, contagem)
                    VALUES (%s, %s, %s, %s, %s, %s)"""
            insert = (body.get("id"),cargo.get("codigo"),cargo.get("sigla"),cargo.get("codSuperior"),cargo.get("titular"),cargo.get("contagem"))
            cursor.execute(sql,insert)

            connection.commit()

            email = body.get("emails")
            if(email):
                for em in email:
                    sql = """INSERT INTO emails(
                            email, id_candidato_email)
                            VALUES (%s, %s)"""
                    insert = (em,body.get("id"))
                    cursor.execute(sql,insert)
                    connection.commit()

            sites = body.get("sites")
            if (sites):
                for st in sites:
                    sql = """INSERT INTO sites(
                                        site, id_candidato_site)
                                        VALUES (%s, %s)"""
                    insert = (st, body.get("id"))
                    cursor.execute(sql, insert)
                    connection.commit()

            vices = body.get("vices")
            if(vices):
                for vice in vices:
                    sql = """INSERT INTO vice(
                            id_candidato_vice, composicaocoligacao, 
                            ds_cargo, dt_ultima_atualizacao, 
                            nm_candidato, nm_partido, nm_urna, 
                            nomecoligacao, nr_candidato, 
                            sg_partido, sg_ue, 
                            situacaocandidato, sq_candidato, 
                            sq_candidato_superior, sq_eleicao, 
                            stregistro, urlfoto)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

                    insert = (body.get("id"),vice.get("composicaoColigacao"),
                              vice.get("ds_CARGO"),vice.get("dt_ULTIMA_ATUALIZACAO"),
                              vice.get("nm_CANDIDATO"),vice.get("nm_PARTIDO"),
                              vice.get("nm_URNA"),vice.get("nomeColigacao"),
                              vice.get("nr_CANDIDATO"),vice.get("sg_PARTIDO"),
                              vice.get("sg_UE"),vice.get("situacaoCandidato"),
                              vice.get("sq_CANDIDATO"),vice.get("sq_CANDIDATO_SUPERIOR"),
                              vice.get("sq_ELEICAO"),vice.get("stRegistro"),vice.get("urlFoto"))

                    cursor.execute(sql, insert)
                    connection.commit()

            eleicoesanteriores = body.get("eleicoesAnteriores")
            if(eleicoesanteriores):
                for anterior in eleicoesanteriores:
                    sql = """INSERT INTO eleicoesanteriores(
                             cargo, ideleicao, 
                             id_candidato_eleicoes_anteriores, local, 
                             nomecandidato, nomeurna, 
                             nrano, partido, 
                             sgue, situacaototalizacao, 
                             txtlink)
                            VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

                    insert = (anterior.get("cargo"), anterior.get("id"), body.get("id"),anterior.get("local"),
                              anterior.get("nomeCandidato"), anterior.get("nomeUrna"),
                              anterior.get("nrAno"), anterior.get("partido"),
                              anterior.get("sgUe"), anterior.get("situacaoTotalizacao"),
                              anterior.get("txtLink"))

                    cursor.execute(sql, insert)
                    connection.commit()

            bens = body.get("bens")
            if (bens):
                for ben in bens:
                    sql = """INSERT INTO bens(
                                dataultimaatualizacao, descricao, 
                                descricaodetipodebem, ordem, 
                                valor, id_candidato_bens)
                             VALUES ( %s, %s, %s, %s, %s, %s);"""

                    insert = (ben.get("dataUltimaAtualizacao"), ben.get("descricao"),
                              ben.get("descricaoDeTipoDeBem"), ben.get("ordem"),
                              ben.get("valor"),body.get("id"))

                    cursor.execute(sql, insert)
                    connection.commit()


            eleicao = body.get("eleicao")
            if(eleicao):
                sql = """INSERT INTO eleicao(
                             id, siglauf, 
                            localidadesgue, ano, 
                            codigo, nomeeleicao, 
                            tipoeleicao, turno, 
                            tipoabrangencia, dataeleicao, 
                            codsituacaoeleicao, descricaosituacaoeleicao, 
                            descricaoeleicao, id_candidato)
                            VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

                insert = (eleicao.get("id"), body.get("id"), eleicao.get("siglaUF"), eleicao.get("localidadeSgUe"),
                          eleicao.get("ano"), eleicao.get("codigo"),
                          eleicao.get("nomeEleicao"), eleicao.get("tipoEleicao"),
                          eleicao.get("turno"), eleicao.get("tipoAbrangencia"),
                          eleicao.get("dataEleicao"),eleicao.get("codSituacaoEleicao"),
                          eleicao.get("descricaoSituacaoEleicao"),eleicao.get("descricaoEleicao"))

                cursor.execute(sql, insert)
                connection.commit()


            arquivos = body.get("arquivos")
            if(arquivos):
                for arquivo in arquivos:
                    sql = """INSERT INTO arquivos(
                                nome, url, 
                                tipo, codtipo, 
                                fullfilepath, fileinputstream, 
                                filebytearray, id_candidato_arquivos)
                             VALUES ( %s, %s, %s, %s, %s, %s, %s, %s);"""

                    insert = (arquivo.get("nome"), arquivo.get("url"),arquivo.get("tipo"),
                              arquivo.get("codTipo"), arquivo.get("fullFilePath"),
                              arquivo.get("fileInputStream"), arquivo.get("fileByteArray"),
                              body.get("id"))

                    cursor.execute(sql, insert)
                    connection.commit()

            substituto = body.get("substituto")
            if(substituto):
                sql = """INSERT INTO substituto(
                             sqeleicao, sqcandidato, 
                             sgue, nrano, 
                             nmcandidato, url, 
                             id_Candidato)
                            VALUES ( %s, %s, %s, %s, %s, %s, %s);"""

                insert = (substituto.get("sqEleicao"), substituto.get("sqCandidato"), substituto.get("sgUe"),
                          substituto.get("nrAno"), substituto.get("nmCandidato"),
                          substituto.get("url"),body.get("id"))

                cursor.execute(sql, insert)
                connection.commit()

            print("Nome: " + body.get("nomeUrna"))

    except psycopg2.Error as error:
        if(connection):
            return "Falha na conexão com DataBase" + error

    finally:
        if(connection):
            cursor.close()
            connection.close()
            return "OK"


if __name__ == '__main__':
    divudacaoconta()
    #app.run()

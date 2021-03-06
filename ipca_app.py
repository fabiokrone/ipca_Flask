import pandas as pd
from flask import Flask, render_template, redirect, session
from flask_bootstrap import Bootstrap

ipca_app = Flask(__name__)
Bootstrap(ipca_app)

@ipca_app.route('/', methods=("POST", "GET"))
def index():
   
    return render_template('index.html', ipca_12=ipca(),tables=html_table() )
    
def ipca():
    #Lendo o arquivo
    data = pd.read_excel ('ipca_com_tratativa.xlsx') 

    #Pegando as últimas 12 linhas do df
    df = pd.DataFrame(data, columns= ['valor']).iloc[-12:]

    #Convertendo o tipo de dado para numeric
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce')

    #Aplicando o método sum para pegar o acumulado 12m
    ipca = df.sum()

    #Apresentar apeans 2 casas decimais após a vírgula
    ipca_12m = str(round(ipca[0], 2))
    
    return ipca_12m
    
def html_table():
    #Lendo o arquivo
    data = pd.read_excel ('ipca_com_tratativa.xlsx') 

    #Pegando as últimas 12 linhas do df
    df = pd.DataFrame(data).iloc[-12:]
    tables = [df.to_html(classes='data', header="true", index=False)]

    return tables
   


@ipca_app.route('/ipca')
def IPCA_A():
    # IPCA
    return render_template('ipca.html', ipca_12=ipca())


@ipca_app.errorhandler(404)
def page_not_found(e):
    # função que seta o 404 explicitamente
    return render_template('404.html'), 404
     

if __name__ == '__main__':
	ipca_app.run(debug=True)

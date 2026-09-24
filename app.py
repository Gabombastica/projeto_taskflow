# Importe a Biblioteca
from flask import Flask, render_template, request

# Criar objeto flask "apelido - app"
app = Flask(__name__)

# Base fake
base_fake = []

# Rotas
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pessoa')
def pessoa():
    return render_template('pessoa.html')

@app.route('/criar_pessoa'), methods = ['GET', 'POST']
def criar_pessoa():
    if request.method == 'GET':
        return render_template('criar_pessoa.html')


@app.route('/atividade/criar', methods=['GET', 'POST'])
def criar_atividade():
    if request.method == 'POST':
        # Aqui recebe dados do Formulário
        nome_atividade = request.form.get('form_nome')
        descricao_atividade = request.form.get('form_descricao')
        data_atividade = request.form.get('form_data')
        prioridade_atividade = request.form.get('form_prioridade')
        tipo_atividade = request.form.getlist('form_tipo')
        responsavel_atividade = request.form.get('form_responsavel')
        recurso_atividade = request.form.get('form_recurso')

        dados = {
            'nome': nome_atividade,
            'descricao': descricao_atividade,
            'data': data_atividade,
            'prioridade': prioridade_atividade,
            'tipo': tipo_atividade,
            'responsavel': responsavel_atividade,
            'recurso': recurso_atividade
        }
        print(f"dados cadastrados: {dados}")
        base_fake.append(dados)
        print(f"base fake: {base_fake}")
        return render_template('listar_atividades.html', dados_atividade = base_fake)

    return render_template('criar_atividade.html')


@app.route('/atividades/listar')
def listar_atividades():
    return render_template('listar_atividades.html', dados_atividade = base_fake)


# Iniciar aplicação web
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
# Nada deve ser colocado abaixo.

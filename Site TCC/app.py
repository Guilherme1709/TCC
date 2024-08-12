from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Exemplo de dados para teste
    postagens = [
        {
            "id": 1,
            "titulo": "Postagem 1",
            "conteudo": "Conteúdo da postagem 1",
            "local_identificado": "Local 1"
        },
        {
            "id": 2,
            "titulo": "Postagem 2",
            "conteudo": "Conteúdo da postagem 2",
            "local_identificado": "Local 2"
        }
    ]
    return render_template('index.html', postagens=postagens)

if __name__ == '__main__':
    app.run(debug=True)

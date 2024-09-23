import sqlite3

def inserir(nome:str, url:str) -> None:
    conn = sqlite3.connect('historico.db')
    cursor = conn.cursor()
    cursor.execute(F'INSERT INTO musicas(nome, url) VALUES("{nome}", "{url}")')
    conn.commit()
    conn.close()


def consultar() -> str:
    conn = sqlite3.connect('historico.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM musicas')
    result = cursor.fetchall()
    return result

def musicas_list():
    lista = consultar()
    for i in lista:
        print(i)

def remover(nome:str):
    conn = sqlite3.connect('historico.db')
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM musicas WHERE nome="{nome}"')
    conn.commit()
    conn.close()


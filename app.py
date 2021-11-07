from flask import Flask, render_template, flash, redirect, request, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from createdb import *
from datetime import *
import pandas as pd
from insertdb import insert_db
import datetime
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sofia:cioccolato98@localhost:5432/mydb'
app.secret_key = 'omega596'
get_method = False
insert_db()
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password


@login_manager.user_loader
def load_user(user_id):
    conn = engine.connect()
    rs = conn.execute(select([gestori]).where(gestori.c.id == user_id))
    user = rs.fetchone()
    conn.close()
    if user is not None:
        return User(user.id, user.email, user.password)
    else:
        return


# funzione che ritorna un'istanza della classe User a partire dall'indirizzo email
def user_by_email(user_email):
    conn = engine.connect()
    rs = conn.execute(select([gestori]).where(gestori.c.email == user_email))
    user = rs.fetchone()
    conn.close()
    return User(user.id, user.email, user.password)


@app.route('/', methods=['GET'])
def home():
    global get_method
    conn = engine.connect()
    d = dolci.alias()
    g = gestione.alias()
    ing = ingredienti.alias()
    ric = ricette.alias()
    s1 = select([d.c.id_d, d.c.prezzo, g.c.numero, g.c.data]). \
        where(d.c.id_d == g.c.cod_dolce). \
        order_by(d.c.id_d)
    rs1 = conn.execute(s1)
    rec = rs1.fetchall()
    s2 = select([func.count(d.c.id_d).label('num_paste')])
    rs2 = conn.execute(s2)
    r = rs2.fetchone()
    n = int(r['num_paste'])
    if get_method == False:
        for i in range(n):
            data = datetime.datetime(rec[i]['data'].year, rec[i]['data'].month, rec[i]['data'].day)
            data_odierna = datetime.datetime.today()
            id_d = int(rec[i]['id_d'])
            prezzo = float(rec[i]['prezzo'])
            numero = int(rec[i]['numero'])
            if (data_odierna - data).days == 1:
                prezzo -= (prezzo * 20) / 100
            elif (data_odierna - data).days == 2:
                prezzo -= (prezzo * 80) / 100
            elif (data_odierna - data).days >= 3 and (data_odierna - data).days != 0:
                numero -= numero
            prezzo = round(prezzo, 2)
            u1 = dolci.update().values(prezzo=prezzo). \
                where(dolci.c.id_d == id_d)
            conn.execute(u1)
            u2 = gestione.update().values(numero=numero). \
                where(gestione.c.cod_dolce == id_d)
            conn.execute(u2)
            get_method = True
    s = select([d.c.nome, d.c.prezzo, g.c.numero]). \
        where(d.c.id_d == g.c.cod_dolce). \
        order_by(d.c.id_d)
    rs = conn.execute(s)
    r = rs.fetchall()
    s1 = select([d.c.id_d, ing.c.nome, ric.c.quantita, ric.c.unita_di_misura, ric.c.componente]). \
        select_from(d.outerjoin(ric, d.c.id_d == ric.c.dolce).outerjoin(ing, ing.c.id_i == ric.c.ingrediente)). \
        order_by(d.c.id_d)
    rs1 = conn.execute(s1)
    r1 = rs1.fetchall()
    conn.close()
    final = []
    for row in r:
        data = [row[0], row[1], row[2]]
        final.append(data)
    lista_dolci_ing = []
    d0, d1, d2, d3, d4 = ([] for i in range(5))
    for row in r1:
        d0.append(row[0]) if row[0] is not None else d0.append("")
        d1.append(row[1]) if row[1] is not None else d1.append("")
        d2.append(row[2]) if row[2] is not None else d2.append("")
        d3.append(row[3]) if row[3] is not None else d3.append("")
        d4.append(row[4]) if row[4] is not None else d4.append("")
    data = {'id': d0, 'ingrediente': d1, 'quantita': d2, 'unita': d3, 'componente': d4}
    df = pd.DataFrame(data)
    grouped = df.groupby(df.id)
    for k in range(1, n + 1):
        group = grouped.get_group(k).reset_index()
        lista_ing = []
        for index, row in group.iterrows():
            lista_ing.append([row['ingrediente'], row['quantita'], row['unita'], "(" + row['componente'] + ")"])
        lista_dolci_ing.append(lista_ing)
    return render_template('home.html', rec=final, lista_dolci=lista_dolci_ing, npaste=n)


@app.route('/accedi', methods=['GET'])
def accedi():
    if current_user.is_authenticated:
        return redirect(url_for('private'))
    return render_template('accedi.html')


def verify_password(hashpwd, pwd):
    return check_password_hash(hashpwd, pwd)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        conn = engine.connect()
        u_email = request.form['email']
        u_pwd = request.form['pass']
        s1 = select([gestori.c.email]).where(gestori.c.email == u_email)
        s2 = select([gestori.c.password]).where(gestori.c.email == u_email)
        r_s1 = conn.execute(s1)
        r_s2 = conn.execute(s2)
        real_email = r_s1.fetchone()
        real_pwd = r_s2.fetchone()
        conn.close()
        # controllo se l'email e/o la password presentate sono corrette
        if (real_email is None or real_pwd is None):
            return render_template('accedi.html', err_cred='Credenziali invalide.')
        elif check_password_hash(real_pwd['password'], u_pwd):
            user = user_by_email(request.form['email'])
            # conserva le informazioni dell'utente nella sessione utilizzando Flask-Login
            login_user(user)
            return redirect(url_for('private'))
        else:
            return render_template('accedi.html', err_pwd='Password errata.')
    else:
        return redirect(url_for('accedi'))


@app.route('/private', methods=['GET'])
@login_required  # richiede autenticazione
def private():
    conn = engine.connect()
    s = select([dolci.c.nome])
    rs = conn.execute(s)
    r = rs.fetchall()
    conn.close()
    return render_template('backoffice.html', dolci=r)


@app.route('/logout', methods=['GET'])
@login_required  # richiede autenticazione
def logout():
    # rimuove le informazioni sull'utente dalla sessione utilizzando Flask-login
    logout_user()
    return redirect(url_for('accedi'))

def remove_spaces(str_list):
    for i, str in enumerate(str_list):
        str_list[i] = " ".join(str.split())
    return str_list

@app.route('/inserisci_dolce', methods=['GET', 'POST'])
def inserisci_dolce():
    u_id = int(current_user.get_id())
    if (u_id == 1 or u_id == 2) and request.method == 'POST':
        conn = engine.connect()
        dolce = request.form['dolce']
        prezzo = request.form['prezzo']
        numero = request.form['numero']
        ingrediente = remove_spaces(request.form.getlist('ingrediente'))
        quantita = remove_spaces(request.form.getlist('quantita'))
        misura = remove_spaces(request.form.getlist('misura'))
        remove_spaces(request.form.getlist('componente'))
        componente = remove_spaces(request.form.getlist('componente'))
        data = datetime.date.today()
        s = select([func.max(dolci.c.id_d).label('cod_dolce')])
        rs = conn.execute(s)
        r = rs.fetchone()
        s1 = select([ingredienti.c.nome, func.max(ingredienti.c.id_i).label('cod_ingrediente')]). \
            group_by(ingredienti.c.nome)
        rs1 = conn.execute(s1)
        r1 = rs1.fetchall()
        list_ing = [row['nome'] for row in r1]
        cod_dolce = int(r['cod_dolce']) + 1
        cod_ingredeinte = int(r1[0]['cod_ingrediente'])
        i1 = dolci.insert().values(id_d=cod_dolce, nome=dolce, prezzo=prezzo)
        i2 = gestione.insert().values(numero=numero, data=data, cod_dolce=cod_dolce, cod_gestore=u_id)
        conn.execute(i1)
        conn.execute(i2)
        for j in range(len(ingrediente)):
            if ingrediente[j] not in list_ing and ingrediente[j] and ingrediente[j].strip():
                cod_ingredeinte = cod_ingredeinte + 1
                i3 = ingredienti.insert().values(id_i=cod_ingredeinte, nome=ingrediente[j])
                conn.execute(i3)
        for k in range(len(ingrediente)):
            if not ingrediente[k] or not ingrediente[k].strip():
                continue
            res = conn.execute(select([ingredienti.c.id_i]).where(ingredienti.c.nome == ingrediente[k])).fetchone()
            q = None if not quantita[k] or not quantita[k].strip() else quantita[k]
            m = None if not misura[k] or not misura[k].strip() else misura[k]
            c = None if not componente[k] or not componente[k].strip() else componente[k]
            i4 = ricette.insert().values(dolce=cod_dolce, ingrediente=int(res['id_i']),
                                         quantita=q, unita_di_misura=m, componente=c)
            conn.execute(i4)
        conn.close()
        flash("Operazione andata a buon fine!")
        return redirect(url_for('private'))
    else:
        return redirect(url_for('/'))


@app.route('/modifica_dolce', methods=['GET', 'POST'])
def modifica_dolce():
    u_id = int(current_user.get_id())
    if (u_id == 1 or u_id == 2) and request.method == 'POST':
        conn = engine.connect()
        nome = request.form.get('nome')
        prezzo = request.form['prezzo']
        numero = request.form['numero']
        data = datetime.date.today()
        if prezzo and prezzo.strip():
            u = dolci.update().values(prezzo=prezzo). \
                where(dolci.c.nome == nome)
            conn.execute(u)
        if numero and numero.strip():
            u = gestione.update().values(numero=numero, data=data, cod_gestore=u_id). \
                where(and_(dolci.c.nome == nome),
                      dolci.c.id_d == gestione.c.cod_dolce)
            conn.execute(u)
        conn.close()
        flash("Operazione andata a buon fine!")
        return redirect(url_for('private'))
    else:
        return redirect(url_for('/'))

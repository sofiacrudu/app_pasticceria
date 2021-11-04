from werkzeug.security import generate_password_hash
from createdb import *
import datetime

def insert_db():
    conn = engine.connect()
    s = select([dolci.c.nome])
    rs = conn.execute(s)
    r = rs.fetchone()
    conn.close()
    if r is None:
        conn = engine.connect()

        ins_gest = gestori.insert()
        passwordluana = generate_password_hash('google15')
        passwordmaria = generate_password_hash('yahoo20')
        conn.execute(ins_gest, [
            {'id_g': '1', 'nome': 'luana', 'email': 'luana@gmail.com', 'password': passwordluana},
            {'id_g': '2', 'nome': 'maria', 'email': 'maria@gmail.com', 'password': passwordmaria}
        ])

        ins_dolci = dolci.insert()
        conn.execute(ins_dolci, [
            {'id_d': '1', 'nome': 'Millefoglie', 'prezzo': '32'},
            {'id_d': '2', 'nome': 'Crostata di mandorle', 'prezzo': '36'},
            {'id_d': '3', 'nome': 'Cheesecake', 'prezzo': '28'},
            {'id_d': '4', 'nome': 'Cestino alla crema', 'prezzo': '1.20'},
            {'id_d': '5', 'nome': 'Cestino al cioccolato', 'prezzo': '1.50'},
            {'id_d': '6', 'nome': 'Cestino alla frutta', 'prezzo': '1.75'},
            {'id_d': '7', 'nome': 'Bigné chantilly', 'prezzo': '2.15'},
            {'id_d': '8', 'nome': 'Zuppa inglese', 'prezzo': '2.30'},
            {'id_d': '9', 'nome': 'Pasticcini di Riso', 'prezzo': '1.70'}
        ])

        ins_gestione = gestione.insert()
        data = datetime.date.today()
        conn.execute(ins_gestione, [
            {'numero': '3', 'data': data, 'cod_dolce': '1', 'cod_gestore': '1'},
            {'numero': '5', 'data': data, 'cod_dolce': '2', 'cod_gestore': '1'},
            {'numero': '2', 'data': data, 'cod_dolce': '3', 'cod_gestore': '1'},
            {'numero': '8', 'data': data, 'cod_dolce': '4', 'cod_gestore': '2'},
            {'numero': '6', 'data': data, 'cod_dolce': '5', 'cod_gestore': '2'},
            {'numero': '10', 'data': data, 'cod_dolce': '6', 'cod_gestore': '2'},
            {'numero': '14', 'data': data, 'cod_dolce': '7', 'cod_gestore': '2'},
            {'numero': '9', 'data': data, 'cod_dolce': '8', 'cod_gestore': '2'},
            {'numero': '7', 'data': data, 'cod_dolce': '9', 'cod_gestore': '2'}
        ])
        ins_ingredienti = ingredienti.insert()
        conn.execute(ins_ingredienti, [
            {'id_i': '1', 'nome': 'Pasta Sfoglia'},
            {'id_i': '2', 'nome': 'Farina 00'},
            {'id_i': '3', 'nome': 'Sale'},
            {'id_i': '4', 'nome': 'Latte'},
            {'id_i': '5', 'nome': 'Acqua'},
            {'id_i': '6', 'nome': 'Zucchero'},
            {'id_i': '7', 'nome': 'Tuorli'},
            {'id_i': '8', 'nome': 'Panna fresca'},
            {'id_i': '9', 'nome': 'Estratto di vaniglia'},
            {'id_i': '10', 'nome': 'Burro'},
            {'id_i': '11', 'nome': 'Farina di mandorle'},
            {'id_i': '12', 'nome': 'Uova'},
            {'id_i': '13', 'nome': 'Farina di riso'},
            {'id_i': '14', 'nome': 'Biscotti Digestive'},
            {'id_i': '15', 'nome': 'Formaggio fresco spalmabile'},
            {'id_i': '16', 'nome': 'Succo di limone'},
            {'id_i': '17', 'nome': 'Amido di mais'},
            {'id_i': '18', 'nome': 'Frutti di bosco'},
            {'id_i': '19', 'nome': 'Lievito in polvere'},
            {'id_i': '20', 'nome': 'Cioccolato fondente'},
            {'id_i': '21', 'nome': 'Frutta fresca'},
            {'id_i': '22', 'nome': 'Fecola di patate'},
            {'id_i': '23', 'nome': 'Riso'},
            {'id_i': '24', 'nome': 'Scorza di un arancio'}
        ])

        ins_ricette = ricette.insert()
        conn.execute(ins_ricette, [
            {'dolce': '1', 'ingrediente': '1', 'quantita': '670', 'unita_di_misura': 'g', 'componente': 'Pasta Sfoglia'},
            {'dolce': '1', 'ingrediente': '2', 'quantita': '120', 'unita_di_misura': 'g', 'componente': 'Crema'},
            {'dolce': '1', 'ingrediente': '3', 'quantita': '2', 'unita_di_misura': 'g', 'componente': 'Crema'},
            {'dolce': '1', 'ingrediente': '4', 'quantita': '200', 'unita_di_misura': 'g', 'componente': 'Crema'},
            {'dolce': '1', 'ingrediente': '5', 'quantita': '300', 'unita_di_misura': 'g', 'componente': 'Crema'},
            {'dolce': '1', 'ingrediente': '6', 'quantita': '200', 'unita_di_misura': 'g', 'componente': 'Crema'},
            {'dolce': '1', 'ingrediente': '7', 'quantita': '150', 'unita_di_misura': 'g', 'componente': 'Crema'},
            {'dolce': '1', 'ingrediente': '8', 'quantita': '100', 'unita_di_misura': 'g', 'componente': 'Crema'},
            {'dolce': '1', 'ingrediente': '9', 'quantita': '1', 'unita_di_misura': 'cucchiaio', 'componente': 'Crema'},
            {'dolce': '2', 'ingrediente': '2', 'quantita': '245', 'unita_di_misura': 'g', 'componente': 'Pasta Frolla'},
            {'dolce': '2', 'ingrediente': '10', 'quantita': '245', 'unita_di_misura': 'g', 'componente': 'Pasta Frolla'},
            {'dolce': '2', 'ingrediente': '6', 'quantita': '50', 'unita_di_misura': 'g', 'componente': 'Pasta Frolla'},
            {'dolce': '2', 'ingrediente': '11', 'quantita': '245', 'unita_di_misura': 'g', 'componente': 'Pasta Frolla'},
            {'dolce': '2', 'ingrediente': '12', 'quantita': '100', 'unita_di_misura': 'g', 'componente': 'Pasta Frolla'},
            {'dolce': '2', 'ingrediente': '4', 'quantita': '400', 'unita_di_misura': 'g', 'componente': 'Crema'},
            {'dolce': '2', 'ingrediente': '13', 'quantita': '50', 'unita_di_misura': 'g', 'componente': 'Crema'},
            {'dolce': '2', 'ingrediente': '9', 'quantita': '1', 'unita_di_misura': 'cucchiaio', 'componente': 'Crema'},
            {'dolce': '2', 'ingrediente': '6', 'quantita': '80', 'unita_di_misura': 'g', 'componente': 'Crema'},
            {'dolce': '3', 'ingrediente': '14', 'quantita': '240', 'unita_di_misura': 'g', 'componente': 'Base'},
            {'dolce': '3', 'ingrediente': '10', 'quantita': '100', 'unita_di_misura': 'g', 'componente': 'Base'},
            {'dolce': '3', 'ingrediente': '15', 'quantita': '500', 'unita_di_misura': 'g', 'componente': 'Crema'},
            {'dolce': '3', 'ingrediente': '6', 'quantita': '65', 'unita_di_misura': 'g', 'componente': 'Crema'},
            {'dolce': '3', 'ingrediente': '12', 'quantita': '1', 'unita_di_misura': None, 'componente': 'Crema'},
            {'dolce': '3', 'ingrediente': '16', 'quantita': '1', 'unita_di_misura': 'cucchiaio', 'componente': 'Crema'},
            {'dolce': '3', 'ingrediente': '8', 'quantita': '100', 'unita_di_misura': 'g', 'componente': 'Crema'},
            {'dolce': '3', 'ingrediente': '7', 'quantita': '1', 'unita_di_misura': None, 'componente': 'Crema'},
            {'dolce': '3', 'ingrediente': '17', 'quantita': '25', 'unita_di_misura': 'g', 'componente': 'Crema'},
            {'dolce': '3', 'ingrediente': '9', 'quantita': '1', 'unita_di_misura': 'cucchiaio', 'componente': 'Crema'},
            {'dolce': '3', 'ingrediente': '18', 'quantita': None, 'unita_di_misura': 'q.b.', 'componente': 'Copertura'},
            {'dolce': '4', 'ingrediente': '2', 'quantita': '300', 'unita_di_misura': 'g', 'componente': 'Cestino'},
            {'dolce': '4', 'ingrediente': '10', 'quantita': '150', 'unita_di_misura': 'g', 'componente': 'Cestino'},
            {'dolce': '4', 'ingrediente': '3', 'quantita': '1', 'unita_di_misura': 'pizzico', 'componente': 'Cestino'},
            {'dolce': '4', 'ingrediente': '6', 'quantita': '150', 'unita_di_misura': 'g', 'componente': 'Cestino'},
            {'dolce': '4', 'ingrediente': '12', 'quantita': '110', 'unita_di_misura': 'g', 'componente': 'Cestino'},
            {'dolce': '4', 'ingrediente': '19', 'quantita': '1', 'unita_di_misura': 'cucchiaino', 'componente': 'Cestino'},
            {'dolce': '4', 'ingrediente': '4', 'quantita': '500', 'unita_di_misura': 'g', 'componente': 'Crema pasticcera'},
            {'dolce': '4', 'ingrediente': '6', 'quantita': '150', 'unita_di_misura': 'g', 'componente': 'Crema pasticcera'},
            {'dolce': '4', 'ingrediente': '9', 'quantita': '1', 'unita_di_misura': 'cucchiaio',
             'componente': 'Crema pasticcera'},
            {'dolce': '4', 'ingrediente': '7', 'quantita': '90', 'unita_di_misura': 'g', 'componente': 'Crema pasticcera'},
            {'dolce': '4', 'ingrediente': '17', 'quantita': '50', 'unita_di_misura': 'g', 'componente': 'Crema pasticcera'},
            {'dolce': '5', 'ingrediente': '2', 'quantita': '300', 'unita_di_misura': 'g', 'componente': 'Cestino'},
            {'dolce': '5', 'ingrediente': '10', 'quantita': '150', 'unita_di_misura': 'g', 'componente': 'Cestino'},
            {'dolce': '5', 'ingrediente': '3', 'quantita': '1', 'unita_di_misura': 'pizzico', 'componente': 'Cestino'},
            {'dolce': '5', 'ingrediente': '6', 'quantita': '150', 'unita_di_misura': 'g', 'componente': 'Cestino'},
            {'dolce': '5', 'ingrediente': '12', 'quantita': '110', 'unita_di_misura': 'g', 'componente': 'Cestino'},
            {'dolce': '5', 'ingrediente': '19', 'quantita': '1', 'unita_di_misura': 'cucchiaino', 'componente': 'Cestino'},
            {'dolce': '5', 'ingrediente': '20', 'quantita': '50', 'unita_di_misura': 'g',
             'componente': 'Ganache al cioccolato'},
            {'dolce': '5', 'ingrediente': '8', 'quantita': '250', 'unita_di_misura': 'g',
             'componente': 'Ganache al cioccolato'},
            {'dolce': '6', 'ingrediente': '2', 'quantita': '300', 'unita_di_misura': 'g', 'componente': 'Cestino'},
            {'dolce': '6', 'ingrediente': '10', 'quantita': '150', 'unita_di_misura': 'g', 'componente': 'Cestino'},
            {'dolce': '6', 'ingrediente': '3', 'quantita': '1', 'unita_di_misura': 'pizzico', 'componente': 'Cestino'},
            {'dolce': '6', 'ingrediente': '6', 'quantita': '150', 'unita_di_misura': 'g', 'componente': 'Cestino'},
            {'dolce': '6', 'ingrediente': '12', 'quantita': '110', 'unita_di_misura': 'g', 'componente': 'Cestino'},
            {'dolce': '6', 'ingrediente': '19', 'quantita': '1', 'unita_di_misura': 'cucchiaino', 'componente': 'Cestino'},
            {'dolce': '6', 'ingrediente': '4', 'quantita': '500', 'unita_di_misura': 'g', 'componente': 'Crema pasticcera'},
            {'dolce': '6', 'ingrediente': '6', 'quantita': '150', 'unita_di_misura': 'g', 'componente': 'Crema pasticcera'},
            {'dolce': '6', 'ingrediente': '9', 'quantita': '1', 'unita_di_misura': 'cucchiaio',
             'componente': 'Crema pasticcera'},
            {'dolce': '6', 'ingrediente': '7', 'quantita': '90', 'unita_di_misura': 'g', 'componente': 'Crema pasticcera'},
            {'dolce': '6', 'ingrediente': '17', 'quantita': '50', 'unita_di_misura': 'g', 'componente': 'Crema pasticcera'},
            {'dolce': '6', 'ingrediente': '21', 'quantita': None, 'unita_di_misura': 'q.b.', 'componente': 'Copertura'},
            {'dolce': '7', 'ingrediente': '5', 'quantita': '160', 'unita_di_misura': 'ml', 'componente': 'Pasta Choux'},
            {'dolce': '7', 'ingrediente': '6', 'quantita': '2', 'unita_di_misura': 'cucchiaini',
             'componente': 'Pasta Choux'},
            {'dolce': '7', 'ingrediente': '10', 'quantita': '150', 'unita_di_misura': 'g', 'componente': 'Pasta Choux'},
            {'dolce': '7', 'ingrediente': '12', 'quantita': '6', 'unita_di_misura': 'uova', 'componente': 'Pasta Choux'},
            {'dolce': '7', 'ingrediente': '4', 'quantita': '200', 'unita_di_misura': 'ml', 'componente': 'Pasta Choux'},
            {'dolce': '7', 'ingrediente': '3', 'quantita': '2', 'unita_di_misura': 'cucchiaini',
             'componente': 'Pasta Choux'},
            {'dolce': '7', 'ingrediente': '2', 'quantita': '200', 'unita_di_misura': 'g', 'componente': 'Pasta Choux'},
            {'dolce': '7', 'ingrediente': '4', 'quantita': '750', 'unita_di_misura': 'g', 'componente': 'Crema chantilly'},
            {'dolce': '7', 'ingrediente': '7', 'quantita': '5', 'unita_di_misura': None, 'componente': 'Crema chantilly'},
            {'dolce': '7', 'ingrediente': '2', 'quantita': '105', 'unita_di_misura': 'g', 'componente': 'Crema chantilly'},
            {'dolce': '7', 'ingrediente': '9', 'quantita': '1', 'unita_di_misura': 'cucchiaio',
             'componente': 'Crema chantilly'},
            {'dolce': '7', 'ingrediente': '8', 'quantita': '300', 'unita_di_misura': 'ml', 'componente': 'Crema chantilly'},
            {'dolce': '7', 'ingrediente': '6', 'quantita': '180', 'unita_di_misura': 'g', 'componente': 'Crema chantilly'},
            {'dolce': '8', 'ingrediente': '12', 'quantita': '110', 'unita_di_misura': 'g', 'componente': 'Pan di spagna'},
            {'dolce': '8', 'ingrediente': '22', 'quantita': '30', 'unita_di_misura': 'g', 'componente': 'Pan di spagna'},
            {'dolce': '8', 'ingrediente': '3', 'quantita': '1', 'unita_di_misura': 'pizzico',
             'componente': 'Pan di spagna'},
            {'dolce': '8', 'ingrediente': '2', 'quantita': '30', 'unita_di_misura': 'g', 'componente': 'Pan di spagna'},
            {'dolce': '8', 'ingrediente': '6', 'quantita': '60', 'unita_di_misura': 'g', 'componente': 'Pan di spagna'},
            {'dolce': '8', 'ingrediente': '9', 'quantita': '1', 'unita_di_misura': 'cucchiaio',
             'componente': 'Pan di spagna'},
            {'dolce': '8', 'ingrediente': '4', 'quantita': '400', 'unita_di_misura': 'g', 'componente': 'Crema Pasticcera'},
            {'dolce': '8', 'ingrediente': '7', 'quantita': '72', 'unita_di_misura': 'g', 'componente': 'Crema Pasticcera'},
            {'dolce': '8', 'ingrediente': '6', 'quantita': '140', 'unita_di_misura': 'g', 'componente': 'Crema Pasticcera'},
            {'dolce': '8', 'ingrediente': '20', 'quantita': '50', 'unita_di_misura': 'g', 'componente': 'Crema Pasticcera'},
            {'dolce': '8', 'ingrediente': '8', 'quantita': '100', 'unita_di_misura': 'g', 'componente': 'Crema Pasticcera'},
            {'dolce': '8', 'ingrediente': '17', 'quantita': '45', 'unita_di_misura': 'g', 'componente': 'Crema Pasticcera'},
            {'dolce': '8', 'ingrediente': '9', 'quantita': '1', 'unita_di_misura': 'cucchiaio',
             'componente': 'Crema Pasticcera'},
            {'dolce': '9', 'ingrediente': '2', 'quantita': '160', 'unita_di_misura': 'g', 'componente': 'Pasta frolla'},
            {'dolce': '9', 'ingrediente': '6', 'quantita': '80', 'unita_di_misura': 'g', 'componente': 'Pasta frolla'},
            {'dolce': '9', 'ingrediente': '12', 'quantita': '2', 'unita_di_misura': None, 'componente': 'Pasta frolla'},
            {'dolce': '9', 'ingrediente': '10', 'quantita': '80', 'unita_di_misura': 'g', 'componente': 'Pasta frolla'},
            {'dolce': '9', 'ingrediente': '6', 'quantita': '50', 'unita_di_misura': 'g', 'componente': 'Farcitura'},
            {'dolce': '9', 'ingrediente': '23', 'quantita': '70', 'unita_di_misura': 'g', 'componente': 'Farcitura'},
            {'dolce': '9', 'ingrediente': '7', 'quantita': '3', 'unita_di_misura': None, 'componente': 'Farcitura'},
            {'dolce': '9', 'ingrediente': '4', 'quantita': '450', 'unita_di_misura': 'ml', 'componente': 'Farcitura'},
            {'dolce': '9', 'ingrediente': '9', 'quantita': '1', 'unita_di_misura': 'cucchiaio', 'componente': 'Farcitura'},
            {'dolce': '9', 'ingrediente': '24', 'quantita': None, 'unita_di_misura': 'q.b.', 'componente': 'Farcitura'}
        ])

        conn.close()

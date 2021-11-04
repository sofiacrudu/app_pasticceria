from sqlalchemy import *

uri='postgresql://sofia:cioccolato98@localhost:5432/mydb'
engine=create_engine(uri, echo=True)
metadata=MetaData()

dolci = Table('dolci', metadata,
              Column('id_d', Integer, primary_key=True),
              Column('nome', String),
              Column('prezzo', Float)
              )

gestori = Table('gestori', metadata,
                Column('id', Integer, primary_key=True),
                Column('nome', String),
                Column('email', String),
                Column('password', String),
                )

gestione = Table('gestione', metadata,
                 Column('id_g', Integer, primary_key=True),
                 Column('numero', Integer),
                 Column('data', Date),
                 Column('cod_dolce', Integer, ForeignKey('dolci.id_d', onupdate="CASCADE", ondelete="SET NULL")),
                 Column('cod_gestore', Integer, ForeignKey('gestori.id', onupdate="CASCADE", ondelete="SET NULL"))
                 )

ricette = Table('ricette', metadata,
              Column('id_r', Integer, primary_key=True),
              Column('dolce', Integer, ForeignKey('dolci.id_d', onupdate="CASCADE", ondelete="SET NULL")),
              Column('ingrediente', Integer, ForeignKey('ingredienti.id_i', onupdate="CASCADE", ondelete="SET NULL")),
              Column('quantita', Integer),
              Column('unita_di_misura', String),
              Column('componente', String)
              )

ingredienti = Table('ingredienti', metadata,
              Column('id_i', Integer, primary_key=True),
              Column('nome', String)
              )

metadata.create_all(engine)







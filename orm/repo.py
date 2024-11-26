import orm.modelos as modelos
from sqlalchemy.orm import Session

# Esta función es llamada por api.py
# para atender GET '/usuarios/{id}'
# select * from app.usuarios where id = id_usuario
def usuario_por_id(sesion:Session,id_usuario:int):
    print("select * from app.usuarios where id = ", id_usuario)
    return sesion.query(modelos.Usuario).filter(modelos.Usuario.id==id_usuario).first()


def compra_por_id(sesion:Session, id_compra:int):
    print("selecc* from app.compras where id =", id_compra)
    return sesion.query(modelos.Compra).filter(modelos.Compra.id==id_compra).first()

def foto_por_id(sesion:Session, id_foto:int):
    print("selecc* from app.compras where id =", id_foto)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id== id_foto).first()

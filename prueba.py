
# Agregar Usuario
from contexto.Usuario import Usuario
from datos.ListaDeUsuarios import ListaDeUsuarios

u = Usuario()
u.nombres = "Josue"
u.apellidos = "lopez"
u.edad = 37
u.IDsTemperatura = 1
u.IDsPresion = 1
u.IDsAcelerometro = 1
u.IDsRitmoCardiaco = 1

l = ListaDeUsuarios()
l.agregarUsuario(u)

# Obtener lista de usuarios
usuarios = l.obtenerUsuarios()

# Busca usuario por id
u = l.obtenerUsuarioPorId(1)



from contexto.Medicamento import Medicamento
from datos.ListaDeMedicamentos import ListaDeMedicamentos

# agregar Medicamento
m = Medicamento()
m.descripcion = "Yodohidroxiquinoleina"
l = ListaDeMedicamentos()
l.agregarMedicamento(m)

# devuelve medicamento
medicamentos = l.obtenerMedicamentos()

# obtenerMedicamentoPorId
m = l.obtenerMedicamentoPorId(1)


# agregar grupos
from datos.ListaDeGrupos import ListaDeGrupos
from contexto.Grupo import Grupo

g = Grupo()
g.periodo = 4
g.medicamento = m
g.horaInicial = 12

lg = ListaDeGrupos()
lg.crearGrupo(g)

# lista de todos los grupos
listaDeGrupos = lg.obtenerGrupos()


from datos.ListaDeUsuarios import ListaDeUsuarios


l = ListaDeUsuarios()
u = l.obtenerUsuarioPorId(3)

from datos.Grupo import Grupo

g = Grupo(19)
# agrega miembro al grupo y dosis
g.agregarUsuario(u, 200)

# devuelve los miembros del grupo
miembros = g.obtenerUsuarios()

for m in miembros:
    u = m[0]
    dosis = m[1]
    print(u.nombres + ", " + u.apellidos + " dosis: " + str(dosis))
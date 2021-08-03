import mysql.connector


#Con esto como que leemos nuestra base de datos y se la asignamos a una variable, ademas le tenemos que pasar un usuario
midb = mysql.connector.connect(
	host='localhost',
	user='root',
	password='enzo',
	database='prueba'
)
cursor = midb.cursor() #Un cursor es un objeto que nos permite interactuar con la base de datos mediante el lenguaje sql

#INSERTAR DATOS
sql = 'insert into Usuario (email, username, edad) values (%s, %s, %s)'
values = ('asd@gmail.com', 'nombre_usuario', 45)

#ACTUALIZAR DATOS
sql = 'update Usuario set email = %s where id = %s'
values = ('naranja@gmail.com', 2)

#ELIMINAR DATOS
sql = 'delete from Usuario where id = %s'
values = (2, )    #tiene que ser si o si una tupla y agregar una coma si es que es un solo item

cursor.execute(sql, values) #Cuando nosotros vamos a ejecutar una consulta de sql y ademas vamos a tener valores que estos sean remplazados despues, en ese caso mi metodo de .execute() va a recibir 2 argumentos, el primer valor va a ser la consulta al sql y el segundo los valores que yo voy a ingresar


cursor.execute('select * from Usuario')
cursor.execute('select * from Usuario limit 1')   #Para que nos muestre 1 solo elemento , 2 para dos , 3 para tres y asi , nose si se podra poner un rango

cursor.execute('show create table Usuario') #Nos muestra con cual script se creo nuestra tabla y como se hizo, es mas que todo por si te olvidas de como era tu tabla

midb.commit()   #Para guardar los cambios que vamos haciendo en la base de datos , funciona igual que un commit and push en 'GIT'

resultado = cursor.fetchall() #Para indicarle que nos traiga de vuelta los resultados, nos va a devolver todas las instancias que halla encontrado
resultado = cursor.fetchone() #Nos devuelve el primer resultado que a encontrado nada mas
print(resultado)

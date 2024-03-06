lista = list(range(100))

print(lista)
print(50*'*')
#list comprehensions
pares = [element for element in lista if element % 2 == 0]
print(pares)

#dictionary comprehensions
studentuid = [1,2,3]
students = ['Jose', 'Juan', 'Larsen']

students_whit_id = {uid: student for uid, student in  zip(studentuid, students)}
print(students_whit_id)
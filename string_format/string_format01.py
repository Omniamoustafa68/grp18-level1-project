client_id = 101
client_name= 'ahmes omar'
client_invoice = 76544578.456899

#client has id = 101, his name is ahmed omar, his inovice value = 78987679.987656
print('---1- print with concat---')
print('client has id = ' + str(client_id) + '\n\t, his name is ' + client_name+',his invoice value = ', str(client_invoice))

print('---2- print with multi parameters')
print('client has is = ', client_id, 'his name is ', client_name , 'his invoice value =', client_invoice)

print('3- string formating using placeholder')
print('client has id = %d ,his name is %s , his invoice value = %.2f' %(client_id, client_name, client_invoice))

print('4- string format')
print('client id = {:d}, his name is {:s} , his invoice = {:,.2f}' . format(client_id, client_name,client_invoice))
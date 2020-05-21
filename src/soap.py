from zeep import Client

#cliente = Client(wsdl='http://www.dneonline.com/calculator.asmx?WSDL')
#print("Suma")
#print(cliente.service.Add(50,5))
#print("Multiplicacion")
#print(cliente.service.Multiply(50,5))
#print("Suma")
#print(cliente.service.Multiply(50,5))

cliente = Client(wsdl='https://www.dataaccess.com/webservicesserver/NumberConversion.wso?wsdl')
print(cliente.service.NumberToDollars(10.55))
print(cliente.service.NumberToWords(10.00))

cliente = Client(wsdl='https://cvnet.cpd.ua.es/servicioweb/publicos/pub_gestdocente.asmx?wsdl')
print(cliente.service.wsagrupacionesResponse([]))
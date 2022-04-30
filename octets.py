def ip_class(address):
    address.split('.')

    octets = address.split('.')
    oct1 = int(octets[0])
    if len(str(oct1)) > 3 or len(str(oct1)) <1:
        return 'Error in Length, Input Valid IP Address range'
    if oct1 >= 1 and oct1 < 127:
        return 'Class A'
    elif oct1 == 127:
        return 'Return the slab'
    elif oct1 >= 128 and oct1 < 192:
        return 'Class B'
    elif oct1 >= 192 and oct1 <224:
        return 'Class C'
    elif oct1 >= 224 and oct1 < 240:
        return 'Class D'
    elif oct1 >= 240 and oct1 <255:
        return 'Class E'
    else:
        return ('Please use a valid IP address')

try:
    ip_address = input( 'What IP address do you want to analyze?')
    print(ip_class(ip_address))
except ValueError:
    print ('Value Error')



import os, sys
import subprocess

def Console(comando):
	
	if comando == 'help' or comando == '-h' or comando == '-?' :
		
		print(' ')
		print('Script que funciona bajo la herramienta Nmap. ')
		print('No hemos escogido todos las funciones de la herramienta, solo  algunas para escaner de Red,')
		print('Funciones:')
		print('	-O (Detectar Sistem Operativo. ej: -O IP)')
		print('	-sP (Enlistar los host ctivos en la Red. ej: -sP IP)')
		print('	-Pn -p ')
		print('	-v -A (Informcion detallada de un Host. ej: -v -A IP')
		print('	-p ( Ver Puertos Abiertos. ej: -p puerto o -p puerto_inicial-puerto_final)')
		print('	-sV (ver puertos y servicios de un host con su Version . ej -sV IP)')
		print('	-v -iR')
		print(' ')
		print('Script:')
		print_scripts()
		print(' ')
		
	elif comando == 'exit' or comando == '-q' :
		
		print('\n\033[32m''NSEarch - Version: Monkey 0.1:\033[96m Hasta La Proxima''\n')
		exit()

	elif comando == 'categoria :: script' :
		
		print_scripts()
		print(' ')

	elif comando== 'clear':
		
		os.system("clear")

	elif comando == '--script auth':
		
		scripts(comando)

	elif comando == 'iflist':
	
		iflist()

	elif comando == 'setIP':

		setIP(ingresar_IP())

	elif comando == 'getIP':
		
		obtener_IP()

	elif comando == '--script safe':
		
		scripts(comando)

	elif comando == '--script all':
		
		scripts(comando)

	elif comando == '--script default':
		
		scripts(comando)

	elif comando == '--script vuln':
		
		scripts(comando)
	elif comando == '--script malware':
		
		scripts(comando)


	else:
		
		Nmap(comando)
		

def Nmap(comando):
	
	nmap = "nmap " + str(comando)
	
	print('\n\033[93m''Ejecutando: ', comando,'\033[92m')
	resultados_nmap = subprocess.Popen(nmap, shell=True, stdout=subprocess.PIPE)
	while resultados_nmap.poll() is None:
	    salida_nmap = resultados_nmap.stdout.readline()
	    print('\033[92m',salida_nmap.decode(sys.getdefaultencoding()).rstrip())

def getNSE():
	
	global nse 
	return nse


def setNSE(nses):
	
	global nse
	nse = nses
	return nse

def getIP():
	
	global ip 
	return ip

def setIP(ips):
	
	global ip
	ip = ips
	return ip 

def ingresar_IP():
	
	print('\033[92m''Direccion IP >> ','\033[91m', end = '')
	ip = input()
	setIP(ip)
	return ip

def obtener_IP():
	
	try:
		print('Direccion IP Ingresada >> ','\033[91m', getIP())

	except NameError as e:
		
		print('\033[91m''No se ha Cargado un Direccion IP al Script. Ejecute setIP')
		ingresar_IP() 

def iflist():
	os.system('nmap -iflist')



def print_scripts():
	

    print('--script auth: ejecuta todos sus scripts disponibles para autenticación')
    print('--script default: ejecuta los scripts básicos por defecto de la herramienta')
    print('--script discovery: recupera información del target o víctima')
    print('--script external: script para utilizar recursos externos')
    print('--script intrusive: utiliza scripts que son considerados intrusivos para la víctima o target')
    print('--script malware: revisa si hay conexiones abiertas por códigos maliciosos o backdoors (puertas traseras)')
    print('--script safe: ejecuta scripts que no son intrusivos')
    print('--script vuln: descubre las vulnerabilidades más conocidas')
    print('--script all: ejecuta absolutamente todos los scripts con extensión NSE disponibles')


def scripts(comando):

	obtener_IP()
	script = '-f -sS -sV ' + str(comando) +' '+getIP()
	#print('\033[92m''Script Ejecutado: ', script)
	Nmap(script)

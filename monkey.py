import console
import readline

def nse():
 try:
  try:
    console.setNSE(False)
    while console.getNSE()!= True:
      banner ='\033[0;36m'+'''
      ================================================
       _   _  _____  _____                     _
      | \ | |/  ___||  ___|                   | |
      |  \| |\ `--. | |__    __ _  _ __   ___ | |__
      | . ` | `--. \|  __|  / _` || '__| / __|| '_  |
      | |\  |/\__/ /| |___ | (_| || |   | (__ | | | |
      \_| \_/\____/ \____/  \__,_||_|    \___||_| |_|
      ================================================
      \033[32m NSEarch \033[0;36m|  Version: Monkey 0.1
      @marto_nieto_g16 | marto.nieto.g16@gmail.com
      Comunidad Bytes Codes       |  @BytesCodes
      ================================================
      '''+'\033[0m'
      print(banner)

      print('\033[96m''monkey >> ','\033[92m', end ='')
      comando = readline.get_completer_delims()
      readline.set_completer_delims(comando.replace('-', ''))

      comando = input()
      console.Console(comando)
      
  except NameError as es:
    print('\n\033[91m''Error!. Funcion getIP')
 except KeyboardInterrupt as e:
  print('\n\033[93m''\n\033[32m NSEarch - Version: Monkey:\033[93m Hasta La Proxima''\n')

nse()
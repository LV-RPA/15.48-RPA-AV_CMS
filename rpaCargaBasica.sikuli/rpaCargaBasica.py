import datetime
desde = datetime.datetime.now() + datetime.timedelta(days=-15)
hasta = datetime.datetime.now()
ftpip = "10.4.3.220"
user_gestel = "ot_dchs0"
pass_gestel = "abc00abc"
ftpruta = "/home/geslis/ot_dchs0"
link_inguz = "http://www.anovo.pe/inguz"
link_carga = "http://www.anovo.pe/inguz/formRutinas/frmCargarOrdenes.aspx"
user_inguz = "74590179"
pass_inguz = "jarvis"
basica = (r'\\10.120.15.48\CargaInguz\Basica')
speedy = (r'\\10.120.15.48\CargaInguz\Speedy')
delete_files = r'del /S /Q \\10.120.15.48\CargaInguz\*'
print(desde)
print(hasta)

print("abrir excel")
type("r",KeyModifier.WIN)
sleep(2)
paste("excel")
sleep(2)
type(Key.ENTER)
sleep(10)

print("abrir el archivo")
type("q",KEY_ALT)
sleep(3)
type("o",KEY_ALT)
sleep(5)
type("l",KEY_CTRL)
sleep(3)
paste(basica)
sleep(2)
type(Key.ENTER)
sleep(2)
click(Pattern("1571152681950.png").targetOffset(-18,3))
sleep(2)
type(Key.ENTER)
sleep(2)

print("eliminar 1")
wait("1571152748899.png",120)
sleep(2)
click(Pattern("1571153094134.png").targetOffset(-4,1))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(2)

print("eliminar 2")
click(Pattern("1571153218276.png").targetOffset(-81,1))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(2)

print("eliminar 3")
click(Pattern("1571153307341.png").targetOffset(-78,2))
sleep(2)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(2)

print("eliminar 4")
click(Pattern("1571153367646.png").targetOffset(-79,2))
sleep(2)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(2)

print("eliminar 5")
click(Pattern("1571153438128.png").targetOffset(-82,0))
sleep(2)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(2)

print("eliminar 6")
click(Pattern("1571153479982.png").targetOffset(-81,1))
sleep(2)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(2)

print("eliminar 7")
click(Pattern("1571773450091.png").targetOffset(-81,2))
sleep(2)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(2)

print("eliminar 8")
click(Pattern("1571153778261.png").targetOffset(-83,1))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(2)

print("eliminar 9")
click(Pattern("1571153846799.png").targetOffset(-78,0))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(2)

print("eliminar 10")
click(Pattern("1571153933550.png").targetOffset(-82,2))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))
sleep(1)
click(Pattern("1571153155396.png").targetOffset(4,-20))

print("Cambiar cabezeras")
sleep(3)
type(Key.UP)
sleep(2)
type(Key.LEFT)
sleep(2)
paste("DISTRITO")
sleep(2)
type(Key.LEFT*3)
sleep(2)
paste("DIA INSCRIP")
sleep(2)
type(Key.LEFT)
sleep(2)
paste("DIRECCION")
sleep(2)
type(Key.LEFT)
sleep(2)
paste("CLIENTE")
sleep(2)
type(Key.LEFT*3)
sleep(2)
paste("NRSER")
sleep(2)

print("Guardar Archivo")
type("a",KEY_ALT)
sleep(2)
type("d",KEY_ALT)
sleep(5)
type("a",KEY_ALT)
sleep(2)
click(Pattern("1571154817639.png").targetOffset(45,1))
sleep(5)

#//--------------------FIREFOX-------------------//#
print("abrir firefox")
type("r",KeyModifier.WIN)
sleep(2)
paste("firefox")
type(Key.ENTER)
sleep(15)

print("iniciar sesion")
paste(Pattern("1566427253659.png").targetOffset(-224,25), user_inguz)
sleep(2)
type(Key.TAB)
sleep(2)
paste(pass_inguz)
sleep(2)
type(Key.ENTER)
sleep(60)
type("l",KEY_CTRL)
sleep(2)
paste(link_carga)
sleep(2)
type(Key.ENTER)
sleep(15)
click(Pattern("1566427365594.png").similar(0.80).targetOffset(11,-24))
sleep(3)
type(Key.DOWN*11)
sleep(3)
click(Pattern("1571155213099.png").targetOffset(-154,-25))
sleep(2)

print("buscar el archivo")
type("l",KEY_CTRL)
sleep(2)
paste(basica)
sleep(2)
type(Key.ENTER)
sleep(2)
click(Pattern("1571155274477.png").similar(0.80).targetOffset(-20,1))
sleep(1)
type(Key.ENTER)
sleep(2)
click(Pattern("1571155305391.png").targetOffset(328,-27))
sleep(3)
wait(Pattern("1560615777602.png").similar(0.80),1800)

print("fin de la carga")
sleep(3)
type("w",KEY_CTRL)
sleep(3)

print("cerrar procesos")
type("r",KeyModifier.WIN)
sleep(2)
type("cmd")
type(Key.ENTER)
sleep(2)
paste(r'taskkill /F /IM firefox.exe')
type(Key.ENTER)
sleep(2)
type("exit")
sleep(1)
type(Key.ENTER)
sleep(2)
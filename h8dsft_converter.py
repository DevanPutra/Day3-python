def convert(kelv,celss,kelvf,celsf):
  cels = kelv - 273.15                               #cels= celcius
  kelv = celss + 273.15                              #kelv= kelvin #cells= celsius ke kelvin
  fahrk = 9/5*(kelvf-273.15) + 32                    #fahrk= fahrenheit ke kelvin #kelvf= kelvin ke fahrenheit
  fahrc = (celsf*1.8) + 32                           #fahrc= fahrenheit ke celcius #celsf= celcius ke kelvin 
  return (cels,kelv,fahrk,fahrc)
print (convert(0, 0, 0,0));



def convert(kelv,celss):
  cels = kelv - 273.15                               #cels= celcius
  kelv = celss + 273.15                              #kelv= kelvin #cells= celsius ke kelvin
  return (cels,kelv)
print (convert(0, 0));


def convert(kelvf,celsf):
  fahrk = 9/5*(kelvf-273.15) + 32                   #fahrk= fahrenheit ke kelvin #kelvf= kelvin ke fahrenheit
  fahrc = (celsf*1.8) + 32                           #fahrc= fahrenheit ke celcius #celsf= celcius ke kelvin 
  return (fahrk,fahrc)
print (convert(0, 0));


def convert(fahrk,fahrc):
  kelv = ((fahrk + 459.67)/ 1.8)                    #fahrk= fahrenheit ke kelvin #kelvf= kelvin ke fahrenheit
  cels = (5/9*(fahrc-32))                    #fahrc= fahrenheit ke celcius #celsf= celcius ke kelvin 
  return (kelv,cels)
print (convert(0,0))
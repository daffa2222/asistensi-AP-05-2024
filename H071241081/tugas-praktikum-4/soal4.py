def kalkulator_sederhana(x,y,z) :
		if  x ==  '+':
			return y + z
		elif  x == '-' :
			return y - z
		elif  x  == '*':
			return  y * z
		elif   x  == '/' and  z != 0:
			return y /z 
		elif x  == '/' and  z == 0 :
			return 'INPUT INVALID'
		else :
			return 'INPUT INVALID'
          
try :
	y = float (input ('MASUKKAN ANGKA PERTAMA :'))
	z = float (input ('MASUKKAN ANGKA KEDUA :'))
	x = input ('MASUKKAN OPERASI : (+,-,/,*)')
	print (kalkulator_sederhana(x,y,z))
     
except : 
     print ("INPUT INVALID")
        
    
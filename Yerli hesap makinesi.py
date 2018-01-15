while True:
	print("Seçenekler:")
	print("İki sayıyı birbirine eklemek için 'ekle' yazın")
	print("İki sayıyı birbirinden çıkartmak için 'çıkart' yazın")
	print("İki sayıyı birbiriyle çarpmak için 'çarp' yazın")
	print("İki sayıyı birbirine bölmek için 'böl' yazın")
	print("İki sayının birinin diğer üssünü almak için 'üssü' yazın")	
	print("Çıkmak için 'çık' yazın")
	user_input = input(": ")

	if user_input == "çık":
		break
	elif user_input == "ekle":
		num1=float(input("Bir sayı giriniz: "))
		num2=float(input("Diğer sayıyı giriniz: "))
		result=str(num1+num2)
		print("Cevap "+result)
	elif user_input == "çıkart":
		num1=float(input("Bir sayı giriniz: "))
		num2=float(input("Diğer sayıyı giriniz: "))
		result=str(num1-num2)
		print("Cevap "+result)
	elif user_input == "çarp":
		num1=float(input("Bir sayı giriniz: "))
		num2=float(input("Diğer sayıyı giriniz: "))
		result=str(num1*num2)
		print("Cevap "+result)
	elif user_input == "böl":
		num1=float(input("Bir sayı giriniz: "))
		num2=float(input("Diğer sayıyı giriniz: "))
		result=str(num1/num2)
		print("Cevap "+result)
	elif user_input == "üssü":
		num1=float(input("Üssü alınacak sayıyı giriniz: "))
		num2=float(input("Kaç üssü?: "))
		result=str(num1**num2)
		print("Cevap "+result)	
	else:
		print("Yanlış giriş yaptınız, lütfen tekrar deneyin.")
	

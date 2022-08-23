class Content:
	def __init__(self, name, addr, phone):
		self.name = name
		self.addr = addr
		self.phone = phone

	def print_init(self):
		print("name : ",self.name)
		print("addr : ",self.addr)
		print("phone : ",self.phone)

def delete_info(peoples,name):
	for key in peoples.keys():
		if key == name:
			del key

def print_all(peoples):
	for people in peoples:
		print("Name : ", people.name,end="")
		print("  Address : ", people.addr,end="")
		print("   Phone Number : ", people.phone)

def input_menu():
	print("1. 주소 입력")
	print("2. 주소 삭제")
	print("3. 주소 출력")
	print("4. 종료")

	menu = input(" 번호 : ")
	return int(menu)


###############################################################################

peoples = list()

while(True):
	menu=input_menu()
	
	if(menu == 1):
		Name = input("Name  :")
		Addr = input("Address  :")
		Phone = input("PhoneNumber  :")
		addr_cls = Content(Name, Addr, Phone);
		addr_cls.print_init()
		#peoples.append({"Name":addr_cls.name,"Address":addr_cls.addr,"Phone":addr_cls.phone})
		peoples.append(addr_cls)
	elif(menu == 2):
		pass
		#Name=input("삭제할 인간의 이름 : ")
		
	elif(menu == 3):
		print_all(peoples)
	elif(menu == 4):
		break
	else:
		print("잘못된 입력. 다시 입력하시오")
	

#작성한 파일 내에서 실행.,.,.,.,.,...
if __name__=="main":
	main()

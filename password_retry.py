password = 'a123456' # 避免改太多地方
time = 3
while time > 0:
	time = time - 1
	pwd = input('請輸入使用者密碼(共有三次機會)：')
	if pwd == password:
		print('登入成功')
		break # 逃出迴圈
	else:
		print('密碼錯誤！')
		if time > 0:
			print('還有' , time,'次機會')
		else:
			print('機會用盡，請重新登入')


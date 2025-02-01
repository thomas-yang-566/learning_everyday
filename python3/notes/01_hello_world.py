#01_hello_world.py
print("01_hello_world.py python3!")

message = "Hello from python world!"
print(message)
message = "hello from Python Crash Course world!"

print(message)
# comment string
message = 'test single qoute'
print(message)
message = 'I telll my frient:"test in double qoute" and escape\''
print(message)

## title, 首字母会变大写
print(message.title())
## 全大写
message = 'Ada Lovelace'
print("upper:",message.upper())
print("lower:",message.lower())

frist_name = 'ada'
last_name = 'lovelace'

full_name = f"{frist_name} {last_name}" ## f-strings // f:format
print(full_name)
print(f"hello, {full_name.title()}!")

print("format: \n{}_{}".format(frist_name, last_name))

favorite_language = ' python '
print('lstrip\t"'+favorite_language.lstrip()+'"')
print('rstrip\t"'+favorite_language.rstrip()+'"')
print('strip\t"'+favorite_language.strip()+'"')
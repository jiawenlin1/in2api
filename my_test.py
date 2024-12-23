import requests

url = "http://192.168.17.24:9000/history_file//48/a8/48a85c51-2888-4d39-a156-719211f04d8e.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minioadmin%2F20241222%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241222T151859Z&X-Amz-Expires=3600&X-Amz-Meta-Platform=5&X-Amz-Meta-Projectpath=%2F01105%2Ftest%2Fasd.jpg&X-Amz-Meta-Userid=20220223&X-Amz-SignedHeaders=host&X-Amz-Signature=cbd4ebca77d4e392b1cd220d426921635a4a4d9b67cb036e7647c0508d569ef7"
files_value = r"C:\Users\admin\PycharmProjects\EOS_API_AUTOMATION_TEST\testcase\2_file\asd.jpg"
# with open(files_value, 'rb') as file:
#     payload = file.read()
payload=open(files_value, 'rb')
headers = {
    'Content-Type': 'application/octet-stream'
}

response = requests.request("PUT", url, headers=headers, data=payload)
print(123)
print(response.status_code)
print(response.text)

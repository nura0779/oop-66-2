from urllib import response

import requests
# эта библиотека нужна для отправки запросов к сайтам
# она используется, чтобы скачивать информацию из интернета прямо в код

response = requests.get('https://example.com')
print("Статус ответа от сайта: ", response.status_code)

def find_two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [2, 7, 11, 15]
target = 9

result = find_two_sum(nums, target)
print("результат: ", result)
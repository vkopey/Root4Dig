import csv
from ollama import chat
from ollama import ChatResponse
import re

text0="Прокласифікуй текст за тональністю (позитивний-2, нейтральний-1, негативний-0) і виведи тільки цифру класу: "
text0='Прокласифікуй текст відповіді на питання і виведи тільки оцінку (позитивні-2, нейтральні-1, негативні-0). Питання: "Які ваші очікування в цьому проєкті щодо набуття нових навичок?". Текст відповіді: '
text0="Прокласифікуй музичні навички людини і виведи тільки цифру класу (високі-2, середні-1, відсутні-0), якщо вона володіє такими музичними інструментами: "
text0="Чи відноситься один з цих музичних інструментів до карпатських народних або фолькльорних (виведи тільки 1-так або 0-ні): "
#Перетвори текст в офіційну адміністративну назву центру місцевості. Виведи тільки цю назву: Полісся
text0='Прокласифікуй текст відповіді на питання і виведи тільки оцінку відповіді (позитивні-2, нейтральні-1, негативні-0). Питання: "Які ваші очікування в цьому проєкті щодо отримання нових знань?". Текст відповіді: '


def llm(text):
    response: ChatResponse = chat(model='qwen3:235b-a22b', messages=[
    {
        'role': 'user',
        'content': text0+text,
    },
    ])
    #print(response['message']['content'])
    print(response.message.content)
    return response.message.content

def parse(text):
    mo=re.match("\<think\>.*\</think\>.*([0-9])", text, re.S)
    if mo:
        return mo.group(1)
    else:
        return ""

csv_file=open("c:\\Users\\Kopei\\Downloads\\form.csv", "r", encoding="utf-8") # відкрити файл для читання
reader=csv.reader(csv_file, delimiter = ';') # об'єкт для читання

C=[]
for row in list(reader)[1:]:
    text=row[33]
    print(text)
    answer=llm(text)
    c=parse(answer)
    C.append([c])

csv_file.close() # закрити файл

csv_file=open("c:\\Users\\Kopei\\Downloads\\form1.csv", "w", newline="") # відкрити файл для запису
writer = csv.writer(csv_file, delimiter = ';') # об'єкт для запису
writer.writerows(C)
#for c in C:
#    writer.writerow([c]) # записати рядок
csv_file.close() # закрити файл

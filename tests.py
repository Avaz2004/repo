def discriminant(a, b, c):
    return (b ** 2) - 4 * a * c


# функция для нахождения корней уравнения
def solution(a, b, c):
    if discriminant(a, b, c) < 0:
        return str('корней нет')
    elif discriminant(a, b, c) == 0:
        x = -b / (2 * a)
        return x
    elif discriminant(a, b, c) > 0:
        x_1 = (-b + discriminant(a, b, c) ** 0.5) / (2 * a)
        x_2 = (-b - discriminant(a, b, c) ** 0.5) / (2 * a)
        return x_1, x_2

def vote(votes):
    count = []
    for i in votes:
        count.append(votes.count(i))
        max_times = max(count)
        n = count.index(max_times)
    return votes[n]


documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }
def get_name(doc_number):
  for numbers in documents:
    if doc_number == numbers['number']:
      return numbers['name']
  return 'Документ не найден'

def get_directory(doc_number):
  for key in directories.keys():
    number_list = directories[key]
    if doc_number in number_list:
      return key
  return 'Полки с таким документом не найдено'

def add(document_type, number, name, shelf_number):
  key = str(shelf_number)
  directories[key].append(number)
  documents.append({'type': document_type, 'number': number, 'name': name})


if __name__ == '__main__':
    print(solution(2, 7, 15))
    print(solution(1, -3, 20))
    print(solution(-4, 25, -26))
    print(solution(1, 1, 1))
    print(solution(0,0,0))

    print(vote([1, 1, 1, 2, 3]))
    print(vote([1, 2, 3, 2, 2]))

    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('passport', '5620 784', 'Павел Петрович', 3)
    print(get_directory("5620 784"))
    print(get_name("5620 784"))
    print(get_directory("5620 783"))
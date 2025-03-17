def total_salary(path: str) -> tuple[int, int]:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total_num = 0
            salary_list = []
            try:
                for item in file:
                    if len(item.strip()) == 0:
                        print('File stores an empty row')
                        return 0, 0

                    item_list = item.strip().split(',')
                    salary_list.append(item_list[-1])
                    total_num = round(total_num + float(item_list[-1]))

                average_num = round(total_num / len(salary_list))
                return total_num, average_num
            except ValueError:
                print('Values error')
                return 0, 0
    except FileNotFoundError as error:
        print(error)
        return 0, 0
    except IOError as error:
        print(error)
        return 0, 0
    except Exception as error:
        print(error)
        return 0, 0

total, average = total_salary('salaries.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

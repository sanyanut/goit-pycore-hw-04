def get_cats_info(path: str) -> list|None:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_dict = []
            try:
                for line in file:
                    if len(line.strip()) == 0:
                        print('File stores an empty row')
                        return None

                    cat_line = line.strip().split(',')
                    new_cat_dict = {
                        'id': cat_line[0],
                        'name': cat_line[1],
                        'age': cat_line[2],
                    }
                    cats_dict.append(new_cat_dict)
                return cats_dict
            except Exception as error:
                print(error)
                return None
    except FileNotFoundError as error:
        print(error)
        return None
    except Exception as error:
        print(error)
        return None

cats_info = get_cats_info('cats.txt')
print(cats_info)
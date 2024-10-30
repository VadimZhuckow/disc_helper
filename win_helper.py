import subprocess
import re

def disk_usage():
    try:
        result = subprocess.run(['wmic', 'logicaldisk', 'get', 'name,freespace,size'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('utf-8')

        if result.stderr:
            print("Ошибка при выполнении команды wmic:", result.stderr.decode('utf-8'))
            return

        lines = output.strip().splitlines()

        if len(lines) < 2:
            print("Нет доступных дисков или неверный вывод команды.")
            return

        for line in lines[1:]:
            line = line.strip()
            if line:
                print(f"Обработанная строка: '{line}'")

                match = re.match(r'(\S+)\s+(\S+)\s+(\S+)', line)
                if match:
                    free_space, drive_letter, total_space = match.groups()

                    if free_space.isdigit() and total_space.isdigit():
                        free_space = int(free_space)
                        total_space = int(total_space)
                        used_space = total_space - free_space
                        print(
                            f"{drive_letter} использовано {used_space / (1024 ** 3):.2f} ГБ из {total_space / (1024 ** 3):.2f} ГБ ({free_space / (1024 ** 3):.2f} ГБ свободно)")
                    else:
                        print(
                            f"Неверные данные для диска {drive_letter}: свободное пространство = '{free_space}', общее пространство = '{total_space}'")
                else:
                    print(f"Неверный формат строки: '{line}'")
            else:
                print("Пустая строка, пропускаем.")

    except Exception as e:
        print("Произошла ошибка:", str(e))


disk_usage()

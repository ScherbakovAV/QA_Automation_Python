### Задание 1.

Дополнить проект фикстурой, которая после каждого шага теста
дописывает в заранее созданный файл stat.txt строку вида:
* время
* кол-во файлов из конфига
* размер файла из конфига
* статистика загрузки процессора из файла /proc/loadavg
(можно писать просто всё содержимое этого файла).

### Задание 2. (дополнительное задание)

Дополнить все тесты ключом команды 7z -t (тип архива).
Вынести этот параметр в конфиг.

### Решение:
* добавлена фикстура *write_stat* в *confitest.py*, записывающая лог после каждого шага тестов в файл *stat.txt*
* в файл *config.yaml* добавлено два параметра для расширений архива: существующего и несуществующего
* параметры для расширений интегрированы в тесты
* в тесты для создания архива добавлен ключ -t с целью изменения типа архива
* добавлен негативный тест для проверки создания архива с несуществующим расширением
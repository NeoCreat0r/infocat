# InfoCat - OSINT System
Компактная утилита для сбора информации о системе. Дает большое количество данных и возможность владельцу оставаться в тени. Управление производиться при помощи Telegram бота.
## Description
![logo](https://github.com/NeoCreat0r/infocat/blob/main/infocat.png)

Давай теперь разберем, что подразумевается под словом "данные". Ведь список составляет большое количество терминов при упоминании такого слова. А собирает утилита такую информацию:

 1. IP адрес
 2. MAC адрес
 3. Имя пользователя
 4. Тип операционной системы
 5. Скорость работы системы
 6. Время
 7. Скриншот
 8. Скорость интернет-соединения
 9. Модель процессора
 10. Частота процессора (минимальная/максимальная/средняя)
 11. Звук с микрофона (длительность записи в секундах)
 12. Запущенные процессы
 
Имеется два режима работы:
 * Скрытый
 * Публичный
 
Чтобы изменить режим работы требуется сменить расширение готового файла. **py** отвечает за открытую, публичную работу. Соответственно **pyw** является его соперником и делает все действия без назойливого окна консоли.
 
### Warning
Для работы программы исполняемый файл обязан распологаться в той же директории, что и иконка вместе с логотипом. В противном случаи программа не будет работать.

### TIPS
Компиляция готвого system-файла происходит при помощи утилиты **pyinstaller** с использованием команды:
* `pyinstaller -F -i путь_до_иконки --onefile путь_до_файла_system.py`

Если в конечном счете вы получаете ошибку следует обновить все используемые программой модули. Чтобы получить все данные отправьте своему боту команду _/start_ и ожидайте результата. При отправке множества команд программа крашнется и на устройстве не будут удалены файлы, а тебе придет множество копий файлов.


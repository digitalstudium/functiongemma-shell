sample_dataset = [
    # --- check_website ---
    {
        "user_content": "ya.ru",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"ya.ru"}',
    },
    {
        "user_content": "сайт ya.ru",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"ya.ru"}',
    },
    {
        "user_content": "проверь ya.ru",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"ya.ru"}',
    },
    {
        "user_content": "проверь, открывается ли ya.ru",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"ya.ru"}',
    },
    {
        "user_content": "проверь доступность https://ya.ru",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"https://ya.ru"}',
    },
    {
        "user_content": "проверь статус сайта google.com",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"google.com"}',
    },
    {
        "user_content": "доступен ли google.com?",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"google.com"}',
    },
    {
        "user_content": "проверь https://example.com",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"https://example.com"}',
    },
    {
        "user_content": "узнай, отвечает ли example.com",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"example.com"}',
    },
    {
        "user_content": "проверь, жив ли github.com",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"github.com"}',
    },
    {
        "user_content": "проверка сайта https://github.com",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"https://github.com"}',
    },
    {
        "user_content": "посмотри, работает ли https://openai.com",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"https://openai.com"}',
    },
    {
        "user_content": "проверь доступность openai.com",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"openai.com"}',
    },
    {
        "user_content": "сайт https://stackoverflow.com доступен?",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"https://stackoverflow.com"}',
    },
    {
        "user_content": "проверь, открывается ли stackoverflow.com",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"stackoverflow.com"}',
    },
    {
        "user_content": "проверь https://news.ycombinator.com",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"https://news.ycombinator.com"}',
    },
    {
        "user_content": "проверь доступность news.ycombinator.com",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"news.ycombinator.com"}',
    },
    {
        "user_content": "проверь, отвечает ли https://httpstat.us/200",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"https://httpstat.us/200"}',
    },
    {
        "user_content": "проверь, отвечает ли https://httpstat.us/404",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"https://httpstat.us/404"}',
    },
    {
        "user_content": "проверь, отвечает ли https://httpstat.us/500",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"https://httpstat.us/500"}',
    },
    {
        "user_content": "проверь, отвечает ли https://httpstat.us/503",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"https://httpstat.us/503"}',
    },
    {
        "user_content": "проверь https://www.python.org",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"https://www.python.org"}',
    },
    {
        "user_content": "работает ли www.python.org?",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"www.python.org"}',
    },
    {
        "user_content": "проверь https://ru.wikipedia.org",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"https://ru.wikipedia.org"}',
    },
    {
        "user_content": "доступна ли ru.wikipedia.org",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"ru.wikipedia.org"}',
    },
    {
        "user_content": "проверь https://ya.ru:443",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"https://ya.ru:443"}',
    },
    {
        "user_content": "проверь http://example.com",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"http://example.com"}',
    },
    {
        "user_content": "проверь https://example.com/?q=test",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"https://example.com/?q=test"}',
    },
    {
        "user_content": "сайт corporate.internal.local доступен?",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"corporate.internal.local"}',
    },
    {
        "user_content": "проверь dev.internal",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"dev.internal"}',
    },
    {
        "user_content": "проверь статус https://intranet.local",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"https://intranet.local"}',
    },
    {
        "user_content": "проверь https://localhost",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"https://localhost"}',
    },
    {
        "user_content": "проверь http://127.0.0.1",
        "tool_name": "check_website",
        "tool_arguments": '{"url":"http://127.0.0.1"}',
    },
    # --- find_largest_file ---
    {
        "user_content": "найди самый большой файл в текущей папке",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"."}',
    },
    {
        "user_content": "какой самый большой файл здесь?",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"."}',
    },
    {
        "user_content": "покажи самый большой файл в .",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"."}',
    },
    {
        "user_content": "найди самый большой файл в /var/log",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/var/log"}',
    },
    {
        "user_content": "самый большой файл в /tmp",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/tmp"}',
    },
    {
        "user_content": "найди самый большой файл в /usr",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/usr"}',
    },
    {
        "user_content": "покажи крупнейший файл в /opt",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/opt"}',
    },
    {
        "user_content": "найди самый большой файл в /etc",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/etc"}',
    },
    {
        "user_content": "найди самый большой файл в /home",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/home"}',
    },
    {
        "user_content": "проверь, какой самый большой файл в моей домашней папке",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"~"}',
    },
    {
        "user_content": "найди самый большой файл в ~/Downloads",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"~/Downloads"}',
    },
    {
        "user_content": "самый большой файл в ~/Документы",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"~/Документы"}',
    },
    {
        "user_content": "найди самый большой файл в ~/Desktop",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"~/Desktop"}',
    },
    {
        "user_content": "найди самый большой файл в /srv",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/srv"}',
    },
    {
        "user_content": "найди самый большой файл в /mnt",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/mnt"}',
    },
    {
        "user_content": "найди самый большой файл в /media",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/media"}',
    },
    {
        "user_content": "покажи самый большой файл в /var",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/var"}',
    },
    {
        "user_content": "самый большой файл в /var/tmp",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/var/tmp"}',
    },
    {
        "user_content": "найди самый большой файл в /root",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/root"}',
    },
    {
        "user_content": "найди самый большой файл в /boot",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/boot"}',
    },
    {
        "user_content": "какой самый большой файл в /bin?",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/bin"}',
    },
    {
        "user_content": "покажи крупнейший файл в /sbin",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/sbin"}',
    },
    {
        "user_content": "найди самый большой файл в /lib",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/lib"}',
    },
    {
        "user_content": "найди самый большой файл в /lib64",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/lib64"}',
    },
    {
        "user_content": "проверь /run — какой там самый большой файл",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/run"}',
    },
    {
        "user_content": "найди самый большой файл в /var/cache",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/var/cache"}',
    },
    {
        "user_content": "самый большой файл в /var/lib",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/var/lib"}',
    },
    {
        "user_content": "найди самый большой файл в /var/www",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/var/www"}',
    },
    {
        "user_content": "найди самый большой файл в /home/user",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/home/user"}',
    },
    {
        "user_content": "покажи крупнейший файл в /data",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/data"}',
    },
    {
        "user_content": "найди самый большой файл в /workspace",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"/workspace"}',
    },
    {
        "user_content": "какой самый большой файл в ../",
        "tool_name": "find_largest_file",
        "tool_arguments": '{"directory":"../"}',
    },
    # --- get_system_info ---
    {"user_content": "система", "tool_name": "get_system_info", "tool_arguments": "{}"},
    {
        "user_content": "инфо о системе",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "покажи информацию о системе",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "выведи данные о системе",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "какая у меня операционная система?",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "узнай версию ОС и ядра",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "какой hostname у машины?",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "покажи hostname и сведения о системе",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "сколько ядер CPU?",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "сколько потоков/ядер у процессора?",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "сколько оперативной памяти доступно?",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "покажи объем RAM",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "сколько места на диске осталось?",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "проверь свободное место на дисках",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "дай сводку: ОС, CPU, RAM, диск",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "покажи системные характеристики",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "какая архитектура системы?",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "хочу узнать параметры сервера",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "что за машина: cpu/память/диск/хост?",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "выведи информацию о железе и ОС",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "покажи текущие системные ресурсы",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "узнай, сколько всего диска и сколько свободно",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "сколько памяти и дискового пространства?",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "покажи сведения о платформе",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "мне нужны системные данные (hostname, os, cpu)",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "собери краткую информацию о системе",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "посмотри, какая система установлена",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "проверь конфигурацию сервера",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "какие ресурсы доступны на этой машине?",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
    {
        "user_content": "покажи данные: hostname, cpu cores, ram, disk",
        "tool_name": "get_system_info",
        "tool_arguments": "{}",
    },
]

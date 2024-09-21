import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sys

# Попытка импорта ttkthemes
try:
    from ttkthemes import ThemedTk

    print("ttkthemes успешно импортирован")
except ImportError:
    print("Не удалось импортировать ttkthemes. Используем стандартный Tk.")
    ThemedTk = tk.Tk


class WebsiteTutorialApp:
    def __init__(self, root):
        print("Инициализация WebsiteTutorialApp")
        self.root = root
        self.root.title("Создание Вашего Первого Сайта")
        self.root.geometry("1200x700")  # Увеличенная ширина окна

        self.style = ttk.Style()
        self.style.configure("TButton", padding=10, font=("Arial", 12))
        self.style.configure("TLabel", font=("Arial", 12))
        self.style.configure("Header.TLabel", font=("Arial", 18, "bold"))

        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.current_step = 0
        self.selected_html_code = None
        self.selected_css_code = None
        self.selected_js_code = None

        self.examples = {
            "html": {
                "name": "Улучшенный макет",
                "code": """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Мой Первый Сайт</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="site-header">
        <nav class="main-nav">
            <ul class="nav-list">
                <li class="nav-item"><a href="#home" class="nav-link">Главная</a></li>
                <li class="nav-item"><a href="#about" class="nav-link">О нас</a></li>
                <li class="nav-item"><a href="#services" class="nav-link">Услуги</a></li>
                <li class="nav-item"><a href="#contact" class="nav-link">Контакты</a></li>
            </ul>
        </nav>
    </header>
    <main class="main-content">
        <section id="home" class="hero">
            <h1 class="hero-title">Добро пожаловать на мой сайт</h1>
            <p class="hero-text">Здесь вы найдете много интересной информации.</p>
            <button id="cta-button" class="cta-button">Узнать больше</button>
        </section>
        <section id="about" class="about-section">
            <h2 class="section-title">О нас</h2>
            <p class="section-text">Мы - команда энтузиастов, создающих удивительные веб-сайты.</p>
        </section>
        <section id="services" class="services-section">
            <h2 class="section-title">Наши услуги</h2>
            <ul class="services-list">
                <li class="service-item">Веб-дизайн</li>
                <li class="service-item">Разработка</li>
                <li class="service-item">SEO-оптимизация</li>
            </ul>
        </section>
        <section id="contact" class="contact-section">
            <h2 class="section-title">Свяжитесь с нами</h2>
            <form id="contact-form" class="contact-form">
                <input type="text" id="name" name="name" placeholder="Ваше имя" required>
                <input type="email" id="email" name="email" placeholder="Ваш email" required>
                <textarea id="message" name="message" placeholder="Ваше сообщение" required></textarea>
                <button type="submit" class="submit-button">Отправить</button>
            </form>
        </section>
    </main>
    <footer class="site-footer">
        <p class="footer-text">&copy; 2024 Мой Первый Сайт. Все права защищены.</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>""",
                "explanations": {
                    "<body>": "Содержит все видимое содержимое веб-страницы",
                    "<header class=\"site-header\">": "Верхняя часть сайта, обычно содержит логотип и главное меню",
                    "<nav class=\"main-nav\">": "Главная навигация сайта",
                    "<ul class=\"nav-list\">": "Список элементов меню",
                    "<li class=\"nav-item\">": "Отдельный пункт меню",
                    "<a href=\"#home\" class=\"nav-link\">": "Ссылка на секцию 'Главная' с классом для стилизации",
                    "<main class=\"main-content\">": "Основное содержимое страницы",
                    "<section id=\"home\" class=\"hero\">": "Секция-герой, первый экран сайта",
                    "<h1 class=\"hero-title\">": "Главный заголовок страницы",
                    "<button id=\"cta-button\" class=\"cta-button\">": "Кнопка призыва к действию",
                    "<section id=\"about\" class=\"about-section\">": "Секция 'О нас'",
                    "<h2 class=\"section-title\">": "Заголовок секции",
                    "<ul class=\"services-list\">": "Список услуг",
                    "<form id=\"contact-form\" class=\"contact-form\">": "Форма обратной связи",
                    "<input type=\"text\">": "Текстовое поле ввода",
                    "<textarea>": "Многострочное текстовое поле",
                    "<footer class=\"site-footer\">": "Нижняя часть сайта, обычно содержит копирайт и дополнительные ссылки",
                    "<script src=\"script.js\">": "Подключение внешнего JavaScript файла"
                }
            },
            "css": {
                "name": "Улучшенные стили",
                "code": """/* Глобальные стили */
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    color: #333;
}

/* Стили заголовка */
.site-header {
    background-color: #3498db;
    padding: 1rem;
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 1000;
}

.nav-list {
    list-style-type: none;
    padding: 0;
    display: flex;
    justify-content: center;
}

.nav-item {
    margin: 0 15px;
}

.nav-link {
    color: white;
    text-decoration: none;
    font-weight: bold;
    transition: color 0.3s ease;
}

.nav-link:hover {
    color: #ecf0f1;
}

/* Стили основного содержимого */
.main-content {
    padding-top: 60px; /* Учитываем высоту фиксированного заголовка */
}

.hero {
    background-color: #ecf0f1;
    text-align: center;
    padding: 100px 20px;
}

.hero-title {
    font-size: 2.5em;
    margin-bottom: 20px;
}

.cta-button {
    background-color: #e74c3c;
    color: white;
    border: none;
    padding: 10px 20px;
    font-size: 1.2em;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.cta-button:hover {
    background-color: #c0392b;
}

/* Стили секций */
.section-title {
    text-align: center;
    margin-bottom: 30px;
}

.about-section, .services-section, .contact-section {
    padding: 50px 20px;
}

.services-list {
    list-style-type: none;
    padding: 0;
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
}

.service-item {
    background-color: #3498db;
    color: white;
    padding: 20px;
    margin: 10px;
    border-radius: 5px;
    text-align: center;
    flex-basis: calc(33.333% - 20px);
}

/* Стили формы */
.contact-form {
    max-width: 500px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
}

.contact-form input,
.contact-form textarea {
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
}

.submit-button {
    background-color: #2ecc71;
    color: white;
    border: none;
    padding: 10px 20px;
    font-size: 1.1em;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.submit-button:hover {
    background-color: #27ae60;
}

/* Стили футера */
.site-footer {
    background-color: #34495e;
    color: white;
    text-align: center;
    padding: 1rem;
    margin-top: 50px;
}""",
                "explanations": {
                    "body": "Стили для всего тела документа",
                    ".site-header": "Стили для шапки сайта",
                    ".nav-list": "Стили для списка навигации",
                    ".nav-item": "Стили для элементов навигации",
                    ".nav-link": "Стили для ссылок в навигации",
                    ".main-content": "Стили для основного содержимого",
                    ".hero": "Стили для героя-секции (первого экрана)",
                    ".cta-button": "Стили для кнопки призыва к действию",
                    ".section-title": "Стили для заголовков секций",
                    ".services-list": "Стили для списка услуг",
                    ".service-item": "Стили для отдельной услуги",
                    ".contact-form": "Стили для формы обратной связи",
                    ".submit-button": "Стили для кнопки отправки формы",
                    ".site-footer": "Стили для футера сайта",
                    "transition": "Добавляет плавный переход при изменении свойств",
                    "flex-basis": "Задает базовый размер flex-элемента",
                    "z-index": "Управляет порядком наложения элементов"
                }
            },
            "js": {
                "name": "Интерактивные элементы",
                "code": """// Ждем, пока весь DOM загрузится
document.addEventListener('DOMContentLoaded', () => {
    // Получаем необходимые элементы
    const ctaButton = document.getElementById('cta-button');
    const contactForm = document.getElementById('contact-form');
    const navLinks = document.querySelectorAll('.nav-link');

    // Обработчик для кнопки CTA
    ctaButton.addEventListener('click', () => {
        alert('Спасибо за ваш интерес! Мы свяжемся с вами в ближайшее время.');
    });

    // Обработчик отправки формы
    contactForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;

        console.log('Отправка формы:', { name, email, message });
        alert('Форма отправлена успешно!');
        contactForm.reset();
    });

    // Плавная прокрутка для навигационных ссылок
    navLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Анимация появления элементов при прокрутке
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    function handleScrollAnimation() {
        const elements = document.querySelectorAll('.service-item, .section-title, .hero-title');
        elements.forEach(el => {
            if (isElementInViewport(el)) {
                el.classList.add('visible');
            }
        });
    }

    window.addEventListener('scroll', handleScrollAnimation);
    handleScrollAnimation();
});""",
                "explanations": {
                    "document.addEventListener('DOMContentLoaded', () => {": "Выполняет код после загрузки DOM",
                    "document.getElementById": "Получает элемент по его id",
                    "document.querySelectorAll": "Получает все элементы, соответствующие селектору",
                    "addEventListener": "Добавляет обработчик события к элементу",
                    "event.preventDefault()": "Предотвращает действие по умолчанию (например, отправку формы)",
                    "contactForm.reset()": "Сбрасывает все поля формы",
                    "link.getAttribute('href')": "Получает значение атрибута href",
                    "targetElement.scrollIntoView()": "Плавно прокручивает страницу к указанному элементу",
                    "isElementInViewport": "Проверяет, находится ли элемент в видимой области экрана",
                    "getBoundingClientRect()": "Возвращает размер элемента и его позицию относительно viewport",
                    "classList.add()": "Добавляет CSS класс к элементу",
                    "window.addEventListener('scroll')": "Добавляет обработчик события прокрутки страницы"
                }
            }
        }

        self.show_start_screen()

    def show_start_screen(self):
        print("Отображение начального экрана")
        self.current_step = 0  # Сбрасываем шаг в начало
        self.clear_frame()
        ttk.Label(self.main_frame, text="Добро пожаловать в Мир Веб-Разработки!", style="Header.TLabel").pack(pady=20)
        ttk.Label(self.main_frame, text="Этот интерактивный туториал проведет вас через основные шаги создания вашего первого веб-сайта.").pack(pady=10)
        ttk.Label(self.main_frame, text="Вы изучите основы HTML, CSS и JavaScript - три ключевых инструмента веб-разработки.").pack(pady=10)
        ttk.Button(self.main_frame, text="Начать Путешествие", command=self.next_step).pack(pady=20)

    def next_step(self):
        print("Переход к следующему шагу")
        self.current_step += 1
        if self.current_step == 1:
            self.show_html_step()
        elif self.current_step == 2:
            self.show_css_step()
        elif self.current_step == 3:
            self.show_js_step()
        elif self.current_step == 4:
            self.create_website()

    def show_html_step(self):
        print("Отображение шага HTML")
        self.clear_frame()
        self.show_step("HTML", "HTML (HyperText Markup Language) - это основа любого веб-сайта.\nОн определяет структуру и содержание вашей страницы.", self.examples["html"])

    def show_css_step(self):
        print("Отображение шага CSS")
        self.clear_frame()
        self.show_step("CSS", "CSS (Cascading Style Sheets) отвечает за внешний вид вашего сайта.\nС помощью CSS вы можете изменять цвета, шрифты, расположение элементов и многое другое.", self.examples["css"])

    def show_js_step(self):
        print("Отображение шага JavaScript")
        self.clear_frame()
        self.show_step("JavaScript", "JavaScript делает ваш сайт интерактивным и динамичным.\nС его помощью вы можете реагировать на действия пользователя и изменять содержимое страницы.", self.examples["js"])

    def show_step(self, title, description, example):
        print(f"Отображение шага: {title}")
        ttk.Label(self.main_frame, text=f"Шаг {self.current_step}: {title}", style="Header.TLabel").pack(pady=20)
        ttk.Label(self.main_frame, text=description).pack(pady=10)

        code_frame = ttk.Frame(self.main_frame)
        code_frame.pack(fill=tk.BOTH, expand=True)

        self.code_editor = tk.Text(code_frame, wrap=tk.NONE, width=60, height=20, font=("Courier", 10))
        self.code_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.code_editor.insert(tk.END, example["code"])

        x_scrollbar = ttk.Scrollbar(self.main_frame, orient="horizontal", command=self.code_editor.xview)
        x_scrollbar.pack(fill="x")
        self.code_editor.configure(xscrollcommand=x_scrollbar.set)

        self.explanation_text = tk.Text(code_frame, wrap=tk.WORD, width=40, height=20, font=("Arial", 10))
        self.explanation_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.explanation_text.config(state=tk.DISABLED)

        self.code_editor.bind("<Motion>", self.show_explanation)

        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(pady=20)
        ttk.Button(button_frame, text="Назад", command=self.previous_step).pack(side="left", padx=10)
        ttk.Button(button_frame, text="Далее", command=self.next_step).pack(side="left", padx=10)

        # Сохраняем выбранный код для текущего шага
        if self.current_step == 1:
            self.selected_html_code = example["code"]
        elif self.current_step == 2:
            self.selected_css_code = example["code"]
        elif self.current_step == 3:
            self.selected_js_code = example["code"]

    def show_explanation(self, event):
        index = self.code_editor.index(f"@{event.x},{event.y}")
        line, col = map(int, index.split("."))
        text = self.code_editor.get(f"{line}.0", f"{line}.end")
        example = self.examples[self.get_current_language()]
        explanations = example["explanations"]

        self.explanation_text.config(state=tk.NORMAL)
        self.explanation_text.delete("1.0", tk.END)

        for key, value in explanations.items():
            if key in text:
                self.explanation_text.insert(tk.END, f"{key}:\n{value}\n\n")
                break

        self.explanation_text.config(state=tk.DISABLED)

    def get_current_language(self):
        if self.current_step == 1:
            return "html"
        elif self.current_step == 2:
            return "css"
        elif self.current_step == 3:
            return "js"

    def previous_step(self):
        print("Переход к предыдущему шагу")
        if self.current_step > 1:
            self.current_step -= 1
            if self.current_step == 1:
                self.show_html_step()
            elif self.current_step == 2:
                self.show_css_step()
            elif self.current_step == 3:
                self.show_js_step()
        else:
            self.show_start_screen()

    def create_website(self):
        print("Создание сайта")
        # Используем выбранные коды для создания файлов
        html_content = self.selected_html_code if self.selected_html_code else self.examples["html"]["code"]
        css_content = self.selected_css_code if self.selected_css_code else self.examples["css"]["code"]
        js_content = self.selected_js_code if self.selected_js_code else self.examples["js"]["code"]

        # Создаем директорию для сайта
        directory = filedialog.askdirectory(title="Выберите директорию для сохранения сайта")
        if directory:
            try:
                # Создаем HTML файл
                with open(f"{directory}/index.html", 'w', encoding='utf-8') as file:
                    file.write(html_content)

                # Создаем CSS файл
                with open(f"{directory}/styles.css", 'w', encoding='utf-8') as file:
                    file.write(css_content)

                # Создаем JavaScript файл
                with open(f"{directory}/script.js", 'w', encoding='utf-8') as file:
                    file.write(js_content)

                messagebox.showinfo("Успех", "Ваш сайт успешно создан!")
                self.show_congratulations()
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось создать сайт: {e}")
        else:
            print("Создание сайта отменено")

    def show_congratulations(self):
        print("Отображение поздравления")
        self.clear_frame()
        ttk.Label(self.main_frame, text="Поздравляем!", style="Header.TLabel").pack(pady=20)
        ttk.Label(self.main_frame, text="Вы успешно создали свой первый веб-сайт!").pack(pady=10)
        ttk.Label(self.main_frame, text="Теперь вы можете открыть файл index.html в браузере и увидеть результат.").pack(pady=10)
        ttk.Label(self.main_frame, text="Продолжайте изучать веб-разработку и создавайте удивительные проекты!").pack(pady=10)
        ttk.Button(self.main_frame, text="Начать заново", command=self.show_start_screen).pack(pady=20)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

def main():
    print(f"Python version: {sys.version}")
    print("Запуск главной функции")
    try:
        root = ThemedTk(theme="arc")
        print("ThemedTk инициализирован")
    except Exception as e:
        print(f"Ошибка при инициализации ThemedTk: {e}")
        print("Использование стандартного Tk")
        root = tk.Tk()

    app = WebsiteTutorialApp(root)
    print("WebsiteTutorialApp создан")
    root.mainloop()
    print("Главный цикл завершен")

if __name__ == "__main__":
    main()
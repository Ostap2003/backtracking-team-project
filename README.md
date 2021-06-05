# :leftwards_arrow_with_hook: Вирішення задач за допомогою бектрекінгу

## :large_blue_circle: Лабіринт

Розроблена програма, що опрацьовує лабіринт у форматі списку списків. Головний клас - ```PathFinder``` отримує 2 ключових параметри: координати початку (входу) лабіринту та його координати кінця лабіринту (виходу) і також є 3 додаткові параметри:
- **maze** - користувач може передати готовий лабіринт у форматі списку списків
- **path** - якщо не дано готовий лабіринт maze, користувач може вказати шлях до текстового файлу із заданим лабіринтом
- **draw_maze** - булеве значення, відповідає за графічне представлення проходження лабіринту за допомогою бібліотеки ```turtle```. Дефолтне значення - ```False```.

Головний метод класу - ```find_path()```, саме він містить алгоритм знахдження шляху від стартової точки до фінішної. Алгоритм працює за принципом backtracking:
```python
current_position = start_position
stack add current_posotion
mark curr_cell as a path
while current_position != exit_position:
    check if neighboring cells are unvisited (up, right, left, bottom)
    if neighboring cell is unvisited:
        mark it as path
        current_position = unvisited_cell
        add it to the stack
    elif all neighboring cells are visited or are walls:
        pop last position from the stack
        set popped cell as used cell
```
<br></br>
**Приклад роботи програми:**
<br>
![](https://github.com/Ostap2003/backtracking-team-project/blob/main/img/maze_solution.png)
<br>
<br>
_<a href="https://github.com/Ostap2003/backtracking-team-project/wiki/Solving-mazes">Дізнатись більше</a>_

## :large_blue_circle: Кросворд
**Кросворд** представляє собою прямокутник, заповнений буквами, де кожен рядок та колонка — окреме слово.
<br>
Для реалізації було використано **бектрекінг**, тобто кожна клітинка окремо заповнювалася, а якщо жодна буква не підходить, 
то звільняється попередня клітинка та заповнюється іншою літерою.
<br>
<br>
Було вирішено **не перебирати літери по алфавіту**, а за порядком, при якому можна згенерувати **якнайбільше слів**. Для цього 
створюється словник із кожною літерою алфавіту, як ключем,
та кількість всіх можливих слів, які існують, якби ця літера була б на певний позиції.
<br>

_<a href="https://github.com/Ostap2003/backtracking-team-project/wiki/Crossword">Дізнатись більше</a>_

## :large_blue_circle: Розфарбування графа
У теці **m_coloring_problem** знаходиться модуль **graph_coloring.py**, який містить клас `Graph` для знаходження розфарбування графа за його матрицею  суміжності.

Алгоритм полягає в тому, щоб присвоювати кольори **по одному** різним вершинам. 
Перш ніж призначати колір, перевіряємо **безпеку** даного кольора для вже призначених кольорів **суміжних** вершин, тобто перевіряємо, 
чи мають сусідні вершини однаковий колір чи ні.
<br>
Якщо існує призначення кольору, яке не порушує умови, то додаємо це присвоєння до часткового розв'язку. 
Якщо призначення кольору неможливе, то повертаємось назад і повертаємо false.
<br><br>
**Приклад використання:**
```
>>> adj_matrix = [[0, 1, 1, 1],
                  [1, 0, 1, 0],
                  [1, 1, 0, 1],
                  [1, 0, 1, 0]]
>>> graph = Graph(adj_matrix)
>>> graph.get_graph_coloring(4)
>>> Solution for coloring current graph with 4 colors:
>>> [1, 2, 3, 2]

>>> graph.get_graph_coloring(1)
>>> Coloring current graph with 1 colors is impossible
>>> False
```
_<a href="https://github.com/Ostap2003/backtracking-team-project/wiki/Graph-m-coloring-problem">Дізнатись більше</a>_

## :large_blue_circle: Судоку
Пошук правильної комбінації цифр, який є рішенням судоку, реалізований на основі **алгоритму бектрекінгу**.
<br><br>
Створюється клас, у який може передаватися список списків (**матриця**) початкового стану судоку в належному вигляді 
або шлях до файлу. Якщо передається файл, викликається допоміжний метод, щоб його прочитати та перезаписати інформацію
у список (матрицю). Далі викликається **метод для перевірки**, чи значення в списку відповідають умові (тобто належать цифрі
на проміжку [0, 9]). В кінці конструктор викликає функцію для розширення доступу до інформації, яка заповнює списки 
стовпців та квадратів на основі вже готового (заданого) списку рядків.
<br><br>
Для заповнення списку до стану вирішеного судоку потрібно викликати рекурсивну функцію, 
яка заповнює список на основі бектрекінгу та передати значення 0, 0 (початок списку). 
**Рекурсія працює наступним чином:** Спочатку перевіряється, чи в комірці вже є цифра, відмінна від нуля; якщо ні, 
то на проміжку від 1 до 9 включно шукається перша можлива цифра, якої ще немає в поточному рядку, стовпчику 
та квадраті. Розраховуються індекси наступної комірки та від них викликається ця ж функція. 
<br><br>
Якщо рекурсія знаходиться на останній можливій клітинці (8, 8), то, якщо вдалось підібрати цифру, повертається True. 
Рекурсія повертає False, якщо не підходить жодна цифра. Якщо рекурсія від наступної клітинки повертає False, рекурсія
продовжує перебирати варіанти. Рекурсія також повертає True, якщо від наступної клітинки вона повернула True, що і
забезпечує вихід з рекурсії. Результати вирішеного судоку зберігаються в списках (атрибутах) класу.

<br>
**Фрагмент з візуалізації:**


![](https://github.com/Ostap2003/backtracking-team-project/blob/main/img/sudoku_visual.jpg)
<br>
_<a href="https://github.com/Ostap2003/backtracking-team-project/wiki/Sudoku">Дізнатись більше</a>_





## :busts_in_silhouette: Над проєктом працювали:
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/UstymHanyk/"><img src="https://avatars.githubusercontent.com/u/25267338?v=4" width="100px;" alt=""/><br /></a><b>Устим Ганик</b><br />реалізував розфарбування графів <hr> <a href="https://github.com/Ostap2003/backtracking-team-project/commits?author=UstymHanyk" title="Code">:memo: коміти учасника</a></td>
    <td align="center"><a href="https://github.com/Ostap2003"><img src="https://avatars.githubusercontent.com/u/71087467?v=4" width="100px;" alt=""/><br /></a><b>Остап Дутка</b><br />розробив знаходження шляху в лабіринті <hr><a href="https://github.com/Ostap2003/backtracking-team-project/commits?author=Ostap2003" title="Code">:memo: коміти учасника</a></td>
    <td align="center"><a href="https://github.com/tkachyshyn"><img src="https://avatars.githubusercontent.com/u/70962806?v=4" width="100px;" alt=""/><br /></a><b>Анастасія Ткачишин</b><br />створила розв'язання кросвордів <hr><a href="https://github.com/Ostap2003/backtracking-team-project/commits?author=tkachyshyn" title="Code">:memo: коміти учасника</a></td>
  </tr>

  <tr >
    <td align="center"><a href="https://github.com/MykhailoBronytskyi"><img src="https://avatars.githubusercontent.com/u/71325627?v=4" width="100px;" alt=""/><br /></a><b>Михайло Броницький</b><br />реалізував вирішення криптофриметичних пазлів<hr><a href="https://github.com/Ostap2003/backtracking-team-project/commits?author=MykhailoBronytskyi" title="Code">:memo: коміти учасника</a></td>
    <td align="center"><a href="https://github.com/krasniukk"><img src="https://avatars.githubusercontent.com/u/72805134?v=4" width="100px;" alt=""/><br /></a><b>Тетяна Краснюк</b><br />розробила вирішення судоку<hr><a href="https://github.com/Ostap2003/backtracking-team-project/commits?author=krasniukk" title="Code">:memo: коміти учасника</a></td>
    <td align="center"><a href="https://github.com/Ostap2003/backtracking-team-project/wiki"><h2>Вікі проєкту :books:</h2></a></td>
  </tr>
</table>


<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## :closed_lock_with_key: Ліцензія:

[MIT](https://choosealicense.com/licenses/mit/)
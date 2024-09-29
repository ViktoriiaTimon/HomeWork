adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
new = adwentures_of_tom_sawer.replace("\n", " ")
print(new)
# task 02 ==

""" Замініть .... на пробіл
"""
dot_off = new.replace("....", " ")
print (dot_off)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
gap_off = dot_off.split()
line = " ".join(dot_off.split())
print(line)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = line.count('h')
print(count_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
line_word = line.split()
upper_word_count = 0
for word in line_word:
    if word[0].isupper():
        upper_word_count += 1
print(upper_word_count)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_tom = line_word.index("Tom")
print(first_tom)
second_tom = line_word.index("Tom", first_tom + 1)
print(second_tom)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer_sentences =line.split('.') #I used the edited sentence version
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith("By the time"):
        print(f'The sentence is present "{sentence.strip()}"')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
if adwentures_of_tom_sawer_sentences[-1].strip() == '':
    last_sentence = adwentures_of_tom_sawer_sentences[-2].strip()
print(last_sentence)
print(len(last_sentence.split()))
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import collections
from datetime import datetime as dt
from collections import Counter

print(os.listdir("C:/Users/1201065/2 Module_2"))


# In[2]:


# Читаем файл.
data = pd.read_csv('data.csv')

# Выводим на экран первые 5 строк.
data.head()


# In[3]:


# Определяем длину датасета.
len(data)


# # Предобработка датасета

# In[4]:


# Создаем список с ответами.
answer_ls = []

# Новые колонки в датасете: profit (profit = revenue-budget), month.


# # 1. У какого фильма из списка самый большой бюджет?
# Варианты ответов:
# 1. The Dark Knight Rises (tt1345836)
# 2. Spider-Man 3 (tt0413300)
# 3. Avengers: Age of Ultron (tt2395427)
# 4. The Warrior's Way	(tt1032751)
# 5. Pirates of the Caribbean: On Stranger Tides (tt1298650)

# In[5]:


# Выводим информацию о датасете.
#data.info()

# Удаляем дубликаты по столбцу 'imdb_id'.
data.drop_duplicates(subset = 'imdb_id', keep = 'first', inplace = True)

# Фильтруем датасет по условию: фильм с самым большим бюджетом.
film_max_budget = data[data['budget'] == data['budget'].max()]
film_max_budget

# Добавлем номер ответа в список с ответами.
answer_ls.append(4)


# # 2. Какой из фильмов самый длительный (в минутах)
# 1. The Lord of the Rings: The Return of the King	(tt0167260)
# 2. Gods and Generals	(tt0279111)
# 3. King Kong	(tt0360717)
# 4. Pearl Harbor	(tt0213149)
# 5. Alexander	(tt0346491)

# In[6]:


# Фильтруем датасет по условию: самый длительный фильм в минутах.
film_max_runtime = data[data['runtime'] == data['runtime'].max()]
film_max_runtime

# Добавляем номер ответа в список с ответами.
answer_ls.append(2)


# # 3. Какой из фильмов самый короткий (в минутах)
# Варианты ответов:
# 
# 1. Home on the Range	tt0299172
# 2. The Jungle Book 2	tt0283426
# 3. Winnie the Pooh	tt1449283
# 4. Corpse Bride	tt0121164
# 5. Hoodwinked!	tt0443536

# In[7]:


# Фильтруем датасет по условию: самый короткий фильм (в минутах).
film_min_runtime = data[data['runtime'] == data['runtime'].min()]
film_min_runtime

# Добавляем номер ответа в список с ответами.
answer_ls.append(3)


# # 4. Средняя длительность фильма?
# 
# Варианты ответов:
# 1. 115
# 2. 110
# 3. 105
# 4. 120
# 5. 100
# 

# In[8]:


# Вычисляем среднюю длительность фильма через функцию mean().
film_mean_runtime = data['runtime'].mean()
film_mean_runtime

# Добавляем номер ответа в список с ответами.
answer_ls.append(2)


# # 5. Средняя длительность фильма по медиане?
# Варианты ответов:
# 1. 106
# 2. 112
# 3. 101
# 4. 120
# 5. 115
# 
# 
# 

# In[9]:


# Вычисляем среднюю длительность фильма по медиане().
film_median_runtime = data['runtime'].median()
film_median_runtime

# Добавляем номер ответа в список с ответами.
answer_ls.append(1)


# # 6. Какой самый прибыльный фильм?
# Варианты ответов:
# 1. The Avengers	tt0848228
# 2. Minions	tt2293640
# 3. Star Wars: The Force Awakens	tt2488496
# 4. Furious 7	tt2820852
# 5. Avatar	tt0499549

# In[10]:


# Добавляем новый столбец 'profit'.
data['profit'] = data['revenue']-data['budget']

# Фильтруем датасет по условию: какой фильм самый прибыльный.
film_max_profit = data[data['profit'] == data['profit'].max()]
film_max_profit

# Добавляем номер ответа в список с ответами.
answer_ls.append(5)


# # 7. Какой фильм самый убыточный?
# Варианты ответов:
# 1. Supernova tt0134983
# 2. The Warrior's Way tt1032751
# 3. Flushed Away	tt0424095
# 4. The Adventures of Pluto Nash	tt0180052
# 5. The Lone Ranger	tt1210819

# In[11]:


# Фильтруем датасет по условию: какой фильм самый убыточный.
film_min_profit = data[data['profit'] == data['profit'].min()]
film_min_profit

# Добавляем номер ответа в список с ответами.
answer_ls.append(2)


# # 8. Сколько всего фильмов в прибыли?
# Варианты ответов:
# 1. 1478
# 2. 1520
# 3. 1241
# 4. 1135
# 5. 1398
# 

# In[12]:


# Фильтреум датасет по условию: фильмы в прибыли. 
data_filter_by_profit = data[data['profit']>0]

# Считаем количество фильмов в прибыли.
films_profit_count  = len(data_filter_by_profit)
films_profit_count

# Добавляем номер ответа в список с ответами.
answer_ls.append(1)


# # 9. Самый прибыльный фильм в 2008 году?
# Варианты ответов:
# 1. Madagascar: Escape 2 Africa	tt0479952
# 2. Iron Man	tt0371746
# 3. Kung Fu Panda	tt0441773
# 4. The Dark Knight	tt0468569
# 5. Mamma Mia!	tt0795421

# In[44]:


# Фильтруем датасет по условию: фильмы, выпущенные в 2008 году. 
# Групируем датасет, сортируем столбец 'profit' по убыванию.
# Выводим 1 строчку, соответствующею фильму с самой высокой прибылью.
data[data['release_year'] == 2008].groupby(['original_title'])['profit'].sum().sort_values(ascending = False).head(1)

# Добавляем номер ответа в список с ответами
answer_ls.append(4)


# # 10. Самый убыточный фильм за период с 2012 по 2014 (включительно)?
# Варианты ответов:
# 1. Winter's Tale	tt1837709
# 2. Stolen	tt1656186
# 3. Broken City	tt1235522
# 4. Upside Down	tt1374992
# 5. The Lone Ranger	tt1210819
# 

# In[14]:


# Фильтруем датасет по условию: фильмы, выпущенные за период с 2012 по 2014. 
# Групируем датасет, сортируем столбец 'profit' по возрастанию.
# Выводим 1 строчку, соответствующею самому убыточному фильму.
data[(data['release_year'] >= 2012) & (data['release_year'] <= 2014)].groupby(['original_title'])['profit'].sum().sort_values(ascending = True).head(1)

# Добавляем номер ответа в список с ответами
answer_ls.append(5)


# # 11. Какого жанра фильмов больше всего?
# Варианты ответов:
# 1. Action
# 2. Adventure
# 3. Drama
# 4. Comedy
# 5. Thriller

# In[15]:


# Создаем список, в который поместим жанры фильмов.
genres_list = []
for i in data['genres']:
    for j in i.split('|'): 
        genres_list.append(j)

# Методом .Counter() посчитаем количество жанров в 'genres_list' и группируем результаты.
genres_count = collections.Counter()
for i in genres_list:
    genres_count[i] += 1

# Отсортируем словарь genres_count.
# Для этого создадим список кортежей ("ключ", "значение").
list_genres_count = list(genres_count.items())

# Отсортируем список 'list_genres_count' по вторым элементам.
list_genres_count.sort(key = lambda i: i[1], reverse=True)

# Выведем результат на экран.
for i in list_genres_count:
    print(i[0], ':', i[1])

# Добавляем номер ответа в список с ответами.
answer_ls.append(3)


# # 12. Какого жанра среди прибыльных фильмов больше всего?
# Варианты ответов:
# 1. Drama
# 2. Comedy
# 3. Action
# 4. Thriller
# 5. Adventure

# In[16]:


# Используем ранее отфильтрованный по прибыльности датасет, сохраненный в переменной 'data_filter_by_profit'.
# Создаем список с жанрами прибыльных фильмов.
profitable_genres = []
for i in data_filter_by_profit['genres']:
    for j in i.split('|'): 
        profitable_genres.append(j)

# Методом .Counter() посчитаем количество жанров в 'profitable_genres' и группируем результаты.
profitable_genres_count = collections.Counter()
for i in profitable_genres:
    profitable_genres_count[i]+=1

# Отсортируем словарь 'profitable_genres_count'.
# Для этого создадим список кортежей ("ключ", "значение").
list_profitable_genres_count = list(profitable_genres_count.items())

# Отсортируем 'list_profitable_genres_count' по вторым элементам.
list_profitable_genres_count.sort(key=lambda i: i[1], reverse = True)

# Выведем результат на экран.
for i in list_profitable_genres_count:
    print(i[0], ':', i[1])

# Добавляем номер ответа в список с ответами.
answer_ls.append(1)


# # 13. Кто из режиссеров снял больше всего фильмов?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Ridley Scott 
# 3. Steven Soderbergh
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[17]:


# Создадим список, в который поместим всех режиссеров.
director = []
for i in data['director']:
    for j in i.split('|'): 
        director.append(j)

# Методом .Counter() посчитаем количество фильмов в director и cгруппируем результаты.
director_films_count = collections.Counter()
for i in director:
    director_films_count[i] += 1 
    
# Отсортируем словарь 'director_films_count'.
# Для этого создадим список кортежей ("ключ", "значение").
list_director_films_count = list(director_films_count.items())

# Отсортируем 'list_director_films_count' по вторым элементам.
list_director_films_count.sort(key = lambda i: i[1], reverse = True)

# Выведем результат на экран.
for i in list_director_films_count:
    print(i[0], ':', i[1])

# Добавляем номер ответа в список с ответами.
answer_ls.append(3)


# # 14. Кто из режиссеров снял больше всего Прибыльных фильмов?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Clint Eastwood
# 3. Steven Spielberg
# 4. Ridley Scott
# 5. Christopher Nolan

# In[18]:


# Используем ранее отфильтрованный по прибыльности датасет, сохраненный в переменной 'data_filter_by_profit'.
# Создаем список с режиссерами прибыльных фильмов.
director_profitable_films = []
for i in data_filter_by_profit['director']:
    for j in i.split('|'): 
        director_profitable_films.append(j)

# Методом .Counter() посчитаем количество режиссеров в 'director_profitable_films' и группируем результаты.
director_profitable_films_count = collections.Counter()
for i in director_profitable_films:
    director_profitable_films_count[i] += 1

# Отсортируем словарь 'director_profitable_films_count'.
# Для этого создадим список кортежей ("ключ", "значение").
list_director_profitable_films_count = list(director_profitable_films_count.items())

# Отсортируем 'list_director_profitable_films_count' по вторым элементам.
list_director_profitable_films_count.sort(key = lambda i: i[1], reverse = True)

# Выведем результат на экран.
for i in list_director_profitable_films_count:
    print(i[0], ':', i[1])   
    
# Добавляем номер ответа в список с ответами .   
answer_ls.append(4)


# # 15. Кто из режиссеров принес больше всего прибыли?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Christopher Nolan
# 3. David Yates
# 4. James Cameron
# 5. Peter Jackson
# 

# In[19]:


# Используем ранее отфильтрованный по прибыльности датасет, сохраненный в переменной 'data_filter_by_profit'.
# Создаем daraframe, в котором есть список режиссеров и прибыль снятых фильмов.
director_profitable=pd.DataFrame(data_filter_by_profit['director'].str.split('|').tolist(),index=data_filter_by_profit['profit']).stack().reset_index([0])

# Меняем название колонки с режиссером на 'director'.
director_profitable.columns=['profit','director']

# Создаем сводную таблицу, в которой в качестве индексов используем колонку с режиссерами, суммируем прибыль.
director_profitable_max = director_profitable.pivot_table(index='director',values='profit', aggfunc=sum)

# Находим режиссера с максимальной прибылью
director_profitable_max[director_profitable_max['profit'] == director_profitable_max['profit'].max()]

# Добавляем номер ответа в список с ответами 
answer_ls.append(5)


# # 16. Какой актер принес больше всего прибыли?
# Варианты ответов:
# 1. Emma Watson
# 2. Johnny Depp
# 3. Michelle Rodriguez
# 4. Orlando Bloom
# 5. Rupert Grint

# In[20]:


# Используем ранее отфильтрованный по прибыльности датасет, сохраненный в переменной 'data_filter_by_profit'.
# Создаем daraframe, в котором есть список актеров и прибыль снятых фильмов.
actor_profitable=pd.DataFrame(data_filter_by_profit['cast'].str.split('|').tolist(),index=data_filter_by_profit['profit']).stack().reset_index([0])

# Меняем название колонки с актером на 'actor'.
actor_profitable.columns=['profit','actor']

# Создаем сводную таблицу, в которой в качестве индексов используем колонку с актерами, суммируем прибыль.
actor_profitable=actor_profitable.pivot_table(index='actor',values='profit', aggfunc=sum)

# Сортируем таблицу по убыванию прибыли.
actor_profitable.sort_values(by=['profit'],ascending=False).reset_index().head(1)

# Добавляем номер ответа в список с ответами .
answer_ls.append(1)


# # 17. Какой актер принес меньше всего прибыли в 2012 году?
# Варианты ответов:
# 1. Nicolas Cage
# 2. Danny Huston
# 3. Kirsten Dunst
# 4. Jim Sturgess
# 5. Sami Gayle

# In[21]:


# Фильтруем датасет по условию: год реализации 2012.
data_filter_by_profit_2012 = data[data['release_year'] == 2012]

# Создаем daraframe, в котором есть список актеров и прибыль снятых фильмов.
actor_min_profitable=pd.DataFrame(data_filter_by_profit_2012['cast'].str.split('|').tolist(),index=data_filter_by_profit_2012['profit']).stack().reset_index([0])

# Меняем название колонки с актером на 'actor'.
actor_min_profitable.columns=['profit','actor']

# Создаем сводную таблицу, в которой в качестве индексов используем колонку с актерами, суммируем прибыль.
actor_min_profitable=actor_min_profitable.pivot_table(index='actor',values='profit', aggfunc=sum)

# Сортируем таблицу по возрастанию прибыли.
actor_min_profitable.sort_values(['profit'],ascending=True).reset_index().head(1)

# Добавляем номер ответа в список с ответами.
answer_ls.append(3)


# # 18. Какой актер снялся в большем количестве высокобюджетных фильмов? (в фильмах где бюджет выше среднего по данной выборке)
# Варианты ответов:
# 1. Tom Cruise
# 2. Mark Wahlberg 
# 3. Matt Damon
# 4. Angelina Jolie
# 5. Adam Sandler

# In[22]:


# Фильтруем датасет по условию: бюджет фильма выше среднего.
data_filter_by_budget = data[data['budget'] > data['budget'].mean()]

# Создаем daraframe, в котором есть список актеров и id снятых высокобюджетных фильмов.
actor_max_budget=pd.DataFrame(data_filter_by_budget['cast'].str.split('|').tolist(),index=data_filter_by_budget['imdb_id']).stack().reset_index([0])

# Меняем название колоноки с актером на 'actor'.
actor_max_budget.columns=['count_actor','actor']

# Создаем сводную таблицу, в которой в качестве индексов используем колонку с актерами, считаем количество фильмов по полю imdb_id.
actor_max_budget=actor_max_budget.pivot_table(index='actor',values='count_actor', aggfunc='count')

# Сортируем таблицу по возрастанию количества фильмов.
actor_max_budget.sort_values(['count_actor'],ascending=False).reset_index().head(1)

# Добавляем номер ответа в список с ответами 
answer_ls.append(3)


# # 19. В фильмах какого жанра больше всего снимался Nicolas Cage?  
# Варианты ответа:
# 1. Drama
# 2. Action
# 3. Thriller
# 4. Adventure
# 5. Crime

# In[23]:


# Создаем dataframe, который содержит перечень всех актеров с их ID.
all_actors=pd.DataFrame(data['cast'].str.split('|').tolist(),index=data['imdb_id']).stack().reset_index([0])

# Создаем dataframe, который содержт перечень всех жанров с их ID.
all_genres=pd.DataFrame(data['genres'].str.split('|').tolist(),index=data['imdb_id']).stack().reset_index([0])

# Объединяем два dataframe.
data_join_actor_genres = all_actors.merge(all_genres, on='imdb_id', how='left')

# Переименовываем колонки.
data_join_actor_genres.columns = ['id','actor','genres']

# Фильтруем таблицу так, чтобы там остались жанры, в которых играет Nicolas Cage.
data_Nicolas_Cage = data_join_actor_genres[data_join_actor_genres['actor']=='Nicolas Cage']

# Подсчитываем количество жанров.
Nicolas_Cage_genres = collections.Counter()
for i in data_Nicolas_Cage['genres']:
    Nicolas_Cage_genres[i]+=1

# Выводим отсортированный в порядке убывания результат.
list_Nicolas_Cage_genres = list(Nicolas_Cage_genres.items())
list_Nicolas_Cage_genres.sort(key=lambda i: i[1], reverse = True)

for i in list_Nicolas_Cage_genres:
    print(i[0], ':', i[1]) 

# Добавляем номер ответа в список с ответами.
answer_ls.append(2)


# # 20. Какая студия сняла больше всего фильмов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[24]:


# Создаем dataframe, который содержит перечень всех студий с количеством фильмов.
pd.DataFrame(data['production_companies'].str.split('|').tolist()).stack().value_counts().idxmax()

# Добавляем номер ответа в список с ответами. 
answer_ls.append(1)


# # 21. Какая студия сняла больше всего фильмов в 2015 году?
# Варианты ответа:
# 1. Universal Pictures
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[25]:


# Фильтруем датасет по условию: фильмы, реализованные в 2015 .
data_films_2015 = data[data['release_year'] == 2015]

# Создаем dataframe, в котором считаем количество фильмов и выводим студию с максимальным значением.
pd.DataFrame(data_films_2015.production_companies.str.split('|').tolist()).stack().value_counts().idxmax()

# Добавляем номер ответа в список с ответами.
answer_ls.append(4)


# # 22. Какая студия заработала больше всего денег в жанре комедий за все время?
# Варианты ответа:
# 1. Warner Bros
# 2. Universal Pictures (Universal)
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Walt Disney

# In[46]:


# Создаем dataframe, который содержит перечень всех студий с их ID.
all_production_companies=pd.DataFrame(data['production_companies'].str.split('|').tolist(),index=data['imdb_id']).stack().reset_index([0])

# Используем созданный ранее dataframe all_genres, который содержит перечень всех жанров с их ID.
#all_genres=pd.DataFrame(data['genres'].str.split('|').tolist(),index=data['imdb_id']).stack().reset_index([0])

# Создаем dataframe, который содержит перечень всех ID с их доходом.
all_profit=pd.DataFrame(data['revenue'].tolist(),index=data['imdb_id']).stack().reset_index([0])

# Объединяем два dataframe.
data_join_companies_genres = all_production_companies.merge(all_genres, on='imdb_id', how='left')
data_join_companies_genres_revenue = data_join_companies_genres.merge(all_profit, on='imdb_id', how='left')

# Переименовываем колонки.
data_join_companies_genres_revenue.columns = ['id','companies','genres', 'revenue']

# Фильтруем таблицу по жанру.
comedy= data_join_companies_genres_revenue[data_join_companies_genres_revenue['genres'] == 'Comedy']

# Создаем сводную таблицу с компанией и суммой ее дохода.
comedy_companies_max_profit=comedy.pivot_table(index='companies',values='revenue', aggfunc='sum')

# Фильтруем таблицу по доходу.
comedy_companies_max_profit.sort_values(['revenue'],ascending=False).reset_index()

# Добавляем номер ответа в список с ответами.
answer_ls.append(2)


# # 23. Какая студия заработала больше всего денег в 2012 году?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Lucasfilm

# In[48]:


# Фильтруем датасет по условию: фильмы, реализованные в 2012. 
data_2012 = data[data['release_year'] == 2012]

# Создаем dataframe, который содержит перечень всех компаний с их доходами.
data_films_2012 = pd.DataFrame(data_2012['production_companies'].str.split('|').tolist(),index=data_2012['revenue']).stack().reset_index([0])

# Переименовываем столбцы.
data_films_2012.columns = ['revenue','companies']

# Создаем сводную таблицу.
data_films_2012_pivot = data_films_2012.pivot_table(index='companies',values='revenue', aggfunc='sum')

# Сортируем таблицу по возрастанию доходов.
data_films_2012_pivot.sort_values(['revenue'],ascending=False).reset_index().head(1)

# Добавляем номер ответа в список с ответами.
answer_ls.append(3)


# # 24. Самый убыточный фильм от Paramount Pictures
# Варианты ответа:
# 
# 1. K-19: The Widowmaker tt0267626
# 2. Next tt0435705
# 3. Twisted tt0315297
# 4. The Love Guru tt0811138
# 5. The Fighter tt0964517

# In[28]:


# Используем ранее созданный dataframe all_production_companies, который содержт перечень всех студий с их ID.
#all_production_companies=pd.DataFrame(data['production_companies'].str.split('|').tolist(),index=data['imdb_id']).stack().reset_index([0])

# Создаем dataframe, который содержит перечень всех фильмов с их ID.
all_films=pd.DataFrame(data['original_title'].str.split('|').tolist(),index=data['imdb_id']).stack().reset_index([0])

# Создаем dataframe, который содержит перечень всех ID с прибылью.
all_profit=pd.DataFrame(data['profit'].tolist(),index=data['imdb_id']).stack().reset_index([0])

# Объединяем два dataframe.
data_join_companies_films = all_production_companies.merge(all_films, on='imdb_id', how='left')
data_join_companies_films_profit = data_join_companies_films.merge(all_profit, on='imdb_id', how='left')

# Переименовываем колонки.
data_join_companies_films_profit.columns = ['id','companies','films', 'profit']

# Фильтруем таблицу по компании: содержит Paramount Pictures.
data_new = data_join_companies_films_profit[data_join_companies_films_profit['companies'] == 'Paramount Pictures']

# Создаем сводную таблицу, сортируем по прибыли и выводим результат.
data_new.pivot_table(index='films',values='profit', aggfunc='sum').sort_values(['profit'],ascending=True).reset_index().head(1)

# Добавляем номер ответа в список с ответами.
answer_ls.append(1)


# # 25. Какой Самый прибыльный год (заработали больше всего)?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2002
# 5. 2015

# In[50]:


# Создаем dataframe, который содержит перечень всех годов реализации фильмов с их прибылью.
all_release_year=pd.DataFrame(data['release_year'].tolist(),index=data['profit']).stack().reset_index([0])

# Переименовываем столбцы.
all_release_year.columns = ['profit', 'year']

#Создаем сводную таблицу, сортируем ее по убыванию прибыли и выводим результат.
all_release_year.pivot_table(index='year',values='profit', aggfunc='sum').sort_values(['profit'],ascending=False).reset_index().head(1)

# Добавляем номер ответа в список с ответами.
answer_ls.append(5)


# # 26. Какой Самый прибыльный год для студии Warner Bros?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2010
# 5. 2015

# In[30]:


# Используем ранее созданный dataframe all_production_companies, который содержт перечень всех студий с их ID.
#all_production_companies=pd.DataFrame(data['production_companies'].str.split('|').tolist(),index=data['imdb_id']).stack().reset_index([0])

# Используем ранее созданный dataframe all_profit, который содержт перечень всех ID с прибылью.
#all_profit=pd.DataFrame(data['profit'].tolist(),index=data['imdb_id']).stack().reset_index([0])

# Создаем dataframe, который содержит перечень всех годов реализации с их id.
all_year=pd.DataFrame(data['release_year'].tolist(),index=data['imdb_id']).stack().reset_index([0])

# Объединяем два dataframe.
data_join_companies_year = all_production_companies.merge(all_year, on='imdb_id', how='left')
data_join_companies_year_profit = data_join_companies_year.merge(all_profit, on='imdb_id', how='left')

# Переименовываем колонки.
data_join_companies_year_profit.columns = ['id','companies','year', 'profit']

# Фильтруем таблицу по компании: содержит Warner Bros.
data_Warner_Bros = data_join_companies_year_profit[data_join_companies_year_profit['companies'].str.contains('Warner Bros')]

# Создаем сводную таблицу, сортируем по прибыли и выводим результат.
data_Warner_Bros.pivot_table(index='year',values='profit', aggfunc='sum').sort_values(['profit'],ascending=False).reset_index().head(1)

# Добавляем номер ответа в список с ответами.
answer_ls.append(1)


# # 27. В каком месяце за все годы суммарно вышло больше всего фильмов?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[52]:


# Создаем столбец с месяцем.
data['month']  = data['release_date'].apply(lambda date:dt.strptime(date,'%m/%d/%Y').month) 

# Создаем сводную таблицу с месяцем и количеством снятых фильмов.
month_films_count = data.pivot_table(index='month',values='original_title', aggfunc='count').sort_values(['original_title'],ascending=False).reset_index()
month_films_count.head(1)

# Добавляем номер ответа в список с ответами.
answer_ls.append(4)


# # 28. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)
# Варианты ответа:
# 1. 345
# 2. 450
# 3. 478
# 4. 523
# 5. 381

# In[32]:


# Фильтруем таблицу month_films_coun по меясцам: содержит 6,7,9 месяцы.
month_films_count_summer = month_films_count[(month_films_count['month']==6) | (month_films_count['month']==7) | (month_films_count['month']==8)]
month_films_count_summer['original_title'].sum()

# Добавляем номер ответа в список с ответами. 
answer_ls.append(2)


# # 29. Какой режисер выпускает (суммарно по годам) больше всего фильмов зимой?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Christopher Nolan
# 3. Clint Eastwood
# 4. Ridley Scott
# 5. Peter Jackson

# In[33]:


# Фильтруем таблицу по зимним месяцам.
data_winter = data[(data['month']==12) | (data['month']==1) | (data['month']==2)]

# Создаем daraframe, в котором есть список режиссеров с их id.
all_director_winter=pd.DataFrame(data_winter['director'].str.split('|').tolist(),index=data_winter['imdb_id']).stack().reset_index([0])

# Создаем daraframe, в котором есть список фильмов с их id.
all_films_winter=pd.DataFrame(data_winter['original_title'].tolist(),index=data_winter['imdb_id']).stack().reset_index([0])

# Объединяем два dataframe.
data_join_director_films = all_director_winter.merge(all_films_winter, on='imdb_id', how='left')
#data_join_director_films_year = data_join_director_films.merge(all_year_winter, on='imdb_id', how='left')

# Переименовываем колонки.
data_join_director_films.columns = ['id','director','films']

# Создаем сводную таблицу, сортируем по прибыли и выводим результат.
data_join_director_films.pivot_table(index='director',values='films', aggfunc='count').sort_values(['films'],ascending=False).reset_index().head(1)

# Добавляем номер ответа в список с ответами 
answer_ls.append(5)


# # 30. Какой месяц чаще всего по годам самый прибыльный?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[34]:


# Создаем сводную таблицу, сортируем по прибыли и выводим результат.
data.pivot_table(index='month',values='profit',aggfunc='sum').reset_index().sort_values(['profit'],ascending = False).head(1)

# Добавляем номер ответа в список с ответами.
answer_ls.append(2)


# # 31. Названия фильмов какой студии в среднем самые длинные по количеству символов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[35]:


# Объединяем два dataframe.
data_join_companies_films = all_production_companies.merge(all_films, on='imdb_id', how='left')

# Переименовываем колонки.
data_join_companies_films.columns=['id','companies','film']

# Считаем количество символов в столбце film.
data_join_companies_films['len_name'] = data_join_companies_films['film'].apply(lambda film: len(film))

# Создаем сводную таблицу со средним количеством символов и выводим результат.
data_join_companies_films_len = data_join_companies_films.pivot_table(index='companies',values='len_name', aggfunc='mean').sort_values(['len_name'],ascending=False).reset_index().head(1)
data_join_companies_films_len

# Добавляем номер ответа в список с ответами. 
answer_ls.append(5)


# # 32. Названия фильмов какой студии в среднем самые длинные по количеству слов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[36]:


# Считаем количество слов в столбце film.
data_join_companies_films['len_word'] = data_join_companies_films['film'].apply(lambda film: len(set(film.split())))

# Создаем сводную таблицу со средним количеством символов и выводим результат.
data_join_companies_films.pivot_table(index='companies',values='len_word', aggfunc='mean').sort_values(['len_word'],ascending=False).reset_index().head(1)

# Добавляем номер ответа в список с ответами.
answer_ls.append(5)


# # 33. Сколько разных слов используется в названиях фильмов?(без учета регистра)
# Варианты ответа:
# 1. 6540
# 2. 1002
# 3. 2461
# 4. 28304
# 5. 3432

# In[37]:


import re

# Создаем список, в который поместим все слова, встречающиеся в названии фильмов.
original_title_list = []
for i in data['original_title']:
    for j in i.split():
        original_title_list.append(j.lower())

# Подсчитываем количество уникальных значений.
pd.DataFrame(original_title_list).nunique()

# Добавляем номер ответа в список с ответами.
answer_ls.append(3)


# # 34. Какие фильмы входят в 1 процент лучших по рейтингу?
# Варианты ответа:
# 1. Inside Out, Gone Girl, 12 Years a Slave
# 2. BloodRayne, The Adventures of Rocky & Bullwinkle
# 3. The Lord of the Rings: The Return of the King
# 4. 300, Lucky Number Slevin

# In[38]:


# Создаем dataframe, который содержит перечень всех фильмов с их ID
films_vote_average_max=data.pivot_table(index='original_title',values='vote_average', aggfunc='mean').sort_values(['vote_average'],ascending=False).reset_index()
films_vote_average_max.head(int(len(films_vote_average_max)/100))

# Добавляем номер ответа в список с ответами
answer_ls.append(1)


# # 35. Какие актеры чаще всего снимаются в одном фильме вместе
# Варианты ответа:
# 1. Johnny Depp & Helena Bonham Carter
# 2. Hugh Jackman & Ian McKellen
# 3. Vin Diesel & Paul Walker
# 4. Adam Sandler & Kevin James
# 5. Daniel Radcliffe & Rupert Grint

# In[39]:


# Вводим переменные-счетчики.
Johnny_Depp_and_Helena_Bonham_Carter = 0
Hugh_Jackman_and_Ian_McKellen = 0
Vin_Diesel_and_Paul_Walker = 0
Adam_Sandler_and_Kevin_James = 0
Daniel_Radcliffe_and_Rupert_Grint = 0

# Проводим подсчет количества пар с помощью цикла.
for i in pd.Series(data['cast']):
    if 'Johnny Depp' in i and 'Helena Bonham Carter' in i:
        Johnny_Depp_and_Helena_Bonham_Carter +=1
    elif 'Hugh Jackman' in i and 'Ian McKellen' in i:
        Hugh_Jackman_and_Ian_McKellen +=1
    elif 'Vin Diesel' in i and 'Paul Walker' in i:
        Vin_Diesel_and_Paul_Walker +=1
    elif 'Adam Sandler' in i and 'Kevin James' in i:
        Adam_Sandler_and_Kevin_James +=1
    elif 'Daniel Radcliffe' in i and 'Rupert Grint' in i:
        Daniel_Radcliffe_and_Rupert_Grint +=1
    else: 0

# Выводим результат на экран.
print('Johnny Depp & Helena Bonham Carter:',Johnny_Depp_and_Helena_Bonham_Carter)
print('Hugh Jackman & Ian McKellen:',Hugh_Jackman_and_Ian_McKellen)
print('Vin Diesel & Paul Walker:',Vin_Diesel_and_Paul_Walker)
print('Adam Sandler & Kevin James:',Adam_Sandler_and_Kevin_James)
print('Daniel Radcliffe & Rupert Grint:',Daniel_Radcliffe_and_Rupert_Grint)

# Добавляем номер ответа в список с ответами.
answer_ls.append(5)


# # 36. У какого из режиссеров выше вероятность выпустить фильм в прибыли? (5 баллов)101
# Варианты ответа:
# 1. Quentin Tarantino
# 2. Steven Soderbergh
# 3. Robert Rodriguez
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[40]:


# Создаем daraframe, в котором есть список режиссеров с их id
all_director=pd.DataFrame(data['director'].str.split('|').tolist(),index=data['imdb_id']).stack().reset_index([0])

# Создаем daraframe, в котором есть список фильмов с их id
all_profit=pd.DataFrame(data['profit'].tolist(),index=data['imdb_id']).stack().reset_index([0])

# Создаем daraframe, в котором есть список фильмов с их id
all_films_id=pd.DataFrame(data['original_title'].tolist(),index=data['imdb_id']).stack().reset_index([0])

# Объединяем два dataframe
data_join_director_profit = all_director.merge(all_profit, on='imdb_id', how='left')
data_join_director_profit_films = data_join_director_profit.merge(all_films_id, on='imdb_id', how='left')

# Переименовываем столбцы
data_join_director_profit_films.columns = ['id','director','profit', 'film']

# Выбираем строки, где есть режиссеры из списка
new = data_join_director_profit_films[data_join_director_profit_films['director'].str.contains('Quentin Tarantino|Steven Soderbergh|Robert Rodriguez|Christopher Nolan|Clint Eastwood',na=False)]
new = new.reset_index(drop=True)

list_directors = ['Quentin Tarantino','Steven Soderbergh','Robert Rodriguez','Christopher Nolan','Clint Eastwood']

# В цикле фильтруем датасет 'new' по условию: прибыль больше 0
# Находим вероятность выпуска прибыльного фильма для каждого режиссера иъ списка 'list_directors'

result={}
for i in list_directors:
    df=new.query('director in @i')
    prob=len(df.query('profit>0'))/len(df['profit'])
    result[i]=prob

# Выводим результат
result

# Добавляем номер ответа в список с ответами.
answer_ls.append(4)


# # Submission

# In[41]:


len(answer_ls)


# In[42]:


pd.DataFrame({'Id':range(1,len(answer_ls)+1), 'Answer':answer_ls}, columns=['Id', 'Answer'])


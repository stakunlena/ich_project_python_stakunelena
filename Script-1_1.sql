/* скрипт для поиска фильмов по ключевому слову */
SELECT film_id, title, description, release_year
FROM film
WHERE title LIKE CONCAT('%', ? , '%')
ORDER BY title
LIMIT 10;
/* слово для поиска вводится вместо ?*/


/* запрос списка жанров и их идентификаторов*/
SELECT DISTINCT category_id, name
FROM category
ORDER BY category_id;


-- запрос выводит список фильмов по  введенному ID категории  например (category_id = 15) без названия категории
SELECT f.film_id, f.title, f.description, f.release_year, fc.category_id
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
WHERE fc.category_id = 15;


-- запрос выводит список фильмов по  введенному ID категории  например (category_id = 15) с названием категории
SELECT 
    f.film_id, 
    f.title, 
    f.description, 
    f.release_year, 
    fc.category_id,
    c.name AS category_name
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE fc.category_id = 15;


-- запрос выводит диапазон годов 
SELECT 
    MIN(release_year) AS min_year, 
    MAX(release_year) AS max_year
FROM film;

-- запрос выводит список фильмов по введенному году 

SELECT film_id, title, description, release_year
FROM film
WHERE release_year = 2006;

SELECT 
    f.film_id, 
    f.title, 
    -- f.description, 
    f.release_year, 
    c.name AS category_name
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE f.release_year = 2010;


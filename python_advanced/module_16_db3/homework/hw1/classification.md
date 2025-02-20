## Типы связей между таблицами в схеме

![](../img/cinema_schema_diagram.png)

| Тип связи | Таблица 1       | Таблица 2      | Таблица 3     |  
|:---------:|-----------------|----------------|---------------|
|    1:M    | movie_direction | director       | movie         |   
|    1:N    | oscar_awarded   | movie          |               |  
|    1:M    | movie_cast      | movie          | actors        |        
  


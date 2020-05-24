select name, max(high) as Max_High, extract(hour from cast(ts as timestamp)) as Hour_of_Day
from stock_data_delivery
group by (name, extract(hour from cast(ts as timestamp)))
order by name, Hour_of_Day
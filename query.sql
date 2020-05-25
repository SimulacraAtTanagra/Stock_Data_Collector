select a.name, a.high, a.ts, a.hour
FROM ( select name, high, ts, extract(hour from cast(ts as timestamp)) as "hour" from stock_data_delivery) a, (select name, max(high) as "maxhigh", extract(hour from cast(ts as timestamp)) as "hour"
from stock_data_delivery
group by (name, extract(hour from cast(ts as timestamp))))b
where (a.high = b.maxhigh and a.name = b.name and a.hour = b.hour)
order by a.name,a.hour





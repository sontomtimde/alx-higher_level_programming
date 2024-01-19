
5 lines (5 loc) · 168 Bytes
-- Displays the max temperature of each state, ordered by state name.
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;

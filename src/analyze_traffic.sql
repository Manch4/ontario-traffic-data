--1. Traffic events ordered by type
SELECT 
    event_type,
    COUNT(*) AS event_count
FROM traffic_events --From our traffic events
GROUP BY event_type 
ORDER BY event_count DESC; --Takes event_type and count from traffic events and orders by event type greatest to least

-- 2. Roads by number of trafic events 
SELECT 
    road,
    COUNT(*) AS event_count 
FROM traffic_events
WHERE road IS NOT NULL
    AND road <> ''
GROUP BY road
ORDER BY event_count DESC
LIMIT 10; --Takes road and count (where road is not null or blank) and orders it by roads with greatest to least incidents (top 10) 


-- 3. Traffic events by direction
SELECT
    direction,
    COUNT(*) AS event_count
FROM traffic_events
WHERE direction IS NOT NULL
    AND direction <> ''
GROUP BY direction
ORDER BY event_count DESC; --Takes direction and count (where direction is not null or blank) and orders direction greatest to least incidents (top 10)


-- 4. Full closure vs. non-full closure
SELECT
    CASE
        WHEN is_full_closure = 1 THEN 'Full closure'
        ELSE 'Not full closure'
    END AS closure_status,
    COUNT(*) AS event_count
FROM traffic_events
GROUP BY closure_status
ORDER BY event_count DESC; -- Selects and sets when is_full_closure is true to "Full closure" and "not full closure" otherwise sets it to closure_status and groups it by closure_status by greatest to least # of closures
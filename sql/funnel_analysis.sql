-- Funnel stage summary
SELECT
    event_name,
    COUNT(DISTINCT user_id) AS users_reached_stage
FROM events
GROUP BY event_name
ORDER BY users_reached_stage DESC;

-- Feature adoption summary
SELECT
    feature_name,
    COUNT(*) AS total_events,
    COUNT(DISTINCT user_id) AS unique_users
FROM events
WHERE feature_name IS NOT NULL
GROUP BY feature_name
ORDER BY unique_users DESC;

-- Activation rate
SELECT
    COUNT(DISTINCT CASE WHEN event_name = 'account_activated' THEN user_id END) * 100.0 /
    COUNT(DISTINCT CASE WHEN event_name = 'signup_completed' THEN user_id END) AS activation_rate_pct
FROM events;

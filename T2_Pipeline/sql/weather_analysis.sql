SELECT
    time,
    temperature_celsius,
    humidity_percent,
    wind_speed_kmh,
    is_hot_day
FROM
    `velvety-tangent-393618.weather_data.weather_metrics`
WHERE
    temperature_celsius > 35
ORDER BY
    temperature_celsius DESC;
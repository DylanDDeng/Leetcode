SELECT
    player_id,
    device_id
FROM Activity
WHERE (player_id, event_date) in (
    SELECT player_id, MIN(event_date) FROM Activity
    GROUP BY player_id
)
;
/* 
注意这里要考虑到玩家在第一个日期有多个设备登录的情况； 
如果遇到这样的情况，要把所有设备id都返回，而不是只返回其中默认的第一条 
*/ 

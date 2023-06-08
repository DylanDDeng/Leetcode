SELECT ROUND(IFNULL(
    (SELECT COUNT(DISTINCT CONCAT(requester_id, '_', accepter_id)) FROM RequestAccepted) / 
    (SELECT COUNT(DISTINCT CONCAT(sender_id, '_', send_to_id)) FROM FriendRequest), 0), 2)
AS accept_rate;
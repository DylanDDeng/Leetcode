
select name  
from SalesPerson
where sales_id not in
    (
    select sales_id -- ②再找出与该公司有销售往来的员工号
    from Orders
    where com_id  in 
        (
        select com_id  -- ①先找出com_id 1 
        from Company
        where name='RED')
    )
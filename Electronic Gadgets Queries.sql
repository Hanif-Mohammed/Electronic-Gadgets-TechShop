create database techshop;
use techshop;

#1 CUSTOMERS TABLE
create table Customers(
CustomerID int not null auto_increment,
FirstName varchar(20) not null,
LastName varchar(20) not null,
Email varchar(30),
Phone int,
Address varchar(100),
primary key (CustomerID),
unique(Email,Phone)
);
desc customers;

#2 PRODUCTS TABLE
create table Products(
ProductID int not null auto_increment,
ProductName varchar(20) not null,
Description varchar(30),
Price int not null,
primary key (ProductID)
);
desc products;

#3 ORDERS TABLE
create table Orders(
OrderID int not null auto_increment,
CustomerID int not null,
OrderDate date,
TotalAmount decimal(7,2),
primary key (OrderID),
foreign key (CustomerID) references Customers(CustomerID) on delete cascade
);
desc orders;

#4 ORDER DETAILS TABLE
create table orderdetails(
orderdetailid int not null auto_increment,
orderid int not null,
productId int not null,
quantity int not null,
primary key(orderdetailid),
foreign key(orderid) references orders(orderid) on delete cascade,
foreign key(productid) references products(productid) on delete cascade
);
desc orderdetails;

create table Inventory(
InventoryID int not null auto_increment,
ProductID int not null,
QuantityInStock int,
LastStockUpdate datetime,
primary key (InventoryID),
foreign key(ProductID) references Products(ProductID) on delete cascade
);
desc inventory;

insert into customers(firstname,lastname,email,phone,address) values
('Robert','Deniro','robden@gmail.com',1234567890,'houston'),
('al','pacino','alpac@gmail.com',1234567891,'madrid'),
('christopher','nolan','chrisnol@gmail.com',1234567892,'london'),
('martin','scorsese','marscor@gmail.com',1234567893,'new york'),
('cilian','murphy','cilmurph@gmail.com',1234567894,'belfast'),
('denzel','washington','denwash@gmail.com',1234567895,'DC'),
('hugh','jackman','hugjack@gmail.com',1234567896,'sydney'),
('dev','patel','patel@gmail.com',1234567897,'delhi'),
('ryan','reynolds','ryanrey@gmail.com',1234567898,'toronto'),
('brad','pitt','bpit@gmail.com',1234567899,'las vegas');
select * from customers;

insert into Products(productname,description,price) values
('laptops','gaming laptops',50000),
('antivirus','safe and secure',2000),
('ethernet','high speed internet',1000),
('tablet','handy and portable',20000),
('stylus','draw imagination',3000),
('GPU','visual rendering',40000),
('CPU','high speed process',40000),
('RAM','quick multitasking',8000),
('ROM','big storage access',8000),
('monitor','HD display monitor',5000);
select * from products;

insert into orders(customerid,orderdate,totalamount) values
(1,'2025-03-01',50000.00), #1-laptop
(2,'2025-03-03',2000.00), #1-antivirus
(3,'2025-03-05',3000.00), #3-ethernet
(4,'2025-03-07',16000.00), #2-ram
(5,'2025-03-08',15000.00), #3-monitor
(6,'2025-03-09',80000.00), #2-cpu
(7,'2025-03-11',16000.00), #2-rom
(8,'2025-03-14',40000.00), #1-gpu
(9,'2025-03-16',40000.00), #2-tablet
(10,'2025-03-17',9000.00); #3-stylus
select * from orders;

insert into OrderDetails(orderid,productid,quantity) values
(1,1,1), #1-laptop
(2,2,1), #1-antivirus
(3,3,3), #3-ethernet
(4,8,2), #2-ram
(5,10,3),#3-monitor
(6,7,2), #2-cpu
(7,9,2), #2-rom
(8,6,1), #1-gpu
(9,4,2), #2-tablet
(10,5,3); #3-stylus
select * from orderdetails;

insert into inventory(productid,quantityinstock,laststockupdate) values
(1,100,'2025-03-18 10:00:00'), #laptop
(2,200,'2025-03-18 10:00:00'), #antivirus
(3,50,'2025-03-18 10:00:00'), #ethernet
(4,80,'2025-03-18 10:00:00'), #tablet
(5,80,'2025-03-18 10:00:00'), #stylus
(6,50,'2025-03-18 10:00:00'), #GPU
(7,50,'2025-03-18 10:00:00'), #CPU
(8,100,'2025-03-18 10:00:00'), #RAM
(9,100,'2025-03-18 10:00:00'), #ROM
(10,50,'2025-03-18 10:00:00'); #monitor

#TASK 2

#1
select concat(firstname,'_',lastname) as Fullname,email from customers;

#2
select orders.orderid,orders.orderdate,concat(customers.firstname,'_',customers.lastname) as Fullname
from orders join customers on orders.customerid = customers.customerid;

#3
insert into customers(firstname,lastname,email,address) values('chris','evans','eva@gmail.com','chicago');
select * from customers;

#4
update  products
set price=price*1.1;
select * from products;

#5
delete from customers where customerid=1;
select * from customers;

#6
insert into customers(firstname,lastname,email,phone,address) values
('henry','cavill','cavil@gmail.com','1234567880','manchester');
insert into orders(customerid,orderdate,totalamount) values
(last_insert_id(),'2025-03-18',11000.00); #5 antivirus  
select * from orders;

#7
update customers
set email='jackman@gmail.com',address='perth'
where customerid=7;
select * from customers;

#8
update orders o
join(
    select od.orderid, sum(p.price * od.quantity) as newtotal
    from orderdetails od
    join products p on od.productid = p.productid
    group by od.orderid
)
 as calculated_totals on o.orderid = calculated_totals.orderid
set o.totalamount = calculated_totals.newtotal;
select * from orderdetails;

#9
delete from orderdetails
where orderid in(select orderid from orders where customerid = 2);
delete from orders
where orderid=2;
select * from orderdetails;

#10
insert into products(productname,description,price)  values
('wi-fi','wireless connectivity',1100);
select * from products;

#11
alter table orders
add column orderstatus varchar(10) default 'pending';
update orders
set orderstatus='shipped'
where orderid=3;
select * from orders;

#12
alter table customers
add column totalorders int default 0;
update customers 
set totalorders=(
select count(*)
from orders
where orders.customerid=customers.customerid
);
select * from customers;

#TASK 3
#1
select o.orderid, o.orderdate, o.totalamount,CONCAT(c.firstname, ' ', c.lastname) as customername, 
c.Email, c.Phone, c.Address from orders o
join customers c on o.customerid = c.customerid
order by o.orderdate;

#2
select p.productname,SUM(od.quantity * p.price) as totalrevenue
from orderdetails od
join products p on od.productid = p.productid
group by p.productname
order by totalrevenue desc;

#3
select distinct c.customerid,CONCAT(c.firstname, ' ', c.lastname) as customername, 
c.Email, c.Phone, c.Address from customers c
join orders o on c.customerid = o.customerid
order by customername;

#4
select p.productname, SUM(od.quantity) as totalquantityordered
from orderdetails od
join products p on od.productid = p.productid
group by p.productid, p.productname
order by totalquantityordered desc
limit 1;

#5
alter table products add column category varchar(50);
update products 
set category = 'Electronic Gadgets' 
where productname in ('laptops', 'tablet', 'GPU', 'CPU', 'RAM', 'ROM', 'monitor', 'stylus', 'ethernet','wi-fi');
select p.productname, p.category 
from products p
where p.category = 'Electronic Gadgets';

#6
select c.customerid,CONCAT(c.firstname, ' ', c.lastname) as customername,
round(avg(o.totalamount)) as Averageordervalue
from orders o
join customers c on o.customerid = c.customerid
group by c.customerid, customername
order by customerid;

#7
select o.orderid,CONCAT(c.firstname, ' ', c.lastname) as customername,
c.Email,c.Phone,c.Address, o.totalamount AS totalrevenue
from orders o
join customers c on o.customerid = c.customerid
order by o.totalamount desc
limit 1;

#8
select p.productname,COUNT(od.productid) as totalorders
from products p
left join orderdetails od on p.productid = od.productid
where p.category = 'Electronic Gadgets'
group by p.productname
order by totalorders desc;

#9
select distinct c.customerid, CONCAT(c.firstname, ' ', c.lastname) as customername
from customers c
join orders o on c.customerid = o.customerid
join orderdetails od on o.orderid = od.orderid
join products p on od.productid = p.productid
where p.productname = 'monitor' and p.category = 'Electronic Gadgets';

#10
select SUM(o.totalamount) as totalrevenue
from orders o
where o.orderdate between '2025-03-01' and '2025-03-30';

#TASK 4

#1
select c.customerid, c.firstname, c.lastname
from customers c
where not exists (
    select 1 from orders o where o.customerid = c.customerid
);

#2
select (select COUNT(*) from inventory where QuantityInStock > 0) AS Totalavailableproducts;

#3
select (select SUM(totalamount) from orders) as Totalrevenue;

#4
select (select avg(od.quantity) 
from orderdetails od 
join products p on od.Productid = p.productid 
where p.category = 'Electronic Gadgets') as avgquantityordered;

#5
select(select SUM(o.totalamount) 
from orders o 
where o.customerid =  5) as Totalrevenue;

#6
select c.customerid, CONCAT(c.firstname, ' ', c.lastname) as Customername, COUNT(o.orderid) as Totalorders
from customers c
join orders o on c.customerid = o.customerid
group by c.customerid
having totalorders = (select MAX(ordercount) from (select customerid, COUNT(orderid) as ordercount 
from orders group by customerid) as sub);

#7
select category, Totalquantityordered  from (  
select p.category, SUM(od.quantity) as Totalquantityordered  
from products p  
join orderdetails od on p.productid = od.productid  
group by p.category  
) as categorysales  
order by totalquantityordered desc
limit 1;

#8
select CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName, s.TotalSpending  
from customers c join (  
select o.customerid, SUM(od.quantity * p.price) as Totalspending  
from orders o  
join orderdetails od on o.orderid = od.orderid  
join products p on od.productid = p.productid  
where p.category = 'Electronic Gadgets'  
group by o.customerid
order by Totalspending desc  
limit 1  
) s on c.customerid = s.customerid;

#9
select (select SUM(Totalamount) from Orders) / (select COUNT(*) from orders) 
as AverageOrderValue;

#10
select CONCAT(c.Firstname, ' ', c.Lastname) as Customerfullname,
(select COUNT(*) from orders o where o.customerid = c.customerid) as totalorders 
from customers c;

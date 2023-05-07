use banking;

create table Account
( acc_number int primary key,
pin varchar(50),
name varchar(100),
description varchar(200));



insert into Account (acc_number,pin,name) values (100,'1564','jack');
select * from Account;

select * from transactions;




create table transactions(
transaction_id int primary key AUTO_INCREMENT ,
transaction_name varchar(100),
acc_number int,
amount int,
FOREIGN KEY (acc_number) REFERENCES Account(acc_number)
);



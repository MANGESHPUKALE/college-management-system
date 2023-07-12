create database if not exists collegedb;
use collegedb;


create table if not exists department
(
id int unsigned primary key,
dname varchar(50) not null,
hod varchar(50) not null
);
desc department;

create table if not exists student
(
rno int unsigned primary key,
name varchar(60) not null,
email varchar(100) not null,
dept varchar(100) not null
);
desc student;






delimiter $$

drop trigger if exists t1 $$
create trigger t1 before insert on department for each row
begin

	if(new.id is null) or (new.id < 1) or (new.id is blank)then
		signal SQLSTATE '11111' set message_text = "Invalid ID";
	end if;


	if(new.dname is null) or (length(trim(new.dname))=0)
	or (length(new.dname) < 1) then
		signal SQLSTATE '22222' set message_text = "Invalid Deprtment Name";
	end if;

	if(new.hod is null) or (length(trim(new.hod))=0)
	or (length(new.hod) < 2) or (not new.hod regexp "^[A-Za-z ]+$") then
		signal SQLSTATE '33333' set message_text = "Invalid HOD Name";
	end if;

end $$



drop trigger if exists t2 $$
create trigger t2 before update on department for each row
begin

	if(new.id is null) or (new.id < 1) then
		signal SQLSTATE '11111' set message_text = "Invalid ID";
	end if;


	if(new.dname is null) or (length(trim(new.dname))=0)
	or (length(new.dname) < 1) then
		signal SQLSTATE '22222' set message_text = "Invalid Department Name";
	end if;

	if(new.hod is null) or (length(trim(new.hod))=0)
	or (length(new.hod) < 2) or (not new.hod regexp "^[A-Za-z ]+$") then
		signal SQLSTATE '33333' set message_text = "Invalid HOD Name";
	end if;

end $$

drop trigger if exists t3 $$
create trigger t3 before insert on student for each row
begin
	if(new.rno is null) or (new.rno < 1) then
		signal SQLSTATE '11111' set message_text = "Invalid rno";
	end if;


	if(new.name is null) or (length(trim(new.name))=0)
	or (length(new.name) < 2) or (not new.name regexp "^[A-Za-z ]+$") then
		signal SQLSTATE '22222' set message_text = "Invalid Name";
	end if;

	if(new.email is null) or (length(trim(new.email))=0)
	or (length(new.email) < 5) then
		signal SQLSTATE '33333' set message_text = "Invalid Email";

	end if;

end $$


drop trigger if exists t4 $$
create trigger t4 before update on student for each row
begin

	if(new.rno is null) or (new.rno < 1) then
		signal SQLSTATE '11111' set message_text = "Invalid rno";
	end if;


	if(new.name is null) or (length(trim(new.name))=0)
	or (length(new.name) < 2) or (not new.name regexp "^[A-Za-z ]+$") then
		signal SQLSTATE '22222' set message_text = "Invalid Name";
	end if;

	if(new.email is null) or (length(trim(new.email))=0)
	or (length(new.email) < 5) then
		signal SQLSTATE '33333' set message_text = "Invalid Email";

	end if;
end $$

delimiter ;


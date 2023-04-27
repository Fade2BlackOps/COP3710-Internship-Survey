CREATE TABLE students
	(ID		            numeric(6) primary key,
	 name               varchar(50) not null
);

CREATE TABLE companies
    (name               varchar(50) primary key not null,
     location           varchar(50)
);

CREATE TABLE internships
    (ID                 numeric(4) primary key,
     date_start         date,
     date_end           date,
     company            varchar(50) not null,
     description        varchar(100),
     foreign key (company) references companies (name)
        on delete cascade
);

CREATE TABLE surveys -- according to Word doc, "internship survey"
    (ID                 numeric(10) primary key,
     student_ID         numeric(6),
     internship_ID      numeric(4),
     company            varchar(50),
     duty_description   varchar(150),
     foreign key (student_ID) references students (ID)
        on delete set null,
     foreign key (internship_ID) references internships (ID),
     foreign key (company)  references companies
);

CREATE TABLE tags
    (name               varchar(50) primary key,
     description        varchar(150)
);

CREATE TABLE takes
    (student_ID         numeric(6) primary key,
     survey_ID          numeric(10) primary key,
     foreign key (student_ID) references students (ID)
        on delete cascade,
     foreign key (survey_ID) references surveys (ID)
        on delete cascade
);

CREATE TABLE reviews
    (survey_ID          numeric(10) primary key,
     internship_ID      numeric(4) primary key ,
     foreign key (survey_ID) references surveys (ID)
        on delete cascade,
     foreign key (internship_ID) references internships (ID)
        on delete cascade
);

CREATE TABLE intern_tags
    (tag                varchar(50),
     internship_ID      numeric(4) primary key,
     foreign key (tag) references tags (name)
        on delete cascade,
     foreign key (internship_ID) references internships (ID)
        on delete cascade
);

CREATE TABLE survey_tags
    (tag                varchar(50),
     survey_ID          numeric(10),
     foreign key (tag) references tags (name)
        on delete cascade,
     foreign key (survey_ID) references surveys (ID)
        on delete cascade
);


insert into students values(342472, 'Vasil');
insert into students values(123456, 'Justin');
insert into students values(069420, 'Paula');
insert into students values(815258, 'Ayleen');

insert into companies values('Amazon', 'California');
insert into companies values('Arthrex', 'Florida');
insert into companies values('Discount Weazels by Hobo Joe', 'The Moon');
insert into companies values('Ubisoft', 'Los Angeles');

insert into internships values(0000, '2022-05-27', '2023-04-22', 'Ubisoft', 'Engineering Intern');
insert into internships values(0001, '2022-05-27', '2023-04-22', 'Arthrex', 'Business Analyst Intern');


select * from students;

select id, name
from students;

select *
from surveys
where student_ID = 342472;

select name
from companies;

select name
from tags;

insert into internships values(0000, '2022-05-27', '2023-04-22', 'Ubisoft', 'Engineering Intern');
insert into internships values(0001, '2022-05-27', '2023-04-22', 'Arthrex', 'Business Analyst Intern');

select * from internships;

update internships
set date_end = '6969-04-20'
where ID = 0000;

insert into companies values('Discount Weasels by Hobo Joe', 'The Moon');

insert into tags values('Money', 'This internship pays real well! :D');
insert into tags values('Free', 'This internship does not pay.  :(');

select * from tags;

insert into surveys values(0000000000, 342472, 0000, 'Ubisoft', 'I did stuff to make games :)');

insert into survey_tags values('Money', 0);
insert into survey_tags values('Free', 0);

create view submission_data as
    select sur.ID, stu.name, i.description, i.date_start, i.date_end, sur.company, group_concat(svt.tag, ', ') as tags
    from surveys sur
    left outer join students stu on sur.student_ID = stu.ID
    left outer join internships i on sur.internship_ID = i.ID
    left outer join survey_tags svt on sur.ID = svt.survey_ID;

select *
from submission_data;

select *
from survey_tags;

drop view submission_data;

/*
drop table surveys;
drop table companies;
drop table intern_tags;
drop table internships;
drop table reviews;
drop table students;
drop table survey_tags;
drop table tags;
drop table takes; */


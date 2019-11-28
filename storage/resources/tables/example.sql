create table if not exists {} (
    id int auto_increment,
    field_a int not null,
    field_b varchar(32) not null,
    primary key (id)
) engine=INNODB;

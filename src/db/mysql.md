main_title: MySQL Cheatsheet
lang: mysql

#------------------------------------------------------------------------------
title: Grant user access to a database

GRANT ALL PRIVILEGES ON database_name.* TO new_user'@'localhost' IDENTIFIED BY 'user_password';

#------------------------------------------------------------------------------
title: Set root password
# sudo /etc/init.d/mysql stop
# sudo mysqld_safe --skip-grant-tables &
# mysql -u root
  use mysql
  update user set authentication_string=PASSWORD("MyPassword") where User='root';
  flush privileges;
  quit

# sudo /etc/init.d/mysql stop
#------------------------------------------------------------------------------



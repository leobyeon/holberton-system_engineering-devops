# change the name of the file
file { '/var/www/html/wp-includes/class-wp-locale.phpp':
		source => '/var/www/html/wp-includes/class-wp-locale.php',
		ensure => present
}

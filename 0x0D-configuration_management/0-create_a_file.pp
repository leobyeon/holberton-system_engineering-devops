# creates a file in /tmp
file { '/tmp':
  ensure  => 'file',
  mode    => '0744',
  path    => '/tmp/holberton',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}

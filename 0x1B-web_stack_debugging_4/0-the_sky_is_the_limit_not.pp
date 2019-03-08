# fix the stack to take 2000 requests

service { 'nginx' :
  ensure => 'running',
  enable => true
}

file {'/etc/default/nginx' :
  ensure => present
}
-> exec { 'change_ulimit' :
  path    => '/bin',
  command => 'sed -i --follow-symlinks s/15/1000/ /etc/default/nginx',
  notify  => Service['nginx']
}

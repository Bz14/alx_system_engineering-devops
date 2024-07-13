# Setup New Ubuntu server with nginx

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

file {'/var/www/html/index.html':
     content => 'Hello World!'
}

exec { 'add_custom_header':
  command  => 'sed -i "/server_name _;/a \\        add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package['nginx'],
}

exec {'redirect_me':
     command => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
     provider => 'shell'
}

service {'nginx':
	ensure => running,
	require => Package['nginx']
}
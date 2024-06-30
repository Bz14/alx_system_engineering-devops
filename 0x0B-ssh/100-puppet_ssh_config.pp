#!/usr/bin/env bash
#Client configuration file
file { '/etc/ssh/ssh_config':
  ensure  => file,
}

file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication',
}

file_line {'Use a Identityfile':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^IdentityFile',
}

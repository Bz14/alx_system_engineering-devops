#!/usr/bin/env bash
#Client configuration file
file { '/etc/ssh/ssh_config':
  ensure  => 'present',
}

file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => 'PasswordAuthentication yes',
  replace => 'true',
}

file_line {'Use a Identityfile':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentifyFile ~/.ssh/config',
  match   => '^IdentifyFile',
}

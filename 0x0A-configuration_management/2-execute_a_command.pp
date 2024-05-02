# Executing a command
execute {'killmenow' :
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell',
  returns  => [0, 1],
}
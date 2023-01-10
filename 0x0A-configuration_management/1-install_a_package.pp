#install flask

exec { 'flask':
  command => '/bin/python3  pip3 install flask -v 2.1.0',
}

#install flask
package {'flask':
  ensure   => 'latest',
  provider => 'pip3',
}

package { "default-jre":
  ensure => present,
}

package { "docker.io":
  ensure => present,
}

package { "unzip":
  ensure => present,
}

# JVM 1.7

$ JAVA_HOME=`/usr/libexec/java_home -v 1.7` java -Xmx32600m -XX:+PrintFlagsFinal 2> /dev/null | grep UseCompressedOops
     bool UseCompressedOops   := true
$ JAVA_HOME=`/usr/libexec/java_home -v 1.7` java -Xmx32766m -XX:+PrintFlagsFinal 2> /dev/null | grep UseCompressedOops
     bool UseCompressedOops   = false

# JVM 1.8
$ JAVA_HOME=`/usr/libexec/java_home -v 1.8` java -Xmx32766m -XX:+PrintFlagsFinal 2> /dev/null | grep UseCompressedOops
     bool UseCompressedOops   := true
$ JAVA_HOME=`/usr/libexec/java_home -v 1.8` java -Xmx32767m -XX:+PrintFlagsFinal 2> /dev/null | grep UseCompressedOops
     bool UseCompressedOops   = false
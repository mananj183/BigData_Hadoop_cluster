import os

# Configuration of hdfs-site.xml file
os.chdir("/etc/hadoop/")
myfile1 = open("hdfs-site.xml","w")
myfile1.write('<?xml version="1.0"?>\n')
myfile1.write('<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n')
myfile1.write("<!-- Put site-specific property overrides in this file. -->\n\n")
myfile1.write("<configuration>\n")
myfile1.write("<property>\n")
myfile1.write("<name>dfs.data.dir</name>\n")
myfile1.write("<value>/dn1</value>\n")
myfile1.write("</property>\n")
myfile1.write("</configuration>\n")
myfile1.close()

ip = input("IP Address of namenode: ")

# Configuration of the core-site.xml file
os.chdir("/etc/hadoop/")
myfile2 = open("core-site.xml","w")
myfile2.write('<?xml version="1.0"?>\n')
myfile2.write('<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n')
myfile2.write("<!-- Put site-specific property overrides in this file. -->\n\n")
myfile2.write("<configuration>\n")
myfile2.write("<property>\n")
myfile2.write("<name>fs.default.name</name>\n")
myfile2.write("<value>hdfs://{ip_address}:9001</value>\n".format(ip_address = ip))
myfile2.write("</property>\n")
myfile2.write("</configuration>\n")
myfile2.close()

# Starting the datanode
os.system("hadoop-daemon.sh start datanode")
os.system("jps")



# Automated BigData_Hadoop_cluster
**Setup your own BigData Hadoop Cluster just by simply installing and executing these files in your system. You only need to know what is namenode and datanode and a hadoop cluster and the basics of concept of remote login. Attached is a python script which automatically setups the hadoop cluster using just one system with the help of remote login in your Linux Operating system.**
## Installation Steps:
- Download and Install the hadoop-1.2.1-1.x86_64.rpm and jdk-8u171-linux-x64.rpm softwares.
- In all the systems you use to setup the cluster go to new path `/root/Desktop` by running the command `cd /root/Desktop`
- Create new directory `arth-python` in this path using the command `mkdir arth-python`
- Now you need to setup one system as the `main system` in which you will run your main program
  - In this `Main system` download the `main.py, main_namenode.py and main_datanode.py` files attached here and paste these files in the `arth-python` directory.
  - To confirm the files are present in this directory go to this directory using the command `cd /root/Desktop/arth-python` and run `ls` command to see the files present there.
- Now we setup the sub-system(s) you want to include in the cluster
  - In these `sub-system(s)` download the `namenode.py` and `datanode.py` files attached here and paste these files in the `arth-python` directory.
  - To confirm the files are present in this directory go to this directory using the command `cd /root/Desktop/arth-python` and run `ls` command to see the files present there.
 - Now the `Automation Script` is ready to use to setup the cluster.
 - This automation script can only be run by the `Main System` which contains the `main` program.
 - To run this `automation Script` in the main system go to arth-python directory by running the command `cd /root/Desktop/arth-python` 
 - Now we run the driver program i.e. `main.py` using the command `python3 main.py`.
 ## The output of this script shows a `Menu of options` you can choose to setup the cluster from this one system i.e. Main system while the sub-systems are there in running state which is required for the hadoop cluster to have all the system connected as 'live'.

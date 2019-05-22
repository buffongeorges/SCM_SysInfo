# SCM_SysInfo
github repository: https://github.com/yassine-dridi/SCM_SysInfo.git

Projet Architecture des systèmes Informatiques (software configuration management service )

The goal of this project is to set up a software configuration management environment based on Git, Redmine and Jenkins. We wish to integrate a system that runs unit tests of an application, computes metrics and publish reports. It concerns people who knows about System Configuration Management techniques as well as people who have interest in IT, no related knowledge of the subject but wants to discover this area.


Requirements: an installation of Jenkins, you can get it here
https://jenkins.io/download/

Redmine bitnami https://bitnami.com/stack/redmine


setup: 
in git bash, change directory to your redmine location
cd /c/Bitnami/redmine-4.0.3-2

then clone the repo
git clone --mirror https://github.com/yassine-dridi/SCM_SysInfo.git
<br>
<br>

Then in bitnami, sign in (top right)
administration --> project --> create a new project, then select it --> repositories (the option within the project)
then paste the local path to the git, in my case it was C:\Bitnami\redmine-4.0.3-2\SCM_SysInfo.git

Check the box and save




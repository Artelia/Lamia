This folder is aimed to enable the developpement in a Windows environnement with Visual Studio Code using a docker image.
The analytics repository will be mounted inside the docker container created , which contains all necessary packages.

For doing this :

A - Installations 

1 - Install Visual Studio code ( https://code.visualstudio.com/download )

2 - Install the VSC's plugin "Remote Development extensionpack"

3 - Install git (https://git-scm.com/download/win)

4 - install Docker for windows (>= windows 10) :  https://docs.docker.com/docker-for-windows/install/

	After install, go to settings and :
		a/ enable local drive share in  Resources/file sharing
		b/ set the proxy in Resources/proxies 

5 - install  VcXsrv Windows X Server for gui things (https://sourceforge.net/projects/vcxsrv/ )
     (make sure disable access control is checked when launching)

5 - Start VSC and Docker

B - Set up VSC and Docker

1 - Create a folder on your local drive and clone the analytics' git repository with powershell :

git clone http://gitlab.openocean.fr/openocean/Analytics.git
git fetch -a
git checkout develop

2 - In VSC :

	a/open the command palette (View/Command Palette...) and write "Remote-containers: Open folder in container"
	b/ choose the analytics folder containing the clone 
	c/ wait for VSC to create the docker image (maybe 30mn)
	
3 - You can now code with VSC !!

4 - for working with gui things (geany, qgis...), update the ip adress of DISPLAY var in .devcontainer.json with your ipadress

C - Push your modifications

	a/ open the command palette (View/Command Palette...) and write "Remote-containers: Reopen localy"
	b/ the VSC git functions are now enabled and you can commit/push/... your work.
	c/ open the command palette (View/Command Palette...) and write "Remote-containers: Open folder in container" 
	   to continue working
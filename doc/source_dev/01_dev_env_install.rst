.. toctree::
    :maxdepth: 2

Development environment install
#################################

Prerequites
********************

The dev env here is based on this stack :

* Computer with Windows 10
* Docker installed
* Visual Studio Code installed
* git installed
* vcxsrv for dislaying qt gui

Install all those prerequites before going on

The global logic is :

* code is hosted on win10 filer
* with visual studio, we create a docker image for the environment
* Visual studio mount the win10 image of Lamia repository under /usr/src/Lamia


Download lamia repo
********************

Create an account on github and then :

.. code-block:: 
    
    git clone https://github.com/Artelia/Lamia.git



Configure Visual Studio Code
****************************

You must install the "Remote - Containers" extension. It enables to create a development environment image based 
on the files wihtin the Lamia/.devcontainer repository.

Modify the files within Lamia/.devcontainer repository
*********************************************************

Dockerfile
==============

Depending on the proxy presence, comment or uncomment those two lines

.. code-block:: 

    ARG http_proxy=http://[proxyip]:[proxyport]
    ARG https_proxy=http://[proxyip]:[proxyport]

devcontainer.json
==============

You'll have to adapt those lines dépending on :

* a proxy : uncomment the lines with http_proxy and https_proxy keys
* your local ip (got with ipconfig in powershell) for the DISPLAY key.


.. code-block::

    "remoteEnv": {
        "PATH": "${containerEnv:PATH}:/usr/src/Lamia",
        "PYTHONPATH": "${containerEnv:PYTHONPATH}:/usr/src/Lamia:/usr/share/qgis/python:/usr/share/qgis/python/plugins:/usr/lib/python38.zip:/usr/lib/python3.8",
        "DISPLAY": "192.168.1.17:0.0",
        [ ... ]
        // "http_proxy": "http://[proxyip]:[proxyport]",
        // "https_proxy": "http://[proxyip]:[proxyport]",
    },


Launch vcxsrv
*********************************************************

Launch the vcxsrv app on windows. On starting, choose :

* Start no client

* Disable access control

Launch Docker
*********************************************************

No tricks.

Open the Lamia folder with Visual Studio Code
**********************************************

VSCode will ask you to open Lamia in a remote container. Choose this option.
The first time it can be long as the image of Lamia env has to be built on docker.

It's done !!
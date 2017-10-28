# PyGPToolbox
PyGPToolbox - A python geometry processing toolbox

This is a toolbox of python functions for geometry processing. This toolbox contains only straight python scripts (.py) and only depends on standard python libraries. <br /><br />

## Installation 
Simply adding the "PyGPToolbox/src" directory to your include path and importing desired functions. For example,<br /><br />
_import sys_ <br />
_sys.path.append('/path/to/PyGPToolbox/src')_<br />
_from [functionName] import *_<br /><br />

## Main dependencies: <br />
- numpy<br />
- scipy<br />
- mayavi<br />
- matplotlib<br /><br />

## Optional dependencies: <br />
Few scripts depend on other fantastic libraries. If you do not have these libraries, you can still run most of the scripts. <br />
- PyAMG <br /><br />

## Demos: <br />
To run the demo code, simply go to the "PyGPToolbox/src" folder and run the demo. For example: <br />
_cd /path/to/PyGPToolbox/src_<br />
_python [demo_functionName]_<br /><br />
Here we show few demos using the functions in this PyGPToolbox<br />
- Wave Kernel Signatures [Aubry 11], Heat Kernel Signatures [Sun 09] (demo_kernelSignatures.py)<br />
<img src="https://github.com/htliu1992/PyGPToolbox/raw/master/figures/WKS.gif" width = "300"/><img src="https://github.com/htliu1992/PyGPToolbox/raw/master/figures/HKS.gif" width = "300"/>

- Implicit Mean Curvature Flow [Desbrun 99], Conformal Mean Curvature Flow [Kazhdan 12] (demo_implicitMeanCurvatureFlow.py)<br />
<img src="https://github.com/htliu1992/PyGPToolbox/raw/master/figures/implicitMCF.gif" width = "400"/><img src="https://github.com/htliu1992/PyGPToolbox/raw/master/figures/conformalMCF.gif" width = "250"/>

- Stein Variational Gradient Descent [Liu 16] (demo_SteinVariationalGradientDescent.py)<br />
<img src="https://github.com/htliu1992/PyGPToolbox/raw/master/figures/SVGD.gif" width = "400"/>

## Contact us:<br />
This toolbox is still in development by Hsueh-Ti Derek Liu and has been benefited from members of the Dynamic Graphics Project at University of Toronto. If you have any question or are intersted in contributing, please contact Hsueh-Ti Derek Liu (htliu1992@gmail.com).

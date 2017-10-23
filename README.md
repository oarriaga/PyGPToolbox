# PyGPToolbox
PyGPToolbox - A python geometry processing toolbox

This is a toolbox of python functions for geometry processing. This toolbox contains only straight python scripts (.py) and only depends on standard python libraries. Installation is simply adding the PyGPToolbox directory to your include path. For example,<br /><br />
_import sys_ <br />
_sys.path.append('/path/to/PyGPToolbox')_<br /><br />

To import desired functions, simply add <br /><br />
_from [functionName] import *_<br /><br />

Main dependencies: <br />
- numpy<br />
- scipy<br />
- mayavi<br />
- matplotlib<br /><br />

Optional dependencies: <br />
Few scripts depend on other fantastic libraries. If you do not have these libraries, you can still run most of the scripts. <br />
- PyAMG <br />

Demos: <br />
Here we show few demos using the functions in this PyGPToolbox<br />
- Laplace Eigenfunctions (demo_visualizeLaplace.py)<br />
<img src="https://github.com/htliu1992/PyGPToolbox/raw/master/figures/LaplaceModes.gif" width = "200"/>

- Wave Kernel Signatures (demo_kernelSignatures.py)<br />
<img src="https://github.com/htliu1992/PyGPToolbox/raw/master/figures/WKS.gif" width = "300"/>

- Mean Curvature Flow (demo_implicitMeanCurvatureFlow.py)<br />
<img src="https://github.com/htliu1992/PyGPToolbox/raw/master/figures/implicitMCF.gif" width = "400"/>

- Stein Variational Gradient Descent (demo_demo_SteinVariationalGradientDescent.py)<br />
<img src="https://github.com/htliu1992/PyGPToolbox/raw/master/figures/SVGD.gif" width = "400"/>


Contact us:<br />
This toolbox is still in development by Hsueh-Ti Derek Liu and members of the Dynamic Graphics Project at University of Toronto. If you have any question or are intersted in contributing, please contact Hsueh-Ti Derek Liu (htliu1992@gmail.com).

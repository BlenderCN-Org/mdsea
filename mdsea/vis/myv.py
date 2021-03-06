#!/usr/local/bin/python
# coding: utf-8
import logging

from mayavi import mlab

from mdsea import loghandler
from mdsea.analytics import SysManager, Vis

log = logging.getLogger(__name__)
log.addHandler(loghandler)


class MayaviAnimation(Vis):
    def __init__(self, sm: SysManager, frame_step: int = 1) -> None:
        super(MayaviAnimation, self).__init__(sm, frame_step)
        
        # Disable the rendering, to get bring up the figure quicker:
        figure = mlab.gcf()
        mlab.clf()
        figure.scene.disable_render = True
        
        for i in range(self.sm.NUM_PARTICLES):
            mlab.points3d(self.x[0][i], self.y[0][i], self.z[0][i],
                          color=self.color(self.speeds[0][i], alpha=False),
                          resolution=8 * 3)
        
        # Every object has been created, we can reenable the rendering.
        figure.scene.disable_render = False
        
        mlab.show()

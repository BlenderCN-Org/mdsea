#!/usr/local/bin/python3
# coding: utf-8
from tests import mdsea as md

# Instantiate system manager  ---
sm = md.SysManager.new(ndim=2, num_particles=6 ** 2, steps=500,
                       vol_fraction=0.2, radius_particle=0.5,
                       pot=md.Potential.lennardjones(1, 1))

# Instantiate simulation  ---
sim = md.ContinuousPotentialSolver(sm)

# Generate initial velocities  ---
vgen = md.VelGen(ndim=sm.NDIM, nparticles=sm.NUM_PARTICLES)
sim.v_vec = vgen.mb(sm.MASS, sm.TEMP, sm.K_BOLTZMANN)

# Generate initial positions  ---
cgen = md.PosGen(ndim=sm.NDIM, nparticles=sm.NUM_PARTICLES, boxlen=sm.LEN_BOX)
sim.r_vec = cgen.simplecubic()

# Run the simulation  ---
sim.run_simulation()

# Run 2D animation with matplotlib  ---
from mdsea.vis.mpl import Animation

anim = Animation(sm, frame_step=6)
anim.anim(colorspeed=True)

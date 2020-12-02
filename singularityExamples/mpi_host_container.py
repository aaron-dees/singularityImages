"""
MPI Bandwidth
Contents:
  CentOS 7
  GNU compilers (upstream)
  Mellanox OFED
  OpenMPI version 3.1.2
"""

Stage0 += comment(__doc__, reformat=False)

# CentOS base image
Stage0 += baseimage(image='centos:7')

# GNU compilers
Stage0 += gnu()

# Mellanox OFED
Stage0 += mlnx_ofed()

# OpenMPI
Stage0 += openmpi(configure_opts=['--with-slurm'], infiniband=False, cuda=False, version='3.1.2')

# MPI Hello World
Stage0 += copy(src='hello_world.c', dest='/var/tmp/hello_world.c')
Stage0 += shell(commands=['mpicc -o /usr/local/bin/hello_world /var/tmp/hello_world.c'])

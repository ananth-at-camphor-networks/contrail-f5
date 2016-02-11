#
# Copyright (c) 2013 Juniper Networks, Inc. All rights reserved.
#

env = DefaultEnvironment().Clone()

sources = [
    'setup.py',
    'requirements.txt',
    '__init__.py',
    'f5/__init__.py',
    'f5/bigip/__init__.py',
    'f5/bigip/bigip.py',
    'f5/bigip/bigip_interfaces/__init__.py',
    'f5/bigip/bigip_interfaces/arp.py',
    'f5/bigip/bigip_interfaces/cluster.py',
    'f5/bigip/bigip_interfaces/device.py',
    'f5/bigip/bigip_interfaces/l2gre.py',
    'f5/bigip/bigip_interfaces/monitor.py',
    'f5/bigip/bigip_interfaces/nat.py',
    'f5/bigip/bigip_interfaces/pool.py',
    'f5/bigip/bigip_interfaces/route.py',
    'f5/bigip/bigip_interfaces/rule.py',
    'f5/bigip/bigip_interfaces/selfip.py',
    'f5/bigip/bigip_interfaces/snat.py',
    'f5/bigip/bigip_interfaces/stat.py',
    'f5/bigip/bigip_interfaces/system.py',
    'f5/bigip/bigip_interfaces/virtual_server.py',
    'f5/bigip/bigip_interfaces/vlan.py',
    'f5/bigip/bigip_interfaces/vxlan.py',
    'f5/bigip/exceptions.py',
    'f5/bigip/pycontrol/__init__.py',
    'f5/bigip/pycontrol/pycontrol.py',
    'f5/common/__init__.py',
    'f5/common/constants.py',
    'f5/common/logger.py',
]

sdist_gen = env.Command('dist', sources,
                        'cd ' + Dir('.').path + ' && python setup.py sdist')
env.Default(sdist_gen)
env.Alias('contrail-f5', sdist_gen)

if 'install' in BUILD_TARGETS:
    cmd = 'cd ' + Dir('.').path + ' && python setup.py install %s'
    env.Alias('install',
              env.Command(None, sources, cmd % env['PYTHON_INSTALL_OPT']))

# Local Variables:
# mode: python
# End:

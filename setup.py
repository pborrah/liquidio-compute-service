from distutils.core import setup
setup(name='liquidio-compute-service',
      version='1.0',
      packages=['liquidio_compute_service','liquidio_compute_service.lib','liquidio_compute_service.octlinux_configure', 'liquidio_compute_service.x86_configure'],
      package_data={'liquidio_compute_service':	['liquidio-compute-service.service','liquidio-compute']},
      data_files=[ ('/usr/lib/systemd/system/', ['liquidio-compute-service.service']),('/usr/bin/',['liquidio-compute'])]
     )

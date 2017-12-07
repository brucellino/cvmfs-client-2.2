import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_cvmfs_client(host):
    """Test that the CVMFS client is properly installed"""
    pkg = host.package('cvmfs')
    client = host.file('/usr/bin/cvmfs2')
    version = '2.4.3'

    assert pkg.is_installed
    assert pkg.version.startswith(version)

def test_CODE_RADE_mounted(host):
    """Check that the CODE-RADE repo is mounted"""

    assert host.mount_point("/cvmfs/code-rade.africa-grid.org").exists

def test_CODE_RADE_version(host):
    """Check CODE-RADE version"""

    cvmfs_version = host.file('/cvmfs/code-rade.africa-grid.org/version')
    assert cvmfs_version.exists
    assert cvmfs_version.contains('FR3')
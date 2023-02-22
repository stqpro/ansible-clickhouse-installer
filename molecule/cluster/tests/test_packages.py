"""Test installed packages using testinfra."""

import pytest

@pytest.mark.parametrize("package", [
    "zookeeperd",
    "zookeeper",
    "default-jdk",
    "gnupg",
    "ca-certificates",
    "clickhouse-client",
    "clickhouse-server-common",
    "clickhouse-server-base"
])
def test_packages(host, package):
    pkg = host.package(package)
    assert pkg.is_installed

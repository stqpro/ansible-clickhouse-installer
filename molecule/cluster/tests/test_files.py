"""Test users and files using Testinfra."""

import pytest

@pytest.mark.parametrize("user,group", [
    ("zookeeper", "zookeeper"),
    ("clickhouse", "clickhouse")
])
def test_users(host, user, group):
    usr = host.user(user)
    assert usr.exists
    assert usr.group == group

@pytest.mark.parametrize("name,owner,group", [
    ("/var/lib/zookeeper/myid", "zookeeper", "zookeeper"),
    ("/var/log/zookeeper", "zookeeper", "zookeeper"),
    ("/etc/zookeeper/conf/zoo.cfg", "zookeeper", "zookeeper"),
    ("/etc/clickhouse-server/config.d/clickhouse_macros.xml", "clickhouse", "clickhouse"),
    ("/etc/clickhouse-server/config.d/clickhouse_remote_servers.xml", "clickhouse", "clickhouse"),
    ("/etc/clickhouse-server/config.d/clickhouse_zookeeper.xml", "clickhouse", "clickhouse"),
    ("/etc/clickhouse-server/config.d/clickhouse_config.xml", "clickhouse", "clickhouse"),
])
def test_files(host, name, owner, group):
    target = host.file(name)
    assert target.exists
    assert target.user == owner
    assert target.group == group

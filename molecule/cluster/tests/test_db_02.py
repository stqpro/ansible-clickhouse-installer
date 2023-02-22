"""Testing db writing and reading using testinfra."""


def test_db_read(host):
    cmd = host.run('clickhouse-client --query "SELECT COUNT(*) from test.Migrations;"')
    assert cmd.stdout == "3\n"  # correct if records count equals to nodes count

    cmd = host.run('clickhouse-client --query "DROP TABLE test.Migrations SYNC;"')
    assert cmd.succeeded

    cmd = host.run('clickhouse-client --query "DROP DATABASE test SYNC;"')
    assert cmd.succeeded

"""Testing db writing and reading using testinfra."""


def test_db_record(host):
    cmd = host.run('clickhouse-client --query "CREATE DATABASE test;"')
    assert cmd.succeeded

    cmd = host.run(f'clickhouse-client --query \
        "CREATE TABLE test.Migrations ( date Date DEFAULT toDate(now()), id UInt64, time UInt64) \
        ENGINE = ReplicatedMergeTree(\'/clickhouse/tables/{{shard}}/test/Migrations\', \
        \'{{replica}}\', date, (id, time), 8192);"')
    assert cmd.succeeded

    cmd = host.run('clickhouse-client --query "INSERT INTO test.Migrations (date) VALUES (689);"')
    assert cmd.succeeded

    cmd = host.run('clickhouse-client --query "SELECT * from test.Migrations;"')
    assert cmd.stdout.startswith("1971-11-21")

    cmd = host.run('clickhouse-client --query "DROP TABLE test.Migrations SYNC;"')
    assert cmd.succeeded

    cmd = host.run('clickhouse-client --query "DROP DATABASE test SYNC;"')
    assert cmd.succeeded


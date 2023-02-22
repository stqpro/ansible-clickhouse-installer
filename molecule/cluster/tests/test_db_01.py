"""Testing db writing and reading using testinfra."""


def test_db_record(host):
    cmd = host.run('clickhouse-client --query "CREATE DATABASE test;"')
    assert cmd.succeeded

    cmd = host.run(f'clickhouse-client --query \
        "CREATE TABLE test.Migrations (date Date DEFAULT toDate(now()), uuid UUID, id UInt64) \
        ENGINE = ReplicatedMergeTree(\'/clickhouse/tables/{{shard}}/test/Migrations\', \'{{replica}}\', \
        date, (uuid, id), 8192);"')
    assert cmd.succeeded

    cmd = host.run('clickhouse-client --query "INSERT INTO test.Migrations (uuid) VALUES (generateUUIDv4());"')
    assert cmd.succeeded

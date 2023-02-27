Ansible Clickhouse Installer
=========

Installs Clickhouse to one or several nodes and configures replication with Zookeeper.

Requirements
------------

At this moment the role can install Clickhouse to nodes running only Debian 11 (bullseye).

Example Playbook
----------------

Playbook can be similar to this:

    - name: Set up Clickhouse
    - hosts: clickhouse
      roles:
        - ansible-clickhouse-installer

Specify variable `zookeeper_id` to every host in inventory.

Example inventory file:

    [clickhouse]
    host1 ansible_host=ansible-host-1 zookeeper_id=1
    host2 ansible_host=ansible-host-2 zookeeper_id=2
    host3 ansible_host=ansible-host-3 zookeeper_id=3

License
-------

MIT (whatever it means :) )

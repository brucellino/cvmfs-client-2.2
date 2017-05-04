[![Build Status](https://travis-ci.org/brucellino/cvmfs-client-2.2.svg?branch=master)](https://travis-ci.org/brucellino/cvmfs-client-2.2) [![Code Climate](https://codeclimate.com/github/AAROC/cvmfs-client-2.2/badges/gpa.svg)](https://codeclimate.com/github/AAROC/cvmfs-client-2.2) [![Test Coverage](https://codeclimate.com/github/AAROC/cvmfs-client-2.2/badges/coverage.svg)](https://codeclimate.com/github/AAROC/cvmfs-client-2.2/coverage) [![Issue Count](https://codeclimate.com/github/AAROC/cvmfs-client-2.2/badges/issue_count.svg)](https://codeclimate.com/github/AAROC/cvmfs-client-2.2)

CVMFS client (version 2.2)
=========

This role is to install CVMFS clients and configure them to use the CODE-RADE `fastrepo`.

Requirements
------------

none, but uses escalated priveliges to install packages and start services.

##  Running in Docker containers.

Note that for running in docker containers you need to give Docker access to the fuse module. This can be done by adding :

```
--cap-add SYS_ADMIN --cap-add MKNOD --device=/dev/fuse --sety-opt apparmor:unconfined
```

to the docker run commands.

Role Variables
--------------

  * `prerequisites`: the list of prerequiste packages


Dependencies
------------

none

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: cvmfs-clients
      roles:
         - { role: brucellino.cvmfs-client-2.2, become: true }

License
-------

Apache-2.0

Author Information
------------------

Bruce Becker. http://github.com/brucellino http://brucellino.github.io

For [Africa-Arabia Regional Operations Centre](http://www.africagrid.org)

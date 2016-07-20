[![Build Status](https://travis-ci.org/AAROC/aaroc.github.io.svg?branch=master)](https://travis-ci.org/AAROC/aaroc.github.io)

CVMFS client (version 2.2)
=========

This role is to install CVMFS clients and configure them to use the CODE-RADE `fastrepo`.

Requirements
------------

non

Role Variables
--------------

  * `prerequisites`: the list of prerequiste packages


Dependencies
------------

non

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

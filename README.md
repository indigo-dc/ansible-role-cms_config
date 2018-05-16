cms_config Role
=========

Configure CVMFS,  ENV Variables,  TFC, Proxy, etc for CMS


Role Variables
--------------

Mandatory variables:

- `audience`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_input_path`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_input_protocol`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_local_site`:  MANDATORY - NO DEFAULT AVAILABLE
- `cms_local_site`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_proxycache_token_manager`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_stageoutprefix_fallback`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_stageoutprefix`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_stageoutserver_fallback`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_stageoutserver`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_stageoutsite_fallback`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_stageoutsite`: MANDATORY - NO DEFAULT AVAILABLE
- `iam_access_token`: MANDATORY - NO DEFAULT AVAILABLE
- `iam_client_id`: MANDATORY - NO DEFAULT AVAILABLE
- `iam_client_secret`: MANDATORY - NO DEFAULT AVAILABLE
- `iam_credential_endpoint`: MANDATORY - NO DEFAULT AVAILABLE
- `iam_endpoint`: MANDATORY - NO DEFAULT AVAILABLE
- `mysquid_host`: MANDATORY - NO DEFAULT AVAILABLE
- `mysquid_host`: MANDATORY - NO DEFAULT AVAILABLE
- `proxycache_host`: MANDATORY - NO DEFAULT AVAILABLE
- `proxycache_host`: MANDATORY - NO DEFAULT AVAILABLE
- `watts_endpoint`: MANDATORY - NO DEFAULT AVAILABLE


Optional variables:
- `cms_proxycache_image`:   default: "spiga/ttscache"
- `cms_squid_image`:  default: "spiga/frontiersquidv1"
- `cms_wn_image`:  default: "spiga/cmswn"
- `elasticsearch_secret`: default: ""
- `monitordb_ip`:  default: ""

Dependencies
------------

None

Example Playbook
----------------

This is an example of how to use `cms_config` role:

    - hosts: servers
      roles:
         - { role: indigo-dc.cms_config, cms_config_cms_local_site: "MY_SITE", cms_config_stageoutsite: "MY_STAGEOUTSITE", cms_config_stageoutserver: "MY_STAGEOUTSERVER", cms_config_stageoutprefix: "MY_STAGEOUT_PREFIX", cms_config_stageoutsite_bkp: "MY_STAGEOUTSITE_BKP",  cms_config_stageoutserver_bkp: "MY_STAGEOUTSERVER_BKP", cms_config_iam_token: "MY_IAM_TOKEN", cms_config_iam_client_id: "MY_IAM_CLIENT_ID", cms_config_iam_client_secret: "MY_IAM_CLIENT_SECRET"  }

License
-------

Apache Licence v2 [1]

[1] http://www.apache.org/licenses/LICENSE-2.0


Author Information
------------------

marica.antonacci@ba.infn.it

daniele.spiga@pg.infn.it

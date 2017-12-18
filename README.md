cms_config Role
=========

Configure CVMFS,  ENV Variables,  TFC, Proxy, etc for CMS


Role Variables
--------------

Mandatory variables:

- `cms_config_cms_local_site`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_config_stageoutsite`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_config_stageoutserver`: MANDATORY - NO DEFAULT AVAILABLE 
- `cms_config_stageoutprefix`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_config_stageoutsite_fallback`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_config_stageoutserver_fallback`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_config_stageoutprefix_fallback`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_config_iam_token`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_config_iam_client_id`: MANDATORY - NO DEFAULT AVAILABLE
- `cms_config_iam_client_secret`: MANDATORY - NO DEFAULT AVAILABLE

Optional variables:
- `cms_config_cvmfs_repositories` (default: "cms")
- `cms_config_mysquid_host` (default: "localhost")
- `cms_config_mysquid_port` (default: 3128)
- `cms_config_proxycache_host` (default: "localhost")
- `cms_config_proxycache_port` (default: 80)
- `cms_config_proxycache_serviceport` (default: 8080)
- `cms_config_squid_image` (default: "spiga/frontiersquidv1")
- `cms_config_wn_image` (default: "spiga/cmswndemo_v2")
- `cms_config_proxycache_image` (default: "spiga/ttsinterface_v1")


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

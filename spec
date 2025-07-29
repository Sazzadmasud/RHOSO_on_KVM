apiVersion: core.openstack.org/v1beta1
kind: OpenStackControlPlane
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"core.openstack.org/v1beta1","kind":"OpenStackControlPlane","metadata":{"annotations":{},"name":"openstack-control-plane","namespace":"openstack"},"spec":{"barbican":{"apiOverride":{"route":{}},"enabled":false,"template":{"barbicanAPI":{"override":{"service":{"internal":{"metadata":{"annotations":{"metallb.universe.tf/address-pool":"internalapi","metallb.universe.tf/allow-shared-ip":"internalapi","metallb.universe.tf/loadBalancerIPs":"172.17.0.89"}},"spec":{"type":"LoadBalancer"}}}},"replicas":1},"barbicanKeystoneListener":{"replicas":1},"barbicanWorker":{"replicas":1},"databaseInstance":"openstack","secret":"osp-secret"}},"cinder":{"apiOverride":{"route":{}},"enabled":true,"template":{"cinderAPI":{"override":{"service":{"internal":{"metadata":{"annotations":{"metallb.universe.tf/address-pool":"internalapi","metallb.universe.tf/allow-shared-ip":"internalapi","metallb.universe.tf/loadBalancerIPs":"172.10.20.89"}},"spec":{"type":"LoadBalancer"}}}}},"cinderBackup":{"networkAttachments":["storage"],"replicas":0},"cinderScheduler":{"replicas":1},"cinderVolumes":{"nfs":{"customServiceConfig":"[nfs]\nvolume_backend_name=nfs\nvolume_driver=cinder.volume.drivers.nfs.NfsDriver\nnfs_snapshot_support=true\nnas_secure_file_operations=false\nnas_secure_file_permissions=false\n","customServiceConfigSecrets":["cinder-nfs-config"],"networkAttachments":["storage"]}},"databaseInstance":"openstack","secret":"osp-secret"}},"designate":{"apiOverride":{"route":{}},"enabled":false,"template":{"databaseInstance":"openstack","designateAPI":{"override":{"service":{"internal":{"metadata":{"annotations":{"metallb.universe.tf/address-pool":"internalapi","metallb.universe.tf/allow-shared-ip":"internalapi","metallb.universe.tf/loadBalancerIPs":"172.10.20.89"}},"spec":{"type":"LoadBalancer"}}}}},"designateBackendbind9":{"networkAttachments":["designate"],"replicas":1,"storageClass":"local-storage","storageRequest":"10G"},"designateCentral":{"replicas":1},"designateMdns":{"networkAttachments":["designate"],"replicas":0},"designateProducer":{"replicas":0},"designateWorker":{"networkAttachments":["designate"],"replicas":0},"secret":"osp-secret"}},"dns":{"template":{"options":[{"key":"server","values":["10.0.0.103"]}],"override":{"service":{"metadata":{"annotations":{"metallb.universe.tf/address-pool":"ctlplane","metallb.universe.tf/allow-shared-ip":"ctlplane","metallb.universe.tf/loadBalancerIPs":"172.10.10.89"}},"spec":{"type":"LoadBalancer"}}},"replicas":1}},"galera":{"templates":{"openstack":{"storageRequest":"500M"},"openstack-cell1":{"storageRequest":"500M"}}},"glance":{"enabled":true,"template":{"databaseInstance":"openstack","glanceAPIs":{"default":{"networkAttachments":["storage"],"override":{"service":{"internal":{"metadata":{"annotations":{"metallb.universe.tf/address-pool":"internalapi","metallb.universe.tf/allow-shared-ip":"internalapi","metallb.universe.tf/loadBalancerIPs":"172.10.20.89"}},"spec":{"type":"LoadBalancer"}}}},"replicas":1,"type":"single"}},"keystoneEndpoint":"default","storage":{"storageClass":"nfs","storageRequest":"10G"}}},"heat":{"apiOverride":{"route":{}},"cnfAPIOverride":{"route":{}},"enabled":false,"template":{"databaseInstance":"openstack","heatAPI":{"override":{"service":{"internal":{"metadata":{"annotations":{"metallb.universe.tf/address-pool":"internalapi","metallb.universe.tf/allow-shared-ip":"internalapi","metallb.universe.tf/loadBalancerIPs":"172.10.2089"}},"spec":{"type":"LoadBalancer"}}}},"replicas":1},"heatEngine":{"override":{"service":{"internal":{"metadata":{"annotations":{"metallb.universe.tf/address-pool":"internalapi","metallb.universe.tf/allow-shared-ip":"internalapi","metallb.universe.tf/loadBalancerIPs":"172.10.20.89"}},"spec":{"type":"LoadBalancer"}}}},"replicas":1},"secret":"osp-secret"}},"horizon":{"apiOverride":{"route":{}},"enabled":true,"template":{"replicas":1,"secret":"osp-secret"}},"ironic":{"enabled":false,"template":{"databaseInstance":"openstack","ironicAPI":{"replicas":1},"ironicConductors":[{"replicas":1,"storageRequest":"10G"}],"ironicInspector":{"replicas":1},"ironicNeutronAgent":{"replicas":1},"secret":"osp-secret"}},"keystone":{"apiOverride":{"route":{}},"template":{"databaseInstance":"openstack","override":{"service":{"internal":{"metadata":{"annotations":{"metallb.universe.tf/address-pool":"internalapi","metallb.universe.tf/allow-shared-ip":"internalapi","metallb.universe.tf/loadBalancerIPs":"172.10.20.89"}},"spec":{"type":"LoadBalancer"}}}},"secret":"osp-secret"}},"manila":{"apiOverride":{"route":{}},"enabled":false,"template":{"manilaAPI":{"networkAttachments":["internalapi"],"override":{"service":{"internal":{"metadata":{"annotations":{"metallb.universe.tf/address-pool":"internalapi","metallb.universe.tf/allow-shared-ip":"internalapi","metallb.universe.tf/loadBalancerIPs":"172.10.20.89"}},"spec":{"type":"LoadBalancer"}}}},"replicas":1},"manilaScheduler":{"replicas":1},"manilaShares":{"share1":{"networkAttachments":["storage"],"replicas":1}}}},"memcached":{"templates":{"memcached":{"replicas":1}}},"neutron":{"apiOverride":{"route":{}},"template":{"databaseInstance":"openstack","networkAttachments":["internalapi"],"override":{"service":{"internal":{"metadata":{"annotations":{"metallb.universe.tf/address-pool":"internalapi","metallb.universe.tf/allow-shared-ip":"internalapi","metallb.universe.tf/loadBalancerIPs":"172.10.20.89"}},"spec":{"type":"LoadBalancer"}}}},"secret":"osp-secret"}},"nova":{"apiOverride":{"route":{}},"template":{"apiServiceTemplate":{"override":{"service":{"internal":{"metadata":{"annotations":{"metallb.universe.tf/address-pool":"internalapi","metallb.universe.tf/allow-shared-ip":"internalapi","metallb.universe.tf/loadBalancerIPs":"172.10.20.89"}},"spec":{"type":"LoadBalancer"}}}}},"cellTemplates":{"cell0":{"cellDatabaseAccount":"nova-cell0","cellDatabaseInstance":"openstack","cellMessageBusInstance":"rabbitmq","hasAPIAccess":true},"cell1":{"cellDatabaseAccount":"nova-cell1","cellDatabaseInstance":"openstack-cell1","cellMessageBusInstance":"rabbitmq-cell1","hasAPIAccess":true,"noVNCProxyServiceTemplate":{"enabled":true,"networkAttachments":["internalapi","ctlplane"]}}},"metadataServiceTemplate":{"override":{"service":{"metadata":{"annotations":{"metallb.universe.tf/address-pool":"internalapi","metallb.universe.tf/allow-shared-ip":"internalapi","metallb.universe.tf/loadBalancerIPs":"172.10.20.89"}},"spec":{"type":"LoadBalancer"}}}},"schedulerServiceTemplate":{"override":{"service":{"metadata":{"annotations":{"metallb.universe.tf/address-pool":"internalapi","metallb.universe.tf/allow-shared-ip":"internalapi","metallb.universe.tf/loadBalancerIPs":"172.10.2089"}},"spec":{"type":"LoadBalancer"}}}},"secret":"osp-secret"}},"octavia":{"enabled":false,"template":{"databaseInstance":"openstack","octaviaAPI":{"replicas":1},"secret":"osp-secret"}},"ovn":{"template":{"ovnDBCluster":{"ovndbcluster-nb":{"dbType":"NB","networkAttachment":"internalapi","replicas":1,"storageRequest":"10G"},"ovndbcluster-sb":{"dbType":"SB","networkAttachment":"internalapi","replicas":1,"storageRequest":"10G"}}}},"placement":{"apiOverride":{"route":{}},"template":{"databaseInstance":"openstack","override":{"service":{"internal":{"metadata":{"annotations":{"metallb.universe.tf/address-pool":"internalapi","metallb.universe.tf/allow-shared-ip":"internalapi","metallb.universe.tf/loadBalancerIPs":"172.10.20.89"}},"spec":{"type":"LoadBalancer"}}}},"secret":"osp-secret"}},"rabbitmq":{"templates":{"rabbitmq":{"override":{"service":{"metadata":{"annotations":{"metallb.universe.tf/address-pool":"internalapi","metallb.universe.tf/loadBalancerIPs":"172.10.20.85"}},"spec":{"type":"LoadBalancer"}}}},"rabbitmq-cell1":{"override":{"service":{"metadata":{"annotations":{"metallb.universe.tf/address-pool":"internalapi","metallb.universe.tf/loadBalancerIPs":"172.17.0.86"}},"spec":{"type":"LoadBalancer"}}}}}},"redis":{"enabled":false},"secret":"osp-secret","storageClass":"nfs","swift":{"enabled":true,"proxyOverride":{"route":{}},"template":{"swiftProxy":{"networkAttachments":["storage"],"override":{"service":{"internal":{"metadata":{"annotations":{"metallb.universe.tf/address-pool":"internalapi","metallb.universe.tf/allow-shared-ip":"internalapi","metallb.universe.tf/loadBalancerIPs":"172.10.20.89"}},"spec":{"type":"LoadBalancer"}}}},"replicas":1},"swiftRing":{"ringReplicas":1},"swiftStorage":{"networkAttachments":["storage"],"replicas":1,"storageClass":"nfs","storageRequest":"10Gi"}}},"telemetry":{"enabled":true,"template":{"autoscaling":{"aodh":{"databaseAccount":"aodh","databaseInstance":"openstack","passwordSelectors":null,"secret":"osp-secret"},"enabled":false,"heatInstance":"heat"},"ceilometer":{"enabled":true,"secret":"osp-secret"},"logging":{"annotations":{"metallb.universe.tf/address-pool":"internalapi","metallb.universe.tf/allow-shared-ip":"internalapi","metallb.universe.tf/loadBalancerIPs":"172.10.20.89"},"cloNamespace":"openshift-logging","enabled":false,"ipaddr":"172.17.0.89","port":10514},"metricStorage":{"enabled":false,"monitoringStack":{"alertingEnabled":true,"scrapeInterval":"30s","storage":{"persistent":{"pvcStorageRequest":"20G"},"retention":"24h","strategy":"persistent"}}}}}}}
  creationTimestamp: "2025-07-16T20:49:32Z"
  finalizers:
  - openstack.org/openstackcontrolplane
  generation: 1
  labels:
    core.openstack.org/openstackcontrolplane: ""
  name: openstack-control-plane
  namespace: openstack
  resourceVersion: "9949157"
  uid: 19555e73-dc4c-4ae0-8cd2-cfb5cdbe8eea
spec:
  barbican:
    apiOverride:
      route:
        metadata:
          annotations:
            api.barbican.openstack.org/timeout: 90s
            haproxy.router.openshift.io/timeout: 90s
    enabled: false
    template:
      apiTimeout: 90
      barbicanAPI:
        apiTimeout: 0
        enableSecureRBAC: true
        override:
          service:
            internal:
              metadata:
                annotations:
                  metallb.universe.tf/address-pool: internalapi
                  metallb.universe.tf/allow-shared-ip: internalapi
                  metallb.universe.tf/loadBalancerIPs: 172.17.0.89
              spec:
                type: LoadBalancer
        replicas: 1
        resources: {}
        tls:
          api:
            internal: {}
            public: {}
      barbicanKeystoneListener:
        replicas: 1
        resources: {}
      barbicanWorker:
        replicas: 1
        resources: {}
      databaseAccount: barbican
      databaseInstance: openstack
      globalDefaultSecretStore: simple_crypto
      passwordSelectors:
        pkcs11pin: PKCS11Pin
        service: BarbicanPassword
        simplecryptokek: BarbicanSimpleCryptoKEK
      preserveJobs: false
      rabbitMqClusterName: rabbitmq
      secret: osp-secret
      serviceAccount: ""
      serviceUser: barbican
      simpleCryptoBackendSecret: osp-secret
  cinder:
    apiOverride:
      route:
        metadata:
          annotations:
            api.cinder.openstack.org/timeout: 60s
            haproxy.router.openshift.io/timeout: 60s
    enabled: true
    template:
      apiTimeout: 60
      cinderAPI:
        override:
          service:
            internal:
              metadata:
                annotations:
                  metallb.universe.tf/address-pool: internalapi
                  metallb.universe.tf/allow-shared-ip: internalapi
                  metallb.universe.tf/loadBalancerIPs: 172.10.20.89
              spec:
                type: LoadBalancer
        replicas: 1
        resources: {}
        tls:
          api:
            internal: {}
            public: {}
      cinderBackup:
        networkAttachments:
        - storage
        replicas: 0
        resources: {}
      cinderScheduler:
        replicas: 1
        resources: {}
      cinderVolumes:
        nfs:
          customServiceConfig: |
            [nfs]
            volume_backend_name=nfs
            volume_driver=cinder.volume.drivers.nfs.NfsDriver
            nfs_snapshot_support=true
            nas_secure_file_operations=false
            nas_secure_file_permissions=false
          customServiceConfigSecrets:
          - cinder-nfs-config
          networkAttachments:
          - storage
          replicas: 1
          resources: {}
      databaseAccount: cinder
      databaseInstance: openstack
      dbPurge:
        age: 30
        schedule: 1 0 * * *
      memcachedInstance: memcached
      passwordSelectors:
        service: CinderPassword
      preserveJobs: false
      rabbitMqClusterName: rabbitmq
      secret: osp-secret
      serviceUser: cinder
    uniquePodNames: false
  designate:
    apiOverride:
      route: {}
    enabled: false
    template:
      apiTimeout: 120
      backendMdnsServerProtocol: ""
      backendType: ""
      backendWorkerServerProtocol: ""
      customServiceConfig: '# add your customization here'
      databaseAccount: designate
      databaseInstance: openstack
      designateAPI:
        apiTimeout: 0
        backendMdnsServerProtocol: ""
        backendType: ""
        backendWorkerServerProtocol: ""
        databaseAccount: designate
        override:
          service:
            internal:
              metadata:
                annotations:
                  metallb.universe.tf/address-pool: internalapi
                  metallb.universe.tf/allow-shared-ip: internalapi
                  metallb.universe.tf/loadBalancerIPs: 172.10.20.89
              spec:
                type: LoadBalancer
        passwordSelectors:
          service: DesignatePassword
        replicas: 1
        resources: {}
        secret: ""
        serviceAccount: ""
        serviceUser: designate
        tls:
          api:
            internal: {}
            public: {}
      designateBackendbind9:
        backendMdnsServerProtocol: ""
        backendType: ""
        backendWorkerServerProtocol: ""
        controlNetworkName: designate
        databaseAccount: designate
        netUtilsImage: ""
        networkAttachments:
        - designate
        override: {}
        passwordSelectors:
          service: DesignatePassword
        replicas: 1
        resources: {}
        secret: ""
        serviceAccount: ""
        serviceUser: designate
        storageClass: local-storage
        storageRequest: 10G
      designateCentral:
        backendMdnsServerProtocol: ""
        backendType: ""
        backendWorkerServerProtocol: ""
        databaseAccount: designate
        passwordSelectors:
          service: DesignatePassword
        replicas: 1
        resources: {}
        secret: ""
        serviceAccount: ""
        serviceUser: designate
        tls: {}
      designateMdns:
        backendMdnsServerProtocol: ""
        backendType: ""
        backendWorkerServerProtocol: ""
        controlNetworkName: designate
        databaseAccount: designate
        netUtilsImage: ""
        networkAttachments:
        - designate
        override: {}
        passwordSelectors:
          service: DesignatePassword
        replicas: 0
        resources: {}
        secret: ""
        serviceAccount: ""
        serviceUser: designate
        tls: {}
      designateNetworkAttachment: designate
      designateProducer:
        backendMdnsServerProtocol: ""
        backendType: ""
        backendWorkerServerProtocol: ""
        databaseAccount: designate
        passwordSelectors:
          service: DesignatePassword
        replicas: 0
        resources: {}
        secret: ""
        serviceAccount: ""
        serviceUser: designate
        tls: {}
      designateUnbound:
        override: {}
        replicas: 1
        resources: {}
        serviceAccount: ""
      designateWorker:
        backendMdnsServerProtocol: ""
        backendType: ""
        backendWorkerServerProtocol: ""
        databaseAccount: designate
        networkAttachments:
        - designate
        passwordSelectors:
          service: DesignatePassword
        replicas: 0
        resources: {}
        secret: ""
        serviceAccount: ""
        serviceUser: designate
        tls: {}
      passwordSelectors:
        service: DesignatePassword
      preserveJobs: false
      rabbitMqClusterName: rabbitmq
      redisServiceName: designate-redis
      resources: {}
      secret: osp-secret
      serviceUser: designate
  dns:
    enabled: true
    template:
      dnsDataLabelSelectorValue: dnsdata
      options:
      - key: server
        values:
        - 10.0.0.103
      override:
        service:
          metadata:
            annotations:
              metallb.universe.tf/address-pool: ctlplane
              metallb.universe.tf/allow-shared-ip: ctlplane
              metallb.universe.tf/loadBalancerIPs: 172.10.10.89
          spec:
            type: LoadBalancer
      replicas: 1
  galera:
    enabled: true
    templates:
      openstack:
        logToDisk: false
        replicas: 1
        secret: osp-secret
        storageClass: nfs
        storageRequest: 500M
        tls: {}
      openstack-cell1:
        logToDisk: false
        replicas: 1
        secret: osp-secret
        storageClass: nfs
        storageRequest: 500M
        tls: {}
  glance:
    apiOverrides:
      default:
        route:
          metadata:
            annotations:
              api.glance.openstack.org/timeout: 60s
              haproxy.router.openshift.io/timeout: 60s
    enabled: true
    template:
      apiTimeout: 60
      databaseAccount: glance
      databaseInstance: openstack
      dbPurge:
        age: 30
        schedule: 1 0 * * *
      glanceAPIs:
        default:
          apiTimeout: 60
          containerImage: registry.redhat.io/rhoso/openstack-glance-api-rhel9@sha256:4584fe20883d30267383981da10cfa9838524fe9cda48301f2e5dffc755eb62e
          imageCache:
            cleanerScheduler: '*/30 * * * *'
            prunerScheduler: 1 0 * * *
            size: ""
          networkAttachments:
          - storage
          override:
            service:
              internal:
                metadata:
                  annotations:
                    metallb.universe.tf/address-pool: internalapi
                    metallb.universe.tf/allow-shared-ip: internalapi
                    metallb.universe.tf/loadBalancerIPs: 172.10.20.89
                spec:
                  type: LoadBalancer
          replicas: 1
          resources: {}
          storage: {}
          tls:
            api:
              internal: {}
              public: {}
          type: single
      imageCache:
        cleanerScheduler: ""
        prunerScheduler: ""
        size: ""
      keystoneEndpoint: default
      memcachedInstance: memcached
      passwordSelectors:
        service: GlancePassword
      preserveJobs: false
      quotas:
        imageCountTotal: 0
        imageCountUpload: 0
        imageSizeTotal: 0
        imageStageTotal: 0
      secret: ""
      serviceUser: glance
      storage:
        storageClass: nfs
        storageRequest: 10G
    uniquePodNames: false
  heat:
    apiOverride:
      route:
        metadata:
          annotations:
            api.heat.openstack.org/timeout: 600s
            haproxy.router.openshift.io/timeout: 600s
    cnfAPIOverride:
      route:
        metadata:
          annotations:
            api.heat.openstack.org/timeout: 600s
            haproxy.router.openshift.io/timeout: 600s
    enabled: false
    template:
      apiTimeout: 600
      databaseAccount: heat
      databaseInstance: openstack
      heatAPI:
        override:
          service:
            internal:
              metadata:
                annotations:
                  metallb.universe.tf/address-pool: internalapi
                  metallb.universe.tf/allow-shared-ip: internalapi
                  metallb.universe.tf/loadBalancerIPs: 172.10.2089
              spec:
                type: LoadBalancer
        replicas: 1
        resources: {}
        tls:
          api:
            internal: {}
            public: {}
      heatCfnAPI:
        override: {}
        replicas: 1
        resources: {}
        tls:
          api:
            internal: {}
            public: {}
      heatEngine:
        replicas: 1
        resources: {}
      memcachedInstance: memcached
      passwordSelectors:
        authEncryptionKey: HeatAuthEncryptionKey
        service: HeatPassword
        stackDomainAdminPassword: HeatStackDomainAdminPassword
      preserveJobs: false
      rabbitMqClusterName: rabbitmq
      secret: osp-secret
      serviceUser: heat
  horizon:
    apiOverride:
      route: {}
    enabled: true
    template:
      customServiceConfig: '# add your customization here'
      extraMounts: []
      memcachedInstance: memcached
      override: {}
      preserveJobs: false
      replicas: 1
      resources: {}
      secret: osp-secret
      tls: {}
  ironic:
    apiOverride:
      route:
        metadata:
          annotations:
            api.ironic.openstack.org/timeout: 60s
            haproxy.router.openshift.io/timeout: 60s
    enabled: false
    inspectorOverride:
      route:
        metadata:
          annotations:
            haproxy.router.openshift.io/timeout: 60s
            inspector.ironic.openstack.org/timeout: 60s
    template:
      apiTimeout: 60
      customServiceConfig: '# add your customization here'
      databaseAccount: ironic
      databaseInstance: openstack
      ironicAPI:
        customServiceConfig: '# add your customization here'
        override: {}
        replicas: 1
        resources: {}
        tls:
          api:
            internal: {}
            public: {}
      ironicConductors:
      - conductorGroup: ""
        customServiceConfig: '# add your customization here'
        replicas: 1
        resources: {}
        storageClass: ""
        storageRequest: 10G
      ironicInspector:
        customServiceConfig: '# add your customization here'
        databaseAccount: ironic-inspector
        override: {}
        passwordSelectors:
          service: IronicInspectorPassword
        preserveJobs: true
        replicas: 1
        resources: {}
        serviceUser: ironic-inspector
        tls:
          api:
            internal: {}
            public: {}
      ironicNeutronAgent:
        customServiceConfig: '# add your customization here'
        rabbitMqClusterName: rabbitmq
        replicas: 1
        resources: {}
      passwordSelectors:
        service: IronicPassword
      preserveJobs: true
      rabbitMqClusterName: rabbitmq
      rpcTransport: json-rpc
      secret: osp-secret
      serviceUser: ironic
      standalone: false
      storageClass: nfs
  keystone:
    apiOverride:
      route:
        metadata:
          annotations:
            api.keystone.openstack.org/timeout: 60s
            haproxy.router.openshift.io/timeout: 60s
    enabled: true
    template:
      adminProject: admin
      adminUser: admin
      apiTimeout: 60
      databaseAccount: keystone
      databaseInstance: openstack
      enableSecureRBAC: true
      fernetMaxActiveKeys: 5
      fernetRotationDays: 1
      httpdCustomization:
        processNumber: 3
      memcachedInstance: memcached
      override:
        service:
          internal:
            metadata:
              annotations:
                metallb.universe.tf/address-pool: internalapi
                metallb.universe.tf/allow-shared-ip: internalapi
                metallb.universe.tf/loadBalancerIPs: 172.10.20.89
            spec:
              type: LoadBalancer
      passwordSelectors:
        admin: AdminPassword
      preserveJobs: false
      rabbitMqClusterName: rabbitmq
      region: regionOne
      replicas: 1
      resources: {}
      secret: osp-secret
      tls:
        api:
          internal: {}
          public: {}
      trustFlushArgs: ""
      trustFlushSchedule: 1 * * * *
      trustFlushSuspend: false
  manila:
    apiOverride:
      route:
        metadata:
          annotations:
            api.manila.openstack.org/timeout: 60s
            haproxy.router.openshift.io/timeout: 60s
    enabled: false
    template:
      apiTimeout: 60
      customServiceConfig: '# add your customization here'
      databaseAccount: manila
      dbPurge:
        age: 30
        schedule: 1 0 * * *
      debug:
        dbPurge: false
      manilaAPI:
        customServiceConfig: '# add your customization here'
        networkAttachments:
        - internalapi
        override:
          service:
            internal:
              metadata:
                annotations:
                  metallb.universe.tf/address-pool: internalapi
                  metallb.universe.tf/allow-shared-ip: internalapi
                  metallb.universe.tf/loadBalancerIPs: 172.10.20.89
              spec:
                type: LoadBalancer
        replicas: 1
        resources: {}
        tls:
          api:
            internal: {}
            public: {}
      manilaScheduler:
        customServiceConfig: '# add your customization here'
        replicas: 1
        resources: {}
      manilaShares:
        share1:
          customServiceConfig: '# add your customization here'
          networkAttachments:
          - storage
          replicas: 1
          resources: {}
      memcachedInstance: memcached
      passwordSelectors:
        service: ManilaPassword
      preserveJobs: false
      rabbitMqClusterName: rabbitmq
      serviceUser: manila
  memcached:
    enabled: true
    templates:
      memcached:
        cacheSize: 9932
        maxConn: 8192
        replicas: 1
        tls:
          mtls:
            authCertSecret: {}
  neutron:
    apiOverride:
      route:
        metadata:
          annotations:
            api.neutron.openstack.org/timeout: 120s
            haproxy.router.openshift.io/timeout: 120s
    enabled: true
    template:
      apiTimeout: 120
      corePlugin: ml2
      databaseAccount: neutron
      databaseInstance: openstack
      memcachedInstance: memcached
      ml2MechanismDrivers:
      - ovn
      networkAttachments:
      - internalapi
      override:
        service:
          internal:
            metadata:
              annotations:
                metallb.universe.tf/address-pool: internalapi
                metallb.universe.tf/allow-shared-ip: internalapi
                metallb.universe.tf/loadBalancerIPs: 172.10.20.89
            spec:
              type: LoadBalancer
      passwordSelectors:
        service: NeutronPassword
      preserveJobs: false
      rabbitMqClusterName: rabbitmq
      replicas: 1
      resources: {}
      secret: osp-secret
      serviceUser: neutron
      tls:
        api:
          internal: {}
          public: {}
        ovn: {}
  nova:
    apiOverride:
      route: {}
    enabled: true
    template:
      apiDatabaseAccount: nova-api
      apiDatabaseInstance: openstack
      apiMessageBusInstance: rabbitmq
      apiServiceTemplate:
        customServiceConfig: ""
        override:
          service:
            internal:
              metadata:
                annotations:
                  metallb.universe.tf/address-pool: internalapi
                  metallb.universe.tf/allow-shared-ip: internalapi
                  metallb.universe.tf/loadBalancerIPs: 172.10.20.89
              spec:
                type: LoadBalancer
        replicas: 1
        resources: {}
        tls:
          api:
            internal: {}
            public: {}
      apiTimeout: 60
      cellTemplates:
        cell0:
          cellDatabaseAccount: nova-cell0
          cellDatabaseInstance: openstack
          cellMessageBusInstance: rabbitmq
          conductorServiceTemplate:
            customServiceConfig: ""
            replicas: 1
            resources: {}
          dbPurge:
            archiveAge: 30
            purgeAge: 90
            schedule: 0 0 * * *
          hasAPIAccess: true
          memcachedInstance: ""
          metadataServiceTemplate:
            customServiceConfig: ""
            enabled: false
            override: {}
            replicas: 1
            resources: {}
            tls: {}
          noVNCProxyServiceTemplate:
            customServiceConfig: ""
            enabled: false
            override: {}
            replicas: 1
            resources: {}
            tls:
              service: {}
              vencrypt: {}
        cell1:
          cellDatabaseAccount: nova-cell1
          cellDatabaseInstance: openstack-cell1
          cellMessageBusInstance: rabbitmq-cell1
          conductorServiceTemplate:
            customServiceConfig: ""
            replicas: 1
            resources: {}
          dbPurge:
            archiveAge: 30
            purgeAge: 90
            schedule: 0 0 * * *
          hasAPIAccess: true
          memcachedInstance: ""
          metadataServiceTemplate:
            customServiceConfig: ""
            enabled: false
            override: {}
            replicas: 1
            resources: {}
            tls: {}
          noVNCProxyServiceTemplate:
            customServiceConfig: ""
            enabled: true
            networkAttachments:
            - internalapi
            - ctlplane
            override: {}
            replicas: 1
            resources: {}
            tls:
              service: {}
              vencrypt: {}
      keystoneInstance: keystone
      memcachedInstance: memcached
      metadataServiceTemplate:
        customServiceConfig: ""
        enabled: true
        override:
          service:
            metadata:
              annotations:
                metallb.universe.tf/address-pool: internalapi
                metallb.universe.tf/allow-shared-ip: internalapi
                metallb.universe.tf/loadBalancerIPs: 172.10.20.89
            spec:
              type: LoadBalancer
        replicas: 1
        resources: {}
        tls: {}
      passwordSelectors:
        metadataSecret: MetadataSecret
        prefixMetadataCellsSecret: MetadataCellsSecret
        service: NovaPassword
      preserveJobs: false
      schedulerServiceTemplate:
        customServiceConfig: ""
        replicas: 1
        resources: {}
      secret: osp-secret
      serviceUser: nova
  octavia:
    apiOverride:
      route:
        metadata:
          annotations:
            api.octavia.openstack.org/timeout: 120s
            haproxy.router.openshift.io/timeout: 120s
    enabled: false
    template:
      amphoraCustomFlavors: []
      amphoraImageContainerImage: ""
      apacheContainerImage: ""
      apiTimeout: 120
      customServiceConfig: '# add your customization here'
      databaseAccount: octavia
      databaseInstance: openstack
      lbMgmtNetwork:
        createDefaultLbMgmtNetwork: true
        manageLbMgmtNetworks: true
      octaviaAPI:
        apiTimeout: 0
        customServiceConfig: '# add your customization here'
        databaseAccount: octavia
        databaseInstance: ""
        override: {}
        passwordSelectors:
          database: OctaviaDatabasePassword
          service: OctaviaPassword
        persistenceDatabaseAccount: octavia-persistence
        preserveJobs: false
        replicas: 1
        resources: {}
        secret: ""
        serviceAccount: ""
        serviceUser: octavia
        tenantDomainName: Default
        tenantName: service
        tls:
          api:
            internal: {}
            public: {}
          ovn: {}
      octaviaHealthManager:
        amphoraCustomFlavors: []
        amphoraImageOwnerID: ""
        customServiceConfig: '# add your customization here'
        databaseAccount: ""
        databaseInstance: ""
        lbMgmtNetworkID: ""
        lbSecurityGroupID: ""
        octaviaProviderSubnetCIDR: ""
        octaviaProviderSubnetGateway: ""
        passwordSelectors:
          database: OctaviaDatabasePassword
          service: OctaviaPassword
        persistenceDatabaseAccount: ""
        resources: {}
        role: ""
        secret: ""
        serviceAccount: ""
        serviceUser: ""
        tenantDomainName: ""
        tenantName: ""
        tls: {}
      octaviaHousekeeping:
        amphoraCustomFlavors: []
        amphoraImageOwnerID: ""
        customServiceConfig: '# add your customization here'
        databaseAccount: ""
        databaseInstance: ""
        lbMgmtNetworkID: ""
        lbSecurityGroupID: ""
        octaviaProviderSubnetCIDR: ""
        octaviaProviderSubnetGateway: ""
        passwordSelectors:
          database: OctaviaDatabasePassword
          service: OctaviaPassword
        persistenceDatabaseAccount: ""
        resources: {}
        role: ""
        secret: ""
        serviceAccount: ""
        serviceUser: ""
        tenantDomainName: ""
        tenantName: ""
        tls: {}
      octaviaNetworkAttachment: octavia
      octaviaRsyslog:
        networkAttachments:
        - octavia
        octaviaProviderSubnetCIDR: ""
        octaviaProviderSubnetGateway: ""
        resources: {}
        serviceAccount: ""
        serviceUser: ""
      octaviaWorker:
        amphoraCustomFlavors: []
        amphoraImageOwnerID: ""
        customServiceConfig: '# add your customization here'
        databaseAccount: ""
        databaseInstance: ""
        lbMgmtNetworkID: ""
        lbSecurityGroupID: ""
        octaviaProviderSubnetCIDR: ""
        octaviaProviderSubnetGateway: ""
        passwordSelectors:
          database: OctaviaDatabasePassword
          service: OctaviaPassword
        persistenceDatabaseAccount: ""
        resources: {}
        role: ""
        secret: ""
        serviceAccount: ""
        serviceUser: ""
        tenantDomainName: ""
        tenantName: ""
        tls: {}
      passwordSelectors:
        database: OctaviaDatabasePassword
        service: OctaviaPassword
      persistenceDatabaseAccount: octavia-persistence
      preserveJobs: false
      rabbitMqClusterName: rabbitmq
      resources: {}
      secret: osp-secret
      serviceUser: octavia
      sshPrivkeySecret: octavia-ssh-privkey-secret
      sshPubkey: octavia-ssh-pubkey
      tenantDomainName: Default
      tenantName: service
  openstackclient:
    template:
      openStackConfigMap: openstack-config
      openStackConfigSecret: openstack-config-secret
  ovn:
    enabled: true
    template:
      ovnController:
        external-ids:
          availability-zones: []
          enable-chassis-as-gateway: true
          ovn-bridge: br-int
          ovn-encap-type: geneve
          system-id: random
        networkAttachment: ""
        resources: {}
        tls: {}
      ovnDBCluster:
        ovndbcluster-nb:
          dbType: NB
          electionTimer: 10000
          inactivityProbe: 60000
          logLevel: info
          networkAttachment: internalapi
          override: {}
          probeIntervalToActive: 60000
          replicas: 1
          resources: {}
          storageRequest: 10G
          tls: {}
        ovndbcluster-sb:
          dbType: SB
          electionTimer: 10000
          inactivityProbe: 60000
          logLevel: info
          networkAttachment: internalapi
          override: {}
          probeIntervalToActive: 60000
          replicas: 1
          resources: {}
          storageRequest: 10G
          tls: {}
      ovnNorthd:
        logLevel: info
        nThreads: 1
        replicas: 1
        resources: {}
        tls: {}
  placement:
    apiOverride:
      route: {}
    enabled: true
    template:
      apiTimeout: 60
      customServiceConfig: ""
      databaseAccount: placement
      databaseInstance: openstack
      override:
        service:
          internal:
            metadata:
              annotations:
                metallb.universe.tf/address-pool: internalapi
                metallb.universe.tf/allow-shared-ip: internalapi
                metallb.universe.tf/loadBalancerIPs: 172.10.20.89
            spec:
              type: LoadBalancer
      passwordSelectors:
        service: PlacementPassword
      preserveJobs: false
      replicas: 1
      resources: {}
      secret: osp-secret
      serviceUser: placement
      tls:
        api:
          internal: {}
          public: {}
  rabbitmq:
    enabled: true
    templates:
      rabbitmq:
        delayStartSeconds: 30
        override:
          service:
            metadata:
              annotations:
                metallb.universe.tf/address-pool: internalapi
                metallb.universe.tf/loadBalancerIPs: 172.10.20.85
            spec:
              type: LoadBalancer
        persistence:
          storage: 10Gi
        queueType: Mirrored
        rabbitmq: {}
        replicas: 1
        resources:
          limits:
            cpu: "2"
            memory: 2Gi
          requests:
            cpu: "1"
            memory: 2Gi
        secretBackend:
          externalSecret: {}
        service:
          type: ClusterIP
        terminationGracePeriodSeconds: 604800
        tls: {}
      rabbitmq-cell1:
        delayStartSeconds: 30
        override:
          service:
            metadata:
              annotations:
                metallb.universe.tf/address-pool: internalapi
                metallb.universe.tf/loadBalancerIPs: 172.17.0.86
            spec:
              type: LoadBalancer
        persistence:
          storage: 10Gi
        queueType: Mirrored
        rabbitmq: {}
        replicas: 1
        resources:
          limits:
            cpu: "2"
            memory: 2Gi
          requests:
            cpu: "1"
            memory: 2Gi
        secretBackend:
          externalSecret: {}
        service:
          type: ClusterIP
        terminationGracePeriodSeconds: 604800
        tls: {}
  redis:
    enabled: false
  secret: osp-secret
  storageClass: nfs
  swift:
    enabled: true
    proxyOverride:
      route: {}
    template:
      memcachedInstance: memcached
      storageClass: ""
      swiftProxy:
        ceilometerEnabled: false
        encryptionEnabled: false
        memcachedInstance: memcached
        networkAttachments:
        - storage
        override:
          service:
            internal:
              metadata:
                annotations:
                  metallb.universe.tf/address-pool: internalapi
                  metallb.universe.tf/allow-shared-ip: internalapi
                  metallb.universe.tf/loadBalancerIPs: 172.10.20.89
              spec:
                type: LoadBalancer
        passwordSelectors:
          service: SwiftPassword
        rabbitMqClusterName: rabbitmq
        replicas: 1
        secret: osp-secret
        serviceUser: swift
        tls:
          api:
            internal: {}
            public: {}
      swiftRing:
        minPartHours: 1
        partPower: 10
        ringReplicas: 1
        tls: {}
      swiftStorage:
        containerSharderEnabled: false
        memcachedInstance: memcached
        networkAttachments:
        - storage
        replicas: 1
        storageClass: nfs
        storageRequest: 10Gi
  telemetry:
    alertmanagerOverride: {}
    aodhApiOverride:
      route:
        metadata:
          annotations:
            api.aodh.openstack.org/timeout: 60s
            haproxy.router.openshift.io/timeout: 60s
    enabled: true
    prometheusOverride: {}
    template:
      autoscaling:
        aodh:
          apiTimeout: 60
          customServiceConfig: '# add your customization here'
          databaseAccount: aodh
          databaseInstance: openstack
          memcachedInstance: memcached
          override: {}
          passwordSelector:
            aodhService: AodhPassword
            ceilometerService: CeilometerPassword
          preserveJobs: false
          rabbitMqClusterName: rabbitmq
          secret: osp-secret
          serviceUser: aodh
          tls:
            api:
              internal: {}
              public: {}
        enabled: false
        heatInstance: heat
      ceilometer:
        apiTimeout: 60
        customServiceConfig: '# add your customization here'
        enabled: true
        ksmEnabled: true
        ksmTls: {}
        mysqldExporterDatabaseAccountPrefix: mysqld-exporter
        mysqldExporterTLS: {}
        passwordSelector:
          aodhService: AodhPassword
          ceilometerService: CeilometerPassword
        rabbitMqClusterName: rabbitmq
        secret: osp-secret
        serviceUser: ceilometer
        tls: {}
      logging:
        annotations:
          metallb.universe.tf/address-pool: internalapi
          metallb.universe.tf/allow-shared-ip: internalapi
          metallb.universe.tf/loadBalancerIPs: 172.10.20.89
        cloNamespace: openshift-logging
        enabled: false
        port: 10514
        rsyslogQueueSize: 10000
        rsyslogQueueType: linkedList
        rsyslogRetries: 100
        targetPort: 10514
      metricStorage:
        dashboardsEnabled: false
        dataplaneNetwork: ctlplane
        enabled: false
        monitoringStack:
          alertingEnabled: true
          scrapeInterval: 30s
          storage:
            persistent:
              pvcStorageRequest: 20G
              pvcStorageSelector: {}
            retention: 24h
            strategy: persistent
        prometheusTls: {}
  tls:
    ingress:
      ca:
        duration: 87600h0m0s
      cert:
        duration: 43800h0m0s
      enabled: true
    podLevel:
      enabled: true
      internal:
        ca:
          duration: 87600h0m0s
        cert:
          duration: 43800h0m0s
      libvirt:
        ca:
          duration: 87600h0m0s
        cert:
          duration: 43800h0m0s
      ovn:
        ca:
          duration: 87600h0m0s
        cert:
          duration: 43800h0m0s
status:
  conditions:
  - lastTransitionTime: "2025-07-24T17:21:53Z"
    message: Setup complete
    reason: Ready
    status: "True"
    type: Ready
  - lastTransitionTime: "2025-07-16T20:49:37Z"
    message: OpenStackControlPlane CAs completed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneCAReadyCondition
  - lastTransitionTime: "2025-07-24T02:04:30Z"
    message: OpenStackControlPlane Cinder completed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneCinderReady
  - lastTransitionTime: "2025-07-22T12:44:13Z"
    message: OpenStackControlPlane Client completed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneClientReady
  - lastTransitionTime: "2025-07-24T17:21:52Z"
    message: OpenStackControlPlane DNS completed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneDNSReadyCondition
  - lastTransitionTime: "2025-07-17T02:10:30Z"
    message: OpenStackControlPlane cinder service exposed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneExposeCinderReady
  - lastTransitionTime: "2025-07-17T02:10:30Z"
    message: OpenStackControlPlane glance service exposed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneExposeGlanceReady
  - lastTransitionTime: "2025-07-17T02:10:31Z"
    message: OpenStackControlPlane horizon service exposed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneExposeHorizonReady
  - lastTransitionTime: "2025-07-17T02:10:30Z"
    message: OpenStackControlPlane keystone service exposed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneExposeKeystoneAPIReady
  - lastTransitionTime: "2025-07-17T02:10:30Z"
    message: OpenStackControlPlane neutron service exposed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneExposeNeutronReady
  - lastTransitionTime: "2025-07-17T02:10:30Z"
    message: OpenStackControlPlane nova service exposed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneExposeNovaReady
  - lastTransitionTime: "2025-07-17T02:10:30Z"
    message: OpenStackControlPlane placement service exposed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneExposePlacementAPIReady
  - lastTransitionTime: "2025-07-17T02:10:31Z"
    message: OpenStackControlPlane swift service exposed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneExposeSwiftReady
  - lastTransitionTime: "2025-07-24T02:04:57Z"
    message: OpenStackControlPlane Glance completed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneGlanceReady
  - lastTransitionTime: "2025-07-24T02:04:37Z"
    message: OpenStackControlPlane Horizon completed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneHorizonReady
  - lastTransitionTime: "2025-07-17T02:10:31Z"
    message: OpenStackControlPlane InstanceHa CM is available
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneInstanceHaCMReadyCondition
  - lastTransitionTime: "2025-07-23T22:01:42Z"
    message: OpenStackControlPlane KeystoneAPI completed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneKeystoneAPIReady
  - lastTransitionTime: "2025-07-23T04:46:20Z"
    message: OpenStackControlPlane MariaDB completed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneMariaDBReady
  - lastTransitionTime: "2025-07-17T02:10:30Z"
    message: OpenStackControlPlane Memcached completed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneMemcachedReady
  - lastTransitionTime: "2025-07-24T02:04:52Z"
    message: OpenStackControlPlane Neutron completed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneNeutronReady
  - lastTransitionTime: "2025-07-24T02:04:55Z"
    message: OpenStackControlPlane Nova completed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneNovaReady
  - lastTransitionTime: "2025-07-17T02:10:30Z"
    message: OpenStackControlPlane OVN completed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneOVNReady
  - lastTransitionTime: "2025-07-24T02:04:36Z"
    message: OpenStackControlPlane PlacementAPI completed
    reason: Ready
    status: "True"
    type: OpenStackControlPlanePlacementAPIReady
  - lastTransitionTime: "2025-07-24T02:04:37Z"
    message: OpenStackControlPlane RabbitMQ completed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneRabbitMQReady
  - lastTransitionTime: "2025-07-24T02:04:42Z"
    message: OpenStackControlPlane Swift completed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneSwiftReady
  - lastTransitionTime: "2025-07-24T02:06:25Z"
    message: OpenStackControlPlane Telemetry completed
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneTelemetryReady
  - lastTransitionTime: "2025-07-17T02:10:31Z"
    message: OpenStackControlPlane Test Operator CM is available
    reason: Ready
    status: "True"
    type: OpenStackControlPlaneTestCMReadyCondition
  containerImages:
    aodhAPIImage: registry.redhat.io/rhoso/openstack-aodh-api-rhel9@sha256:04fe31852a9668a686c08fb7f312acb73efcc2847225cf042eedfb788fffdaba
    aodhEvaluatorImage: registry.redhat.io/rhoso/openstack-aodh-evaluator-rhel9@sha256:79d4eacc995c1bea57cc7e3d77d61339327cf0fb327f8dbdf448e3749c066f21
    aodhListenerImage: registry.redhat.io/rhoso/openstack-aodh-listener-rhel9@sha256:d4983477091ab27af69dac650889c0b31ea2003ef75734ddf41f42a024bee4a7
    aodhNotifierImage: registry.redhat.io/rhoso/openstack-aodh-notifier-rhel9@sha256:1bf60d34c4694163617650fd382c8833c8b8477d75b8bfa6ac884efbeb0bbb2d
    ceilometerCentralImage: registry.redhat.io/rhoso/openstack-ceilometer-central-rhel9@sha256:3a90bca65461702be51c1b46715209dc1145d0dd5d12733f51c8e1c6fab896e9
    ceilometerComputeImage: registry.redhat.io/rhoso/openstack-ceilometer-compute-rhel9@sha256:4764e17fe45fbb97694434d03ca0d6e4ea4f0a0ed4f9e46cbd1e38119fc47ffb
    ceilometerIpmiImage: registry.redhat.io/rhoso/openstack-ceilometer-ipmi-rhel9@sha256:7969b327e27b76d8a71396c38bb645701ca53bd880ca9ba1bbe3a45ec92b8e9e
    ceilometerNotificationImage: registry.redhat.io/rhoso/openstack-ceilometer-notification-rhel9@sha256:7dbecf6a0b3932f8b716bf5c3d78b3e794909a09af89c76d43f92b795fd27ce1
    ceilometerProxyImage: registry.redhat.io/ubi9/httpd-24@sha256:8439671ecde9adff63df7e4ea8fc10c7cb95195e466cdbe021bac93e82fd245e
    ceilometerSgcoreImage: registry.redhat.io/rhoso-operators/sg-core-rhel9@sha256:35100dc20f944338a47edb1f2b5e7c31c5ddc09565f56582a4811bb689cb0bdd
    cinderAPIImage: registry.redhat.io/rhoso/openstack-cinder-api-rhel9@sha256:1696a137d18218b5f787fb9400c64b67da22ea20762aeadb5328e6f271d19a77
    cinderBackupImage: registry.redhat.io/rhoso/openstack-cinder-backup-rhel9@sha256:f285ba1b2181f65d924cf586b2a100e2d532feaf9c86583d975152b11655d419
    cinderSchedulerImage: registry.redhat.io/rhoso/openstack-cinder-scheduler-rhel9@sha256:02d1952043d73eb2085cff4d65da1e297de6139aee874934dd1a60afd61e59c7
    cinderVolumeImages:
      default: registry.redhat.io/rhoso/openstack-cinder-volume-rhel9@sha256:5972701016be71d9ef4b31a6d5f5102c441678ded14ea8bb59d46323d818e55e
    glanceAPIImage: registry.redhat.io/rhoso/openstack-glance-api-rhel9@sha256:4584fe20883d30267383981da10cfa9838524fe9cda48301f2e5dffc755eb62e
    horizonImage: registry.redhat.io/rhoso/openstack-horizon-rhel9@sha256:ce15372d5123882baaa97ea644d37fc1466cccfe2037588752f59c3bcbe25f27
    infraDnsmasqImage: registry.redhat.io/rhoso/openstack-neutron-server-rhel9@sha256:9817cb5c2813ab42c82bda27fc18e44de624ef560940ff27c61362bcfd8d031a
    infraMemcachedImage: registry.redhat.io/rhoso/openstack-memcached-rhel9@sha256:5b635a44c99e2d5a358c607874aa8579b450ec61073f0bdafeb5bb5b68b24f18
    keystoneAPIImage: registry.redhat.io/rhoso/openstack-keystone-rhel9@sha256:8babdbfd9864f0dcf402d02ed337ea485427213b6a3252d38ff5a788a6b5eee4
    ksmImage: registry.redhat.io/openshift4/ose-kube-state-metrics-rhel9@sha256:1bfade9393da8f9d7894ab11077c29ca2af8a0308af21974edb1cc9429d37061
    mariadbImage: registry.redhat.io/rhoso/openstack-mariadb-rhel9@sha256:10488b7a1f1f643271a19384c20fda89008c2198619496f01cb27090dab24315
    neutronAPIImage: registry.redhat.io/rhoso/openstack-neutron-server-rhel9@sha256:9817cb5c2813ab42c82bda27fc18e44de624ef560940ff27c61362bcfd8d031a
    novaAPIImage: registry.redhat.io/rhoso/openstack-nova-api-rhel9@sha256:209d4df3585dadd212a27ab071936203af37b54a9a9a84352fee9623b46f635e
    novaComputeImage: registry.redhat.io/rhoso/openstack-nova-compute-rhel9@sha256:1be2ab3ff127a4f0df91d7681aa5a034f953328e21a85f8ef5aa942a5ac4536b
    novaConductorImage: registry.redhat.io/rhoso/openstack-nova-conductor-rhel9@sha256:9f446f74410039df82e5bc8899f182be270d4137b71ba21a7e74d8472953a2f4
    novaNovncImage: registry.redhat.io/rhoso/openstack-nova-novncproxy-rhel9@sha256:cabc8e694da286c1acaec4da2e9d2aa9b7493f0d1aaf6dfa198e480fdf335163
    novaSchedulerImage: registry.redhat.io/rhoso/openstack-nova-scheduler-rhel9@sha256:7ab2e14d25402102c685ff778b63b3de5519cb760ae37454904d32098d62deaf
    openstackClientImage: registry.redhat.io/rhoso/openstack-openstackclient-rhel9@sha256:961e2d2057eb6088026a84373cf53e4e678e6e841680bca0ba8121022c396214
    ovnControllerImage: registry.redhat.io/rhoso/openstack-ovn-controller-rhel9@sha256:71ac4a3caf468fbe6972c5a8d089d10b858915fce0372d805093d347c78635a5
    ovnControllerOvsImage: registry.redhat.io/rhoso/openstack-ovn-base-rhel9@sha256:6d187d6f14584dc02067f0f2a95fe7486c9346a1d8dd491ea1cc683246fa68fa
    ovnNbDbclusterImage: registry.redhat.io/rhoso/openstack-ovn-nb-db-server-rhel9@sha256:cedb40ffa0a82343d659d59da2a5da78b2c5bda20a5b65e5a8f7582335d164b5
    ovnNorthdImage: registry.redhat.io/rhoso/openstack-ovn-northd-rhel9@sha256:77d33d53378f73c97c0457c38b6ed28e45d63fa51e1ecaf57ff597e84b81e41d
    ovnSbDbclusterImage: registry.redhat.io/rhoso/openstack-ovn-sb-db-server-rhel9@sha256:4f9df345696687e618663328713e401a14edafa2017e3ebcae0bd93c3060ea2d
    placementAPIImage: registry.redhat.io/rhoso/openstack-placement-api-rhel9@sha256:067488809d2cced255616d36ece211a342421b64d70e338de0065bc087a6b86b
    swiftAccountImage: registry.redhat.io/rhoso/openstack-swift-account-rhel9@sha256:f7b1c49ae89de6042324c592e7a77b290f0e42c64813bb1ab49f5e0316ba6533
    swiftContainerImage: registry.redhat.io/rhoso/openstack-swift-container-rhel9@sha256:7c0b2702d7f53ef82f46b3ecf9be1cb284e755f310c9d16c6a122a4ffd661a6c
    swiftObjectImage: registry.redhat.io/rhoso/openstack-swift-object-rhel9@sha256:dc9e0ea6f95cfb280a47735b51c59149eadc8231b216574f1c36430b5b644e92
    swiftProxyImage: registry.redhat.io/rhoso/openstack-swift-proxy-server-rhel9@sha256:4670b562b90366d27932c93499e4792eae93f8b598d5f12601fce73543b81b44
  deployedVersion: 18.0.9-20250602.2
  observedGeneration: 1
  tls:
    caBundleSecretName: combined-ca-bundle
    caList:
    - expires: "2035-07-14T20:49:09Z"
      name: rootca-public
    - expires: "2035-07-14T20:49:10Z"
      name: rootca-internal
    - expires: "2035-07-14T20:49:35Z"
      name: rootca-libvirt
    - expires: "2035-07-14T20:49:36Z"
      name: rootca-ovn

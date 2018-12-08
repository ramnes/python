# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.12.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1PodSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'active_deadline_seconds': 'int',
        'affinity': 'V1Affinity',
        'automount_service_account_token': 'bool',
        'containers': 'list[V1Container]',
        'dns_config': 'V1PodDNSConfig',
        'dns_policy': 'str',
        'host_aliases': 'list[V1HostAlias]',
        'host_ipc': 'bool',
        'host_network': 'bool',
        'host_pid': 'bool',
        'hostname': 'str',
        'image_pull_secrets': 'list[V1LocalObjectReference]',
        'init_containers': 'list[V1Container]',
        'node_name': 'str',
        'node_selector': 'dict(str, str)',
        'priority': 'int',
        'priority_class_name': 'str',
        'readiness_gates': 'list[V1PodReadinessGate]',
        'restart_policy': 'str',
        'runtime_class_name': 'str',
        'scheduler_name': 'str',
        'security_context': 'V1PodSecurityContext',
        'service_account': 'str',
        'service_account_name': 'str',
        'share_process_namespace': 'bool',
        'subdomain': 'str',
        'termination_grace_period_seconds': 'int',
        'tolerations': 'list[V1Toleration]',
        'volumes': 'list[V1Volume]'
    }

    attribute_map = {
        'active_deadline_seconds': 'activeDeadlineSeconds',
        'affinity': 'affinity',
        'automount_service_account_token': 'automountServiceAccountToken',
        'containers': 'containers',
        'dns_config': 'dnsConfig',
        'dns_policy': 'dnsPolicy',
        'host_aliases': 'hostAliases',
        'host_ipc': 'hostIPC',
        'host_network': 'hostNetwork',
        'host_pid': 'hostPID',
        'hostname': 'hostname',
        'image_pull_secrets': 'imagePullSecrets',
        'init_containers': 'initContainers',
        'node_name': 'nodeName',
        'node_selector': 'nodeSelector',
        'priority': 'priority',
        'priority_class_name': 'priorityClassName',
        'readiness_gates': 'readinessGates',
        'restart_policy': 'restartPolicy',
        'runtime_class_name': 'runtimeClassName',
        'scheduler_name': 'schedulerName',
        'security_context': 'securityContext',
        'service_account': 'serviceAccount',
        'service_account_name': 'serviceAccountName',
        'share_process_namespace': 'shareProcessNamespace',
        'subdomain': 'subdomain',
        'termination_grace_period_seconds': 'terminationGracePeriodSeconds',
        'tolerations': 'tolerations',
        'volumes': 'volumes'
    }

    def __init__(self, active_deadline_seconds=None, affinity=None, automount_service_account_token=None, containers=None, dns_config=None, dns_policy=None, host_aliases=None, host_ipc=None, host_network=None, host_pid=None, hostname=None, image_pull_secrets=None, init_containers=None, node_name=None, node_selector=None, priority=None, priority_class_name=None, readiness_gates=None, restart_policy=None, runtime_class_name=None, scheduler_name=None, security_context=None, service_account=None, service_account_name=None, share_process_namespace=None, subdomain=None, termination_grace_period_seconds=None, tolerations=None, volumes=None):
        """
        V1PodSpec - a model defined in Swagger
        """

        self._active_deadline_seconds = None
        self._affinity = None
        self._automount_service_account_token = None
        self._containers = None
        self._dns_config = None
        self._dns_policy = None
        self._host_aliases = None
        self._host_ipc = None
        self._host_network = None
        self._host_pid = None
        self._hostname = None
        self._image_pull_secrets = None
        self._init_containers = None
        self._node_name = None
        self._node_selector = None
        self._priority = None
        self._priority_class_name = None
        self._readiness_gates = None
        self._restart_policy = None
        self._runtime_class_name = None
        self._scheduler_name = None
        self._security_context = None
        self._service_account = None
        self._service_account_name = None
        self._share_process_namespace = None
        self._subdomain = None
        self._termination_grace_period_seconds = None
        self._tolerations = None
        self._volumes = None
        self.discriminator = None

        if active_deadline_seconds is not None:
          self.active_deadline_seconds = active_deadline_seconds
        if affinity is not None:
          self.affinity = affinity
        if automount_service_account_token is not None:
          self.automount_service_account_token = automount_service_account_token
        self.containers = containers
        if dns_config is not None:
          self.dns_config = dns_config
        if dns_policy is not None:
          self.dns_policy = dns_policy
        if host_aliases is not None:
          self.host_aliases = host_aliases
        if host_ipc is not None:
          self.host_ipc = host_ipc
        if host_network is not None:
          self.host_network = host_network
        if host_pid is not None:
          self.host_pid = host_pid
        if hostname is not None:
          self.hostname = hostname
        if image_pull_secrets is not None:
          self.image_pull_secrets = image_pull_secrets
        if init_containers is not None:
          self.init_containers = init_containers
        if node_name is not None:
          self.node_name = node_name
        if node_selector is not None:
          self.node_selector = node_selector
        if priority is not None:
          self.priority = priority
        if priority_class_name is not None:
          self.priority_class_name = priority_class_name
        if readiness_gates is not None:
          self.readiness_gates = readiness_gates
        if restart_policy is not None:
          self.restart_policy = restart_policy
        if runtime_class_name is not None:
          self.runtime_class_name = runtime_class_name
        if scheduler_name is not None:
          self.scheduler_name = scheduler_name
        if security_context is not None:
          self.security_context = security_context
        if service_account is not None:
          self.service_account = service_account
        if service_account_name is not None:
          self.service_account_name = service_account_name
        if share_process_namespace is not None:
          self.share_process_namespace = share_process_namespace
        if subdomain is not None:
          self.subdomain = subdomain
        if termination_grace_period_seconds is not None:
          self.termination_grace_period_seconds = termination_grace_period_seconds
        if tolerations is not None:
          self.tolerations = tolerations
        if volumes is not None:
          self.volumes = volumes

    @property
    def active_deadline_seconds(self):
        """
        Gets the active_deadline_seconds of this V1PodSpec.
        Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.

        :return: The active_deadline_seconds of this V1PodSpec.
        :rtype: int
        """
        return self._active_deadline_seconds

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds):
        """
        Sets the active_deadline_seconds of this V1PodSpec.
        Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.

        :param active_deadline_seconds: The active_deadline_seconds of this V1PodSpec.
        :type: int
        """

        self._active_deadline_seconds = active_deadline_seconds

    @property
    def affinity(self):
        """
        Gets the affinity of this V1PodSpec.
        If specified, the pod's scheduling constraints

        :return: The affinity of this V1PodSpec.
        :rtype: V1Affinity
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """
        Sets the affinity of this V1PodSpec.
        If specified, the pod's scheduling constraints

        :param affinity: The affinity of this V1PodSpec.
        :type: V1Affinity
        """

        self._affinity = affinity

    @property
    def automount_service_account_token(self):
        """
        Gets the automount_service_account_token of this V1PodSpec.
        AutomountServiceAccountToken indicates whether a service account token should be automatically mounted.

        :return: The automount_service_account_token of this V1PodSpec.
        :rtype: bool
        """
        return self._automount_service_account_token

    @automount_service_account_token.setter
    def automount_service_account_token(self, automount_service_account_token):
        """
        Sets the automount_service_account_token of this V1PodSpec.
        AutomountServiceAccountToken indicates whether a service account token should be automatically mounted.

        :param automount_service_account_token: The automount_service_account_token of this V1PodSpec.
        :type: bool
        """

        self._automount_service_account_token = automount_service_account_token

    @property
    def containers(self):
        """
        Gets the containers of this V1PodSpec.
        List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.

        :return: The containers of this V1PodSpec.
        :rtype: list[V1Container]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        """
        Sets the containers of this V1PodSpec.
        List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.

        :param containers: The containers of this V1PodSpec.
        :type: list[V1Container]
        """
        if containers is None:
            raise ValueError("Invalid value for `containers`, must not be `None`")

        self._containers = containers

    @property
    def dns_config(self):
        """
        Gets the dns_config of this V1PodSpec.
        Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy.

        :return: The dns_config of this V1PodSpec.
        :rtype: V1PodDNSConfig
        """
        return self._dns_config

    @dns_config.setter
    def dns_config(self, dns_config):
        """
        Sets the dns_config of this V1PodSpec.
        Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy.

        :param dns_config: The dns_config of this V1PodSpec.
        :type: V1PodDNSConfig
        """

        self._dns_config = dns_config

    @property
    def dns_policy(self):
        """
        Gets the dns_policy of this V1PodSpec.
        Set DNS policy for the pod. Defaults to \"ClusterFirst\". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.

        :return: The dns_policy of this V1PodSpec.
        :rtype: str
        """
        return self._dns_policy

    @dns_policy.setter
    def dns_policy(self, dns_policy):
        """
        Sets the dns_policy of this V1PodSpec.
        Set DNS policy for the pod. Defaults to \"ClusterFirst\". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.

        :param dns_policy: The dns_policy of this V1PodSpec.
        :type: str
        """

        self._dns_policy = dns_policy

    @property
    def host_aliases(self):
        """
        Gets the host_aliases of this V1PodSpec.
        HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts file if specified. This is only valid for non-hostNetwork pods.

        :return: The host_aliases of this V1PodSpec.
        :rtype: list[V1HostAlias]
        """
        return self._host_aliases

    @host_aliases.setter
    def host_aliases(self, host_aliases):
        """
        Sets the host_aliases of this V1PodSpec.
        HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts file if specified. This is only valid for non-hostNetwork pods.

        :param host_aliases: The host_aliases of this V1PodSpec.
        :type: list[V1HostAlias]
        """

        self._host_aliases = host_aliases

    @property
    def host_ipc(self):
        """
        Gets the host_ipc of this V1PodSpec.
        Use the host's ipc namespace. Optional: Default to false.

        :return: The host_ipc of this V1PodSpec.
        :rtype: bool
        """
        return self._host_ipc

    @host_ipc.setter
    def host_ipc(self, host_ipc):
        """
        Sets the host_ipc of this V1PodSpec.
        Use the host's ipc namespace. Optional: Default to false.

        :param host_ipc: The host_ipc of this V1PodSpec.
        :type: bool
        """

        self._host_ipc = host_ipc

    @property
    def host_network(self):
        """
        Gets the host_network of this V1PodSpec.
        Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.

        :return: The host_network of this V1PodSpec.
        :rtype: bool
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        """
        Sets the host_network of this V1PodSpec.
        Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.

        :param host_network: The host_network of this V1PodSpec.
        :type: bool
        """

        self._host_network = host_network

    @property
    def host_pid(self):
        """
        Gets the host_pid of this V1PodSpec.
        Use the host's pid namespace. Optional: Default to false.

        :return: The host_pid of this V1PodSpec.
        :rtype: bool
        """
        return self._host_pid

    @host_pid.setter
    def host_pid(self, host_pid):
        """
        Sets the host_pid of this V1PodSpec.
        Use the host's pid namespace. Optional: Default to false.

        :param host_pid: The host_pid of this V1PodSpec.
        :type: bool
        """

        self._host_pid = host_pid

    @property
    def hostname(self):
        """
        Gets the hostname of this V1PodSpec.
        Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.

        :return: The hostname of this V1PodSpec.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this V1PodSpec.
        Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.

        :param hostname: The hostname of this V1PodSpec.
        :type: str
        """

        self._hostname = hostname

    @property
    def image_pull_secrets(self):
        """
        Gets the image_pull_secrets of this V1PodSpec.
        ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod

        :return: The image_pull_secrets of this V1PodSpec.
        :rtype: list[V1LocalObjectReference]
        """
        return self._image_pull_secrets

    @image_pull_secrets.setter
    def image_pull_secrets(self, image_pull_secrets):
        """
        Sets the image_pull_secrets of this V1PodSpec.
        ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod

        :param image_pull_secrets: The image_pull_secrets of this V1PodSpec.
        :type: list[V1LocalObjectReference]
        """

        self._image_pull_secrets = image_pull_secrets

    @property
    def init_containers(self):
        """
        Gets the init_containers of this V1PodSpec.
        List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, or Liveness probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/

        :return: The init_containers of this V1PodSpec.
        :rtype: list[V1Container]
        """
        return self._init_containers

    @init_containers.setter
    def init_containers(self, init_containers):
        """
        Sets the init_containers of this V1PodSpec.
        List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, or Liveness probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/

        :param init_containers: The init_containers of this V1PodSpec.
        :type: list[V1Container]
        """

        self._init_containers = init_containers

    @property
    def node_name(self):
        """
        Gets the node_name of this V1PodSpec.
        NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.

        :return: The node_name of this V1PodSpec.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """
        Sets the node_name of this V1PodSpec.
        NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.

        :param node_name: The node_name of this V1PodSpec.
        :type: str
        """

        self._node_name = node_name

    @property
    def node_selector(self):
        """
        Gets the node_selector of this V1PodSpec.
        NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/

        :return: The node_selector of this V1PodSpec.
        :rtype: dict(str, str)
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """
        Sets the node_selector of this V1PodSpec.
        NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/

        :param node_selector: The node_selector of this V1PodSpec.
        :type: dict(str, str)
        """

        self._node_selector = node_selector

    @property
    def priority(self):
        """
        Gets the priority of this V1PodSpec.
        The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority.

        :return: The priority of this V1PodSpec.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this V1PodSpec.
        The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority.

        :param priority: The priority of this V1PodSpec.
        :type: int
        """

        self._priority = priority

    @property
    def priority_class_name(self):
        """
        Gets the priority_class_name of this V1PodSpec.
        If specified, indicates the pod's priority. \"system-node-critical\" and \"system-cluster-critical\" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default.

        :return: The priority_class_name of this V1PodSpec.
        :rtype: str
        """
        return self._priority_class_name

    @priority_class_name.setter
    def priority_class_name(self, priority_class_name):
        """
        Sets the priority_class_name of this V1PodSpec.
        If specified, indicates the pod's priority. \"system-node-critical\" and \"system-cluster-critical\" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default.

        :param priority_class_name: The priority_class_name of this V1PodSpec.
        :type: str
        """

        self._priority_class_name = priority_class_name

    @property
    def readiness_gates(self):
        """
        Gets the readiness_gates of this V1PodSpec.
        If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to \"True\" More info: https://github.com/kubernetes/community/blob/master/keps/sig-network/0007-pod-ready%2B%2B.md

        :return: The readiness_gates of this V1PodSpec.
        :rtype: list[V1PodReadinessGate]
        """
        return self._readiness_gates

    @readiness_gates.setter
    def readiness_gates(self, readiness_gates):
        """
        Sets the readiness_gates of this V1PodSpec.
        If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to \"True\" More info: https://github.com/kubernetes/community/blob/master/keps/sig-network/0007-pod-ready%2B%2B.md

        :param readiness_gates: The readiness_gates of this V1PodSpec.
        :type: list[V1PodReadinessGate]
        """

        self._readiness_gates = readiness_gates

    @property
    def restart_policy(self):
        """
        Gets the restart_policy of this V1PodSpec.
        Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy

        :return: The restart_policy of this V1PodSpec.
        :rtype: str
        """
        return self._restart_policy

    @restart_policy.setter
    def restart_policy(self, restart_policy):
        """
        Sets the restart_policy of this V1PodSpec.
        Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy

        :param restart_policy: The restart_policy of this V1PodSpec.
        :type: str
        """

        self._restart_policy = restart_policy

    @property
    def runtime_class_name(self):
        """
        Gets the runtime_class_name of this V1PodSpec.
        RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod.  If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the \"legacy\" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: https://github.com/kubernetes/community/blob/master/keps/sig-node/0014-runtime-class.md This is an alpha feature and may change in the future.

        :return: The runtime_class_name of this V1PodSpec.
        :rtype: str
        """
        return self._runtime_class_name

    @runtime_class_name.setter
    def runtime_class_name(self, runtime_class_name):
        """
        Sets the runtime_class_name of this V1PodSpec.
        RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod.  If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the \"legacy\" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: https://github.com/kubernetes/community/blob/master/keps/sig-node/0014-runtime-class.md This is an alpha feature and may change in the future.

        :param runtime_class_name: The runtime_class_name of this V1PodSpec.
        :type: str
        """

        self._runtime_class_name = runtime_class_name

    @property
    def scheduler_name(self):
        """
        Gets the scheduler_name of this V1PodSpec.
        If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler.

        :return: The scheduler_name of this V1PodSpec.
        :rtype: str
        """
        return self._scheduler_name

    @scheduler_name.setter
    def scheduler_name(self, scheduler_name):
        """
        Sets the scheduler_name of this V1PodSpec.
        If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler.

        :param scheduler_name: The scheduler_name of this V1PodSpec.
        :type: str
        """

        self._scheduler_name = scheduler_name

    @property
    def security_context(self):
        """
        Gets the security_context of this V1PodSpec.
        SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.

        :return: The security_context of this V1PodSpec.
        :rtype: V1PodSecurityContext
        """
        return self._security_context

    @security_context.setter
    def security_context(self, security_context):
        """
        Sets the security_context of this V1PodSpec.
        SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.

        :param security_context: The security_context of this V1PodSpec.
        :type: V1PodSecurityContext
        """

        self._security_context = security_context

    @property
    def service_account(self):
        """
        Gets the service_account of this V1PodSpec.
        DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.

        :return: The service_account of this V1PodSpec.
        :rtype: str
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        """
        Sets the service_account of this V1PodSpec.
        DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.

        :param service_account: The service_account of this V1PodSpec.
        :type: str
        """

        self._service_account = service_account

    @property
    def service_account_name(self):
        """
        Gets the service_account_name of this V1PodSpec.
        ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/

        :return: The service_account_name of this V1PodSpec.
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        """
        Sets the service_account_name of this V1PodSpec.
        ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/

        :param service_account_name: The service_account_name of this V1PodSpec.
        :type: str
        """

        self._service_account_name = service_account_name

    @property
    def share_process_namespace(self):
        """
        Gets the share_process_namespace of this V1PodSpec.
        Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false. This field is beta-level and may be disabled with the PodShareProcessNamespace feature.

        :return: The share_process_namespace of this V1PodSpec.
        :rtype: bool
        """
        return self._share_process_namespace

    @share_process_namespace.setter
    def share_process_namespace(self, share_process_namespace):
        """
        Sets the share_process_namespace of this V1PodSpec.
        Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false. This field is beta-level and may be disabled with the PodShareProcessNamespace feature.

        :param share_process_namespace: The share_process_namespace of this V1PodSpec.
        :type: bool
        """

        self._share_process_namespace = share_process_namespace

    @property
    def subdomain(self):
        """
        Gets the subdomain of this V1PodSpec.
        If specified, the fully qualified Pod hostname will be \"<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>\". If not specified, the pod will not have a domainname at all.

        :return: The subdomain of this V1PodSpec.
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """
        Sets the subdomain of this V1PodSpec.
        If specified, the fully qualified Pod hostname will be \"<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>\". If not specified, the pod will not have a domainname at all.

        :param subdomain: The subdomain of this V1PodSpec.
        :type: str
        """

        self._subdomain = subdomain

    @property
    def termination_grace_period_seconds(self):
        """
        Gets the termination_grace_period_seconds of this V1PodSpec.
        Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.

        :return: The termination_grace_period_seconds of this V1PodSpec.
        :rtype: int
        """
        return self._termination_grace_period_seconds

    @termination_grace_period_seconds.setter
    def termination_grace_period_seconds(self, termination_grace_period_seconds):
        """
        Sets the termination_grace_period_seconds of this V1PodSpec.
        Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.

        :param termination_grace_period_seconds: The termination_grace_period_seconds of this V1PodSpec.
        :type: int
        """

        self._termination_grace_period_seconds = termination_grace_period_seconds

    @property
    def tolerations(self):
        """
        Gets the tolerations of this V1PodSpec.
        If specified, the pod's tolerations.

        :return: The tolerations of this V1PodSpec.
        :rtype: list[V1Toleration]
        """
        return self._tolerations

    @tolerations.setter
    def tolerations(self, tolerations):
        """
        Sets the tolerations of this V1PodSpec.
        If specified, the pod's tolerations.

        :param tolerations: The tolerations of this V1PodSpec.
        :type: list[V1Toleration]
        """

        self._tolerations = tolerations

    @property
    def volumes(self):
        """
        Gets the volumes of this V1PodSpec.
        List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes

        :return: The volumes of this V1PodSpec.
        :rtype: list[V1Volume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """
        Sets the volumes of this V1PodSpec.
        List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes

        :param volumes: The volumes of this V1PodSpec.
        :type: list[V1Volume]
        """

        self._volumes = volumes

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1PodSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

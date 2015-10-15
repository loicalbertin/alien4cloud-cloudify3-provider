from cloudify.decorators import workflow
from cloudify.workflows import ctx
from cloudify.workflows import tasks as workflow_tasks
from utils import set_state_task
from utils import operation_task
from utils import link_tasks
from utils import CustomContext


@workflow
def a4c_uninstall(**kwargs):
    graph = ctx.graph_mode()
    custom_context = CustomContext(ctx)
    ctx.internal.send_workflow_event(
        event_type='workflow_started',
        message="Starting A4C generated '{0}' workflow execution".format(ctx.workflow_id))
    _a4c_uninstall(ctx, graph, custom_context)
    return graph.execute()


@workflow
def a4c_install(**kwargs):
    graph = ctx.graph_mode()
    custom_context = CustomContext(ctx)
    ctx.internal.send_workflow_event(
        event_type='workflow_started',
        message="Starting A4C generated '{0}' workflow execution".format(ctx.workflow_id))
    _a4c_install(ctx, graph, custom_context)
    return graph.execute()


def _a4c_uninstall(ctx, graph, custom_context):
    #  following code can be pasted in src/test/python/workflows/tasks.py for simulation
    set_state_task(ctx, graph, 'Compute', 'stopped', 'Compute_stopped', custom_context)
    set_state_task(ctx, graph, 'DeletableBlockStorage', 'deleting', 'DeletableBlockStorage_deleting', custom_context)
    set_state_task(ctx, graph, 'DeletableBlockStorage', 'deleted', 'DeletableBlockStorage_deleted', custom_context)
    operation_task(ctx, graph, 'DeletableBlockStorage', 'cloudify.interfaces.lifecycle.delete', 'delete_DeletableBlockStorage', custom_context)
    operation_task(ctx, graph, 'BlockStorage', 'cloudify.interfaces.lifecycle.stop', 'stop_BlockStorage', custom_context)
    set_state_task(ctx, graph, 'BlockStorage', 'deleted', 'BlockStorage_deleted', custom_context)
    set_state_task(ctx, graph, 'BlockStorage', 'stopping', 'BlockStorage_stopping', custom_context)
    set_state_task(ctx, graph, 'Compute', 'deleting', 'Compute_deleting', custom_context)
    set_state_task(ctx, graph, 'Compute', 'deleted', 'Compute_deleted', custom_context)
    operation_task(ctx, graph, 'DeletableBlockStorage', 'cloudify.interfaces.lifecycle.stop', 'stop_DeletableBlockStorage', custom_context)
    set_state_task(ctx, graph, 'BlockStorage', 'deleting', 'BlockStorage_deleting', custom_context)
    set_state_task(ctx, graph, 'DeletableBlockStorage', 'stopped', 'DeletableBlockStorage_stopped', custom_context)
    operation_task(ctx, graph, 'Compute', 'cloudify.interfaces.lifecycle.delete', 'delete_Compute', custom_context)
    set_state_task(ctx, graph, 'Compute', 'stopping', 'Compute_stopping', custom_context)
    set_state_task(ctx, graph, 'BlockStorage', 'stopped', 'BlockStorage_stopped', custom_context)
    operation_task(ctx, graph, 'Compute', 'cloudify.interfaces.lifecycle.stop', 'stop_Compute', custom_context)
    set_state_task(ctx, graph, 'DeletableBlockStorage', 'stopping', 'DeletableBlockStorage_stopping', custom_context)
    operation_task(ctx, graph, 'BlockStorage', 'cloudify.interfaces.lifecycle.delete', 'delete_BlockStorage', custom_context)
    link_tasks(graph, 'Compute_stopped', 'stop_Compute', custom_context)
    link_tasks(graph, 'DeletableBlockStorage_deleting', 'DeletableBlockStorage_stopped', custom_context)
    link_tasks(graph, 'DeletableBlockStorage_deleted', 'delete_DeletableBlockStorage', custom_context)
    link_tasks(graph, 'delete_DeletableBlockStorage', 'DeletableBlockStorage_deleting', custom_context)
    link_tasks(graph, 'stop_BlockStorage', 'BlockStorage_stopping', custom_context)
    link_tasks(graph, 'BlockStorage_deleted', 'delete_BlockStorage', custom_context)
    link_tasks(graph, 'BlockStorage_stopping', 'Compute_deleted', custom_context)
    link_tasks(graph, 'Compute_deleting', 'Compute_stopped', custom_context)
    link_tasks(graph, 'Compute_deleted', 'delete_Compute', custom_context)
    link_tasks(graph, 'stop_DeletableBlockStorage', 'DeletableBlockStorage_stopping', custom_context)
    link_tasks(graph, 'BlockStorage_deleting', 'BlockStorage_stopped', custom_context)
    link_tasks(graph, 'DeletableBlockStorage_stopped', 'stop_DeletableBlockStorage', custom_context)
    link_tasks(graph, 'delete_Compute', 'Compute_deleting', custom_context)
    link_tasks(graph, 'BlockStorage_stopped', 'stop_BlockStorage', custom_context)
    link_tasks(graph, 'stop_Compute', 'Compute_stopping', custom_context)
    link_tasks(graph, 'DeletableBlockStorage_stopping', 'Compute_deleted', custom_context)
    link_tasks(graph, 'delete_BlockStorage', 'BlockStorage_deleting', custom_context)


def _a4c_install(ctx, graph, custom_context):
    #  following code can be pasted in src/test/python/workflows/tasks.py for simulation
    set_state_task(ctx, graph, 'DeletableBlockStorage', 'configuring', 'DeletableBlockStorage_configuring', custom_context)
    set_state_task(ctx, graph, 'Compute', 'created', 'Compute_created', custom_context)
    operation_task(ctx, graph, 'BlockStorage', 'cloudify.interfaces.lifecycle.configure', 'configure_BlockStorage', custom_context)
    operation_task(ctx, graph, 'Compute', 'cloudify.interfaces.lifecycle.create', 'create_Compute', custom_context)
    operation_task(ctx, graph, 'DeletableBlockStorage', 'cloudify.interfaces.lifecycle.configure', 'configure_DeletableBlockStorage', custom_context)
    operation_task(ctx, graph, 'Compute', 'cloudify.interfaces.lifecycle.configure', 'configure_Compute', custom_context)
    set_state_task(ctx, graph, 'Compute', 'initial', 'Compute_initial', custom_context)
    set_state_task(ctx, graph, 'BlockStorage', 'started', 'BlockStorage_started', custom_context)
    operation_task(ctx, graph, 'Compute', 'cloudify.interfaces.lifecycle.start', 'start_Compute', custom_context)
    set_state_task(ctx, graph, 'BlockStorage', 'created', 'BlockStorage_created', custom_context)
    set_state_task(ctx, graph, 'DeletableBlockStorage', 'initial', 'DeletableBlockStorage_initial', custom_context)
    set_state_task(ctx, graph, 'Compute', 'starting', 'Compute_starting', custom_context)
    operation_task(ctx, graph, 'DeletableBlockStorage', 'cloudify.interfaces.lifecycle.create', 'create_DeletableBlockStorage', custom_context)
    set_state_task(ctx, graph, 'Compute', 'configuring', 'Compute_configuring', custom_context)
    set_state_task(ctx, graph, 'Compute', 'configured', 'Compute_configured', custom_context)
    set_state_task(ctx, graph, 'DeletableBlockStorage', 'started', 'DeletableBlockStorage_started', custom_context)
    set_state_task(ctx, graph, 'DeletableBlockStorage', 'starting', 'DeletableBlockStorage_starting', custom_context)
    set_state_task(ctx, graph, 'DeletableBlockStorage', 'creating', 'DeletableBlockStorage_creating', custom_context)
    set_state_task(ctx, graph, 'DeletableBlockStorage', 'configured', 'DeletableBlockStorage_configured', custom_context)
    set_state_task(ctx, graph, 'Compute', 'creating', 'Compute_creating', custom_context)
    set_state_task(ctx, graph, 'BlockStorage', 'initial', 'BlockStorage_initial', custom_context)
    set_state_task(ctx, graph, 'BlockStorage', 'creating', 'BlockStorage_creating', custom_context)
    operation_task(ctx, graph, 'DeletableBlockStorage', 'cloudify.interfaces.lifecycle.start', 'start_DeletableBlockStorage', custom_context)
    set_state_task(ctx, graph, 'DeletableBlockStorage', 'created', 'DeletableBlockStorage_created', custom_context)
    set_state_task(ctx, graph, 'BlockStorage', 'configured', 'BlockStorage_configured', custom_context)
    set_state_task(ctx, graph, 'Compute', 'started', 'Compute_started', custom_context)
    set_state_task(ctx, graph, 'BlockStorage', 'starting', 'BlockStorage_starting', custom_context)
    operation_task(ctx, graph, 'BlockStorage', 'cloudify.interfaces.lifecycle.create', 'create_BlockStorage', custom_context)
    operation_task(ctx, graph, 'BlockStorage', 'cloudify.interfaces.lifecycle.start', 'start_BlockStorage', custom_context)
    set_state_task(ctx, graph, 'BlockStorage', 'configuring', 'BlockStorage_configuring', custom_context)
    link_tasks(graph, 'DeletableBlockStorage_configuring', 'Compute_started', custom_context)
    link_tasks(graph, 'DeletableBlockStorage_configuring', 'DeletableBlockStorage_created', custom_context)
    link_tasks(graph, 'Compute_created', 'create_Compute', custom_context)
    link_tasks(graph, 'configure_BlockStorage', 'BlockStorage_configuring', custom_context)
    link_tasks(graph, 'create_Compute', 'Compute_creating', custom_context)
    link_tasks(graph, 'configure_DeletableBlockStorage', 'DeletableBlockStorage_configuring', custom_context)
    link_tasks(graph, 'configure_Compute', 'Compute_configuring', custom_context)
    link_tasks(graph, 'BlockStorage_started', 'start_BlockStorage', custom_context)
    link_tasks(graph, 'start_Compute', 'Compute_starting', custom_context)
    link_tasks(graph, 'BlockStorage_created', 'create_BlockStorage', custom_context)
    link_tasks(graph, 'Compute_starting', 'Compute_configured', custom_context)
    link_tasks(graph, 'create_DeletableBlockStorage', 'DeletableBlockStorage_creating', custom_context)
    link_tasks(graph, 'Compute_configuring', 'BlockStorage_created', custom_context)
    link_tasks(graph, 'Compute_configuring', 'Compute_created', custom_context)
    link_tasks(graph, 'Compute_configuring', 'DeletableBlockStorage_created', custom_context)
    link_tasks(graph, 'Compute_configured', 'configure_Compute', custom_context)
    link_tasks(graph, 'DeletableBlockStorage_started', 'start_DeletableBlockStorage', custom_context)
    link_tasks(graph, 'DeletableBlockStorage_starting', 'DeletableBlockStorage_configured', custom_context)
    link_tasks(graph, 'DeletableBlockStorage_creating', 'DeletableBlockStorage_initial', custom_context)
    link_tasks(graph, 'DeletableBlockStorage_configured', 'configure_DeletableBlockStorage', custom_context)
    link_tasks(graph, 'Compute_creating', 'Compute_initial', custom_context)
    link_tasks(graph, 'BlockStorage_creating', 'BlockStorage_initial', custom_context)
    link_tasks(graph, 'start_DeletableBlockStorage', 'DeletableBlockStorage_starting', custom_context)
    link_tasks(graph, 'DeletableBlockStorage_created', 'create_DeletableBlockStorage', custom_context)
    link_tasks(graph, 'BlockStorage_configured', 'configure_BlockStorage', custom_context)
    link_tasks(graph, 'Compute_started', 'start_Compute', custom_context)
    link_tasks(graph, 'BlockStorage_starting', 'BlockStorage_configured', custom_context)
    link_tasks(graph, 'create_BlockStorage', 'BlockStorage_creating', custom_context)
    link_tasks(graph, 'start_BlockStorage', 'BlockStorage_starting', custom_context)
    link_tasks(graph, 'BlockStorage_configuring', 'BlockStorage_created', custom_context)
    link_tasks(graph, 'BlockStorage_configuring', 'Compute_started', custom_context)


#following code can be pasted in src/test/python/workflows/context.py for simulation
#def _build_nodes(ctx):
    #types = []
    #types.append('alien.cloudify.openstack.nodes.Volume')
    #types.append('alien.cloudify.openstack.nodes.DeletableVolume')
    #types.append('tosca.nodes.BlockStorage')
    #types.append('tosca.nodes.Root')
    #node_BlockStorage = _build_node(ctx, 'BlockStorage', types, 1)
    #types = []
    #types.append('alien.cloudify.openstack.nodes.DeletableVolume')
    #types.append('tosca.nodes.BlockStorage')
    #types.append('tosca.nodes.Root')
    #node_DeletableBlockStorage = _build_node(ctx, 'DeletableBlockStorage', types, 1)
    #types = []
    #types.append('alien.nodes.openstack.Compute')
    #types.append('tosca.nodes.Compute')
    #types.append('tosca.nodes.Root')
    #node_Compute = _build_node(ctx, 'Compute', types, 1)
    #_add_relationship(node_BlockStorage, node_Compute)
    #_add_relationship(node_DeletableBlockStorage, node_Compute)

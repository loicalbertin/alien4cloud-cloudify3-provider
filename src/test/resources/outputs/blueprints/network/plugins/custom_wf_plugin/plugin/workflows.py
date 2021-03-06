from cloudify.decorators import workflow
from cloudify.workflows import ctx
from cloudify.workflows import tasks as workflow_tasks
from utils import set_state_task
from utils import operation_task
from utils import link_tasks
from utils import CustomContext
from utils import generate_native_node_workflows


@workflow
def a4c_install(**kwargs):
    graph = ctx.graph_mode()
    custom_context = CustomContext(ctx)
    ctx.internal.send_workflow_event(
        event_type='workflow_started',
        message="Starting A4C generated '{0}' workflow execution".format(ctx.workflow_id))
    _a4c_install(ctx, graph, custom_context)
    return graph.execute()


@workflow
def a4c_uninstall(**kwargs):
    graph = ctx.graph_mode()
    custom_context = CustomContext(ctx)
    ctx.internal.send_workflow_event(
        event_type='workflow_started',
        message="Starting A4C generated '{0}' workflow execution".format(ctx.workflow_id))
    _a4c_uninstall(ctx, graph, custom_context)
    return graph.execute()


def _a4c_install(ctx, graph, custom_context):
    #  following code can be pasted in src/test/python/workflows/tasks.py for simulation
    custom_context.register_native_delegate_wf_step('NetPub', 'NetPub_install')
    custom_context.register_native_delegate_wf_step('InternalNetwork', 'InternalNetwork_install')
    custom_context.register_native_delegate_wf_step('Compute', 'Compute_install')
    generate_native_node_workflows(ctx, graph, custom_context, 'install')


def _a4c_uninstall(ctx, graph, custom_context):
    #  following code can be pasted in src/test/python/workflows/tasks.py for simulation
    custom_context.register_native_delegate_wf_step('InternalNetwork', 'InternalNetwork_uninstall')
    custom_context.register_native_delegate_wf_step('Compute', 'Compute_uninstall')
    custom_context.register_native_delegate_wf_step('NetPub', 'NetPub_uninstall')
    generate_native_node_workflows(ctx, graph, custom_context, 'uninstall')


#following code can be pasted in src/test/python/workflows/context.py for simulation
#def _build_nodes(ctx):
    #types = []
    #types.append('alien.nodes.openstack.PrivateNetwork')
    #types.append('alien.nodes.PrivateNetwork')
    #types.append('tosca.nodes.Network')
    #types.append('tosca.nodes.Root')
    #node_InternalNetwork = _build_node(ctx, 'InternalNetwork', types, 1)
    #types = []
    #types.append('alien.nodes.openstack.PublicNetwork')
    #types.append('alien.nodes.PublicNetwork')
    #types.append('tosca.nodes.Network')
    #types.append('tosca.nodes.Root')
    #node_NetPub = _build_node(ctx, 'NetPub', types, 1)
    #types = []
    #types.append('alien.nodes.openstack.Compute')
    #types.append('tosca.nodes.Compute')
    #types.append('tosca.nodes.Root')
    #node_Compute = _build_node(ctx, 'Compute', types, 1)
    #_add_relationship(node_Compute, node_NetPub)
    #_add_relationship(node_Compute, node_InternalNetwork)

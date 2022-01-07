#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        interface=dict(type='str', required=False),
        attribute=dict(type='str', required=False)
    )

    result = dict(
        changed=False,
        dummy='',
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    # if module.check_mode:
    #     module.exit_json(**result)

    command = [
        "wg", 
        "show",
        "all" if module.params["interface"] is None else module.params["interface"],
    ]

    if module.params["attribute"] is not None:
        command.append(module.params["attribute"])

    import subprocess
    out = subprocess.run(command, capture_output=True)
    result['dummy'] = "wtf"
    result["stdout"] = str(out)

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    # if module.params['new']:
    #     result['changed'] = True

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if module.params['interface'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()

from ansible.module_utils.basic import AnsibleModule
import subprocess

class demoClass(object):

    def __init__(self, p_command):
        self.command = p_command

    def run_command(self):
        try:
            process = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE)
            output, error = process.communicate()
        except Exception as e:
            return False
        
        return output, error


def main():
    try:
        # the AnsibleModule object will be our abstraction working with Ansible
        # this includes instantiation, a couple of common attr would be the
        # args/params passed to the execution, as well as if the module
        # supports check mode
        module = AnsibleModule(
            argument_spec=dict(
                command=dict(type='str', required=True)
            ),
            supports_check_mode=True
        )

        v_command = module.params.get('command')

        objClass = demoClass(v_command)

        output, error = objClass.run_command()

        result = dict(
            changed=True,
            message=str(output.decode('ascii').strip()).split("\n")
        )

        module.exit_json(**result)

    except Exception as e:
        result = dict(
                changed=False,
                message=str(e)
            )
        module.fail_json(msg='You requested this to fail', **result)

if __name__ == '__main__':
    main()
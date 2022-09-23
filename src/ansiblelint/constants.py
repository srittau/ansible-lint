"""Constants used by AnsibleLint."""
import os.path
from typing import Literal

DEFAULT_RULESDIR = os.path.join(os.path.dirname(__file__), "rules")
CUSTOM_RULESDIR_ENVVAR = "ANSIBLE_LINT_CUSTOM_RULESDIR"
RULE_DOC_URL = "https://ansible-lint.readthedocs.io/rules/"

SUCCESS_RC = 0
VIOLATIONS_FOUND_RC = 2
INVALID_CONFIG_RC = 3
LOCK_TIMEOUT_RC = 4
EXIT_CONTROL_C_RC = 130

# Minimal version of Ansible we support for runtime
ANSIBLE_MIN_VERSION = "2.12"

ANSIBLE_MOCKED_MODULE = """\
# This is a mocked Ansible module generated by ansible-lint
from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
module: {name}

short_description: Mocked
version_added: "1.0.0"
description: Mocked

author:
    - ansible-lint (@nobody)
'''
EXAMPLES = '''mocked'''
RETURN = '''mocked'''


def main():
    result = dict(
        changed=False,
        original_message='',
        message='')

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    module.exit_json(**result)


if __name__ == "__main__":
    main()
"""

FileType = Literal[
    "playbook",
    "meta",  # role meta
    "tasks",  # includes pre_tasks, post_tasks
    "handlers",  # very similar to tasks but with some specifics
    # https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-roles-and-collections-from-the-same-requirements-yml-file
    "requirements",
    "role",  # that is a folder!
    "yaml",  # generic yaml file, previously reported as unknown file type
    "",  # unknown file type
]


# Aliases for deprecated tags/ids and their newer names
RENAMED_TAGS = {
    "102": "no-jinja-when",
    "104": "deprecated-bare-vars",
    "105": "deprecated-module",
    "106": "role-name",
    "202": "risky-octal",
    "203": "no-tabs",
    "205": "playbook-extension",
    "206": "jinja[spacing]",
    "207": "jinja[invalid]",
    "208": "risky-file-permissions",
    "301": "no-changed-when",
    "302": "deprecated-command-syntax",
    "303": "command-instead-of-module",
    "304": "inline-env-var",
    "305": "command-instead-of-shell",
    "306": "risky-shell-pipe",
    "401": "latest[git]",
    "402": "latest[hg]",
    "403": "package-latest",
    "404": "no-relative-paths",
    "501": "partial-become",
    "502": "unnamed-task",
    "503": "no-handler",
    "504": "deprecated-local-action",
    "505": "missing-import",
    "601": "literal-compare",
    "602": "empty-string-compare",
    "701": "meta-no-info",
    "702": "meta-no-tags",
    "703": "meta-incorrect",
    "704": "meta-video-links",
    "911": "syntax-check",
    "var-spacing": "jinja[spacing]",
    "unnamed-task": "name[missing]",
    "git-latest": "latest[git]",
    "hg-latest": "latest[hg]",
    "no-jinja-nesting": "jinja[invalid]",
    "no-loop-var-prefix": "loop-var-prefix",
}

PLAYBOOK_TASK_KEYWORDS = [
    "tasks",
    "handlers",
    "pre_tasks",
    "post_tasks",
]
NESTED_TASK_KEYS = [
    "block",
    "always",
    "rescue",
]

# Keys that are used internally when parsing YAML/JSON files
SKIPPED_RULES_KEY = "__skipped_rules__"
LINE_NUMBER_KEY = "__line__"
FILENAME_KEY = "__file__"

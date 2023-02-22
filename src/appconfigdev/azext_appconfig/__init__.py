# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

from azext_appconfig._help import helps  # pylint: disable=unused-import


class AppconfigCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        appconfig_custom = CliCommandType(
            operations_tmpl='azext_appconfig.custom#{}')
        super(AppconfigCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                  custom_command_type=appconfig_custom)

    def load_command_table(self, args):
        from azext_appconfig.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_appconfig._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = AppconfigCommandsLoader

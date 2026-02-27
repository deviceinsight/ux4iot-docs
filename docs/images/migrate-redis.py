#!/usr/bin/env python
import json
import re
import subprocess
import sys

from termcolor import colored


def run_command(command):
    runnable_command = command.split()
    output = subprocess.check_output(runnable_command).decode("utf-8")

    return output


def run_command_with_json_output(command):
    output = run_command(command)
    result = json.loads(output)

    return result


def print_usage(error=None):
    if error:
        print(colored(error, 'red'))

    print(f"""
{colored('Usage:', 'white')}
Recommended usage:
- ./migrate-redis.py https://url-to-source-ux4iot-in-azure-portal.com/ https://url-to-target-ux4iot-in-azure-portal.com/

Alternative usage:
- ./migrate-redis.py source_subscription_id source_resource_group source_ux4iot_name target_subscription_id target_resource_group target_ux4iot_name
""")


def parse_ux4iot_args(args):
    if len(args) == 0:
        print_usage('Illegal number of parameters')
        sys.exit(1)

    url_pattern = r'^https?://'  # Regular expression pattern to match the start of a URL
    source_url = args[0]
    target_url = args[1]

    if re.match(url_pattern, source_url) and re.match(url_pattern, target_url):
        # The variable contains a valid URL
        # Extract the subscription ID
        source_subscription_id = re.search(
            r'subscriptions/([^/]+)', source_url).group(1)

        # Extract the resource group
        source_resource_group = re.search(
            r'resourceGroups/([^/]+)', source_url).group(1)

        # Extract the service name
        source_ux4iot_name = re.search(
            r'applications/([^/]+)', source_url).group(1)

        # The variable contains a valid URL
        # Extract the subscription ID
        target_subscription_id = re.search(
            r'subscriptions/([^/]+)', target_url).group(1)

        # Extract the resource group
        target_resource_group = re.search(
            r'resourceGroups/([^/]+)', target_url).group(1)

        # Extract the service name
        target_ux4iot_name = re.search(
            r'applications/([^/]+)', target_url).group(1)

    else:
        # The variable does not contain a valid URL
        if len(args) < 6:
            print_usage("Illegal number of parameters")
            sys.exit(1)

        print(args)

        source_subscription_id = args[0]
        source_resource_group = args[1]
        source_ux4iot_name = args[2]
        target_subscription_id = args[3]
        target_resource_group = args[4]
        target_ux4iot_name = args[5]

    return {
        "source_subscription_id": source_subscription_id,
        "source_resource_group": source_resource_group,
        "source_ux4iot_name": source_ux4iot_name,
        "target_subscription_id": target_subscription_id,
        "target_resource_group": target_resource_group,
        "target_ux4iot_name": target_ux4iot_name,
    }


def copy_redis_file_share(source_storage_account, target_storage_account):
    pass


def get_dump_file_url(subscription_id, resource_group, ux4iot_name):
    managed_app = run_command_with_json_output(
        f"az managedapp show --subscription {subscription_id} --resource-group {resource_group} --name {ux4iot_name}")
    managed_resource_group_id = managed_app['managedResourceGroupId']
    managed_resource_group_resource = run_command_with_json_output(
        f"az resource show --ids {managed_resource_group_id}")  # | jq -r .name)
    managed_resource_group_name = managed_resource_group_resource['name']
    resources = run_command_with_json_output(
        f"az resource list --resource-group {managed_resource_group_name}")
    storage_account_name = next(
        (r['name'] for r in resources if r["type"] == "Microsoft.Storage/storageAccounts"), None)

    print('Getting redisi dump file url')
    storage_redis_dump_file_url = run_command_with_json_output(
        f"az storage file url --account-name {storage_account_name} --path dump.rdb --share-name redis")

    print('Getting sas token for redis dump file')
    sas_token = run_command_with_json_output(
        f"az storage file generate-sas --account-name {storage_account_name} --start 2023-01-09T00:00:00Z --expiry 2023-12-31T23:59:00Z --path dump.rdb --permissions rw --share-name redis")

    return f"{storage_redis_dump_file_url}?{sas_token}"


def main():
    args = sys.argv[1:]
    if len(args) != 2 and len(args) != 6:
        print_usage('Invalid number of arguments')
        return

    try:
        ux4iot = parse_ux4iot_args(args)
        source_storage_account_url = get_dump_file_url(
            ux4iot['source_subscription_id'], ux4iot['source_resource_group'], ux4iot['source_ux4iot_name'])
        target_storage_account_url = get_dump_file_url(
            ux4iot['target_subscription_id'], ux4iot['target_resource_group'], ux4iot['target_ux4iot_name'])
        print(source_storage_account_url)
        print(target_storage_account_url)
        copy_command = f"azcopy copy {source_storage_account_url} {target_storage_account_url}"
        subprocess.run(copy_command.split(), check=True, text=True)
    except AttributeError as e:
        print_usage()
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    main()

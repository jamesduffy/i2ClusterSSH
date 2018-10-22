"""i2ClusterSSH CLI."""
import click
import boto3
import sys


WARNING_INSTNACE_COUNT = 25


def get_valid_aws_regions():
    """Get valid AWS Regions."""
    valid_aws_regions = []
    ec2_client = boto3.client('ec2')
    aws_region_response = ec2_client.describe_regions()
    for region in aws_region_response['Regions']:
        valid_aws_regions.append(region['RegionName'])
    return valid_aws_regions


@click.command()
@click.option('--region', '-r', help="AWS Region")
@click.option('--tag', '-t', multiple=True)
@click.option('--use-public-ip', '-p', is_flag=True, default=False, help="Use public IPs")
@click.option('--no-prompt', is_flag=True, default=False, help="Suppress any prompts when using a non interactive shell.")
def cli(region, tag, use_public_ip, no_prompt):
    """Get a list of AWS Instances by tags and SSH to them in iTerm2."""
    if region not in get_valid_aws_regions():
        click.echo("Region {} is not valid!".format(region))
        sys.exit()

    ec2_resource = boto3.resource('ec2', region_name=region)

    if len(tag) == 0:
        click.echo("You have not specified any tags to filter by. This may cause a large number of instances to be returned.")
        if no_prompt is False and click.confirm("  Do you wish to continue?") is False:
            sys.exit("Quitting before the going gets tough.")

    # Build filters list
    filters = [{
        'Name': 'instance-state-name',
        'Values': ['running']
    }]
    for t in tag:
        t = t.split('=')
        filters.append({
            'Name': 'tag:{}'.format(t[0]),
            'Values': [t[1]]
        })

    ip_addresses = []
    for instance in ec2_resource.instances.filter(Filters=filters):
        if use_public_ip:
            ip_addresses.append(instance.public_ip_address)
        else:
            ip_addresses.append(instance.private_ip_address)

    # Display a warning if we are trying to connect to many instances
    if len(ip_addresses) >= WARNING_INSTNACE_COUNT:
        click.echo("You are attempting to connect to {} instances and this may cause performance issues.".format(len(ip_addresses)))
        if no_prompt is False and click.confirm("  Do you wish to continue?") is False:
            sys.exit("Quitting before the going gets tough.")

    address_string = ''
    for address in ip_addresses:
        address_string += '{} '.format(address)
    address_string.strip()

    click.echo("i2cssh -m {}".format(address_string))


if __name__ == '__main__':
    if getattr(sys, 'frozen', False):
        cli(sys.argv[1:])
    else:
        cli()

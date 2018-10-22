# i2ClusterSSH

Program to get a list of EC2 instances from AWS and SSH into them using iTerm2's split panes feature via i2cssh.

This should be able to replace [ClusterSSH](https://github.com/duncs/clusterssh) and [CsshX](https://github.com/brockgr/csshx). I would often have many issues with both tools (mainly CsshX) as there seems to have been a stop in development for many years.

This is a pretty simple CLI that uses [Click](https://click.palletsprojects.com/en/7.x/) and [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html). It is then packaged using [PyInstaller](https://www.pyinstaller.org/) to create an executable.

## Installation

1. Download the latest release from the releases page
2. Move the binary into your `/usr/local/bin` directory
3. Install i2cssh: `gem install i2cssh`

## Usage

`i2cluster --region us-west-1 -tag Name=webserver`

or 

`i2cluster -r us-west-1 -t Name=webserver`

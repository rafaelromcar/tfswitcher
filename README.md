# TFSWITCHER

Simple Python 3 script to switch Terraform version whenever needed.  
Author: Rafael Romero Carmona <rafaelromcar@gmail.com>

## Requirements

* Python 3

## How to use it

* You need to have write permissions on `/usr/local/bin/`.
* Command: `sudo tfswitcher X.Y.Z`.
    * Example: `sudo tfswitcher 0.9.5` will create a symlink from `/usr/local/bin/terraform-0.9.5` on `/usr/local/bin/terraform`.

## Installation

1. Clone the repository
2. Move the script to one of the folders of your $PATH with the name `tfswitcher`
3. Test it with `tfswitcher -h`

## How does it work?

* It takes one single parameter: the version of Terraform you want run when executing the terraform command.
* It is going to create a symlink on `/usr/local/bin/terraform` to the binary `/usr/local/bin/terraform-VERSION`.

## License

All the content of this repository is under **GPLv3**. You can find the text of the license on the file *gpl.txt*.  
![GLPv3 logo](lgplv3-147x51.png)

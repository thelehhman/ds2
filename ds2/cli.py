#!/usr/bin/env python3

import click
import ds2
from ds2 import shell

@click.group()
def cli():
	ds2.init_dir_struct()
	pass

@click.command(help='Create new database')
@click.argument('name')

def create(name):
	click.echo('Creating db %s' %name)
	db = ds2.Db(name)
	db.create()

@click.command(help='Launch database shell')
@click.argument('name')
def access(name):
	shell.start_shell(name)

@click.command(help='Destroy database')
@click.argument('name')
def destroy(name):
	k = raw_input('Are you sure(y/n) ?')
	if k.lower() == 'y':
		db = ds2.Db(name)
	db.destroy()

@click.command(help='List all databases')
def ls():
	l = ds2.Key()
	for item in l.data:
		click.echo(item['name'])


cli.add_command(create)
cli.add_command(access)
cli.add_command(ls)
cli.add_command(destroy)

if __name__ == "__main__":
	if ds2.conf['home'] is '':
		print( 'Please define DS2_DIR environment variable')
	else:
		cli()

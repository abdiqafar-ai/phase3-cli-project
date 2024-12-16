import click
from databases.student import *
from databases.course import *
from databases.grade import *
from databases.teacher import *
from databases.setup import *
from databases.setup import engine


@click.group()
def cli():
  pass

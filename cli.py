import click
from github_api import get_events, get_issues

@click.group()
def cli():
    pass

@cli.command()
@click.argument('user', required=True)
def github_activity(user):
    events = get_events(user)
    
    push_count = 0

    for event in events:
        if event['type'] == "PushEvent":
            push_count += 1 
    #### NOTA CONTAR LAS EVENTOS DE TIPO IssueCommentEvent Y EL NOMBRE DE USUARIO Y REPO (TYPE['REPO']['NAME'])
    issues = get_issues(user)
    click.echo(f"Pushed {push_count} commits to {event['repo']['name']}")
       
if __name__ == "__main__":
    cli()
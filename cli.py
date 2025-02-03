from datetime import datetime
import click
from github_api import get_events, get_issues

@click.group()
def cli():
    pass

@cli.command()
@click.argument('user', required=True)
def last_events(user):
    # Show de last 3 event of de user
    events = get_events(user)

    for event in events[:3]:
        click.echo(f"Event {event['type']} created in {event['repo']['name']}")
    else:
        click.echo(f"Not activity finde for user {user}")


@cli.command()
@click.argument('user', required=True)
def github_activity(user):
    events = get_events(user)
    event_counts = {}

    for event in events:
        event_type = event['type']
        if event_type in event_counts:
            event_counts[event_type] += 1 
        else:
            event_counts[event_type] = 1 
    
    for event_type, count in event_counts.items():        
        click.echo(f"{count} {event_type} type repositorys")

#Filter user events by type
@cli.command()
@click.argument('user', required=True)
@click.argument('event', required=True)
def filter(user, event):
    user_events = get_events(user)

    for events in user_events:
        if events['type'] == event:
            
            dt = datetime.strptime(events['created_at'], "%Y-%m-%dT%H:%M:%SZ")
            # Extraer solo la parte de la fecha en formato año-mes-día
            date_only = dt.date()
            click.echo(f"Event {events['type']} created in {date_only} in {events['repo']['name']}")



if __name__ == "__main__":
    cli()



      # UTILIZAR ESTE CÓDIGO PARA CREAR EL COMANDO PARA FILTRAR POR EVENTOS
   # for event in events:
   #     if event['type'] == "PushEvent":
   #         repository = event['repo']['name']
   #         if repository == previous_repository:
   #             push_count +=1
   #         else:
   #             if previous_repository:
   #                 click.echo(f"Pushed {push_count} commits to {previous_repository}")
   #             push_count = 1
   #             previous_repository = repository
   # 
   # if previous_repository:
   #     click.echo(f"Pushed {push_count} commits to {previous_repository}")
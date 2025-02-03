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
@click.argument('event_type', required=True)
def filter(user, event_type):
    user_events = get_events(user)

    filtered_event = [event for event in user_events if event['type'] == event_type]
    
    if not filtered_event:
        click.echo(f"{event_type} type event not found for user {user}")

    for event in filtered_event:
        try:
            dt = datetime.strptime(event['created_at'], "%Y-%m-%dT%H:%M:%SZ")
            date_only = dt.date()
        except (ValueError, TypeError) as error:
            click.echo(f"Error in date format:\n {error}")
            continue

        click.echo(f"Event {event['type']} created in {date_only} in {event['repo']['name']}")

### AÑADIR EL CONTROL DE EXECPCIONES AL RESTO DE COMANDOS E INTENTAR HACER QUE EL COMANDO FILTER 
# ####MUESTRE SOLAMENTE LOS ULTIMOS 10 EVENTOS 
if __name__ == "__main__":
    cli()
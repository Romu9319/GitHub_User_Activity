from datetime import datetime
import click
from github_api import get_events

@click.group()
def cli():
    pass

@cli.command()
@click.argument('user', required=True)
def last_events(user):
    """Shows the last 5 events made by the user"""
    try:
        events = get_events(user)
    except Exception as error:
        click.echo(f"Could not connect to servers correctly : {error}")
        return

    if not events:
        click.echo(f"Events not found for user: {user}")

    count = 0
    for event in events:
        try:
            event_type = event.get('type', 'Event type not found')
            event_repo = event.get('repo', 'Repository not found')
            repo_name = event_repo.get('name', 'Repository name not found')
            click.echo(f"Event {event_type} created in {repo_name}")
            count += 1

            if count >= 5:
                break

        except Exception as error:
            click.echo(f"Event processing error: {error}")


@cli.command()
@click.argument('user', required=True)
def github_activity(user):
    """Shows the types of events performed and the times performed by the user"""
    try:
        events = get_events(user)
    except Exception as error:
        click.echo(f"Could not connect to servers correctly : {error}")
        return

    event_counts = {}
    for event in events:
        try:
            event_type = event.get('type','Event type not found')

            if event_type in event_counts:
                event_counts[event_type] += 1 
            else:
                event_counts[event_type] = 1 
        
        except Exception as error:
            click.echo(f"Event processing error: {error}")        
    
    for event_type, count in event_counts.items():        
        click.echo(f"{count} {event_type} events")


@cli.command()
@click.argument('user', required=True)
@click.argument('event_type', required=True)
def filter(user, event_type):
    """Filter the search by event type and show the last 10 events """
    try:
        events = get_events(user)
    except Exception as error:
        click.echo(f"Could not connect to servers correctly : {error}")
        return

    filtered_event = [event for event in events if event['type'] == event_type]
    
    if not filtered_event:
        click.echo(f"{event_type} type event not found for user {user}")

    for event in filtered_event[:10]:
        try:
            dt = datetime.strptime(event['created_at'], "%Y-%m-%dT%H:%M:%SZ")
            date_only = dt.date()
        except (ValueError, TypeError) as error:
            click.echo(f"Error in date format:\n {error}")
            continue

        click.echo(f"Event {event['type']} created in {date_only} in {event['repo']['name']}")


if __name__ == '__main__':
    cli()